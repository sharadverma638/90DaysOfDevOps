# Advanced Git: Merge, Rebase, Stash and Cherry Pick

---

## Task 1: Git Merge

### Create `feature-login`

```bash
# Create and switch to the feature-login branch
git switch -c feature-login

# Creates feature-login and switches to it.
```

### Make the First Commit

Create or update a login documentation file:

```bash
# Create login documentation
cat > login.md <<'EOF'
# Login Feature

The application login feature allows users to securely sign in.
EOF

# Creates login.md with basic login documentation.
```

Stage and commit:

```bash
# Stage the login documentation
git add login.md

# Adds login.md to the staging area.
```

```bash
# Commit the first login change
git commit -m "Add login feature documentation"

# Creates the first commit on feature-login.
```

### Make the Second Commit

```bash
# Add authentication details
cat >> login.md <<'EOF'

## Authentication

Users authenticate with their registered credentials.
EOF

# Adds authentication information to the login documentation.
```

```bash
# Stage the updated login documentation
git add login.md

# Stages the second change.
```

```bash
# Commit the second login change
git commit -m "Add authentication details"

# Creates the second commit on feature-login.
```

### Merge `feature-login` into `main`

```bash
# Switch to the main branch
git switch main

# Moves back to the main branch.
```

```bash
# Merge feature-login into main
git merge feature-login

# Integrates the feature-login branch into main.
```

### Observe the Fast-Forward Merge

Because `main` has not moved forward since `feature-login` was created, Git can move the `main` pointer forward without creating a separate merge commit.

```bash
# View the commit history as a graph
git log --oneline --graph --all

# Displays branches and commits in a compact graph.
```

### Create `feature-signup`

```bash
# Create and switch to the feature-signup branch
git switch -c feature-signup

# Creates feature-signup and switches to it.
```

Make changes and create commits:

```bash
# Create signup documentation
cat > signup.md <<'EOF'
# Signup Feature

New users can create an account through the signup process.
EOF

# Creates documentation for the signup feature.
```

```bash
# Stage the signup documentation
git add signup.md

# Adds signup.md to the staging area.
```

```bash
# Commit the signup feature
git commit -m "Add signup feature"

# Creates the first signup commit.
```

Make another change:

```bash
# Add signup validation details
cat >> signup.md <<'EOF'

## Validation

The signup process validates required user information.
EOF

# Adds validation information to signup.md.
```

```bash
# Stage the validation changes
git add signup.md

# Stages the signup validation changes.
```

```bash
# Commit the validation changes
git commit -m "Add signup validation"

# Creates another commit on feature-signup.
```

### Make a Commit on `main`

```bash
# Switch to main
git switch main

# Moves back to the main branch.
```

```bash
# Create a main branch update
cat > project-status.md <<'EOF'
# Project Status

The DevOps practice project is being developed incrementally.
EOF

# Creates a project status file on main.
```

```bash
# Stage the project status file
git add project-status.md

# Adds the file to the staging area.
```

```bash
# Commit the main branch update
git commit -m "Add project status"

# Creates a new commit on main.
```

### Merge `feature-signup`

```bash
# Merge feature-signup into main
git merge feature-signup

# Merges the signup feature into main.
```

Since both branches have new commits, Git creates a merge commit.

### Observe the Merge Commit

```bash
# View the branch history
git log --oneline --graph --all

# Shows the merge structure and commit history.
```

### Create and Resolve a Merge Conflict

Create a branch:

```bash
# Create a branch for the conflict exercise
git switch -c feature-conflict

# Creates and switches to feature-conflict.
```

Create a file:

```bash
# Create a file for the conflict exercise
cat > config.txt <<'EOF'
environment=development
EOF

# Creates config.txt with a development environment value.
```

```bash
# Stage and commit the initial configuration
git add config.txt
git commit -m "Add environment configuration"

# Saves the initial configuration.
```

Change the same line on the branch:

```bash
# Change the environment on feature-conflict
sed -i 's/environment=development/environment=testing/' config.txt

# Changes the environment value on feature-conflict.
```

```bash
# Commit the feature-conflict change
git add config.txt
git commit -m "Set testing environment"

# Saves the conflicting configuration change.
```

Switch to main and make a different change to the same line:

```bash
# Switch to main
git switch main

# Returns to main.
```

```bash
# Change the same configuration line on main
sed -i 's/environment=development/environment=production/' config.txt

# Changes the same line differently on main.
```

```bash
# Commit the main configuration change
git add config.txt
git commit -m "Set production environment"

# Saves the conflicting main branch change.
```

Merge the branch:

```bash
# Merge the conflicting branch
git merge feature-conflict

# Attempts to merge feature-conflict into main and produces a conflict.
```

Check the conflict:

```bash
# Check the repository status
git status

# Shows the file that contains the merge conflict.
```

Open `config.txt` and resolve the conflict by keeping the desired configuration.

For example:

```text
environment=production
```

Then stage and complete the merge:

```bash
# Stage the resolved conflict
git add config.txt

# Marks the conflict as resolved.
```

```bash
# Complete the merge
git commit -m "Resolve environment configuration conflict"

# Creates the merge commit after resolving the conflict.
```

### Types of Merge

| Fast-Forward Merge                                | Merge Commit                             | Merge Conflict                                                    |
| ------------------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------- |
| Happens when the target branch has no new commits | Happens when both branches have diverged | Happens when Git cannot automatically combine conflicting changes |
| Git moves the branch pointer forward              | Git creates a new merge commit           | Developer must manually resolve the conflicting changes           |
| Does not require a separate merge commit          | Creates a merge commit                   | Merge continues after the conflict is resolved                    |

---

## Task 2: Git Rebase

### Create `feature-dashboard`

```bash
# Create and switch to the dashboard branch
git switch -c feature-dashboard

# Creates feature-dashboard and switches to it.
```

Make the first commit:

```bash
# Create dashboard documentation
cat > dashboard.md <<'EOF'
# Dashboard

The dashboard provides an overview of application activity.
EOF

# Creates dashboard documentation.
```

```bash
# Stage the dashboard documentation
git add dashboard.md

# Adds dashboard.md to the staging area.
```

```bash
# Commit the first dashboard change
git commit -m "Add dashboard documentation"

# Creates the first dashboard commit.
```

Make another commit:

```bash
# Add dashboard metrics
cat >> dashboard.md <<'EOF'

## Metrics

The dashboard displays basic application and deployment metrics.
EOF

# Adds metrics information to the dashboard documentation.
```

```bash
# Stage the dashboard update
git add dashboard.md

# Stages the dashboard changes.
```

```bash
# Commit the dashboard update
git commit -m "Add dashboard metrics"

# Creates another dashboard commit.
```

### Add a Commit to `main`

```bash
# Switch to main
git switch main

# Moves back to main.
```

```bash
# Create a main branch update
cat > monitoring.md <<'EOF'
# Monitoring

Application health and system metrics should be monitored regularly.
EOF

# Creates monitoring documentation on main.
```

```bash
# Stage the monitoring file
git add monitoring.md

# Adds monitoring.md to the staging area.
```

```bash
# Commit the monitoring update
git commit -m "Add monitoring documentation"

# Creates a new commit on main.
```

### Rebase `feature-dashboard` onto `main`

```bash
# Switch to feature-dashboard
git switch feature-dashboard

# Moves to the dashboard branch.
```

```bash
# Rebase feature-dashboard onto main
git rebase main

# Replays the feature-dashboard commits on top of the latest main commit.
```

### View the History

```bash
# View the rebased history
git log --oneline --graph --all

# Displays the branch and commit structure after the rebase.
```

### Rebase vs Merge

| Rebase                                          | Merge                                              |
| ----------------------------------------------- | -------------------------------------------------- |
| Replays commits on top of another branch        | Combines two branch histories                      |
| Produces a more linear history                  | Can preserve the original branching structure      |
| Rewrites commit history                         | Normally does not rewrite existing commits         |
| Useful for cleaning up a private feature branch | Useful when preserving branch history is important |

### Why Should Shared Commits Normally Not Be Rebased?

Rebase creates new versions of commits. If other developers already based work on the original commits, rebasing can cause confusion and require additional work to reconcile the histories.

### When Should You Use Rebase vs Merge?

Use **rebase** when working on a private or local feature branch and you want a cleaner linear history.

Use **merge** when integrating shared branches where preserving the existing history is important.

---

## Task 3: Squash vs Merge Commit

### Create `feature-profile`

```bash
# Create and switch to feature-profile
git switch -c feature-profile

# Creates and switches to the profile feature branch.
```

Make several small commits:

```bash
# Create the profile page
echo "# User Profile" > profile.md
git add profile.md
git commit -m "Add profile page"

# Creates the first small profile commit.
```

```bash
# Add profile information
echo "Users can view their profile information." >> profile.md
git add profile.md
git commit -m "Add profile information"

# Creates the second profile commit.
```

```bash
# Add profile settings
echo "Profile settings can be updated by the user." >> profile.md
git add profile.md
git commit -m "Add profile settings"

# Creates the third profile commit.
```

```bash
# Add profile validation
echo "Profile fields are validated before saving." >> profile.md
git add profile.md
git commit -m "Add profile validation"

# Creates the fourth profile commit.
```

### Squash Merge

```bash
# Switch to main
git switch main

# Moves to main.
```

```bash
# Squash merge the profile branch
git merge --squash feature-profile

# Combines the feature changes into the working tree without creating the feature branch's individual commits.
```

```bash
# Commit the squashed changes
git commit -m "Add user profile feature"

# Creates one commit containing the squashed feature changes.
```

Check the history:

```bash
# View the commit history
git log --oneline --graph --all

# Shows how the squash merge affected the history.
```

### Create `feature-settings`

```bash
# Create and switch to feature-settings
git switch -c feature-settings

# Creates and switches to the settings feature branch.
```

Make several commits:

```bash
# Create settings documentation
echo "# Application Settings" > settings.md
git add settings.md
git commit -m "Add settings page"

# Creates the first settings commit.
```

```bash
# Add notification settings
echo "Users can configure notification preferences." >> settings.md
git add settings.md
git commit -m "Add notification settings"

# Creates the second settings commit.
```

```bash
# Add security settings
echo "Security preferences can be managed from settings." >> settings.md
git add settings.md
git commit -m "Add security settings"

# Creates the third settings commit.
```

Merge normally:

```bash
# Switch to main
git switch main

# Moves to main.
```

```bash
# Merge the settings branch
git merge feature-settings

# Merges the settings branch using the normal merge strategy.
```

### Squash Merge vs Normal Merge

| Squash Merge                                   | Normal Merge                                             |
| ---------------------------------------------- | -------------------------------------------------------- |
| Combines feature changes into one commit       | Preserves the individual feature commits                 |
| Produces a simpler main branch history         | Preserves more detailed development history              |
| Useful when feature commits are small or messy | Useful when individual commits are meaningful            |
| Makes the main history easier to scan          | Provides more detail about how the feature was developed |

---

## Task 4: Git Stash

### Start Work Without Committing

```bash
# Start an unfinished change
echo "Temporary deployment notes" >> deployment.md

# Creates an uncommitted change in deployment.md.
```

Check the status:

```bash
# Check the unfinished changes
git status

# Shows deployment.md as modified.
```

### Stash the Work

```bash
# Save the unfinished work temporarily
git stash push -m "WIP deployment notes"

# Saves the uncommitted changes and cleans the working directory.
```

### List Stashes

```bash
# List all saved stashes
git stash list

# Displays the available stash entries.
```

### Switch Branch and Make Changes

```bash
# Switch to feature-settings
git switch feature-settings

# Moves to feature-settings.
```

Make a temporary change:

```bash
# Add a temporary settings change
echo "Temporary settings note" >> settings.md

# Creates another uncommitted change.
```

Stash it:

```bash
# Save the settings work
git stash push -m "WIP settings notes"

# Saves the settings changes as another stash.
```

### View Multiple Stashes

```bash
# List all stashes
git stash list

# Shows both saved work-in-progress entries.
```

### Apply a Specific Stash

```bash
# Apply a specific stash without deleting it
git stash apply stash@{1}

# Restores the selected stash while keeping it in the stash list.
```

### `git stash pop` vs `git stash apply`

| `git stash pop`                                      | `git stash apply`                           |
| ---------------------------------------------------- | ------------------------------------------- |
| Restores the stash                                   | Restores the stash                          |
| Removes the stash entry after successful application | Keeps the stash entry                       |
| Useful when you no longer need the saved stash       | Useful when you may need to reuse the stash |

### When Is Git Stash Useful?

Git stash is useful when you have unfinished changes but need to switch branches or work on another task without committing incomplete work.

---

## Task 5: Git Cherry Pick

### Create `feature-hotfix`

```bash
# Create and switch to the hotfix branch
git switch -c feature-hotfix

# Creates and switches to feature-hotfix.
```

### Make Three Different Commits

```bash
# Add the first hotfix change
echo "Fix login timeout handling." > hotfix.md
git add hotfix.md
git commit -m "Fix login timeout"

# Creates the first hotfix commit.
```

```bash
# Add the second hotfix change
echo "Improve error logging." >> hotfix.md
git add hotfix.md
git commit -m "Improve error logging"

# Creates the second hotfix commit.
```

```bash
# Add the third hotfix change
echo "Add health check validation." >> hotfix.md
git add hotfix.md
git commit -m "Add health check validation"

# Creates the third hotfix commit.
```

### Find the Commit Hash

```bash
# View the hotfix commits
git log --oneline

# Shows the commit IDs and messages needed for cherry-pick.
```

Example:

```text
c3d4e56 Add health check validation
b2c3d45 Improve error logging
a1b2c34 Fix login timeout
```

The actual commit IDs will be different on your machine.

### Switch to `main`

```bash
# Switch to main
git switch main

# Moves to the main branch.
```

### Cherry Pick Only the Second Commit

Use the actual commit ID of:

```text
Improve error logging
```

Then run:

```bash
# Apply only the second hotfix commit to main
git cherry-pick <second-commit-id>

# Copies the changes from the selected commit into the current branch.
```

### Verify the History

```bash
# View the main branch history
git log --oneline --graph --all

# Shows the cherry-picked commit in the main branch history.
```

### What Does `git cherry-pick` Do?

`git cherry-pick` takes the changes introduced by a specific commit and applies those changes as a new commit on the current branch.

### When Is Cherry Pick Useful?

Cherry-pick is useful when you need one specific fix or change from another branch without merging the entire branch.

### Possible Problems

Cherry-picking can cause conflicts if the selected commit changes code that is different on the current branch. It can also create duplicate changes because the cherry-picked commit gets a new commit identity.

---

## 5 Key Takeaways

1. **Merge** combines branch histories, while **rebase** replays commits to create a more linear history.
2. **Squash merging** combines multiple feature commits into a single commit.
3. **Git stash** temporarily saves unfinished work so you can switch branches without committing it.
4. **Cherry-pick** applies one specific commit from another branch without merging the entire branch.
5. **Merge conflicts** happen when Git cannot automatically combine changes, and they must be resolved manually before completing the merge.
