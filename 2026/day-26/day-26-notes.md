# GitHub CLI: Manage GitHub from Your Terminal

## Task 1: Install and Authenticate

GitHub CLI (`gh`) allows GitHub repositories, issues, pull requests, workflows, and other GitHub features to be managed directly from the terminal.

### Install GitHub CLI

```bash
# Update package information
sudo apt update

# Install GitHub CLI
sudo apt install gh -y

# Check the installed version
gh --version
# This confirms that GitHub CLI is installed.
```

### Authenticate with GitHub

```bash
# Start GitHub authentication
gh auth login

# Follow the prompts:
# - GitHub.com
# - HTTPS
# - Authenticate using a web browser or the displayed authentication method
```

### Verify authentication

```bash
# Check authentication status
gh auth status
# This shows whether you are logged in and which GitHub account is active.
```

### Authentication methods supported by `gh`

GitHub CLI supports authentication through:

* Browser-based login
* Authentication token
* Environment variables such as `GH_TOKEN`
* SSH authentication for Git operations when configured

For normal interactive use, `gh auth login` is the easiest method.

---

## Task 2: Working with Repositories

### Create a new GitHub repository from the terminal

```bash
# Create a temporary public repository with a README
gh repo create devops-gh-cli-test --public --add-readme

# The repository is created under the currently authenticated GitHub account.
```

### Clone a repository using `gh`

```bash
# Clone the test repository using GitHub CLI
gh repo clone devops-gh-cli-test

# Move into the cloned repository
cd devops-gh-cli-test
```

`gh repo clone` performs the repository cloning workflow without requiring the traditional `git clone` command.

### View repository details

```bash
# Show details of the test repository
gh repo view devops-gh-cli-test
# This displays repository information directly in the terminal.
```

### List repositories

```bash
# List repositories belonging to the authenticated account
gh repo list

# Display more repositories if needed
gh repo list --limit 100
```

### Open a repository in the browser

```bash
# Open the repository directly in the default browser
gh repo view devops-gh-cli-test --web
# This opens the GitHub repository page.
```

### Delete the test repository

```bash
# Delete the temporary test repository
gh repo delete devops-gh-cli-test --yes

# This permanently deletes the test repository.
# Verify it is no longer available before continuing.
```

---

## Task 3: Issues

Use the existing `devops-git-practice` repository for the issue exercise.

### Create an issue

```bash
# Create an issue with a title, body and label
gh issue create \
  --repo devops-git-practice \
  --title "Improve deployment documentation" \
  --body "Add clearer deployment verification steps to deployment.md." \
  --label documentation

# GitHub creates the issue and returns its issue number.
```

If the `documentation` label does not exist, check the available labels and use an existing suitable label.

```bash
# List labels available in the repository
gh label list --repo devops-git-practice

# Create the documentation label if needed
gh label create documentation \
  --repo devops-git-practice \
  --description "Documentation improvements"
```

### List open issues

```bash
# List all open issues
gh issue list --repo devops-git-practice

# Show more open issues if required
gh issue list --repo devops-git-practice --limit 50
```

### View a specific issue

Replace `<issue-number>` with the number returned by `gh issue create`.

```bash
# View the specific issue
gh issue view <issue-number> --repo devops-git-practice
# This displays the issue title, body, labels and other details.
```

### Close the issue

```bash
# Close the issue after checking it
gh issue close <issue-number> --repo devops-git-practice

# Verify the issue is closed
gh issue view <issue-number> --repo devops-git-practice
```

### How can `gh issue` be used in automation?

`gh issue` can be used in scripts to automatically create issues when a deployment fails, a monitoring check detects a problem, or a CI/CD process finds an important error.

For example, a script could create an issue automatically when a production health check fails.

---

## Task 4: Pull Requests

Use the existing `devops-git-practice` repository.

### Create a feature branch

```bash
# Make sure the local main branch is current
git switch main
git pull origin main

# Create a feature branch for the PR
git switch -c feature-gh-cli

# Add a small documentation improvement
echo "GitHub CLI verification steps" >> deployment.md

# Check the change
git diff
```

### Commit and push the branch

```bash
# Stage the documentation change
git add deployment.md

# Commit the change
git commit -m "Add GitHub CLI deployment notes"

# Push the feature branch to GitHub
git push -u origin feature-gh-cli
```

### Create the pull request from the terminal

```bash
# Create a pull request using the current branch
gh pr create \
  --base main \
  --head feature-gh-cli \
  --title "Add GitHub CLI deployment notes" \
  --body "Adds GitHub CLI verification steps to the deployment documentation."

# GitHub creates the pull request and returns its URL.
```

You can also use `--fill` to let GitHub CLI fill the title and body from the commits.

```bash
# Create a pull request using commit information
gh pr create --fill
```

### List open pull requests

```bash
# List open pull requests in the repository
gh pr list --repo devops-git-practice
# This displays the open PRs.
```

### View pull request details

Replace `<pr-number>` with your actual PR number.

```bash
# View pull request details
gh pr view <pr-number> --repo devops-git-practice

# View the pull request checks
gh pr checks <pr-number> --repo devops-git-practice

# View the pull request status
gh pr status
```

Reviewers can also be checked from the pull request details on GitHub.

### Merge the pull request

```bash
# Merge the pull request using a merge commit
gh pr merge <pr-number> \
  --repo devops-git-practice \
  --merge

# Delete the remote feature branch after merging if prompted.
```

### Merge methods supported by `gh pr merge`

`gh pr merge` supports:

* Merge commit
* Squash merge
* Rebase merge

The exact options available can also be checked with:

```bash
# Display available pull request merge options
gh pr merge --help
```

### How would I review someone else's PR using `gh`?

I would:

1. List the open PRs.
2. View the PR details.
3. Inspect the changed files.
4. Check CI status.
5. Review the commits.
6. Leave a review or comment.

Useful commands include:

```bash
# List open pull requests
gh pr list

# View a pull request
gh pr view <pr-number>

# View the changed files
gh pr diff <pr-number>

# Check CI status
gh pr checks <pr-number>
```

---

## Task 5: GitHub Actions and Workflows

GitHub CLI can also be used to inspect GitHub Actions workflows and their runs.

Use a public repository that uses GitHub Actions.

```bash
# List workflow runs from a public GitHub repository
gh run list --repo kubernetes/kubernetes --limit 10

# View a specific workflow run
gh run view <run-id> --repo kubernetes/kubernetes
```

Replace `<run-id>` with an actual run ID returned by `gh run list`.

### How can `gh run` help in CI/CD?

`gh run` can be used to:

* Check whether a workflow succeeded or failed.
* Inspect failed workflow runs.
* Retrieve logs.
* Automate deployment verification.
* Monitor CI/CD results from scripts.

Example:

```bash
# View the logs of a workflow run
gh run view <run-id> \
  --repo kubernetes/kubernetes \
  --log
```

### How can `gh workflow` help?

`gh workflow` can be used to manage and inspect GitHub Actions workflows.

```bash
# List workflows in a repository
gh workflow list --repo kubernetes/kubernetes

# View workflow details
gh workflow view <workflow> --repo kubernetes/kubernetes
```

This can be useful when building scripts that monitor or trigger CI/CD workflows.

---

## Task 6: Useful `gh` Tricks

### `gh api`

`gh api` allows GitHub API requests directly from the terminal.

```bash
# Get information about the authenticated GitHub user
gh api user

# Get repository information
gh api repos/{owner}/{repo}
```

The API response can also be requested as JSON fields for scripting.

---

### `gh gist`

Gists can be created and managed from the terminal.

```bash
# Create a gist from a local file
gh gist create deployment.md

# List your gists
gh gist list
```

---

### `gh release`

GitHub releases can be managed directly from the terminal.

```bash
# List releases for a repository
gh release list --repo devops-git-practice

# View a specific release
gh release view <tag>
```

---

### `gh alias`

Aliases can shorten commands that are used frequently.

```bash
# Create a shortcut for listing pull requests
gh alias set prs 'pr list'

# Use the new shortcut
gh prs
```

---

### `gh search repos`

GitHub repositories can be searched from the terminal.

```bash
# Search GitHub repositories related to DevOps
gh search repos devops --limit 10

# Search for Docker-related repositories
gh search repos docker --limit 10
```

---

## Useful Commands Added to `git-commands.md`

Add the following GitHub CLI commands to the existing reference file.

### GitHub CLI

```bash
# Check GitHub CLI version
gh --version

# Authenticate with GitHub
gh auth login

# Check authentication status
gh auth status

# Create a public repository with a README
gh repo create <repo-name> --public --add-readme

# Clone a GitHub repository
gh repo clone <owner>/<repo>

# View repository details
gh repo view <owner>/<repo>

# List repositories
gh repo list

# Open a repository in the browser
gh repo view <owner>/<repo> --web

# Create an issue
gh issue create --repo <owner>/<repo> --title "Title" --body "Description"

# List issues
gh issue list --repo <owner>/<repo>

# View an issue
gh issue view <issue-number> --repo <owner>/<repo>

# Close an issue
gh issue close <issue-number> --repo <owner>/<repo>

# Create a pull request
gh pr create --base main --head <branch>

# List pull requests
gh pr list --repo <owner>/<repo>

# View a pull request
gh pr view <pr-number> --repo <owner>/<repo>

# View pull request changes
gh pr diff <pr-number> --repo <owner>/<repo>

# Check pull request status
gh pr checks <pr-number> --repo <owner>/<repo>

# Merge a pull request
gh pr merge <pr-number> --repo <owner>/<repo> --merge

# List GitHub Actions workflow runs
gh run list --repo <owner>/<repo>

# View a workflow run
gh run view <run-id> --repo <owner>/<repo>

# List workflows
gh workflow list --repo <owner>/<repo>

# Make a GitHub API request
gh api user

# Create a gist
gh gist create <file>

# List releases
gh release list --repo <owner>/<repo>

# Create a command alias
gh alias set <alias> '<command>'

# Search GitHub repositories
gh search repos <search-term>
```

---

## Observations

### GitHub CLI

* GitHub CLI allows GitHub operations to be performed directly from the terminal.
* Authentication is handled with `gh auth login`.
* Repository, issue, pull request and workflow operations can be scripted.
* `--json` output is useful when GitHub CLI commands are used in automation.
* `--repo owner/repo` allows commands to target a specific repository.

### DevOps Use Cases

GitHub CLI can be useful for:

* Automating issue creation after deployment failures.
* Checking pull request status in scripts.
* Monitoring GitHub Actions.
* Automating repository management.
* Integrating GitHub operations into CI/CD scripts.

---

## 5 Key Takeaways

1. **GitHub CLI brings GitHub operations into the terminal**, reducing the need to switch between the terminal and browser.
2. **`gh repo`, `gh issue`, and `gh pr`** can manage repositories, issues and pull requests directly from the command line.
3. **`gh run` and `gh workflow`** are useful for monitoring and automating GitHub Actions workflows.
4. **`gh api` and `--json` output** make GitHub CLI useful for scripting and DevOps automation.
5. **GitHub CLI can automate everyday GitHub tasks**, making it useful for CI/CD and larger DevOps workflows.

---
