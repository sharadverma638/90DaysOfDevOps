# Day 07 - Linux File System Hierarchy and Scenario-Based Practice

> **Note:** Long command outputs have been shortened for readability. Only relevant lines are shown.

## 1. Linux File System Hierarchy

### 1.1 `/` - Root

**Purpose:** The root directory is the starting point of the Linux file system.

**Command:**

```bash
ls -l /
```

**What I found:**

```bash
bin -> usr/bin
boot
dev
etc
home
opt
root
tmp
usr
var
```

**I would use this when:** I need to understand the main Linux file system structure.

### 1.2 `/home` - User Home Directories

**Purpose:** Contains home directories of normal users.

**Command:**

```bash
ls -l /home
```

**What I found:**

```bash
sharad-verma
```

**I would use this when:** I need to access user files and personal data.

### 1.3 `/root` - Root User Home

**Purpose:** Home directory of the root user.

**Command:**

```bash
ls -l /root
```

**What I found:**

```bash
Permission denied
```

**I would use this when:** I need to access root user files with proper permissions.

### 1.4 `/etc` - Configuration

**Purpose:** Contains system and application configuration files.

**Command:**

```bash
ls -l /etc
```

**What I found:**

```bash
hostname
hosts
passwd
nginx
systemd
```

**I would use this when:** I need to check or modify system configuration.

### 1.5 `/var/log` - Log Files

**Purpose:** Stores system and application log files.

**Command:**

```bash
ls -l /var/log
```

**What I found:**

```bash
auth.log
kern.log
syslog
nginx
journal
```

**I would use this when:** I need to troubleshoot errors and check system activity.

### 1.6 `/tmp` - Temporary Files

**Purpose:** Stores temporary files used by applications and users.

**Command:**

```bash
ls -l /tmp
```

**What I found:**

```bash
runbook-demo
node-compile-cache
snap-private-tmp
```

**I would use this when:** I need temporary storage for testing or scripts.

### 1.7 `/bin` - Essential Commands

**Purpose:** Contains essential Linux command binaries.

**Command:**

```bash
ls -l /bin
```

**What I found:**

```bash
/bin -> usr/bin
```

**I would use this when:** I need to access basic Linux commands.

### 1.8 `/usr/bin` - User Commands

**Purpose:** Contains many commonly used Linux commands and applications.

**Command:**

```bash
ls -l /usr/bin
```

**What I found:**

```bash
bash
cat
curl
git
python3
systemctl
vim
wget
```

**I would use this when:** I need to find installed commands and programs.

### 1.9 `/opt` - Optional Applications

**Purpose:** Used for optional or third-party applications.

**Command:**

```bash
ls -l /opt
```

**What I found:**

```bash
Permission denied
```

**I would use this when:** I need to find or manage optional software.

## 2. Hands-on Tasks

### 2.1 Find Large Log Files

**Command:**

```bash
du -sh /var/log/* 2>/dev/null | sort -h | tail -5
```

**Output:**

```bash
2.2M    /var/log/installer
6.4M    /var/log/sysstat
7.9M    /var/log/kern.log
35M     /var/log/syslog
273M    /var/log/journal
```

**Observation:** `/var/log/journal` is using the most space among the listed log locations.

### 2.2 Check Hostname

**Command:**

```bash
cat /etc/hostname
```

**Output:**

```bash
Infinix
```

**Observation:** The hostname of the system is `Infinix`.

### 2.3 Check Home Directory

**Command:**

```bash
ls -la ~
```

**What I found:**

```bash
.bashrc
.gitconfig
.ssh
.docker
Desktop
Documents
Downloads
Videos
```

**Observation:** The home directory contains configuration files, hidden files and personal folders.

## 3. Scenario Practice

## Scenario 1 - Service Not Starting

**Problem:** A web application service called `myapp` failed to start after a server reboot.

### Step 1

```bash
systemctl status myapp
```

**Why:** It shows whether the service is active, failed or stopped.

### Step 2

```bash
journalctl -u myapp -n 50
```

**Why:** It shows recent logs and helps find the reason for the failure.

### Step 3

```bash
systemctl is-enabled myapp
```

**Why:** It checks whether the service is enabled to start automatically after reboot.

### Step 4

```bash
systemctl list-units --type=service
```

**Why:** It helps check available services on the system.

**What I learned:** Always check the service status first, then investigate logs and startup settings.

## Scenario 2 - High CPU Usage

**Problem:** The application server is slow.

### Step 1

```bash
top
```

**Why:** It shows live CPU usage and helps identify busy processes.

### Step 2

```bash
htop
```

**Why:** It gives an interactive view of CPU and process usage.

### Step 3

```bash
ps aux --sort=-%cpu | head -10
```

**Why:** It shows processes sorted by CPU usage.

### Step 4

**Note the PID of the top process.**

**Why:** The PID helps identify the process for further troubleshooting.

**What I learned:** First find the process using high CPU, then investigate that process.

## Scenario 3 - Finding Service Logs

**Problem:** A developer wants to find logs for a systemd-managed service.

### Step 1

```bash
systemctl status ssh
```

**Why:** It checks whether the service is running correctly.

### Step 2

```bash
journalctl -u ssh -n 50
```

**Why:** It shows the last 50 log entries for the service.

### Step 3

```bash
journalctl -u ssh -f
```

**Why:** It follows new log entries in real time.

**What I learned:** `journalctl -u <service>` is useful for checking systemd service logs.

## Scenario 4 - File Permissions Issue

**Problem:** A script gives `Permission denied` when trying to run.

### Step 1

```bash
ls -l /home/user/backup.sh
```

**Why:** It checks the current permissions of the file.

### Step 2

```bash
chmod +x /home/user/backup.sh
```

**Why:** It adds execute permission to the script.

### Step 3

```bash
ls -l /home/user/backup.sh
```

**Why:** It verifies that execute permission was added.

### Step 4

```bash
./backup.sh
```

**Why:** It tests whether the script now runs correctly.

**What I learned:** A script needs execute permission to run directly.

## 4. Why This Matters for DevOps

* **File system knowledge:** Helps find configs, logs and application files.
* **Troubleshooting:** Helps investigate service, CPU and permission problems.
* **Production support:** These skills are useful during incidents and server issues.
* **Automation:** Knowing Linux paths makes scripts and automation more reliable.

## 5. Key Takeaways

* **`/etc`:** Used for system and application configuration.
* **`/var/log`:** Used to find system and application logs.
* **`/home`:** Used for normal users' files and directories.
* **`/tmp`:** Used for temporary files and testing.
* **`/usr/bin`:** Contains commonly used Linux commands.
* **Service troubleshooting:** Check status, logs and boot settings.
* **CPU troubleshooting:** Find the process using the most CPU and note its PID.
* **Logs:** Use `journalctl` to investigate systemd services.
* **Permissions:** Check permissions, add execute permission with `chmod`, then test.
