# File Permissions and File Operations

## Files Created

* devops.txt
* notes.txt
* script.sh
* project/

## Permission Changes

* script.sh: added execute permission
* devops.txt: removed write permission
* notes.txt: changed to 640
* project/: changed to 755

## Commands Used

```bash
# Task 1: Create files
touch devops.txt
echo "This is my DevOps challenge." > notes.txt
vim script.sh
ls -l
```

```bash
# Task 2: Read files
cat notes.txt
vim -R script.sh
head -n 5 /etc/passwd
tail -n 5 /etc/passwd
```

```bash
# Task 3: Check file permissions
ls -l devops.txt notes.txt script.sh
```

```bash
# Task 4: Change file permissions
chmod +x script.sh
./script.sh
chmod -w devops.txt
chmod 640 notes.txt
mkdir project
chmod 755 project
```

```bash
# Task 5: Test file permissions
echo "Testing permissions" >> devops.txt
chmod -x script.sh
./script.sh
```

```bash
# Task 6: Verify final permissions
ls -l devops.txt notes.txt script.sh project
```

## What I Learned

* Learned how to create and read files in Linux.
* Learned how Linux file permissions work.
* Learned how to change permissions using chmod.
* Learned how to test file permissions.
* Learned the difference between read, write, and execute permissions.
