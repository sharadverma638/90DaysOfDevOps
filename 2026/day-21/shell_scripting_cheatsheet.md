# Shell Scripting Cheat Sheet

A simple Shell Scripting reference for DevOps work.

---

## Quick Reference

| Command / Concept | What it does                         |
| ----------------- | ------------------------------------ |
| `#!/bin/bash`     | Tells Linux to use Bash              |
| `echo`            | Prints text                          |
| `read`            | Takes input from the user            |
| `$1`              | First command-line argument          |
| `$?`              | Exit status of the last command      |
| `if`              | Checks a condition                   |
| `for`             | Repeats commands                     |
| `while`           | Repeats while a condition is true    |
| `grep`            | Searches text                        |
| `awk`             | Processes text and columns           |
| `sed`             | Finds and changes text               |
| `cut`             | Extracts parts of a line             |
| `sort`            | Sorts text                           |
| `uniq`            | Removes/counts duplicate lines       |
| `wc`              | Counts lines, words, or characters   |
| `set -e`          | Stops on command failure             |
| `set -u`          | Stops on undefined variables         |
| `set -o pipefail` | Detects failed commands in pipelines |
| `set -x`          | Shows commands while running         |
| `trap`            | Runs a command when an event happens |

---

## 1. Basics

### Shebang

The shebang tells Linux which program should run the script.

```bash
#!/bin/bash
```

---

### Running a Script

First give the script execute permission.

```bash
# Give execute permission
chmod +x script.sh
# Makes the script executable.
```

Run it:

```bash
# Run the script
./script.sh
# Executes the script.
```

You can also run it with Bash:

```bash
# Run the script using Bash
bash script.sh
# Bash reads and runs the script.
```

---

### Comments

Comments are ignored by Bash. They are useful for explaining code.

```bash
# This is a comment
echo "Hello"
# Prints Hello on the screen.
```

---

### Variables

Variables store values.

```bash
# Create variables
NAME="Sharad"
ROLE="DevOps Learner"

# Print variables
echo "$NAME"
echo "$ROLE"
# Displays the values stored in the variables.
```

Do not put spaces around `=` when creating a variable.

---

### Read User Input

`read` takes input from the user.

```bash
# Ask the user for their name
read -p "Enter your name: " NAME

# Display the name
echo "Hello $NAME"
# Reads the user's name and prints a greeting.
```

---

### Command-Line Arguments

Arguments are values passed when running a script.

```bash
# Print the first argument
echo "Hello $1"
# $1 contains the first argument given to the script.
```

Example:

```bash
# Pass Sharad as the first argument
./greet.sh Sharad
# The script receives Sharad as $1.
```

Useful argument variables:

```bash
$0    # Script name
$1    # First argument
$2    # Second argument
$#    # Number of arguments
$@    # All arguments
```

---

## 2. Operators and Conditionals

### String Comparisons

Common string operators:

```bash
"$A" = "$B"      # Equal
"$A" != "$B"     # Not equal
-z "$A"          # String is empty
-n "$A"          # String is not empty
```

Example:

```bash
# Compare two strings
if [ "$ENV" = "production" ]; then
    echo "Production environment"
fi
# Runs the message when ENV is production.
```

---

### Integer Comparisons

Common number operators:

```bash
-eq    # Equal
-ne    # Not equal
-gt    # Greater than
-lt    # Less than
-ge    # Greater than or equal
-le    # Less than or equal
```

Example:

```bash
# Check if a number is greater than 10
if [ "$NUMBER" -gt 10 ]; then
    echo "Number is greater than 10"
fi
# Checks the numeric value.
```

---

### File Tests

Useful file checks:

```bash
-f file.txt    # File exists
-d directory   # Directory exists
-r file.txt    # File is readable
-w file.txt    # File is writable
-x script.sh   # File is executable
```

Example:

```bash
# Check if a file exists
if [ -f "app.log" ]; then
    echo "Log file exists"
else
    echo "Log file does not exist"
fi
# Checks whether app.log is a regular file.
```

---

### if, elif and else

Use these when you need to make decisions.

```bash
# Check the environment
if [ "$ENV" = "production" ]; then
    echo "Production"
elif [ "$ENV" = "staging" ]; then
    echo "Staging"
else
    echo "Development"
fi
# Runs the matching block based on the environment.
```

---

### AND, OR and NOT

`&&` means AND.

```bash
# Run the second command only if the first succeeds
mkdir backup && echo "Backup directory created"
# Prints the message only when mkdir succeeds.
```

`||` means OR.

```bash
# Run the second command if the first fails
mkdir backup || echo "Could not create directory"
# Prints the error message when mkdir fails.
```

`!` means NOT.

```bash
# Check that a file does not exist
if [ ! -f "app.log" ]; then
    echo "Log file is missing"
fi
# Runs when app.log does not exist.
```

---

### case

`case` is useful when there are several choices.

```bash
# Check the selected environment
case "$ENV" in
    production)
        echo "Production selected"
        ;;
    staging)
        echo "Staging selected"
        ;;
    development)
        echo "Development selected"
        ;;
    *)
        echo "Unknown environment"
        ;;
esac
# Matches the value of ENV with one of the available choices.
```

---

## 3. Loops

### for Loop

A `for` loop repeats a command for each item.

```bash
# Print three server names
for server in web01 web02 web03; do
    echo "Checking $server"
done
# Runs once for each server.
```

---

### while Loop

A `while` loop runs while a condition is true.

```bash
# Count from 1 to 5
COUNT=1

while [ "$COUNT" -le 5 ]; do
    echo "$COUNT"
    COUNT=$((COUNT + 1))
done
# Continues until COUNT becomes greater than 5.
```

---

### until Loop

An `until` loop runs until the condition becomes true.

```bash
# Wait until a file exists
until [ -f "ready.txt" ]; do
    echo "Waiting for file..."
    sleep 2
done
# Keeps checking until ready.txt exists.
```

---

### break

`break` stops a loop.

```bash
# Stop when the number reaches 3
for number in 1 2 3 4 5; do
    if [ "$number" -eq 3 ]; then
        break
    fi
    echo "$number"
done
# Stops the loop at 3.
```

---

### continue

`continue` skips the current loop and moves to the next one.

```bash
# Skip number 3
for number in 1 2 3 4 5; do
    if [ "$number" -eq 3 ]; then
        continue
    fi
    echo "$number"
done
# Prints every number except 3.
```

---

### Loop Through Files

```bash
# Check every log file
for file in *.log; do
    echo "Checking $file"
done
# Runs once for every .log file in the directory.
```

---

### while read

Useful for reading a file line by line.

```bash
# Read each server name from servers.txt
while read -r server; do
    echo "Checking $server"
done < servers.txt
# Reads servers.txt one line at a time.
```

---

## 4. Functions

Functions let us group commands and reuse them.

### Define and Call a Function

```bash
# Create a greeting function
greet() {
    echo "Hello DevOps!"
}

# Call the function
greet
# Runs the commands inside the function.
```

---

### Function Arguments

Functions can receive arguments.

```bash
# Create a function that accepts a name
greet() {
    echo "Hello $1"
}

# Call the function
greet "Sharad"
# Passes Sharad as the first function argument.
```

---

### return vs echo

`echo` prints a value.

```bash
# Print a result
add() {
    echo $(( $1 + $2 ))
}

RESULT=$(add 10 20)
echo "$RESULT"
# Uses the printed result from the function.
```

`return` is mainly used for an exit status.

```bash
# Return success or failure
check_file() {
    if [ -f "$1" ]; then
        return 0
    else
        return 1
    fi
}

check_file "app.log"

if [ "$?" -eq 0 ]; then
    echo "File exists"
fi
# Uses the function's exit status to check the result.
```

---

### local

`local` creates a variable only inside the function.

```bash
# Create a local variable
show_name() {
    local NAME="DevOps"
    echo "$NAME"
}

show_name
# NAME is available only inside the function.
```

---

## 5. Text Processing

### grep

Search for text.

```bash
# Find ERROR lines
grep "ERROR" app.log
# Displays lines containing ERROR.
```

Useful option:

```bash
# Search without caring about uppercase or lowercase
grep -i "error" app.log
# Finds error, ERROR, Error, and similar forms.
```

---

### awk

`awk` is useful for working with columns.

```bash
# Print the first column
awk '{print $1}' app.log
# Displays the first space-separated field from each line.
```

Example:

```bash
# Print username and shell from a file
awk '{print $1, $7}' /etc/passwd
# Displays selected fields from /etc/passwd.
```

---

### sed

`sed` can find and replace text.

```bash
# Replace development with production
sed 's/development/production/g' config.txt
# Prints the changed text without modifying the original file.
```

---

### cut

`cut` extracts parts of a line.

```bash
# Get usernames from /etc/passwd
cut -d: -f1 /etc/passwd
# Uses : as the separator and prints the first field.
```

---

### sort

Sorts lines.

```bash
# Sort a list of servers
sort servers.txt
# Prints the servers in sorted order.
```

---

### uniq

Removes repeated lines.

```bash
# Remove duplicate lines
sort servers.txt | uniq
# Sorts the file first and then removes duplicates.
```

Count duplicates:

```bash
# Count repeated values
sort servers.txt | uniq -c
# Shows how many times each value appears.
```

---

### tr

Changes or removes characters.

```bash
# Convert lowercase text to uppercase
echo "devops" | tr 'a-z' 'A-Z'
# Prints DEVOPS.
```

---

### wc

Counts lines, words, and characters.

```bash
# Count lines in a log file
wc -l app.log
# Shows the number of lines.
```

---

### head

Shows the beginning of a file.

```bash
# Show the first 10 lines
head app.log
# Displays the first 10 lines.
```

Show a specific number:

```bash
# Show the first 5 lines
head -5 app.log
# Displays only the first 5 lines.
```

---

### tail

Shows the end of a file.

```bash
# Show the last 10 lines
tail app.log
# Displays the last 10 lines.
```

Follow a log in real time:

```bash
# Watch new log entries
tail -f app.log
# Keeps running and shows new lines as they are added.
```

---

## 6. Useful DevOps One-Liners

### Check if Nginx is Running

```bash
# Check Nginx service status
systemctl is-active --quiet nginx && echo "Nginx is running" || echo "Nginx is not running"
# Prints the current Nginx service state.
```

---

### Find ERROR Lines

```bash
# Show the latest ERROR messages
grep "ERROR" app.log | tail -10
# Displays the last 10 ERROR entries.
```

---

### Check Disk Usage

```bash
# Show disks using more than normal space
df -h
# Displays human-readable disk usage.
```

---

### Check Memory

```bash
# Show memory usage
free -h
# Displays RAM and swap usage in a readable format.
```

---

### Check Listening Ports

```bash
# Show listening TCP and UDP ports
ss -tulpn
# Displays services listening on network ports.
```

---

## 7. Error Handling and Debugging

### `$?`

`$?` contains the exit status of the last command.

`0` normally means success.

```bash
# Create a directory
mkdir backup

# Check the exit status
echo $?
# Prints 0 if mkdir succeeded.
```

---

### exit

`exit` stops the script and returns a status.

```bash
# Stop the script if the file is missing
if [ ! -f "$1" ]; then
    echo "File not found"
    exit 1
fi
# Stops the script with an error status.
```

---

### set -e

Stops the script when a command fails.

```bash
#!/bin/bash

# Stop on command failure
set -e

echo "Starting"
false
echo "This will not run"
# The script stops when false returns an error.
```

---

### set -u

Stops the script when an undefined variable is used.

```bash
#!/bin/bash

# Stop when an undefined variable is used
set -u

echo "$UNDEFINED_VARIABLE"
# The script stops because the variable does not exist.
```

---

### set -o pipefail

Makes a pipeline fail when any command in the pipeline fails.

```bash
#!/bin/bash

# Detect failures inside pipelines
set -o pipefail

false | echo "Hello"

echo $?
# The pipeline returns a failure status because false failed.
```

---

### set -x

Shows commands while the script is running.

```bash
#!/bin/bash

# Enable command debugging
set -x

NAME="DevOps"
echo "$NAME"

set +x
# Shows commands before Bash executes them.
```

---

### trap

`trap` lets us run a command when something happens, such as an exit.

```bash
#!/bin/bash

# Print a message when the script exits
trap 'echo "Script finished"' EXIT

echo "Running script..."
# The trap runs when the script exits.
```

A common DevOps use is cleanup:

```bash
# Remove temporary files when the script exits
trap 'rm -f /tmp/devops-test.txt' EXIT
# Makes sure the temporary file is cleaned up.
```

---

## Key Points

1. **Keep scripts simple.** Use variables, conditions, loops, and functions to avoid repeating commands.
2. **Always validate input.** Check arguments, files, directories, and command results before continuing.
3. **Use Bash tools together.** Commands like `grep`, `awk`, `sed`, `sort`, and `wc` become very powerful when combined.
4. **Handle errors properly.** `$?`, `exit`, `set -e`, `set -u`, `pipefail`, and `trap` help make scripts safer.
5. **Use comments.** Good comments make scripts easier to understand and maintain.
