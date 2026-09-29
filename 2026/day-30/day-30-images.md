# Docker Images and Container Lifecycle

---

## Task 1: Docker Images

Docker images are templates used to create containers.

### Pull Docker Images

```bash
# Pull the Nginx image
sudo docker pull nginx

# Pull the Ubuntu image
sudo docker pull ubuntu

# Pull the Alpine image
sudo docker pull alpine

# List all images on the machine
sudo docker images
# Check the REPOSITORY, TAG, IMAGE ID and SIZE columns.
```

### Ubuntu vs Alpine

| Ubuntu                               | Alpine                               |
| ------------------------------------ | ------------------------------------ |
| Larger image                         | Much smaller image                   |
| Includes more packages and utilities | Includes only the basics             |
| Good for general-purpose workloads   | Good when a small image is preferred |
| Uses more storage                    | Uses less storage                    |

Alpine is much smaller because it is designed as a minimal Linux distribution with fewer packages.

### Inspect an Image

```bash
# Inspect the Nginx image
sudo docker image inspect nginx
# This shows image configuration, environment details, architecture and other metadata.
```

### Remove an Unused Image

```bash
# Remove the Alpine image if it is no longer needed
sudo docker image rm alpine

# Check the remaining images
sudo docker images
# Alpine should be removed if nothing is using it.
```

---

## Task 2: Image Layers

Docker images are built from multiple layers. Each layer represents a change made while building the image.

```bash
# View the layers of the Nginx image
sudo docker image history nginx
# Each row represents a layer and shows its size and the command that created it.
```

Some layers may show a size, while others may show `0B`.

### What are image layers?

Image layers are separate read-only parts of an image. Docker uses layers so unchanged parts can be reused instead of being downloaded or built again.

### Why does Docker use layers?

* Saves storage
* Speeds up image builds
* Makes caching possible
* Allows unchanged layers to be reused

---

## Task 3: Container Lifecycle

I practiced the complete lifecycle using one Nginx container.

### Create Without Starting

```bash
# Create a container without starting it
sudo docker create --name lifecycle-demo nginx

# Check the container state
sudo docker ps -a
# The container should exist but should not be running.
```

### Start the Container

```bash
# Start the container
sudo docker start lifecycle-demo

# Check the container state
sudo docker ps -a
# The container should now show as running.
```

### Pause the Container

```bash
# Pause the running container
sudo docker pause lifecycle-demo

# Check the container state
sudo docker ps -a
# The container should show a paused state.
```

### Unpause the Container

```bash
# Resume the paused container
sudo docker unpause lifecycle-demo

# Check the container state
sudo docker ps -a
# The container should be running again.
```

### Stop the Container

```bash
# Stop the container normally
sudo docker stop lifecycle-demo

# Check the container state
sudo docker ps -a
# The container should now be stopped.
```

### Restart the Container

```bash
# Start the stopped container again
sudo docker restart lifecycle-demo

# Check the container state
sudo docker ps -a
# The container should be running again.
```

### Kill the Container

```bash
# Forcefully stop the running container
sudo docker kill lifecycle-demo

# Check the container state
sudo docker ps -a
# The container should now be stopped.
```

### Remove the Container

```bash
# Remove the stopped container
sudo docker rm lifecycle-demo

# Confirm that it was removed
sudo docker ps -a
# lifecycle-demo should no longer appear.
```

### Container States I Observed

| State   | Meaning                              |
| ------- | ------------------------------------ |
| Created | Container exists but has not started |
| Running | Container is actively running        |
| Paused  | Container is temporarily frozen      |
| Stopped | Container is no longer running       |
| Removed | Container no longer exists           |

---

## Task 4: Working with Running Containers

I used a separate Nginx container for this task.

### Run Nginx in Detached Mode

```bash
# Start an Nginx container in the background
sudo docker run -d --name day30-nginx -p 8080:80 nginx

# Check the running container
sudo docker ps
# The day30-nginx container should be running.
```

### View Logs

```bash
# Show the container logs
sudo docker logs day30-nginx
# This displays the logs produced by the Nginx container.
```

### View Real-Time Logs

```bash
# Follow the logs in real time
sudo docker logs -f --tail 20 day30-nginx
# Press Ctrl+C to stop following the logs.
```

### Exec Into the Container

```bash
# Open a shell inside the running container
sudo docker exec -it day30-nginx /bin/sh
# This opens an interactive shell inside the Nginx container.
```

Inside the container:

```bash
# List the root directory
ls

# Check the Nginx web directory
ls /usr/share/nginx/html

# Exit the container shell
exit
```

### Run One Command Without Entering the Container

```bash
# Check the Nginx version inside the container
sudo docker exec day30-nginx nginx -v
# This runs the command directly inside the container.
```

### Inspect the Container

```bash
# Inspect the container configuration
sudo docker inspect day30-nginx
# Look for the container IP address, port bindings and mount information.
```

Useful focused checks:

```bash
# Show the container IP address
sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' day30-nginx

# Show the published port
sudo docker port day30-nginx
# This shows how host port 8080 maps to container port 80.

# Show mounted filesystems
sudo docker inspect -f '{{json .Mounts}}' day30-nginx
```

---

## Task 5: Cleanup

### Stop All Running Containers

```bash
# Stop all currently running containers
sudo docker ps -q | xargs -r sudo docker stop
# This stops every running container in one command.
```

### Remove All Stopped Containers

```bash
# Remove all stopped containers
sudo docker ps -aq | xargs -r sudo docker rm
# This removes containers that are no longer running.
```

### Remove Unused Images

```bash
# Remove unused Docker images
sudo docker image prune -f
# This removes dangling images that are not being used.
```

### Check Docker Disk Usage

```bash
# Show Docker disk usage
sudo docker system df
# This shows how much space images, containers and volumes are using.
```

---

## Screenshots

Take screenshots of these key commands using the actual output from my machine:

```bash
# Show downloaded Docker images and their sizes
sudo docker images
```

```bash
# Show the container lifecycle state
sudo docker ps -a
```

```bash
# Show image layers
sudo docker image history nginx
```

```bash
# Show the running Nginx container
sudo docker ps
```

```bash
# Inspect the running Nginx container
sudo docker inspect day30-nginx
```

---

## 5 Key Takeaways

1. **Docker images are templates** used to create containers.
2. **Images use layers** to improve caching, storage and build speed.
3. **Containers have a lifecycle** from creation to running, pausing, stopping and removal.
4. **`docker exec`, `docker logs` and `docker inspect`** help manage and troubleshoot running containers.
5. **Regular Docker cleanup** helps keep unused containers and images from consuming disk space.
