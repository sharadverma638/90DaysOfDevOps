# Docker Revision

---

## Self-Assessment Checklist

| Topic                                                              | Status |
| ------------------------------------------------------------------ | ------ |
| Run a container from Docker Hub (interactive + detached)           | Can do |
| List, stop, remove containers and images                           | Can do |
| Explain image layers and how caching works                         | Can do |
| Write a Dockerfile from scratch with FROM, RUN, COPY, WORKDIR, CMD | Can do |
| Explain CMD vs ENTRYPOINT                                          | Can do |
| Build and tag a custom image                                       | Can do |
| Create and use named volumes                                       | Can do |
| Use bind mounts                                                    | Can do |
| Create custom networks and connect containers                      | Can do |
| Write a docker-compose.yml for a multi-container app               | Shaky  |
| Use environment variables and .env files in Compose                | Shaky  |
| Write a multi-stage Dockerfile                                     | Shaky  |
| Push an image to Docker Hub                                        | Can do |
| Use healthchecks and depends_on                                    | Can do |

---

## Quick-Fire Questions

### 1. What is the difference between an image and a container?

An image is a read-only template used to create containers. A container is a running instance of an image.

### 2. What happens to data inside a container when you remove it?

Data stored only inside the container is removed with the container. Data stored in volumes or bind mounts can persist.

### 3. How do two containers on the same custom network communicate?

They can communicate using the container or service name as the hostname.

### 4. What does `docker compose down -v` do differently from `docker compose down`?

`docker compose down -v` also removes the volumes created by Compose. `docker compose down` does not remove those volumes by default.

### 5. Why are multi-stage builds useful?

They separate the build environment from the final runtime image, helping create smaller and cleaner images.

### 6. What is the difference between `COPY` and `ADD`?

`COPY` copies files and directories into the image. `ADD` also supports additional features such as extracting local archives.

### 7. What does `-p 8080:80` mean?

It maps port `8080` on the host to port `80` inside the container.

### 8. How do you check how much disk space Docker is using?

```bash
docker system df
```

---

## Revisit Weak Spots

I marked three areas as shaky:

* Writing a `docker-compose.yml` for a multi-container app
* Using environment variables and `.env` files in Compose
* Writing a multi-stage Dockerfile

I revisited two of these areas through previous hands-on work: Docker Compose multi-container applications and multi-stage Docker builds.

---
