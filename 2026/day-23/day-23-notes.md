# Git Branching and Working with GitHub

---

## Task 1: Understanding Branches

### 1. What is a branch in Git?

A branch is a separate line of development in Git. It allows us to work on features, fixes, or experiments without directly changing the `main` branch.

### 2. Why do we use branches instead of committing everything to `main`?

Branches allow developers to work on changes separately from the main code. This helps keep `main` stable while new features or fixes are being developed.

### 3. What is `HEAD` in Git?

`HEAD` is a pointer that tells Git which branch or commit we are currently working on.

### 4. What happens to your files when you switch branches?

When we switch branches, Git updates the working directory to match the files and commits of the selected branch.

---

## Task 2: Branching Commands - Hands-On

### 1. List all branches

```bash
# List all local branches
git branch

# Shows all local branches and marks the current branch with *.
```

### 2. Create `feature-1`

```bash
# Create the feature-1 branch
git branch feature-1

# Creates a new branch called feature-1.
```

### 3. Switch to `feature-1`

```bash
# Switch to feature-1
git switch feature-1

# Moves the working directory to the feature-1 branch.
```

### 4. Create and switch to `feature-2`

```bash
# Create feature-2 and switch to it
git switch -c feature-2

# Creates feature-2 and switches to it in one command.
```

### 5. Switch between branches

```bash
# Switch back to feature-1
git switch feature-1

# Moves the working directory to feature-1.
```

```bash
# Switch to main
git switch main

# Moves the working directory back to the main branch.
```

### `git switch` vs `git checkout`

| `git switch`                                   | `git checkout`                                           |
| ---------------------------------------------- | -------------------------------------------------------- |
| Modern command designed for switching branches | Older command with multiple purposes                     |
| Mainly used for branch operations              | Can switch branches, restore files, and checkout commits |
| Clearer for branch switching                   | More general-purpose                                     |

### 6. Make a commit on `feature-1`

For this project, we will add a simple deployment documentation file.

First switch to `feature-1`:

```bash
# Switch to the feature-1 branch
git switch feature-1

# Moves the working directory to feature-1.
```

Create `deployment.md`:

```bash
# Create a deployment documentation file
cat > deployment.md <<'EOF'
# Deployment Notes

This file contains basic deployment notes for the DevOps practice project.

## Deployment Flow

1. Build the application.
2. Test the application.
3. Deploy the application.
4. Verify the deployment.
EOF

# Creates deployment.md with a simple deployment workflow.
```

Check the changes:

```bash
# Check the modified and untracked files
git status

# Shows deployment.md as a new file.
```

Stage the file:

```bash
# Stage the deployment documentation
git add deployment.md

# Adds deployment.md to the staging area.
```

Create the commit:

```bash
# Commit the feature-1 change
git commit -m "Add deployment documentation"

# Creates a commit that exists on feature-1.
```

### 7. Switch to `main` and verify the commit is not there

```bash
# Switch back to main
git switch main

# Moves the working directory back to main.
```

Check the history:

```bash
# View the main branch history
git log --oneline

# Shows the commits that exist on main.
```

The commit:

```text
Add deployment documentation
```

should not appear on `main` because it was created only on `feature-1`.

You can also verify that `deployment.md` is not present on `main`:

```bash
# Check whether deployment.md exists on main
ls

# Lists the files currently available on the main branch.
```

### 8. Delete a branch that is no longer needed

`feature-2` was created for practice and is no longer needed.

```bash
# Delete the unused feature-2 branch
git branch -d feature-2

# Deletes the feature-2 branch.
```

### 9. Add branching commands to `git-commands.md`

Add these commands to the existing Git commands reference:

```text
git branch
git branch <branch-name>
git switch <branch-name>
git switch -c <branch-name>
git branch -d <branch-name>
git log --oneline
```

---

## Task 3: Push to GitHub

### 1. Create a new GitHub repository

Create a new GitHub repository named:

```text
devops-git-practice
```

Do **not** initialize it with a README because the local repository already exists.

### 2. Connect the local repository to GitHub

After creating the GitHub repository, add it as the `origin` remote.

```bash
# Add the GitHub repository as the origin remote
git remote add origin https://github.com/<your-username>/devops-git-practice.git

# Connects the local repository to the GitHub repository.
```

Replace `<your-username>` with your actual GitHub username.

Verify the remote:

```bash
# Check the configured remote
git remote -v

# Shows the fetch and push URLs for origin.
```

### 3. Push `main` to GitHub

```bash
# Push the main branch to GitHub
git push -u origin main

# Uploads the local main branch to GitHub and sets its upstream branch.
```

### 4. Push `feature-1` to GitHub

```bash
# Switch to feature-1
git switch feature-1

# Moves to the feature-1 branch.
```

```bash
# Push feature-1 to GitHub
git push -u origin feature-1

# Uploads feature-1 to GitHub and sets its upstream branch.
```

### 5. Verify both branches on GitHub

Open the GitHub repository and verify that these branches are visible:

```text
main
feature-1
```

### 6. Difference between `origin` and `upstream`

| `origin`                                                      | `upstream`                                                         |
| ------------------------------------------------------------- | ------------------------------------------------------------------ |
| Usually refers to the remote repository we directly work with | Usually refers to the original repository when working with a fork |
| Commonly used for pushing and pulling our own repository      | Commonly used for getting changes from the original repository     |
| Example: `origin/main`                                        | Example: `upstream/main`                                           |

For our `devops-git-practice` repository, `origin` will be the GitHub repository we created.

---

## Task 4: Pull from GitHub

### 1. Make a change directly on GitHub

Open the `devops-git-practice` repository on GitHub.

Edit `deployment.md` using the GitHub editor and add:

```text
## Verification

After deployment, verify that the application is running correctly.
```

Commit this change directly on GitHub.

### 2. Pull the change into the local repository

First switch to `main` if the GitHub change was made on `main`:

```bash
# Switch to the main branch
git switch main

# Moves the working directory to main.
```

Pull the latest change:

```bash
# Pull the latest changes from GitHub
git pull origin main

# Downloads the latest changes and integrates them into the local main branch.
```

### 3. Difference between `git fetch` and `git pull`

| `git fetch`                                                          | `git pull`                                                |
| -------------------------------------------------------------------- | --------------------------------------------------------- |
| Downloads changes from the remote repository                         | Downloads changes from the remote repository              |
| Does not automatically integrate the changes into the current branch | Integrates the downloaded changes into the current branch |
| Useful when you want to inspect remote changes first                 | Useful when you want to update your local branch directly |

In simple terms:

```text
git fetch = Download changes

git pull = Download + integrate changes
```

---

## Task 5: Clone vs Fork

### 1. Clone a public repository

Choose any public GitHub repository.

Example:

```bash
# Clone a public repository
git clone https://github.com/TrainWithShubham/90DaysOfDevOps.git

# Downloads the public repository to the local machine.
```

### 2. Fork the same repository

Open the same repository on GitHub and create a fork under your GitHub account.

Then clone your fork:

```bash
# Clone your fork of the repository
git clone https://github.com/<your-username>/90DaysOfDevOps.git

# Downloads your GitHub fork to the local machine.
```

Replace `<your-username>` with your actual GitHub username.

### 3. Difference between clone and fork

| Clone                                     | Fork                                                         |
| ----------------------------------------- | ------------------------------------------------------------ |
| Creates a local copy of a repository      | Creates a copy of a repository under your GitHub account     |
| A Git operation                           | A GitHub feature                                             |
| Used to work with a repository locally    | Used to create your own GitHub version of another repository |
| Does not create another GitHub repository | Creates another GitHub repository                            |

### When would you clone vs fork?

**Clone:** Use it when you want to download a repository to your local machine and work with it.

**Fork:** Use it when you want your own GitHub copy of another repository, especially when you do not have direct write access to the original repository.

### Keep a fork synchronized with the original repository

Add the original repository as `upstream`:

```bash
# Add the original repository as upstream
git remote add upstream https://github.com/TrainWithShubham/90DaysOfDevOps.git

# Connects your local fork to the original repository.
```

Check the configured remotes:

```bash
# View configured remotes
git remote -v

# Shows origin and upstream remote URLs.
```

Fetch changes from the original repository:

```bash
# Download changes from the original repository
git fetch upstream

# Downloads the latest changes from upstream without changing the current branch.
```

Switch to the main branch:

```bash
# Switch to main
git switch main

# Moves to the local main branch.
```

Merge the latest upstream changes:

```bash
# Merge the upstream main branch
git merge upstream/main

# Integrates the latest changes from the original repository into local main.
```

Push the updated branch to your fork:

```bash
# Push the synchronized main branch
git push origin main

# Updates your GitHub fork with the latest changes.
```

---

## 5 Key Takeaways

1. **Branches** allow us to work on features and fixes separately from `main`.
2. **`HEAD`** points to the branch or commit we are currently working on.
3. **`git switch`** is the modern command for switching between branches.
4. **`origin` and `upstream`** help manage our own remote repository and the original repository when working with forks.
5. **Clone and fork are different:** cloning creates a local copy, while forking creates a GitHub copy under your account.
