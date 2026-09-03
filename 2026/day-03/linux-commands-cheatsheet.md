# Linux Commands Cheatsheet

## 1. Process Management

| Command           | Use                                                   |
| ----------------- | ----------------------------------------------------- |
| `ps aux`          | Shows all running processes.                          |
| `top`             | Shows live CPU and memory usage.                      |
| `htop`            | Interactive view of running processes.                |
| `pgrep nginx`     | Finds the PID of a process by name.                   |
| `kill PID`        | Stops a process using its PID.                        |
| `kill -9 PID`     | Force stops a process when normal kill does not work. |
| `pkill nginx`     | Stops processes by their name.                        |
| `jobs`            | Shows jobs running in the current terminal.           |
| `nohup command &` | Runs a command in the background after logout.        |

## 2. File System

| Command                       | Use                                          |
| ----------------------------- | -------------------------------------------- |
| `pwd`                         | Shows the current directory.                 |
| `ls -lah`                     | Lists files with details and readable sizes. |
| `cd /path`                    | Moves to another directory.                  |
| `mkdir test`                  | Creates a new directory.                     |
| `touch file.txt`              | Creates an empty file.                       |
| `cp file1 file2`              | Copies a file.                               |
| `mv old new`                  | Moves or renames a file.                     |
| `rm file`                     | Deletes a file.                              |
| `find /var/log -name "*.log"` | Finds files by name.                         |
| `du -sh *`                    | Shows the size of files and directories.     |
| `df -h`                       | Shows available disk space.                  |
| `chmod 755 file`              | Changes file permissions.                    |
| `chown user:user file`        | Changes file owner and group.                |

## 3. Logs and Troubleshooting

| Command                | Use                                   |
| ---------------------- | ------------------------------------- |
| `cat file`             | Displays file content.                |
| `less file`            | Reads a file page by page.            |
| `head file`            | Shows the first lines of a file.      |
| `tail file`            | Shows the last lines of a file.       |
| `tail -f app.log`      | Continuously watches new log entries. |
| `grep "error" app.log` | Searches for specific text in a log.  |
| `journalctl -u nginx`  | Shows logs for the nginx service.     |

## 4. Networking Troubleshooting

| Command                       | Use                                          |
| ----------------------------- | -------------------------------------------- |
| `ping google.com`             | Checks basic network connectivity.           |
| `ip addr`                     | Shows network interfaces and IP addresses.   |
| `curl -I https://example.com` | Checks whether an HTTP server is responding. |
| `dig example.com`             | Checks DNS information.                      |
| `ss -tuln`                    | Shows listening ports and network sockets.   |
| `traceroute google.com`       | Shows the network path to a destination.     |

## Key Takeaways

* **Process Management:** Used to find, monitor and stop running processes.
* **File System:** Used to manage files, directories, permissions and disk space.
* **Logs and Troubleshooting:** Used to read logs and find application or service errors.
* **Networking:** Used to check connectivity, IPs, DNS, ports and network paths.
