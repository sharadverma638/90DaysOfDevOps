# Linux Practice

## 1. Process Checks

### Command 1

```bash
ps aux
```

**What it does:** Shows all running processes.

**Output:**

```bash
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT COMMAND
root           1  0.0  0.2  27428 15336 ?        Ss   /usr/lib/systemd/systemd
root         383  0.0  0.4 100236 34088 ?        S<s  /usr/lib/systemd/systemd-journald
root        2626  0.0  0.0  14852  1096 ?        Ss   nginx: master process
www-data    2627  0.0  0.0  16956  3968 ?        S    nginx: worker process
sharad-+    3244  2.3  3.9 5270776 286228 ?       Ssl  /usr/bin/gnome-shell
```

> Output shortened for readability.

### Extra Process Check

```bash
ps aux | wc -l
```

**Output:**

```bash
282
```

**Meaning:** There were 282 lines in the `ps aux` output, including the header.

### Command 2

```bash
pgrep systemd
```

**What it does:** Shows the PIDs of processes matching `systemd`.

**Output:**

```bash
1
383
432
433
436
1187
2867
```

## 2. Service Checks

### Command 3

```bash
systemctl list-units --type=service --state=running
```

**What it does:** Shows currently running services.

**Output:**

```bash
UNIT                                  LOAD   ACTIVE SUB     DESCRIPTION
accounts-daemon.service               loaded active running Accounts Service
cron.service                          loaded active running Regular background program processing daemon
dbus.service                          loaded active running D-Bus System Message Bus
nginx.service                         loaded active running A high performance web server
NetworkManager.service                loaded active running Network Manager
rsyslog.service                       loaded active running System Logging Service
systemd-journald.service              loaded active running Journal Service
systemd-logind.service                loaded active running User Login Management
```

> Output shortened for readability.

### Command 4

```bash
systemctl status systemd-journald
```

**What it does:** Checks the status of the systemd journal service.

**Output:**

```bash
● systemd-journald.service - Journal Service
     Loaded: loaded (/usr/lib/systemd/system/systemd-journald.service; static)
     Active: active (running) since Tue 2026-09-01 17:03:55 IST
   Main PID: 383 (systemd-journal)
     Status: "Processing requests..."
     Memory: 29.5M
        CPU: 3.906s
```

**Result:** `systemd-journald` is **active and running**.

## 3. Log Checks

### Command 5

```bash
journalctl -u systemd-journald -n 20
```

**What it does:** Shows the latest 20 logs for systemd-journald.

**Output:**

```bash
Sep 01 17:03:55 Infinix systemd-journald[383]: Collecting audit messages is disabled.
Sep 01 17:03:55 Infinix systemd-journald[383]: Journal started
Sep 01 17:03:55 Infinix systemd-journald[383]: Runtime Journal is 16M
Sep 01 17:03:55 Infinix systemd[1]: systemd-journald.service: Deactivated successfully.
Sep 01 17:03:55 Infinix systemd-journald[383]: Time spent on flushing is 115.404ms
Sep 01 17:03:56 Infinix systemd-journald[383]: Received client request to flush runtime journal.
Sep 01 17:03:56 Infinix systemd-journald[383]: Rotating system journal.
Sep 01 17:04:30 Infinix systemd-journald[383]: Forwarding to syslog missed 1136 messages.
```

> Output shortened for readability.

### Command 6

```bash
journalctl -n 20
```

**What it does:** Shows the latest 20 system log entries.

**Output:**

```bash
Sep 03 14:54:17 Infinix gpg-agent[53736]: can't connect to the daemon
Sep 03 14:57:14 Infinix dbus-daemon[2897]: Successfully activated service
Sep 03 14:57:18 Infinix kernel: audit: type=1400 apparmor="DENIED"
Sep 03 15:00:04 Infinix systemd[1]: Starting sysstat-collect.service
Sep 03 15:00:04 Infinix systemd[1]: Finished sysstat-collect.service
Sep 03 15:00:58 Infinix brave_brave.desktop: ERROR
```

> Output shortened for readability.

## 4. What I Observed

* Linux is running many background processes and services.
* `systemd` is running as PID 1.
* `systemd-journald` is active and running with PID 383.
* `nginx` is also running on the system.
* The logs show both normal system activity and some warnings/errors.

## Key Takeaways

* **Process checks:** Used to find running processes and their PIDs.
* **Service checks:** Used to check whether Linux services are running correctly.
* **Log checks:** Used to find errors, warnings and system activity.
* **Troubleshooting:** Start with the process, check the service, then check its logs.
