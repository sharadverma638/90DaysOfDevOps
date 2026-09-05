# Breather and Revision

## What I Reviewed

* Reviewed my Day 01 learning plan.
* Practiced checking processes and services.
* Practiced file permissions and file operations.
* Revised useful Linux commands.
* Practiced user and file ownership commands.

## Commands Practiced

```bash
# Task 1: Process and service checks
ps
systemctl status nginx
journalctl -u nginx
```

```bash
# Task 2: File operations
echo "Day 12 revision" >> notes.txt
chmod 640 notes.txt
ls -l notes.txt
```

```bash
# Task 3: User and ownership
sudo useradd -m testuser
id testuser
sudo chown testuser notes.txt
ls -l notes.txt
```

## Self Check

### 1. Which 3 commands save me the most time?

* `sudo !!` - runs the previous command with sudo.
* `ll` - quickly shows files and directories with details.
* `cd -` - switches back to the previous directory.


### 2. How do I check if a service is healthy?

* `systemctl status nginx`
* `journalctl -u nginx`
* `ps`

### 3. How do I safely change ownership and permissions?

I first check the current permissions and ownership using `ls -l`. Then I make the required change.

Example:

```bash
sudo chown testuser notes.txt
```

### 4. What will I improve in the next 3 days?

I will focus on improving my Linux commands and troubleshooting skills.

## Key Takeaways

* Linux commands become easier with regular practice.
* Checking service status and logs is important for troubleshooting.
* File permissions and ownership are important for security.
