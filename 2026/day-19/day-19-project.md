# Shell Scripting Project: Log Rotation, Backup and Crontab

---

## Task 1: Log Rotation Script

### `log_rotate.sh`

```bash
#!/bin/bash

set -euo pipefail

rotate_logs() {
    local LOG_DIR="$1"

    if [ ! -d "$LOG_DIR" ]; then
        echo "Error: Directory does not exist: $LOG_DIR"
        return 1
    fi

    local compressed_count=0
    local deleted_count=0

    while IFS= read -r -d '' file; do
        gzip "$file"
        compressed_count=$((compressed_count + 1))
    done < <(find "$LOG_DIR" -type f -name "*.log" -mtime +7 -print0)

    while IFS= read -r -d '' file; do
        rm "$file"
        deleted_count=$((deleted_count + 1))
    done < <(find "$LOG_DIR" -type f -name "*.gz" -mtime +30 -print0)

    echo "Files compressed: $compressed_count"
    echo "Files deleted: $deleted_count"
}

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <log-directory>"
    exit 1
fi

rotate_logs "$1"
```

### Run

```bash
./log_rotate.sh /var/log/myapp
```

### Output

```text
Files compressed: 0
Files deleted: 0
```

The actual numbers depend on the files and their ages in the selected directory.

---

## Task 2: Server Backup Script

### `backup.sh`

```bash
#!/bin/bash

set -euo pipefail

create_backup() {
    local SOURCE_DIR="$1"
    local BACKUP_DIR="$2"

    if [ ! -d "$SOURCE_DIR" ]; then
        echo "Error: Source directory does not exist: $SOURCE_DIR"
        return 1
    fi

    mkdir -p "$BACKUP_DIR"

    local TIMESTAMP
    TIMESTAMP=$(date +%Y-%m-%d)

    local ARCHIVE="$BACKUP_DIR/backup-$TIMESTAMP.tar.gz"

    tar -czf "$ARCHIVE" -C "$(dirname "$SOURCE_DIR")" "$(basename "$SOURCE_DIR")"

    if [ ! -f "$ARCHIVE" ]; then
        echo "Error: Backup archive was not created."
        return 1
    fi

    local SIZE
    SIZE=$(du -h "$ARCHIVE" | cut -f1)

    echo "Backup created: $ARCHIVE"
    echo "Archive size: $SIZE"

    find "$BACKUP_DIR" -type f -name "*.tar.gz" -mtime +14 -delete
    echo "Old backups older than 14 days deleted."
}

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <source-directory> <backup-destination>"
    exit 1
fi

create_backup "$1" "$2"
```

### Run

```bash
./backup.sh /home/sharad-verma/devops /home/sharad-verma/backups
```

### Output

```text
Backup created: /home/sharad-verma/backups/backup-2026-09-11.tar.gz
Archive size: 12K
Old backups older than 14 days deleted.
```

The archive name and size will depend on the actual source directory and current date.

---

## Task 3: Crontab

### Check Current Crontab

```bash
crontab -l
```

This displays the cron jobs currently scheduled for the user.

### Cron Syntax

```text
* * * * * command
│ │ │ │ │
│ │ │ │ └── Day of week (0-7)
│ │ │ └──── Month (1-12)
│ │ └────── Day of month (1-31)
│ └──────── Hour (0-23)
└────────── Minute (0-59)
```

### Cron Entries

#### Run log rotation every day at 2 AM

```cron
0 2 * * * /path/to/log_rotate.sh /var/log/myapp
```

#### Run backup every Sunday at 3 AM

```cron
0 3 * * 0 /path/to/backup.sh /home/sharad-verma/devops /home/sharad-verma/backups
```

#### Run health check every 5 minutes

```cron
*/5 * * * * /path/to/health_check.sh
```

---

## Task 4: Scheduled Maintenance Script

### `maintenance.sh`

```bash
#!/bin/bash

set -euo pipefail

LOG_DIR="/var/log/myapp"
SOURCE_DIR="/home/sharad-verma/devops"
BACKUP_DIR="/home/sharad-verma/backups"
MAINTENANCE_LOG="/var/log/maintenance.log"

log_message() {
    echo "$(date): $1" >> "$MAINTENANCE_LOG"
}

rotate_logs() {
    local compressed_count=0
    local deleted_count=0

    while IFS= read -r -d '' file; do
        gzip "$file"
        compressed_count=$((compressed_count + 1))
    done < <(find "$LOG_DIR" -type f -name "*.log" -mtime +7 -print0)

    while IFS= read -r -d '' file; do
        rm "$file"
        deleted_count=$((deleted_count + 1))
    done < <(find "$LOG_DIR" -type f -name "*.gz" -mtime +30 -print0)

    log_message "Log rotation completed. Compressed: $compressed_count, Deleted: $deleted_count"
}

create_backup() {
    mkdir -p "$BACKUP_DIR"

    local TIMESTAMP
    TIMESTAMP=$(date +%Y-%m-%d)

    local ARCHIVE="$BACKUP_DIR/backup-$TIMESTAMP.tar.gz"

    tar -czf "$ARCHIVE" -C "$(dirname "$SOURCE_DIR")" "$(basename "$SOURCE_DIR")"

    if [ -f "$ARCHIVE" ]; then
        local SIZE
        SIZE=$(du -h "$ARCHIVE" | cut -f1)
        log_message "Backup created: $ARCHIVE, Size: $SIZE"
    else
        log_message "Backup failed."
        return 1
    fi

    find "$BACKUP_DIR" -type f -name "*.tar.gz" -mtime +14 -delete
    log_message "Old backups older than 14 days deleted."
}

main() {
    log_message "Maintenance started."

    rotate_logs
    create_backup

    log_message "Maintenance completed."
}

main
```

### Cron Entry

Run the maintenance script every day at 1 AM:

```cron
0 1 * * * /path/to/maintenance.sh
```

### Sample Maintenance Log

```text
Fri Sep 11 01:00:00 IST 2026: Maintenance started.
Fri Sep 11 01:00:01 IST 2026: Log rotation completed. Compressed: 2, Deleted: 0
Fri Sep 11 01:00:02 IST 2026: Backup created: /home/sharad-verma/backups/backup-2026-09-11.tar.gz, Size: 12K
Fri Sep 11 01:00:02 IST 2026: Old backups older than 14 days deleted.
Fri Sep 11 01:00:02 IST 2026: Maintenance completed.
```

The actual timestamps and output will depend on the system when the script runs.

---

## What I Learned

1. Shell scripts can automate log rotation and server backups to reduce manual maintenance work.
2. `find`, `gzip`, `tar`, and `cron` can be combined to automate regular system administration tasks.
3. Functions, error handling, timestamps, and logging make maintenance scripts more reliable and easier to manage.


## Files Created

* `log_rotate.sh`
* `backup.sh`
* `maintenance.sh`
