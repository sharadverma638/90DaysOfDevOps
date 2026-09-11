# Shell Scripting: Functions and Intermediate Concepts

---

## Task 1: Basic Functions

### `functions.sh`

```bash
#!/bin/bash

greet() {
    echo "Hello, $1!"
}

add() {
    local sum=$(( $1 + $2 ))
    echo "Sum: $sum"
}

greet "Sharad"
add 10 20
```

### Output

```text
Hello, Sharad!
Sum: 30
```

---

## Task 2: Functions with Return Values

### `disk_check.sh`

```bash
#!/bin/bash

check_disk() {
    echo "Disk Usage:"
    df -h /
}

check_memory() {
    echo "Memory Usage:"
    free -h
}

main() {
    check_disk
    echo
    check_memory
}

main
```

### Output

```text
Disk Usage:
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p6   59G   33G   24G  59% /

Memory Usage:
               total        used        free      shared  buff/cache   available
Mem:           7.0Gi       3.0Gi       1.8Gi       881Mi       3.5Gi       4.0Gi
Swap:          4.0Gi       861Mi       3.2Gi
```

---

## Task 3: Strict Mode - `set -euo pipefail`

### `strict_demo.sh`

```bash
#!/bin/bash

set -euo pipefail

echo "Testing set -u:"
if bash -u -c 'echo "$UNDEFINED_VARIABLE"'; then
    echo "Undefined variable test passed."
else
    echo "set -u stopped the command because the variable was undefined."
fi

echo
echo "Testing set -e:"
if bash -e -c 'false; echo "This line will not execute."'; then
    echo "Command completed successfully."
else
    echo "set -e stopped execution after the failed command."
fi

echo
echo "Testing set -o pipefail:"
if bash -o pipefail -c 'false | true'; then
    echo "Pipeline completed successfully."
else
    echo "pipefail detected the failure in the pipeline."
fi
```

### Output

```text
Testing set -u:
bash: line 1: UNDEFINED_VARIABLE: unbound variable
set -u stopped the command because the variable was undefined.

Testing set -e:
set -e stopped execution after the failed command.

Testing set -o pipefail:
pipefail detected the failure in the pipeline.
```

### Strict Mode Explanation

* `set -e` - Stops the script when a command fails.
* `set -u` - Treats the use of an undefined variable as an error.
* `set -o pipefail` - Makes a pipeline fail if any command inside the pipeline fails.

Together, `set -euo pipefail` makes Bash scripts safer and helps detect errors early.

---

## Task 4: Local Variables

### `local_demo.sh`

```bash
#!/bin/bash

local_example() {
    local LOCAL_VAR="Inside function"
    echo "Inside function: $LOCAL_VAR"
}

regular_example() {
    REGULAR_VAR="Created inside function"
    echo "Inside function: $REGULAR_VAR"
}

echo "Local variable example:"
local_example

if [ -z "${LOCAL_VAR+x}" ]; then
    echo "LOCAL_VAR is not available outside the function."
else
    echo "LOCAL_VAR is available outside the function."
fi

echo
echo "Regular variable example:"
regular_example
echo "Outside function: $REGULAR_VAR"
```

### Output

```text
Local variable example:
Inside function: Inside function
LOCAL_VAR is not available outside the function.

Regular variable example:
Inside function: Created inside function
Outside function: Created inside function
```

### Explanation

The `local` keyword keeps a variable limited to the function where it is created.

A regular variable can remain available after the function finishes, which is why `REGULAR_VAR` can be accessed outside `regular_example`.

---

## Task 5: System Info Reporter

### `system_info.sh`

```bash
#!/bin/bash

set -euo pipefail

show_system_info() {
    echo "===== HOSTNAME AND OS ====="
    echo "Hostname: $(hostname)"

    if [ -f /etc/os-release ]; then
        . /etc/os-release
        echo "OS: $PRETTY_NAME"
    else
        echo "OS information not available."
    fi
}

show_uptime() {
    echo "===== UPTIME ====="
    uptime
}

show_disk_usage() {
    echo "===== TOP 5 DISK USAGE ====="
    du -xhd1 / 2>/dev/null | sort -hr | head -n 5 || true
}

show_memory_usage() {
    echo "===== MEMORY USAGE ====="
    free -h
}

show_cpu_processes() {
    echo "===== TOP 5 CPU-CONSUMING PROCESSES ====="
    ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6 || true
}

main() {
    show_system_info
    echo
    show_uptime
    echo
    show_disk_usage
    echo
    show_memory_usage
    echo
    show_cpu_processes
}

main
```

### Output

```text
===== HOSTNAME AND OS =====
Hostname: Infinix
OS: Ubuntu 26.04.1 LTS

===== UPTIME =====
 18:42:41 up 2 days,  8:36,  1 user,  load average: 0.44, 0.53, 0.54

===== TOP 5 DISK USAGE =====
29G	/
9.4G	/usr
8.5G	/home
6.4G	/var
143M	/boot

===== MEMORY USAGE =====
               total        used        free      shared  buff/cache   available
Mem:           7.0Gi       3.3Gi       1.2Gi       886Mi       4.0Gi       3.7Gi
Swap:          4.0Gi       861Mi       3.2Gi

===== TOP 5 CPU-CONSUMING PROCESSES =====
    PID COMMAND         %CPU
 107225 brave           15.3
 107187 brave            8.6
   3151 gnome-shell      4.8
 107363 ptyxis           1.5
  31531 brave            1.1
```

The output will show:

* Hostname and OS information
* System uptime
* Top 5 disk usage entries
* Memory usage
* Top 5 CPU-consuming processes

---

## What I Learned

1. Bash functions make scripts cleaner, reusable, and easier to maintain.
2. `set -euo pipefail` helps detect command failures, undefined variables, and pipeline errors.
3. Local variables and functions help control scope and organize larger shell scripts.


## Files Created

* `functions.sh`
* `disk_check.sh`
* `strict_demo.sh`
* `local_demo.sh`
* `system_info.sh`
