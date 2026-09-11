# Day 17 - Shell Scripting: Loops, Arguments and Error Handling

---

## Task 1: For Loop

### `for_loop.sh`

```bash
#!/bin/bash

fruits=("Apple" "Banana" "Mango" "Orange" "Grapes")

for fruit in "${fruits[@]}"; do
    echo "$fruit"
done
```

### Output

```text
Apple
Banana
Mango
Orange
Grapes
```

### `count.sh`

```bash
#!/bin/bash

for i in {1..10}; do
    echo "$i"
done
```

### Output

```text
1
2
3
4
5
6
7
8
9
10
```

---

## Task 2: While Loop

### `countdown.sh`

```bash
#!/bin/bash

read -p "Enter a number: " NUMBER

while [ "$NUMBER" -ge 0 ]; do
    echo "$NUMBER"
    NUMBER=$((NUMBER - 1))
done

echo "Done!"
```

### Example Output

```text
Enter a number: 5
5
4
3
2
1
0
Done!
```

---

## Task 3: Command-Line Arguments

### `greet.sh`

```bash
#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: ./greet.sh <name>"
    exit 1
fi

echo "Hello, $1!"
```

### Output

```text
$ ./greet.sh Sharad
Hello, Sharad!
```

If no argument is provided:

```text
$ ./greet.sh
Usage: ./greet.sh <name>
```

### `args_demo.sh`

```bash
#!/bin/bash

echo "Total arguments: $#"
echo "All arguments: $@"
echo "Script name: $0"
```

### Output

```text
$ ./args_demo.sh one two three
Total arguments: 3
All arguments: one two three
Script name: ./args_demo.sh
```

---

## Task 4: Install Packages via Script

### `install_packages.sh`

```bash
#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Run as root"
    exit 1
fi

packages=("nginx" "curl" "wget")

for package in "${packages[@]}"; do
    if dpkg -s "$package" &> /dev/null; then
        echo "$package is already installed."
    else
        echo "$package is not installed. Installing..."
        apt-get update
        apt-get install -y "$package"
        echo "$package has been installed."
    fi
done
```

### Output

```text
nginx is already installed.
curl is already installed.
wget is not installed. Installing...
wget has been installed.
```

The actual output depends on which packages are already installed on the system.

---

## Task 5: Error Handling

### `safe_script.sh`

```bash
#!/bin/bash

set -e

mkdir /tmp/devops-test || echo "Directory already exists"
cd /tmp/devops-test || echo "Failed to enter directory"
touch test-file.txt || echo "Failed to create file"

echo "Safe script completed successfully."
```

### Output

```text
Directory already exists
Safe script completed successfully.
```

The directory message depends on whether `/tmp/devops-test` already exists.

The script uses `set -e` to stop execution when an unhandled command fails and uses `||` to provide an error message when a step fails.

---

## What I Learned

1. For and while loops can automate repetitive tasks in Bash.
2. Command-line arguments such as `$1`, `$#`, `$@`, and `$0` allow scripts to receive and use input from the command line.
3. `set -e`, `||`, and root checks help make Bash scripts safer and easier to handle when errors occur.


## Files Created

* `for_loop.sh`
* `count.sh`
* `countdown.sh`
* `greet.sh`
* `args_demo.sh`
* `install_packages.sh`
* `safe_script.sh`
