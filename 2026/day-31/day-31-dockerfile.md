# Dockerfile: Build Your Own Images

---

## Task 1: Your First Dockerfile

Created a custom Ubuntu image and installed `curl`.

### Dockerfile

```dockerfile
FROM ubuntu

RUN apt-get update && apt-get install -y curl

CMD ["echo", "Hello from my custom image!"]
```

### Build the image

```bash
# Build the custom Ubuntu image
sudo docker build -t my-ubuntu:v1 .

# The command builds an Ubuntu-based image and tags it as my-ubuntu:v1
```

### Run the container

```bash
# Run the custom image
sudo docker run --rm my-ubuntu:v1

# The container runs the default CMD and prints the configured message
```

---

## Task 2: Dockerfile Instructions

Created a Dockerfile using `FROM`, `RUN`, `COPY`, `WORKDIR`, `EXPOSE`, and `CMD`.

### Dockerfile

```dockerfile
FROM ubuntu

RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY hello.txt .

EXPOSE 8080

CMD ["cat", "hello.txt"]
```

### Build and run

```bash
# Build the Dockerfile instructions image
sudo docker build -t dockerfile-instructions:v1 .

# Build the image using all required Dockerfile instructions
```

```bash
# Run the Dockerfile instructions image
sudo docker run --rm dockerfile-instructions:v1

# The container runs the CMD and displays the contents of hello.txt
```

### Instructions

| Instruction | Purpose                                            |
| ----------- | -------------------------------------------------- |
| `FROM`      | Selects the base image                             |
| `RUN`       | Executes commands while building the image         |
| `COPY`      | Copies files from the host into the image          |
| `WORKDIR`   | Sets the working directory                         |
| `EXPOSE`    | Documents the port used by the application         |
| `CMD`       | Sets the default command when the container starts |

---

## Task 3: CMD vs ENTRYPOINT

### CMD

```dockerfile
FROM ubuntu

CMD ["echo", "hello"]
```

Build and run:

```bash
# Build the CMD example
sudo docker build -f Dockerfile.cmd -t cmd-demo:v1 .

# Build the image using CMD
```

```bash
# Run the image with its default CMD
sudo docker run --rm cmd-demo:v1

# The default command prints hello
```

A custom command can replace the default `CMD`:

```bash
# Override the default CMD
sudo docker run --rm cmd-demo:v1 echo "great!"

# The custom command replaces the original CMD
```

Actual result:

```text
great!
```

### ENTRYPOINT

```dockerfile
FROM ubuntu

ENTRYPOINT ["echo", "hello"]
```

Build and run:

```bash
# Build the ENTRYPOINT example
sudo docker build -f Dockerfile.entrypoint -t entrypoint-demo:v1 .

# Build the image using ENTRYPOINT
```

```bash
# Run the image with its default ENTRYPOINT
sudo docker run --rm entrypoint-demo:v1

# The ENTRYPOINT runs echo hello
```

```bash
# Pass an additional argument to ENTRYPOINT
sudo docker run --rm entrypoint-demo:v1 "great!"

# The argument is added to the ENTRYPOINT command
```

Actual result:

```text
hello great!
```

### CMD vs ENTRYPOINT

| CMD                                                            | ENTRYPOINT                                                        |
| -------------------------------------------------------------- | ----------------------------------------------------------------- |
| Sets a default command                                         | Sets the main command for the container                           |
| Can be completely replaced by a command passed to `docker run` | Additional arguments are normally passed to the ENTRYPOINT        |
| Useful when the default command may need to be changed         | Useful when the container should always run a specific executable |

---

## Task 4: Build a Simple Web App Image

Created a static HTML page and served it using Nginx.

### `index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Docker App</title>
</head>
<body>
    <h1>Hello from my Docker web app!</h1>
    <p>This page is running inside an Nginx container.</p>
</body>
</html>
```

### Dockerfile

```dockerfile
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
```

### Build the image

```bash
# Build the Nginx web application image
sudo docker build -t devops-web:v1 .

# Build the custom Nginx image
```

### Run the container

```bash
# Start the Nginx web application
sudo docker run -d --name devops-web -p 8080:80 devops-web:v1

# Map host port 8080 to Nginx port 80
```

### Verify the container

```bash
# Check the running container
sudo docker ps

# Verify that the Nginx container is running
```

The web page was accessed through:

```text
http://localhost:8080
```

---

## Task 5: .dockerignore

Created a `.dockerignore` file in the web application project.

```text
*.log
.env
.git
```

The `.dockerignore` file prevents matching files from being included in the Docker build context.

### Test file

```bash
# Create a test log file
echo "This file should not be included in the build context." > test.log

# The test file matches the *.log ignore rule
```

### Build the image

```bash
# Build the image using .dockerignore
sudo docker build -t devops-web:v2 .

# Docker uses the .dockerignore file when preparing the build context
```

---

## Task 6: Build Optimization and Cache

Docker images are built in layers. Docker can reuse unchanged layers from previous builds.

### First build

```bash
# Build the image and create its initial layers
sudo docker build -t devops-web:cache-test .

# Docker creates the image layers
```

### Build again without changes

```bash
# Build the same image again
sudo docker build -t devops-web:cache-test .

# Docker can reuse unchanged layers from the previous build
```

### Change the HTML file

```bash
# Add a small change to the web page
echo '<!-- Docker cache test -->' >> index.html

# The HTML file has now changed
```

### Rebuild

```bash
# Rebuild the image after changing the HTML file
sudo docker build -t devops-web:cache-test .

# Docker reuses unchanged layers and rebuilds layers affected by the change
```

### Why layer order matters

Docker builds an image as a series of layers. When a layer changes, later layers may need to be rebuilt.

Frequently changing instructions should generally be placed later in the Dockerfile. This allows Docker to reuse earlier layers and can make builds faster.

---

## Key Takeaways

1. Dockerfiles are used to build custom Docker images.
2. `FROM`, `RUN`, `COPY`, `WORKDIR`, `EXPOSE`, and `CMD` each have a specific role in building an image.
3. `CMD` provides a default command, while `ENTRYPOINT` defines the main executable.
4. `.dockerignore` prevents unnecessary files from being sent to the Docker build context.
5. Docker layer caching can make repeated image builds faster when unchanged layers are reused.
