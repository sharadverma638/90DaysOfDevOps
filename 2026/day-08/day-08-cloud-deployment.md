# Cloud Deployment

## Commands Used

```bash
sudo apt-get update
# Updates the package list on the server.

sudo apt-get upgrade
# Upgrades installed packages to their latest available versions.

sudo apt install docker.io -y
# Installs Docker on the server.

sudo systemctl status docker
# Checks whether the Docker service is running.

sudo apt install nginx -y
# Installs Nginx web server.

sudo systemctl status nginx
# Checks whether the Nginx service is running.

sudo tail -n 50 /var/log/nginx/access.log > nginx-logs.txt
# Saves the last 50 Nginx access log entries into a file.

sudo tail -n 50 /var/log/nginx/error.log >> nginx-logs.txt
# Adds the last 50 Nginx error log entries to the same file.
```

## Challenges Faced

* I had some difficulty finding the Nginx log files.
* I also had trouble finding the inbound rules settings and allowing traffic on port 80.
* I used Claude to understand these issues and fix them.

## What I Learned

* Learned how to launch and access a cloud server (EC2).
* Learned how to connect to a remote server using SSH.
* Learned how to install and run Docker and Nginx.
* Learned how to allow web traffic using port 80.
* Learned how to collect and check Nginx logs.

## Proof / Files

* [SSH Connection Screenshot](https://github.com/sharadverma638/90DaysOfDevOps/blob/master/2026/day-08/ssh-connection.png)
* [Docker and Nginx Screenshot](https://github.com/sharadverma638/90DaysOfDevOps/blob/master/2026/day-08/docker-nginx.png)
* [Nginx Webpage Screenshot](https://github.com/sharadverma638/90DaysOfDevOps/blob/master/2026/day-08/nginx-webpage.png)
* [Nginx Logs](https://github.com/sharadverma638/90DaysOfDevOps/blob/master/2026/day-08/nginx-logs.txt)
