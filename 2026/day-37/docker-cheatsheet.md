# Docker Cheat Sheet

---

## Container Commands

```bash
docker run nginx
```

Run a container from an image.

```bash
docker run -d nginx
```

Run a container in detached mode.

```bash
docker ps
```

List running containers.

```bash
docker ps -a
```

List all containers.

```bash
docker stop <container>
```

Stop a running container.

```bash
docker rm <container>
```

Remove a container.

```bash
docker exec -it <container> bash
```

Open a shell inside a running container.

```bash
docker logs <container>
```

View container logs.

---

## Image Commands

```bash
docker build -t myimage:v1 .
```

Build an image from a Dockerfile.

```bash
docker pull nginx
```

Download an image from a registry.

```bash
docker push username/myimage:v1
```

Push an image to a registry.

```bash
docker tag myimage:v1 username/myimage:v1
```

Tag an image.

```bash
docker images
```

List local images.

```bash
docker rmi <image>
```

Remove an image.

---

## Volume Commands

```bash
docker volume create myvolume
```

Create a named volume.

```bash
docker volume ls
```

List volumes.

```bash
docker volume inspect myvolume
```

Inspect a volume.

```bash
docker volume rm myvolume
```

Remove a volume.

---

## Network Commands

```bash
docker network create my-app-net
```

Create a custom network.

```bash
docker network ls
```

List Docker networks.

```bash
docker network inspect my-app-net
```

Inspect a network.

```bash
docker network connect my-app-net <container>
```

Connect a container to a network.

---

## Compose Commands

```bash
docker compose up
```

Create and start Compose services.

```bash
docker compose down
```

Stop and remove Compose services.

```bash
docker compose ps
```

List Compose services.

```bash
docker compose logs
```

View Compose logs.

```bash
docker compose build
```

Build Compose images.

---

## Cleanup Commands

```bash
docker system prune
```

Remove unused Docker resources.

```bash
docker system df
```

Show Docker disk usage.

---

## Dockerfile Instructions

```dockerfile
FROM node:22-alpine
```

Set the base image.

```dockerfile
RUN npm install
```

Run a command while building the image.

```dockerfile
COPY . /app
```

Copy files into the image.

```dockerfile
WORKDIR /app
```

Set the working directory.

```dockerfile
EXPOSE 8080
```

Document the container port.

```dockerfile
CMD ["node", "app.js"]
```

Set the default command.

```dockerfile
ENTRYPOINT ["node", "app.js"]
```

Set the main executable for the container.

---
