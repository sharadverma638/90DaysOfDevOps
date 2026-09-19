# DevOps Revision and Self-Assessment

---

## Task 1: Self-Assessment Checklist

I reviewed everything covered so far and marked each area honestly.

### Linux

| Skill                                                                   | Status                 |
| ----------------------------------------------------------------------- | ---------------------- |
| Navigate the file system, create/move/delete files and directories      | Can do confidently |
| Manage processes - list, kill, background/foreground                    | Can do confidently |
| Work with systemd - start, stop, enable, check status of services       |  Can do confidently |
| Read and edit text files using vi/vim or nano                           |  Can do confidently |
| Troubleshoot CPU, memory, and disk issues using top, free, df, du       |  Can do confidently |
| Explain the Linux file system hierarchy                                 |  Can do confidently |
| Create users and groups, manage passwords                               |  Can do confidently |
| Set file permissions using chmod                                        |  Can do confidently |
| Change file ownership with chown and chgrp                              |  Can do confidently |
| Create and manage LVM volumes                                           |  Can do confidently |
| Check network connectivity using ping, curl, netstat, ss, dig, nslookup |  Need to revisit    |
| Explain DNS, IP addressing, subnets, and common ports                   |  Need to revisit    |

### Shell Scripting

| Skill                                                        | Status                 |
| ------------------------------------------------------------ | ---------------------- |
| Write a script with variables, arguments, and user input     |  Can do confidently |
| Use if/elif/else and case statements                         |  Can do confidently |
| Write for, while, and until loops                            |  Can do confidently |
| Define and call functions with arguments and return values   |  Can do confidently |
| Use grep, awk, sed, sort, and uniq for text processing       |  Can do confidently |
| Handle errors with set -e, set -u, set -o pipefail, and trap |  Can do confidently |
| Schedule scripts with crontab                                |  Can do confidently |

### Git and GitHub

| Skill                                                            | Status                 |
| ---------------------------------------------------------------- | ---------------------- |
| Initialize a repository, stage, commit, and view history         |  Can do confidently |
| Create and switch branches                                       |  Can do confidently |
| Push to and pull from GitHub                                     |  Can do confidently |
| Explain clone vs fork                                            |  Can do confidently |
| Merge branches - fast-forward vs merge commit                    |  Can do confidently |
| Rebase a branch and explain when to use it vs merge              |  Need to revisit    |
| Use git stash and git stash pop                                  |  Can do confidently |
| Cherry-pick a commit from another branch                         |  Can do confidently |
| Explain squash merge vs regular merge                            |  Can do confidently |
| Use git reset - soft, mixed, and hard - and git revert           |  Can do confidently |
| Explain GitFlow, GitHub Flow, and Trunk-Based Development        |  Can do confidently |
| Use GitHub CLI to create repositories, pull requests, and issues |  Can do confidently |

---

## Task 2: Revisit My Weak Spots

I selected these three areas for additional hands-on practice.

### Weak Spot 1: Check Network Connectivity

The commands `ping`, `curl`, `netstat`, `ss`, `dig`, and `nslookup` are used for different parts of network troubleshooting.

```bash
# Test whether a host is reachable
ping -c 4 google.com

# Check whether a web service responds
curl -I https://google.com

# Check listening network connections and ports
sudo ss -tulpn

# Check DNS resolution
dig google.com

# Query DNS using nslookup
nslookup google.com
```

### What I Re-learned

I re-learned that each network command checks something different. `ping` checks reachability, `curl` checks the application response, `ss` checks ports and connections, and `dig` and `nslookup` check DNS. Using them together makes troubleshooting easier.

---

### Weak Spot 2: DNS Resolution, IP Addressing, Subnets, and Common Ports

DNS converts a domain name such as `google.com` into an IP address. IP addressing identifies devices, while subnets divide networks into smaller sections.

```bash
# Resolve a domain name to IP addresses
dig google.com

# Query DNS using nslookup
nslookup google.com

# Display local IP addresses
ip addr

# Display routing information
ip route

# Show listening TCP and UDP ports
sudo ss -tulpn
```

Common ports I reviewed:

| Port | Common Service          |
| ---: | ----------------------- |
|   22 | SSH                     |
|   53 | DNS                     |
|   80 | HTTP                    |
|  443 | HTTPS                   |
| 3306 | MySQL                   |
| 5432 | PostgreSQL              |
| 8080 | Common application port |

### What I Re-learned

I re-learned how DNS, IP addresses, subnets, and ports work together. DNS finds the IP address, the IP identifies the host, and the port identifies the service. Subnets help organize and separate networks.

---

### Weak Spot 3: Rebase and When to Use It vs Merge

I revisited rebasing using the `devops-git-practice` project.

```bash
# Switch to the main branch and update it
git switch main
git pull origin main

# Create a dashboard feature branch
git switch -c feature-dashboard

# Make feature commits
echo "Dashboard layout" > dashboard.md
git add dashboard.md
git commit -m "Add dashboard layout"

echo "Dashboard metrics" >> dashboard.md
git add dashboard.md
git commit -m "Add dashboard metrics"

# Return to main and create a new commit
git switch main
echo "Monitoring notes" > monitoring.md
git add monitoring.md
git commit -m "Add monitoring documentation"

# Switch back to the feature branch
git switch feature-dashboard

# Rebase the feature branch onto the latest main
git rebase main

# Review the history
git log --oneline --graph --all
```

### What I Re-learned

I re-learned that rebase moves my feature commits on top of the latest `main`. It gives a cleaner history, but it rewrites commit history. Merge keeps the existing history. I should normally use rebase for my own local work and avoid rebasing shared branches.

### Rebase vs Merge

| Rebase                          | Merge                             |
| ------------------------------- | --------------------------------- |
| Replays commits onto a new base | Combines branch histories         |
| Gives a more linear history     | Keeps the branch history          |
| Rewrites commit history         | Does not rewrite existing commits |
| Useful for local feature work   | Useful for shared branch history  |

---

## Task 3: Quick-Fire Questions

### 1. What does `chmod 755 script.sh` do?

**My answer:**
It gives the owner full permission and gives the group and others read and execute permission.

**Verified answer:**
`755` means owner has `rwx`, while group and others have `r-x`.

---

### 2. What is the difference between a process and a service?

**My answer:**
A process is a running program. A service is usually a background program managed by a service manager like systemd.

**Verified answer:**
A process is a running instance of a program, while a service is usually a background program managed by systemd or another service manager.

---

### 3. How do you find which process is using port 8080?

**My answer:**
I can use `ss` or `lsof`.

**Verified answer:**

```bash
# Find the process using port 8080
sudo ss -tulpn | grep :8080

# Another option
sudo lsof -i :8080
```

---

### 4. What does `set -euo pipefail` do?

**My answer:**
It makes a script stricter and helps stop common errors.

**Verified answer:**
`-e` stops on errors, `-u` catches undefined variables, and `pipefail` catches failures inside pipelines.

---

### 5. What is the difference between `git reset --hard` and `git revert`?

**My answer:**
Reset changes the branch history, while revert creates a new commit to undo changes.

**Verified answer:**

| `git reset --hard`       | `git revert`                      |
| ------------------------ | --------------------------------- |
| Moves the branch pointer | Creates a new commit              |
| Can discard changes      | Keeps the old history             |
| Can rewrite history      | Does not rewrite existing history |
| Better for local work    | Safer for shared work             |

---

### 6. What branching strategy would you recommend for a team of 5 developers shipping weekly?

**My answer:**
I would use GitHub Flow because it is simple and works well with short-lived feature branches and pull requests.

**Verified answer:**
GitHub Flow is a simple workflow for frequent releases using feature branches and pull requests around `main`.

---

### 7. What does `git stash` do and when would you use it?

**My answer:**
It temporarily saves my uncommitted work so I can switch branches without committing unfinished changes.

**Verified answer:**
`git stash` saves uncommitted changes temporarily so I can switch branches or work on something else.

---

### 8. How do you schedule a script to run every day at 3 AM?

**My answer:**
I use crontab and add `0 3 * * *`.

**Verified answer:**

```bash
# Open crontab
crontab -e

# Run the script every day at 3 AM
0 3 * * * /path/to/script.sh
```

---

### 9. What is the difference between `git fetch` and `git pull`?

**My answer:**
Fetch downloads remote changes without merging them. Pull downloads and integrates them into my current branch.

**Verified answer:**
`git fetch` only downloads remote changes. `git pull` downloads and integrates them into the current branch.

---

### 10. What is LVM and why would you use it instead of regular partitions?

**My answer:**
LVM is a flexible way to manage storage. It makes resizing and managing disk space easier.

**Verified answer:**
LVM stands for Logical Volume Manager and provides flexible storage management using physical volumes, volume groups, and logical volumes.

---

## Task 4: Organize My Work

I reviewed my work from previous days and checked that everything is committed, pushed, and organized.

```bash
# Check whether there are uncommitted changes
git status

# Check recent commits
git log --oneline -10

# Check remote repository configuration
git remote -v
```

### Final Checklist

* [x] Days 1-27 are committed and pushed
* [x] `git-commands.md` is up to date
* [x] `shell_scripting_cheatsheet.md` is complete
* [x] GitHub profile and repositories are clean and organized
* [x] No secrets or credentials are exposed in the repositories

My GitHub profile README is already created and will continue to be improved as I learn more DevOps tools, complete projects, and add new work.

---

## Task 5: Teach It Back

### Git Branching Explained Simply

Git branching lets developers work on different changes without disturbing the main branch.
A branch is a separate line of development based on the same repository history.
For example, I can create `feature-login` for login work while `main` stays stable.
After the feature is complete, I can review and merge it into `main`.
Different developers can work on different branches at the same time.
Branches also make testing and experimentation safer.
Merge and rebase are two different ways to integrate branch changes.
Using branches correctly helps keep development organized.

---

## 5 Key Takeaways

1. **Revision helps identify knowledge gaps** before moving to new DevOps topics.
2. **Network troubleshooting requires different tools**, and each command provides different information.
3. **DNS, IP addresses, subnets, and ports work together** when clients communicate with services.
4. **Rebase and merge both integrate changes**, but they handle project history differently.
5. **Regular practice and self-assessment** make Linux, Shell Scripting, Git, and GitHub skills stronger.
