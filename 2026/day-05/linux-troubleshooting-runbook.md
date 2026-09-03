# Linux Troubleshooting Runbook

## Target Service

**Service:** nginx

I used nginx as the target service for this troubleshooting drill.
> **Note:** Long command outputs have been shortened for readability. Only the relevant lines are shown.

## 1. Environment Basics

### `uname -a`

```bash
Linux Infinix 7.0.0-30-generic #30-Ubuntu SMP PREEMPT_DYNAMIC Fri Jul 31 18:22:54 UTC 2026 x86_64 GNU/Linux
```

**Observation:** The system is running a 64-bit Ubuntu Linux kernel.

### `cat /etc/os-release`

```bash
PRETTY_NAME="Ubuntu 26.04.1 LTS"
VERSION_ID="26.04"
VERSION_CODENAME=resolute
```

**Observation:** The system is running Ubuntu 26.04.1 LTS.

## 2. Filesystem Sanity

### `mkdir -p /tmp/runbook-demo`

```bash
```

**Observation:** The test directory was created successfully.

### `cp /etc/hosts /tmp/runbook-demo/hosts-copy && ls -l /tmp/runbook-demo`

```bash
total 4
-rw-r--r-- 1 sharad-verma sharad-verma 374 Sep  3 15:23 hosts-copy
```

**Observation:** The file was copied successfully.

## 3. CPU and Memory

### `ps -o pid,pcpu,pmem,comm -C nginx`

```bash
    PID %CPU %MEM COMMAND
   2626  0.0  0.0 nginx
   2627  0.0  0.0 nginx
   2628  0.0  0.0 nginx
   2629  0.0  0.0 nginx
   2630  0.0  0.0 nginx
```

**Observation:** nginx processes were using almost no CPU or memory at the time of the check.

### `free -h`

```bash
               total        used        free      shared  buff/cache   available
Mem:           7.0Gi       3.3Gi       1.5Gi       725Mi       3.3Gi       3.7Gi
Swap:          4.0Gi       572Mi       3.4Gi       4.0Gi
```

**Observation:** About 3.7 GiB memory was available.

## 4. Disk and IO

### `df -h`

```bash
Filesystem       Size  Used Avail Use% Mounted on
/dev/nvme0n1p6    59G   32G   25G  56% /
/dev/nvme0n1p1    96M   84M   13M  88% /boot/efi
```

**Observation:** The main filesystem has 56% usage. `/boot/efi` is more full at 88%.

### `du -sh /var/log`

```bash
du: cannot read directory '/var/log/speech-dispatcher': Permission denied
du: cannot read directory '/var/log/private': Permission denied
du: cannot read directory '/var/log/sssd': Permission denied
du: cannot read directory '/var/log/gdm3': Permission denied
du: cannot read directory '/var/log/chrony': Permission denied
329M	/var/log
```

**Observation:** `/var/log` uses 329 MB. Some directories could not be read because of permissions.

## 5. Network

### `ss -tulpn`

```bash
tcp   LISTEN 0      511    0.0.0.0:80       0.0.0.0:*
tcp   LISTEN 0      511       [::]:80          [::]:*
```

**Observation:** nginx is listening on port 80.

### `curl -I http://localhost`

```bash
HTTP/1.1 200 OK
Server: nginx/1.28.3 (Ubuntu)
Content-Type: text/html
Content-Length: 615
Connection: keep-alive
```

**Observation:** nginx is responding successfully with HTTP 200 OK.

## 6. Logs

### `journalctl -u nginx -n 50`

```bash
Aug 24 19:10:19 Infinix systemd[1]: Starting nginx.service
Aug 24 19:10:19 Infinix systemd[1]: Started nginx.service
Aug 29 10:04:28 Infinix systemd[1]: Starting nginx.service
Aug 29 10:04:28 Infinix systemd[1]: Started nginx.service
Sep 01 17:04:03 Infinix systemd[1]: Starting nginx.service
Sep 01 17:04:03 Infinix systemd[1]: Started nginx.service
```

**Observation:** nginx has started successfully several times.

### `tail -n 50 /var/log/nginx/error.log`

```bash
2026/08/24 19:10:20 [notice] 75447#75447: using inherited sockets from "5;6;"
```

**Observation:** No major nginx error was shown in the available output.

## Quick Findings

* **CPU:** nginx CPU usage was 0.0%.
* **Memory:** About 3.7 GiB memory was available.
* **Disk:** Root filesystem usage was 56%.
* **Boot EFI:** `/boot/efi` usage was 88%, so it should be monitored.
* **Logs:** `/var/log` uses 329 MB and some directories need higher permissions to read.
* **Network:** nginx is listening on port 80.
* **HTTP:** nginx returned `200 OK`.
* **Service logs:** nginx started successfully.

## If This Worsens

1. Check nginx status with `systemctl status nginx`.
2. Check nginx logs with `journalctl -u nginx`.
3. Check CPU, memory, disk and network usage again.
4. Restart nginx only when necessary.

## Key Takeaways

* **Environment:** Used to identify the Linux system and version.
* **Filesystem:** Used to check files, disk space and permission issues.
* **CPU and Memory:** Used to find resource usage problems.
* **Disk and IO:** Used to detect storage space problems.
* **Network:** Used to check listening ports and service connectivity.
* **Logs:** Used to find errors and understand service activity.
