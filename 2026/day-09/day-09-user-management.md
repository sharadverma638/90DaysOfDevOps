# Linux User & Group Management

## Users & Groups Created

* Users: tokyo, berlin, professor, nairobi
* Groups: developers, admins, project-team

## Group Assignments

* tokyo: developers, project-team
* berlin: developers, admins
* professor: admins
* nairobi: project-team

## Directories Created

* `/opt/dev-project` - group: developers - permissions: 775
* `/opt/team-workspace` - group: project-team - permissions: 775

## Commands Used

```bash
# Task 1: Create Users

sudo useradd -m tokyo
sudo passwd tokyo
sudo useradd -m berlin
sudo passwd berlin
sudo useradd -m professor
sudo passwd professor
sudo useradd -m nairobi
sudo passwd nairobi
```
```bash
# Task 2: Create Groups

sudo groupadd developers
sudo groupadd admins
sudo groupadd project-team
```
```bash
# Task 3: Assign to Groups

sudo usermod -aG developers tokyo
sudo usermod -aG developers berlin
sudo usermod -aG admins berlin
sudo usermod -aG admins professor
sudo usermod -aG project-team nairobi
sudo usermod -aG project-team tokyo
```
```bash
# Task 4: Shared Directory

sudo mkdir -p /opt/dev-project
sudo chgrp developers /opt/dev-project
sudo chmod 775 /opt/dev-project
```
```bash
# Task 5: Team Workspace

sudo mkdir -p /opt/team-workspace
sudo chgrp project-team /opt/team-workspace
sudo chmod 775 /opt/team-workspace
```

## What I Learned

* Learned how to create and manage Linux users.
* Learned how to create groups and assign users to them.
* Learned how to create shared directories using group permissions.
