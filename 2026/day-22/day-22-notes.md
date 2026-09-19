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

### Check Git Installation

```bash
# Check whether Git is installed
git --version

# Displays the installed Git version.
```

### Configure Git Name

```bash
# Set your Git username
git config --global user.name "Your Name"

# Sets the name Git will use for your commits.
```

### Configure Git Email

```bash
# Set your Git email
git config --global user.email "your-email@example.com"

# Sets the email Git will use for your commits.
```

### Verify Git Configuration

```bash
# View Git configuration
git config --list

# Displays the configured Git settings.
```

---

## Task 2: Create Your Git Project

### Create the Project Directory

```bash
# Create the Git practice directory
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

### Check Repository Status

```bash
# Check the current Git status
git status

# Shows the current branch and the state of files in the repository.
```

### Explore the .git Directory

```bash
# List the contents of the hidden .git directory
ls -la .git

# Shows the files and directories Git created for repository management.
```

---

## Task 3: Create Your Git Commands Reference

Instead of creating `git-commands.md`, I added the downloaded Git cheat sheet as:

`git-commands.png`

The image contains the Git commands reference.

[View Git Commands Cheat Sheet](./git-commands.png)

The reference covers commands under:

* Setup & Config
* Basic Workflow
* Viewing Changes

---

## Task 4: Stage and Commit

### Stage the Git Commands Reference

```bash
# Stage the Git commands cheat sheet
git add git-commands.png

# Adds the image to the staging area.
```

### Check What Is Staged

```bash
# Check the staged changes
git status

# Shows which files are staged and ready to commit.
```

### Create the First Commit

```bash
# Create the first meaningful commit
git commit -m "Add Git commands reference"

# Saves the staged changes as a commit in the repository.
```

### View Commit History

```bash
# View the Git commit history
git log

# Shows the commit history with details.
```

---

## Task 5: Make More Changes and Build History

Make changes to the repository and create at least 3 additional commits.

### Check Changes

```bash
# Check changes in the working directory
git status

# Shows files that have been modified or added.
```

### View Detailed Changes

```bash
# View changes before staging
git diff

# Shows the differences between the working directory and the last commit.
```

### Stage Changes

```bash
# Stage the updated files
git add .

# Adds the changes to the staging area.
```

### Create Another Commit

```bash
# Commit the changes
git commit -m "Update Git practice files"

# Saves the staged changes as a new commit.
```

Repeat the process until you have at least 3 commits in your history.

### View Compact History

```bash
# View commit history in compact format
git log --oneline

# Shows each commit on a single line with its short commit ID and message.
```

---

## Task 6: Understand the Git Workflow

Create `day-22-notes.md` and add the following answers.

### 1. What is the difference between `git add` and `git commit`?

`git add` moves selected changes from the working directory to the staging area.

`git commit` saves the staged changes permanently in the Git repository as a commit.

### 2. What does the staging area do? Why doesn't Git just commit directly?

The staging area allows us to select exactly which changes we want to include in the next commit.

This gives us control over what goes into each commit instead of committing every change automatically.

### 3. What information does `git log` show you?

`git log` shows the commit history of the repository.

It normally shows information such as:

* Commit ID
* Author
* Date
* Commit message

### 4. What is the `.git/` folder and what happens if you delete it?

The `.git/` folder contains the internal Git data for the repository, including commit history, configuration, references, and other Git metadata.

If `.git/` is deleted, the directory is no longer a Git repository and its Git history is lost from that local repository.

### 5. What is the difference between a working directory, staging area, and repository?

**Working Directory**

The files where we currently make changes.

**Staging Area**

The area where we select changes that should be included in the next commit.

**Repository**

The Git database where committed changes and history are stored.

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

## 5 Key Takeaways:

1. **Git tracks changes** in files and keeps a history of the project.
2. **`git add` stages changes**, while **`git commit` saves those staged changes** to the repository.
3. **The staging area** lets you choose exactly which changes should go into the next commit.
4. **The `.git/` directory** contains the internal data and history of a Git repository.
5. **Commit history** helps you track what changed, when it changed, and who made the change.
