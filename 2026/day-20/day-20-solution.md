# Bash Scripting Challenge: Log Analyzer and Report Generator

---

## Task 1: Input and Validation

Create a Bash script named `log_analyzer.sh` that accepts a log file path as a command-line argument.

```bash
# Create the log analyzer script
nano log_analyzer.sh
# Opens the script file for editing.
```

### `log_analyzer.sh`

```bash
#!/bin/bash

# Check if a log file argument was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <log_file>"
    exit 1
fi

LOG_FILE="$1"

# Check if the log file exists
if [ ! -f "$LOG_FILE" ]; then
    echo "Error: Log file does not exist: $LOG_FILE"
    exit 1
fi
# Validates the command-line argument and checks that the log file exists.
```

Test the validation:

```bash
# Run without providing a log file
./log_analyzer.sh
# Displays the usage message because no argument was provided.
```

### Output

```text
Usage: ./log_analyzer.sh <log_file>
```

---

## Task 2: Error Count

Count all lines containing the keyword `ERROR` or `Failed`.

```bash
# Count lines containing ERROR or Failed
ERROR_COUNT=$(grep -E "ERROR|Failed" "$LOG_FILE" | wc -l)

echo "Total error count: $ERROR_COUNT"
# Searches for ERROR or Failed and counts the matching lines.
```

### Output

```text
Total error count: 7
```

The supplied log contains 7 matching lines.

---

## Task 3: Critical Events

Search for lines containing `CRITICAL` and display them with their line numbers.

```bash
# Find critical events with line numbers
grep -n "CRITICAL" "$LOG_FILE"
# Displays every CRITICAL event together with its line number.
```

### Output

```text
49:2026-09-11 19:22:20,005 [kube-system] CRITICAL k8s.io.EvictionManager - Eviction threshold triggered on node 'node-worker-pool-3b'. Free space < 5%.
53:2026-09-11 19:22:21,115 [vault-svc] CRITICAL com.hashicorp.vault.Core - Vault step-down triggered! Core cluster state is sealed due to unrecoverable storage engine failure.
55:2026-09-11 19:22:22,405 [api-gateway] CRITICAL com.devops.gateway.Router - Critical service disruption! Core credentials engine unreachable. Falling back to safety circuit.
```

---

## Task 4: Top 5 Error Messages

Extract lines containing `ERROR`, count the most common error messages, sort them in descending order, and display the top 5.

```bash
# Find the top 5 most common ERROR messages
grep "ERROR" "$LOG_FILE" \
    | awk '{$1=$2=$3=""; sub(/^ +/, ""); print}' \
    | sort \
    | uniq -c \
    | sort -rn \
    | head -5
# Extracts ERROR messages, counts duplicates, sorts them, and displays the top 5.
```

### Output

```text
1 com.devops.payment.StripeClient - SSL Handshake failed with ://stripe.com. Remote certificate expired or untrusted.
1 com.devops.payment.Processor - Failed checkout pipeline for tx_9923182. Aborting step.
1 com.devops.cart.SessionStore - Connection lost to Redis Sentinel master 'mymaster'.
1 com.devops.cart.SessionStore - Redis write command failed: JedisConnectionException: Could not get a resource from the pool.
1 com.devops.db.ProxySQL - Removing laggy node postgres-replica-2.internal from load balancer read-pool.
```

---

## Task 5: Summary Report

Generate a report named `log_report_<date>.txt`.

The report should contain:

* Date
* Log file name
* Total number of lines
* Total error count
* Top 5 error messages with count
* Critical events with line numbers

```bash
# Generate the report filename using the current date
DATE=$(date +%Y-%m-%d)
REPORT="log_report_${DATE}.txt"

# Generate the complete summary report
{
    echo "Log Analysis Report"
    echo "==================="
    echo "Date of analysis: $(date)"
    echo "Log file: $LOG_FILE"
    echo "Total lines processed: $(wc -l < "$LOG_FILE")"
    echo "Total error count: $ERROR_COUNT"

    echo
    echo "--- Top 5 Error Messages ---"
    grep "ERROR" "$LOG_FILE" \
        | awk '{$1=$2=$3=""; sub(/^ +/, ""); print}' \
        | sort \
        | uniq -c \
        | sort -rn \
        | head -5

    echo
    echo "--- Critical Events ---"
    grep -n "CRITICAL" "$LOG_FILE"
} > "$REPORT"

echo "Report generated: $REPORT"
# Creates the required summary report containing the log analysis results.
```

Check the generated report:

```bash
# Display the generated report
cat log_report_2026-09-11.txt
# Shows the complete summary report.
```

### Output

```text
Log Analysis Report
===================
Date of analysis: 2026-09-11
Log file: sample_log.log
Total lines processed: 56
Total error count: 7

--- Top 5 Error Messages ---
1 com.devops.payment.StripeClient - SSL Handshake failed with ://stripe.com. Remote certificate expired or untrusted.
1 com.devops.payment.Processor - Failed checkout pipeline for tx_9923182. Aborting step.
1 com.devops.cart.SessionStore - Connection lost to Redis Sentinel master 'mymaster'.
1 com.devops.cart.SessionStore - Redis write command failed: JedisConnectionException: Could not get a resource from the pool.
1 com.devops.db.ProxySQL - Removing laggy node postgres-replica-2.internal from load balancer read-pool.

--- Critical Events ---
49:2026-09-11 19:22:20,005 [kube-system] CRITICAL k8s.io.EvictionManager - Eviction threshold triggered on node 'node-worker-pool-3b'. Free space < 5%.
53:2026-09-11 19:22:21,115 [vault-svc] CRITICAL com.hashicorp.vault.Core - Vault step-down triggered! Core cluster state is sealed due to unrecoverable storage engine failure.
55:2026-09-11 19:22:22,405 [api-gateway] CRITICAL com.devops.gateway.Router - Critical service disruption! Core credentials engine unreachable. Falling back to safety circuit.
```

---

## Task 6: Archive (optional)

Create an `archive/` directory and move the processed log into it.

```bash
# Create the archive directory
mkdir -p archive

# Move the processed log file into the archive
mv "$LOG_FILE" archive/

echo "Log file moved to archive/"
# Moves the processed log into the archive directory.
```

### Output

```text
Log file moved to archive/
```

---

## Commands and Tools Used

* `grep` - Searches for `ERROR`, `Failed`, and `CRITICAL`.
* `awk` - Extracts and formats error messages.
* `sort` - Sorts error messages.
* `uniq` - Counts duplicate messages.
* `head` - Displays the top 5 results.
* `wc` - Counts the total number of log lines.
* `date` - Generates the report date.
* `mkdir` - Creates the archive directory.
* `mv` - Moves the processed log file.

---

## 3 Key Learning Points

1. Bash can automate log analysis and generate useful reports.
2. Commands like `grep`, `awk`, `sort`, `uniq`, and `wc` can be combined to process log files efficiently.
3. Automated error and critical event detection helps system administrators identify important issues quickly.


## Files Created

* `sample_log.log`
* `log_analyzer.sh`
* `log_report_2026-09-11.txt`
