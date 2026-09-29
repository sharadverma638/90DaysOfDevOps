# Multi-Stage Builds and Docker Hub

---

## Task 1: The Problem with Large Images

Created a simple Node.js application:

```javascript
console.log("Hello from Docker!")
```

### Single-Stage Dockerfile

```dockerfile
FROM node:22

WORKDIR /app

COPY index.js .

CMD ["node", "index.js"]
```

Built the image:

```bash
# Build the single-stage Docker image.
sudo docker build -t day35-single-stage:v1 ./single-stage

# Check the size of the single-stage image.
sudo docker images day35-single-stage:v1

# Run the application.
sudo docker run --rm day35-single-stage:v1
```

### Result

The application ran successfully:

```text
Hello from Docker!
```

Image size:

| Image              |   Size |
| ------------------ | -----: |
| day35-single-stage | 1.62GB |

---

## Task 2: Multi-Stage Build

Rewrote the Dockerfile using two stages.

### Multi-Stage Dockerfile

```dockerfile
FROM node:22 AS builder

WORKDIR /app

COPY package.json index.js ./

RUN npm run build

FROM node:22-alpine

WORKDIR /app

COPY --from=builder /app/dist/index.js .

CMD ["node", "index.js"]
```

Built the multi-stage image:

```bash
# Build the multi-stage Docker image.
sudo docker build -t day35-multi-stage:v1 ./multi-stage

# Check the size of the multi-stage image.
sudo docker images day35-multi-stage:v1

# Run the multi-stage image.
sudo docker run --rm day35-multi-stage:v1
```

### Result

The application ran successfully:

```text
Hello from Docker multi-stage build!
```

### Image Size Comparison

| Single-Stage | Multi-Stage |
| ------------ | ----------- |
| 1.62GB       | 238MB       |

The multi-stage image is much smaller because the final image contains only the required application artifact and the minimal runtime image instead of the complete build environment.

---

## Task 3: Push to Docker Hub

Logged in to Docker Hub using the browser-based authentication.

Docker Hub username:

```text
sharadverma638
```

Tagged the image:

```text
sharadverma638/day35-multi-stage:v1
```

Pushed the image successfully:

```text
The push refers to repository [docker.io/sharadverma638/day35-multi-stage]

v1: digest: sha256:491f964860f57af2c04bd870342573293c706ce6e9cbeb07495da55ad1135a08
```

Removed the local multi-stage image and pulled it again from Docker Hub.

```text
Status: Image is up to date for sharadverma638/day35-multi-stage:v1
docker.io/sharadverma638/day35-multi-stage:v1
```

Ran the pulled image successfully:

```text
Hello from Docker multi-stage build!
```

This verified that the image could be pulled from Docker Hub and executed successfully.

---

## Task 4: Docker Hub Repository

Checked the pushed Docker Hub repository.

The pushed image was available as:

```text
sharadverma638/day35-multi-stage:v1
```

The repository description and tags were reviewed in Docker Hub.

The `v1` tag identifies a specific image version. A specific tag can be pulled directly, while `latest` refers to the image assigned the `latest` tag and is not automatically the same as `v1`.

---

## Task 5: Image Best Practices

Applied the required image best practices to a new image.

### Best-Practices Dockerfile

```dockerfile
FROM node:22-alpine

WORKDIR /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY index.js .

USER appuser

CMD ["node", "index.js"]
```

The image was built successfully:

```bash
# Build the best-practices image.
sudo docker build -t day35-best-practices:v1 ./best-practices

# Check the final image size.
sudo docker images day35-best-practices:v1

# Run the application.
sudo docker run --rm day35-best-practices:v1

# Verify that the container runs as the non-root user.
sudo docker run --rm day35-best-practices:v1 id
```

### Result

Application output:

```text
Hello from a Docker best-practices image!
```

Container user:

```text
uid=100(appuser) gid=101(appgroup) groups=101(appgroup),101(appgroup)
```

The container was running as the non-root `appuser`.

### Base Image Size Comparison

| Image          |  Size |
| -------------- | ----: |
| ubuntu:24.04   | 119MB |
| ubuntu         | 160MB |
| node:22-alpine | 238MB |
| my-ubuntu      | 259MB |

The `node:22-alpine` image was used for the application because it provides a smaller Node.js runtime compared with the full `node:22` image used in the single-stage build.

### Best Practices Applied

* Used a minimal Alpine base image.
* Added a non-root `USER`.
* Combined commands in the image build.
* Used a specific `node:22-alpine` tag instead of `latest`.
* Checked image sizes before and after optimization.
* Used multi-stage builds to keep build dependencies out of the final image.

---

## Key Takeaways

1. Multi-stage builds separate the build environment from the final runtime image.
2. Multi-stage builds can significantly reduce the final Docker image size.
3. Docker Hub can be used to push, store, and pull Docker images.
4. Image tags such as `v1` help identify specific image versions.
5. Minimal base images reduce the size of the final image.
6. Running containers as a non-root user is a useful Docker security practice.
