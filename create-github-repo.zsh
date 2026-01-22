#!/bin/zsh

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Icons
CHECK="✓"
CROSS="✗"
ARROW="→"

print_header() {
    echo ""
    echo "${BLUE}${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo "${BLUE}${BOLD}   GitHub Repository Creator${NC}"
    echo "${BLUE}${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

print_success() {
    echo "${GREEN}${CHECK} $1${NC}"
}

print_error() {
    echo "${RED}${CROSS} $1${NC}"
}

print_info() {
    echo "${CYAN}${ARROW} $1${NC}"
}

print_warning() {
    echo "${YELLOW}! $1${NC}"
}

# Check for required dependencies
check_dependencies() {
    local missing=0

    if ! command -v gh &> /dev/null; then
        print_error "GitHub CLI (gh) is not installed"
        echo "  Install it with: brew install gh"
        missing=1
    fi

    if ! command -v git &> /dev/null; then
        print_error "Git is not installed"
        missing=1
    fi

    if [[ $missing -eq 1 ]]; then
        exit 1
    fi

    # Check if gh is authenticated
    if ! gh auth status &> /dev/null; then
        print_error "GitHub CLI is not authenticated"
        echo "  Run: gh auth login"
        exit 1
    fi
}

# Main script
main() {
    print_header

    # Get project root (current directory)
    local project_root="$(pwd)"
    local repo_name="$(basename "$project_root")"

    print_info "Project root: ${BOLD}$project_root${NC}"
    print_info "Repository name: ${BOLD}$repo_name${NC}"
    echo ""

    # Check dependencies
    check_dependencies
    print_success "Dependencies verified"

    # Check if already a GitHub repo
    if git remote get-url origin &> /dev/null; then
        local existing_remote=$(git remote get-url origin)
        print_warning "This folder is already linked to a remote repository:"
        echo "  $existing_remote"
        echo ""
        read -q "REPLY?Do you want to continue anyway? (y/n) "
        echo ""
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo ""
            print_info "Cancelled"
            exit 0
        fi
        echo ""
    fi

    # Repository visibility selection
    echo "${BOLD}Select repository visibility:${NC}"
    echo "  1) Private (default)"
    echo "  2) Public"
    echo ""
    read "visibility_choice?Enter choice [1-2]: "

    local visibility="--private"
    local visibility_label="private"
    case $visibility_choice in
        2)
            visibility="--public"
            visibility_label="public"
            ;;
        *)
            visibility="--private"
            visibility_label="private"
            ;;
    esac
    echo ""

    # Optional description
    read "description?Enter repository description (optional): "
    echo ""

    # Initialize git if needed
    if [[ ! -d ".git" ]]; then
        print_info "Initializing git repository..."
        git init -q
        print_success "Git repository initialized"
    else
        print_success "Git repository already initialized"
    fi

    # Create initial commit if no commits exist
    if ! git rev-parse HEAD &> /dev/null 2>&1; then
        if [[ -n "$(ls -A)" ]]; then
            print_info "Creating initial commit..."
            git add -A
            git commit -q -m "Initial commit"
            print_success "Initial commit created"
        else
            print_warning "Empty directory - creating placeholder commit"
            echo "# $repo_name" > README.md
            git add README.md
            git commit -q -m "Initial commit"
            print_success "Initial commit with README created"
        fi
    else
        print_success "Existing commits found"
    fi

    # Ensure we're on main branch
    local current_branch=$(git branch --show-current)
    if [[ "$current_branch" != "main" ]]; then
        print_info "Renaming branch to 'main'..."
        git branch -M main
        print_success "Branch renamed to 'main'"
    fi

    # Create GitHub repository
    print_info "Creating GitHub repository..."

    local gh_args=("$visibility" "--source=." "--push")
    if [[ -n "$description" ]]; then
        gh_args+=("--description" "$description")
    fi

    if gh repo create "$repo_name" "${gh_args[@]}" 2>&1; then
        echo ""
        print_success "Repository created successfully!"
        echo ""

        # Get and display the repo URL
        local repo_url=$(gh repo view --json url -q .url 2>/dev/null)
        if [[ -n "$repo_url" ]]; then
            echo "${BOLD}Repository URL:${NC}"
            echo "  ${CYAN}$repo_url${NC}"
        fi

        echo ""
        echo "${GREEN}${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        echo "${GREEN}${BOLD}   Done! Your repository is ready.${NC}"
        echo "${GREEN}${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        echo ""
    else
        echo ""
        print_error "Failed to create repository"
        exit 1
    fi
}

main "$@"
