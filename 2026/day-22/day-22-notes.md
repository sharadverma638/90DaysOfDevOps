# Introduction to Git: Your First Repository

---

## Note

For the Git commands reference, instead of creating a `git-commands.md` file, I used a downloaded Git cheat sheet and added it to this day's directory as:

`git-commands.png`

You can view it here:

[View Git Commands Cheat Sheet](./git-commands.png)

> Note: The Day 22 README asks for a `git-commands.md` file. I used `git-commands.png` as my Git commands reference instead.

---

## Task 1: Install and Configure Git

### Verify Git Installation

```bash
# Check whether Git is installed
git --version

# Displays the installed Git version.
```

Example:

```text
git version 2.43.0
```

### Configure Git Name

```bash
# Set the Git username
git config --global user.name "Sharad Verma"

# Sets the name Git will use for commits.
```

### Configure Git Email

```bash
# Set the Git email
git config --global user.email "sharad.verma@example.com"

# Sets the email Git will use for commits.
```

### Verify Git Configuration

```bash
# View the Git configuration
git config --list

# Displays the configured Git settings.
```

---

## Task 2: Create Your Git Project

### Create the Project Directory

```bash
# Create the Git practice project
mkdir devops-git-practice
cd devops-git-practice

# Creates the project directory and enters it.
```

### Initialize the Git Repository

```bash
# Initialize the Git repository
git init

# Creates the hidden .git directory and initializes Git.
```

Example:

```text
Initialized empty Git repository in ~/devops-git-practice/.git/
```

### Check Repository Status

```bash
# Check the current repository status
git status

# Shows the current branch and the state of files.
```

Example:

```text
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

### Explore the `.git` Directory

```bash
# List the contents of the .git directory
ls -la .git

# Shows the internal files and directories created by Git.
```

The `.git` directory contains Git's internal repository data, including information about commits, branches, configuration, and references.

---

## Task 3: Create Your Git Commands Reference

Create the required file:

`git-commands.md`

The file will be maintained throughout the Git and GitHub section of the challenge.

### Setup & Config

| Command                          | What it does                     | Example                                                     |
| -------------------------------- | -------------------------------- | ----------------------------------------------------------- |
| `git --version`                  | Shows the installed Git version. | `git --version`                                             |
| `git config --global user.name`  | Sets the global Git username.    | `git config --global user.name "Sharad Verma"`              |
| `git config --global user.email` | Sets the global Git email.       | `git config --global user.email "sharad.verma@example.com"` |
| `git config --list`              | Displays Git configuration.      | `git config --list`                                         |

### Basic Workflow

| Command             | What it does                                 | Example                                      |
| ------------------- | -------------------------------------------- | -------------------------------------------- |
| `git init`          | Initializes a Git repository.                | `git init`                                   |
| `git status`        | Shows the current repository status.         | `git status`                                 |
| `git add`           | Adds changes to the staging area.            | `git add git-commands.md`                    |
| `git add .`         | Stages all changes in the current directory. | `git add .`                                  |
| `git commit`        | Saves staged changes as a commit.            | `git commit -m "Add Git commands reference"` |
| `git log`           | Shows commit history.                        | `git log`                                    |
| `git log --oneline` | Shows compact commit history.                | `git log --oneline`                          |

### Viewing Changes

| Command             | What it does               | Example             |
| ------------------- | -------------------------- | ------------------- |
| `git diff`          | Shows unstaged changes.    | `git diff`          |
| `git diff --staged` | Shows staged changes.      | `git diff --staged` |
| `git show`          | Shows details of a commit. | `git show HEAD`     |

---

## Task 4: Stage and Commit

### Stage `git-commands.md`

```bash
# Stage the Git commands reference
git add git-commands.md

# Adds git-commands.md to the staging area.
```

### Check What Is Staged

```bash
# Check the staged changes
git status

# Shows the files that are staged and ready to commit.
```

Example:

```text
Changes to be committed:
  new file:   git-commands.md
```

### Create the First Commit

```bash
# Create the first meaningful commit
git commit -m "Add Git commands reference"

# Saves the staged Git commands reference as the first commit.
```

Example:

```text
[main abc1234] Add Git commands reference
 1 file changed, 30 insertions(+)
 create mode 100644 git-commands.md
```

### View Commit History

```bash
# View the commit history
git log

# Displays commit ID, author, date, and commit message.
```

---

## Task 5: Make More Changes and Build History

The Git commands reference is a living document, so update it as new commands are learned.

### First Update

Add more Git commands to `git-commands.md`.

```bash
# Check what changed
git diff

# Shows the changes made since the previous commit.
```

```bash
# Stage the updated Git commands reference
git add git-commands.md

# Adds the updated file to the staging area.
```

```bash
# Commit the first update
git commit -m "Expand Git commands reference"

# Saves the first update as a new commit.
```

### Second Update

Add another group of useful commands to `git-commands.md`.

```bash
# Check the repository status
git status

# Shows the current state of the working directory and staging area.
```

```bash
# Stage the second update
git add git-commands.md

# Adds the updated file to the staging area.
```

```bash
# Commit the second update
git commit -m "Add Git change inspection commands"

# Saves the second update as a new commit.
```

### Third Update

Add more notes or commands to `git-commands.md`.

```bash
# Review the latest changes
git diff

# Shows the changes that will be included in the next commit.
```

```bash
# Stage the third update
git add git-commands.md

# Adds the latest changes to the staging area.
```

```bash
# Commit the third update
git commit -m "Complete Git commands reference"

# Saves the third update as a new commit.
```

### View Compact Commit History

```bash
# View the complete history in compact format
git log --oneline

# Displays each commit on one line with its short commit ID and message.
```

Example:

```text
d4e5f67 Complete Git commands reference
c3d4e56 Add Git change inspection commands
b2c3d45 Expand Git commands reference
a1b2c34 Add Git commands reference
```

The actual commit IDs will be different on your machine.

---

## Task 6: Understand the Git Workflow

Create:

`day-22-notes.md`

### 1. What is the difference between `git add` and `git commit`?

`git add` moves selected changes from the working directory to the staging area.

`git commit` saves the staged changes as a permanent commit in the Git repository.

### 2. What does the staging area do? Why doesn't Git just commit directly?

The staging area allows us to select exactly which changes should be included in the next commit.

This gives us control over the contents of each commit.

### 3. What information does `git log` show you?

`git log` shows the commit history of the repository.

It normally includes:

* Commit ID
* Author
* Date
* Commit message

### 4. What is the `.git/` folder and what happens if you delete it?

The `.git/` folder contains the internal Git data for the repository.

It stores information required for Git to track commits, branches, configuration, and repository history.

If `.git/` is deleted, the directory is no longer a Git repository and the local Git history is lost.

### 5. What is the difference between a working directory, staging area, and repository?

| Working Directory                               | Staging Area                                   | Repository                                                |
| ----------------------------------------------- | ---------------------------------------------- | --------------------------------------------------------- |
| Contains the files we are currently working on. | Contains changes selected for the next commit. | Contains committed changes and project history.           |
| Changes happen here first.                      | Changes are prepared here using `git add`.     | Changes are permanently recorded here using `git commit`. |

### Git Workflow

```text
Working Directory
       |
       | git add
       v
Staging Area
       |
       | git commit
       v
Repository
```

---

## 5 Key Takeaways

1. **Git tracks changes** and maintains the history of a project.
2. **`git add` stages changes**, while **`git commit` saves staged changes** in the repository.
3. **The staging area** lets us select exactly which changes should be included in a commit.
4. **The `.git/` directory** contains the internal data and history of a Git repository.
5. **Regular commits with meaningful messages** create a clean and useful project history.
