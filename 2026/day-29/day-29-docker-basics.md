# Docker Basics

---

## Task 1: What is Docker?

### What is a container?

A container is a lightweight package that contains an application and everything it needs to run. Containers help keep applications consistent across different environments.

### Why do we need containers?

Containers help with:

* Consistent environments
* Faster deployment
* Easy scaling
* Better resource usage
* Isolating applications from each other

### Containers vs Virtual Machines

| Containers                                  | Virtual Machines                        |
| ------------------------------------------- | --------------------------------------- |
| Share the host operating system kernel      | Include a full guest operating system   |
| Lightweight                                 | Heavier                                 |
| Start quickly                               | Take more time to start                 |
| Use fewer resources                         | Use more resources                      |
| Good for microservices and fast deployments | Useful when full OS isolation is needed |

### Docker Architecture

Docker mainly has these parts:

| Component        | Purpose                                         |
| ---------------- | ----------------------------------------------- |
| Docker Client    | Sends commands to Docker                        |
| Docker Daemon    | Manages images, containers and Docker resources |
| Docker Image     | Read-only template used to create containers    |
| Docker Container | Running instance of an image                    |
| Docker Registry  | Stores and distributes Docker images            |

### Docker Architecture in Simple Words

```text
Docker Client
     |
     v
Docker Daemon
     |
     +---- Docker Images
     |
     +---- Docker Containers
     |
     +---- Docker Registry
```

The Docker client sends commands to the Docker daemon. The daemon uses images to create containers. Images can be downloaded from a registry such as Docker Hub.

---

## Task 2: Install Docker

Docker was already used during my earlier cloud server setup, so I first checked whether it was already installed.

```bash
# Check whether Docker is installed
docker --version

# Check the Docker service
sudo systemctl status docker
# This verifies the Docker installation and service status.
```

If Docker is not installed:

```bash
# Update package information
sudo apt update

# Install Docker
sudo apt install docker.io -y

# Start Docker and enable it at boot
sudo systemctl enable --now docker

# Verify the installation
docker --version
# This confirms Docker is installed.
```

### Run the hello-world container

```bash
# Run the official hello-world container
sudo docker run hello-world
# Docker downloads the image if it is not already available and starts a container.
```

### What happened?

Docker checked whether the `hello-world` image was available locally. If it was not available, Docker downloaded it from the registry. Docker then created a container from the image, ran it, displayed the message, and exited the container.

---

## Task 3: Run Real Containers

### Run an Nginx container

```bash
# Run Nginx in the background with a custom name and port mapping
sudo docker run -d --name devops-nginx -p 8080:80 nginx
# Port 8080 on the host is mapped to port 80 inside the Nginx container.
```

Open this in the browser:

```text
http://localhost:8080
```

If Docker is running on a cloud server, open:

```text
http://<server-ip>:8080
```

### Run an Ubuntu container

```bash
# Start Ubuntu in interactive mode
sudo docker run -it --name devops-ubuntu ubuntu bash
# This opens a shell inside the Ubuntu container.
```

Inside the container:

```bash
# Check the current directory
pwd

# List files
ls

# Check the Ubuntu release information
cat /etc/os-release

# Exit the container
exit
```

### List running containers

```bash
# Show currently running containers
sudo docker ps
# This shows containers that are currently running.
```

### List all containers

```bash
# Show running and stopped containers
sudo docker ps -a
# This also includes containers that have already exited.
```

---

## Task 4: Explore Docker

### Detached mode

The Nginx container was started with `-d`, which means detached mode.

```bash
# Start Nginx in detached mode
sudo docker run -d --name devops-nginx -p 8080:80 nginx
# The terminal is returned immediately while the container keeps running in the background.
```

Detached mode lets a container continue running without keeping the terminal attached to it.

### Custom container name

The container was given the name `devops-nginx`.

```bash
# Check the container name
sudo docker ps
# The NAME column should show devops-nginx.
```

### Port mapping

```bash
# Map host port 8080 to container port 80
sudo docker run -d --name devops-nginx -p 8080:80 nginx
# The application is available through host port 8080.
```

### Check container logs

```bash
# View Nginx container logs
sudo docker logs devops-nginx
# This displays output generated by the running container.
```

### Run a command inside the container

```bash
# Check the Nginx version inside the running container
sudo docker exec devops-nginx nginx -v
# This runs a command inside the existing container.
```

Or open a shell:

```bash
# Open a shell inside the running Nginx container
sudo docker exec -it devops-nginx /bin/sh
# This gives an interactive shell inside the container.
```

Inside the container:

```bash
# List the Nginx web root
ls /usr/share/nginx/html

# Exit the container shell
exit
```

### Stop and remove the container

```bash
# Stop the Nginx container
sudo docker stop devops-nginx

# Remove the stopped container
sudo docker rm devops-nginx

# Verify the container was removed
sudo docker ps -a
# devops-nginx should no longer appear in the container list.
```

---

## 5 Key Takeaways

1. **Docker runs applications in containers** that are lightweight and portable.
2. **Images are templates**, while containers are running instances of those images.
3. **`docker run` creates and starts containers** from images.
4. **Port mapping connects the host to a service inside the container.**
5. **Docker is a foundation for modern DevOps**, including CI/CD, microservices, and Kubernetes.

---
