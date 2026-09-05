# File Ownership

## Files & Directories Created

* devops-file.txt
* team-notes.txt
* project-config.yaml
* app-logs/
* heist-project/
* bank-heist/

## Ownership Changes

* devops-file.txt: changed owner to tokyo, then berlin
* team-notes.txt: changed group to heist-team
* project-config.yaml: changed owner to professor and group to heist-team
* app-logs/: changed owner to berlin and group to heist-team
* heist-project/: changed owner to professor and group to planners recursively
* access-codes.txt: tokyo:vault-team
* blueprints.pdf: berlin:tech-team
* escape-plan.txt: nairobi:vault-team

## Commands Used

```bash
# Task 1: Check ownership
ls -l
```
```bash
# Task 2: Change owner
touch devops-file.txt
ls -l devops-file.txt
sudo chown tokyo devops-file.txt
sudo chown berlin devops-file.txt
ls -l devops-file.txt
```
```bash
# Task 3: Change group
touch team-notes.txt
ls -l team-notes.txt
sudo groupadd heist-team
sudo chgrp heist-team team-notes.txt
ls -l team-notes.txt
```
```bash
# Task 4: Change owner and group
touch project-config.yaml
sudo chown professor:heist-team project-config.yaml
mkdir app-logs
sudo chown berlin:heist-team app-logs
ls -ld app-logs
```
```bash
# Task 5: Recursive ownership
mkdir -p heist-project/vault
mkdir -p heist-project/plans
touch heist-project/vault/gold.txt
touch heist-project/plans/strategy.conf
sudo groupadd planners
sudo chown -R professor:planners heist-project/
ls -lR heist-project/
```
```bash
# Task 6: Practice challenge
mkdir bank-heist
touch bank-heist/access-codes.txt
touch bank-heist/blueprints.pdf
touch bank-heist/escape-plan.txt
sudo groupadd vault-team
sudo groupadd tech-team
sudo chown tokyo:vault-team bank-heist/access-codes.txt
sudo chown berlin:tech-team bank-heist/blueprints.pdf
sudo chown nairobi:vault-team bank-heist/escape-plan.txt
ls -l bank-heist/
```

## What I Learned

* Learned how to check file ownership using `ls -l`.
* Learned how to change file owner using `chown`.
* Learned how to change file group using `chgrp`.
* Learned how to change ownership recursively using `chown -R`.
