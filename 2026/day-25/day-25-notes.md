# Git Reset vs Revert and Branching Strategies

---

## Task 1: Git Reset - Hands-On

Git reset moves the current branch pointer to another commit. The three reset modes behave differently.

### Create 3 commits

```bash
# Create commit A
echo "Login deployment notes" > deployment.md
git add deployment.md
git commit -m "Add deployment notes"

# Create commit B
echo "Login monitoring notes" > monitoring.md
git add monitoring.md
git commit -m "Add monitoring notes"

# Create commit C
echo "Login troubleshooting notes" > troubleshooting.md
git add troubleshooting.md
git commit -m "Add troubleshooting notes"

# Show the three commits
git log --oneline -3
# The output should show commits C, B and A.
```

---

### Use `git reset --soft`

```bash
# Move HEAD back one commit while keeping changes staged
git reset --soft HEAD~1

# Check the repository state
git status
# The changes from the removed commit remain staged.
```

`--soft` moves HEAD but keeps the changes in the staging area.

Now re-commit the staged changes:

```bash
# Re-create the commit after the soft reset
git commit -m "Add troubleshooting notes"
# The changes are committed again.
```

---

### Use `git reset --mixed`

```bash
# Move HEAD back one commit and unstage the changes
git reset --mixed HEAD~1

# Check the repository state
git status
# The changes remain in the working directory but are no longer staged.
```

`--mixed` is the default reset mode. It moves HEAD and clears the staging area, but keeps the working directory changes.

Now stage and commit again:

```bash
# Stage the changes again
git add troubleshooting.md

# Commit the changes again
git commit -m "Add troubleshooting notes"
# The changes are saved as a new commit.
```

---

### Use `git reset --hard`

```bash
# Move HEAD back one commit and discard working directory changes
git reset --hard HEAD~1

# Check the repository state
git status
# Changes from the removed commit are discarded from the working directory.
```

`--hard` changes HEAD, the staging area, and the working directory. It can permanently discard uncommitted changes.

Create a new commit so the project can continue:

```bash
# Recreate the troubleshooting file after the hard reset
echo "Updated login troubleshooting notes" > troubleshooting.md
git add troubleshooting.md
git commit -m "Restore troubleshooting notes"

# Show the current history
git log --oneline -5
# The history now reflects the hard reset and the new commit.
```

### Reset comparison

| Reset mode | What happens                                                  |
| ---------- | ------------------------------------------------------------- |
| `--soft`   | Moves HEAD and keeps changes staged                           |
| `--mixed`  | Moves HEAD, unstages changes, keeps working directory changes |
| `--hard`   | Moves HEAD and discards staged and working directory changes  |

### Which one is destructive?

`git reset --hard` is destructive because it can remove changes from the staging area and working directory.

### When would I use each?

* `--soft`: when I want to undo a commit but keep everything staged for a new commit.
* `--mixed`: when I want to undo a commit and review or modify the changes before staging them again.
* `--hard`: when I am sure I want to discard the changes.

### Should reset be used on pushed commits?

Normally, avoid rewriting already-pushed shared history with `git reset`, especially on `main`. For shared branches, `git revert` is usually safer because it adds a new commit instead of rewriting existing history.

---

## Task 2: Git Revert - Hands-On

Create three separate commits so the middle commit can be reverted safely.

```bash
# Create commit X
echo "Payment service deployment notes" > payment.md
git add payment.md
git commit -m "Add payment service notes"

# Create commit Y
echo "Payment validation notes" > payment-validation.md
git add payment-validation.md
git commit -m "Add payment validation notes"

# Create commit Z
echo "Payment monitoring notes" > payment-monitoring.md
git add payment-monitoring.md
git commit -m "Add payment monitoring notes"

# Save the hash of commit Y
Y_HASH=$(git rev-parse HEAD~1)

# Display the three commits
git log --oneline -3
# The output should show Z, Y and X.
```

### Revert commit Y

```bash
# Create a new commit that reverses commit Y
git revert "$Y_HASH"

# Check the repository history
git log --oneline -5
# Commit Y should still appear in the history.
# A new revert commit should appear above it.
```

### What happened?

`git revert` did not remove commit Y from history. Instead, Git created a new commit that reverses the changes introduced by commit Y.

### Reset vs Revert

| `git reset`                                        | `git revert`                                         |
| -------------------------------------------------- | ---------------------------------------------------- |
| Moves the branch pointer to another commit         | Creates a new commit that reverses an earlier commit |
| Can remove commits from the visible branch history | Keeps the original commit in history                 |
| Can rewrite history                                | Does not rewrite existing history                    |
| Usually better for local, unpublished commits      | Safer for shared or pushed branches                  |
| Can be destructive with `--hard`                   | Normally preserves the existing history              |

### When would I use revert vs reset?

I would use `reset` for local commits that have not been shared with others.

I would use `revert` when a commit has already been pushed to a shared branch and needs to be undone safely.

---

## Task 3: Reset vs Revert - Summary

|                                  | `git reset`                                              | `git revert`                                         |
| -------------------------------- | -------------------------------------------------------- | ---------------------------------------------------- |
| What it does                     | Moves the branch pointer to another commit               | Creates a new commit that reverses an earlier commit |
| Removes commit from history?     | It can remove the commit from the current branch history | No, the original commit remains in history           |
| Safe for shared/pushed branches? | Usually no, because it can rewrite history               | Yes, generally safer for shared branches             |
| When to use                      | Local commits that have not been shared                  | Changes that need to be undone after being shared    |

---

## Task 4: Branching Strategies

### 1. GitFlow

GitFlow uses different branch types for different stages of development.

Main branches include:

* `main` - production-ready code
* `develop` - integration branch
* `feature/*` - new features
* `release/*` - release preparation
* `hotfix/*` - urgent production fixes

### Flow

```text
main
  |
  +---- develop
          |
          +---- feature/login
          |
          +---- feature/signup
          |
          +---- release/1.0
          |
          +---- hotfix/payment
```

### When it is used

GitFlow can be useful for projects that have planned releases and multiple stages before production.

### Pros

* Clear separation between development and production
* Dedicated release and hotfix branches
* Works well with scheduled release cycles

### Cons

* More branches to manage
* More complicated workflow
* Can create longer-lived branches

---

### 2. GitHub Flow

GitHub Flow keeps the workflow simple. The main branch stays deployable, and changes are developed on short-lived feature branches.

### Flow

```text
main
  |
  +---- feature/login
  |          |
  |          +---- Pull Request
  |                   |
  +-------------------+
          |
        main
```

### When it is used

GitHub Flow works well for teams that deploy frequently and use pull requests for code review.

### Pros

* Simple workflow
* Short-lived branches
* Pull requests provide review
* Works well with continuous delivery

### Cons

* Less structure for scheduled release management
* Release management may need additional processes
* Large teams may need extra conventions

---

### 3. Trunk-Based Development

Trunk-Based Development keeps the main branch as the central integration point. Developers make small changes and use short-lived branches or commit directly to the main branch depending on the team workflow.

### Flow

```text
main
  |
  +---- short-lived change
  |            |
  |            +---- Pull Request
  |                     |
  +---------------------+
            |
           main
```

### When it is used

It is useful for teams that want frequent integration and small, continuously delivered changes.

### Pros

* Frequent integration
* Short-lived branches
* Reduces long-running branch divergence
* Works well with automated CI/CD

### Cons

* Requires strong automated testing
* Requires disciplined small changes
* Teams need good CI practices

---

### Which strategy for a startup shipping fast?

For a startup shipping frequently, I would choose **GitHub Flow** because it keeps the branching model simple and works well with pull requests and continuous delivery.

### Which strategy for a large team with scheduled releases?

For a large team with scheduled releases, I would choose **GitFlow** because its release and hotfix branches provide more structure around planned releases.

### Open-source project example

I checked the Kubernetes documentation repository. Kubernetes uses `main` for general development, while release-specific work can use development branches such as `dev-1.38`, and release branches are used for backports. This means its workflow does not fit perfectly into only one of the three simplified models above.

A simplified view is:

```text
main
 |
 +---- dev-1.38
 |
 +---- release-1.37
 |
 +---- contributor feature branch
```

---

## Task 5: Git Commands Reference Update

Update the existing `git-commands.md` from the previous days.

### Setup & Config

```bash
# Check the installed Git version
git --version

# Configure Git username
git config --global user.name "Sharad Verma"

# Configure Git email
git config --global user.email "sharad.verma@example.com"

# View Git configuration
git config --list
```

### Basic Workflow

```bash
# Check repository status
git status

# Stage one file
git add deployment.md

# Stage all changes
git add .

# Create a commit
git commit -m "Update deployment notes"

# View commit history
git log

# View compact commit history
git log --oneline

# View unstaged changes
git diff

# View staged changes
git diff --staged
```

### Branching

```bash
# List local branches
git branch

# Create a branch
git branch feature-login

# Switch to a branch
git checkout feature-login

# Create and switch to a branch
git checkout -b feature-signup

# Switch branches using the newer command
git switch main

# Create and switch to a new branch
git switch -c feature-dashboard
```

### Remote

```bash
# Push the current branch
git push origin main

# Download remote changes and integrate them
git pull origin main

# Download remote changes without merging
git fetch origin

# Clone a repository
git clone <repository-url>
```

A **fork** is a GitHub copy of a repository under your own GitHub account. A **clone** is a local copy of a repository on your computer.

### Merging & Rebasing

```bash
# Merge another branch into the current branch
git merge feature-login

# Rebase the current branch onto main
git rebase main

# View branch history as a graph
git log --oneline --graph --all
```

### Stash & Cherry Pick

```bash
# Save uncommitted work
git stash

# List saved stashes
git stash list

# Apply a stash and remove it from the stash list
git stash pop

# Apply a stash without removing it
git stash apply

# Apply one specific commit to the current branch
git cherry-pick <commit-hash>
```

### Reset & Revert

```bash
# Move HEAD back while keeping changes staged
git reset --soft HEAD~1

# Move HEAD back and unstage changes
git reset --mixed HEAD~1

# Move HEAD back and discard changes
git reset --hard HEAD~1

# Create a new commit that reverses an earlier commit
git revert <commit-hash>

# View the history of HEAD movements
git reflog
```

`git reflog` is useful when a commit appears to have disappeared after a reset because it records previous positions of HEAD.

---

## Observations

### Reset

* `--soft` keeps changes staged.
* `--mixed` keeps changes but unstages them.
* `--hard` discards changes from the working directory.
* Reset can rewrite branch history.

### Revert

* Revert creates a new commit.
* The original commit remains in history.
* Revert is generally safer for shared branches.

### Branching Strategies

* GitFlow provides more structure for scheduled releases.
* GitHub Flow keeps the workflow simple around `main` and feature branches.
* Trunk-Based Development focuses on frequent integration and short-lived changes.
* Real projects may combine ideas from multiple branching strategies.

---

## 5 Key Takeaways

1. **`git reset` moves HEAD** and can change or remove commits from the current branch history.
2. **`git revert` creates a new commit** that safely reverses the changes of an earlier commit.
3. **`--soft`, `--mixed`, and `--hard`** differ in how they handle the staging area and working directory.
4. **Branching strategies** such as GitFlow, GitHub Flow, and Trunk-Based Development provide different ways to manage development and releases.
5. **Reset is mainly useful for local commits**, while **revert is generally safer for commits already shared with others**.
