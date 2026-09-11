# Shell Scripting Basics

---

## Task 1: First Shell Script

### hello.sh

```bash
#!/bin/bash

echo "Hello, DevOps!"
```

### Commands Used

```bash
# Make the script executable
chmod +x hello.sh

# Run the script
./hello.sh
```

### Output

```text
Hello, DevOps!
```

### What happens if the shebang is removed?

The shebang tells the system which interpreter should be used to run the script. Without the shebang, running the script directly may result in an error or the system may not know which interpreter to use.

---

## Task 2: Variables

### variables.sh

```bash
#!/bin/bash

NAME="Sharad"
ROLE="DevOps Learner"

echo "Hello, I am $NAME and I am a $ROLE"
```

### Commands Used

```bash
# Make the script executable
chmod +x variables.sh

# Run the script
./variables.sh
```

### Output

```text
Hello, I am Sharad and I am a DevOps Learner
```

### Single Quotes vs Double Quotes

Single quotes treat the text literally, so variables are not expanded.

Double quotes allow variables to be expanded.

Example:

```bash
NAME="Sharad"

echo 'Hello $NAME'
echo "Hello $NAME"
```

Output:

```text
Hello $NAME
Hello Sharad
```

---

## Task 3: User Input

### greet.sh

```bash
#!/bin/bash

read -p "Enter your name: " NAME
read -p "Enter your favourite tool: " TOOL

echo "Hello $NAME, your favourite tool is $TOOL"
```

### Commands Used

```bash
# Make the script executable
chmod +x greet.sh

# Run the script
./greet.sh
```

### Output

```text
Enter your name: Sharad
Enter your favourite tool: Docker
Hello Sharad, your favourite tool is Docker
```

---

## Task 4: If-Else

### check_number.sh

```bash
#!/bin/bash

read -p "Enter a number: " NUMBER

if [ "$NUMBER" -gt 0 ]; then
    echo "The number is positive."
elif [ "$NUMBER" -lt 0 ]; then
    echo "The number is negative."
else
    echo "The number is zero."
fi
```

### Commands Used

```bash
# Make the script executable
chmod +x check_number.sh

# Run the script
./check_number.sh
```

### Output

```text
Enter a number: 10
The number is positive.
```

### file_check.sh

```bash
#!/bin/bash

read -p "Enter a filename: " FILE

if [ -f "$FILE" ]; then
    echo "The file exists."
else
    echo "The file does not exist."
fi
```

### Commands Used

```bash
# Make the script executable
chmod +x file_check.sh

# Run the script
./file_check.sh
```

### Output

```text
Enter a filename: hello.sh
The file exists.
```

---

## Task 5: Combine Everything

### server_check.sh

```bash
#!/bin/bash

SERVICE="nginx"

read -p "Do you want to check the status? (y/n) " CHOICE

if [ "$CHOICE" = "y" ]; then
    systemctl status "$SERVICE"

    if systemctl is-active --quiet "$SERVICE"; then
        echo "$SERVICE is active."
    else
        echo "$SERVICE is not active."
    fi
elif [ "$CHOICE" = "n" ]; then
    echo "Skipped."
else
    echo "Invalid choice."
fi
```

### Commands Used

```bash
# Make the script executable
chmod +x server_check.sh

# Run the script
./server_check.sh
```

### Output

```text
Do you want to check the status? (y/n) y
```

The script checks the status of the `nginx` service and prints whether it is active or not.

If I enter `n`:

```text
Do you want to check the status? (y/n) n
Skipped.
```

---

## What I Learned

* Learned how to create and execute Bash scripts using the shebang and execute permission.
* Learned how to use variables, user input, and conditional statements in Bash.
* Learned how Bash scripts can be used to check files and services.

## Files Created

* `hello.sh`
* `variables.sh`
* `greet.sh`
* `check_number.sh`
* `file_check.sh`
* `server_check.sh`
