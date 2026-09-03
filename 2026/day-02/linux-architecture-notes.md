# Linux Architecture, Processes and systemd

## 1. Linux Architecture

- **Kernel:** The core of Linux. It manages CPU, memory, hardware and processes.
- **User Space:** Where users, commands and applications run.
- **systemd:** The main system and service manager on most modern Linux systems. It starts and manages services.

## 2. Linux Processes

- A **process** is a program that is currently running.
- Every process has a **PID** (Process ID).
- Processes can be started, monitored, stopped and restarted.

### Common Process States

- **Running (R):** Process is running or ready to run.
- **Sleeping (S):** Process is waiting for an event.
- **Stopped (T):** Process has been stopped.
- **Zombie (Z):** Process has finished but its parent has not collected its status.
- **Uninterruptible sleep (D):** Usually waiting for I/O.

## 3. systemd

- `systemd` runs as **PID 1** during normal system startup.
- It starts and manages system services.
- It can start, stop, restart and check services.
- `systemctl` is used to control systemd services.
- `journalctl` is used to view systemd logs.

Example:

```bash
systemctl status nginx
```

This checks the status of the nginx service.

## 4. 5 Useful Commands

```bash
ps
top
systemctl status nginx
kill PID
journalctl
```

- `ps` - Shows running processes.
- `top` - Shows live CPU and memory usage.
- `systemctl` - Manages services.
- `kill` - Sends a signal to a process.
- `journalctl` - Shows systemd logs.

## Key Takeaways

- **Kernel** manages CPU, memory, hardware and processes.
- **Processes** are running programs with a unique PID.
- **systemd** manages system services and starts during boot.
- **systemctl** manages services.
- **journalctl** helps check system logs.
- These basics are important for **DevOps troubleshooting**.
