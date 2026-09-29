# Docker Compose: Multi-Container Basics

---

## Task 1: Install & Verify

I checked whether Docker Compose was available and verified the installed version.

```bash
# Check Docker Compose version
sudo docker compose version

# This verifies that Docker Compose is available
```

Actual output:

```text
Docker Compose version v5.5.1
```

---

## Task 2: Your First Compose File

I created the `compose-basics` folder and created a `docker-compose.yml` file for a single Nginx container.

```yaml
services:
  nginx:
    image: nginx:alpine
    ports:
      - "8080:80"
```

I started the Nginx service with Docker Compose.

```bash
# Start the Nginx container
sudo docker compose up

# This starts Nginx and maps port 8080 on the host to port 80 in the container
```

Nginx started successfully and was accessed through the browser on port `8080`.

The container was then stopped and removed using:

```bash
# Stop and remove the Nginx Compose application
sudo docker compose down

# This removes the container and Compose network
```

---

## Task 3: Two-Container Setup

I created a `docker-compose.yml` containing WordPress and MySQL.

```yaml
services:
  wordpress:
    image: wordpress:latest
    ports:
      - "8081:80"
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress123
      WORDPRESS_DB_NAME: wordpress

  db:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress123
      MYSQL_ROOT_PASSWORD: root123
    volumes:
      - wordpress-db-data:/var/lib/mysql

volumes:
  wordpress-db-data:
```

The WordPress service connects to MySQL using the service name:

```text
WORDPRESS_DB_HOST: db:3306
```

The MySQL data is stored in the named volume:

```text
wordpress-db-data
```

I started both services:

```bash
# Start WordPress and MySQL
sudo docker compose up -d

# This starts both services in the background
```

Actual running services:

```text
NAME                            IMAGE              SERVICE     STATUS
wordpress-compose-db-1          mysql:8.0          db          Up
wordpress-compose-wordpress-1   wordpress:latest   wordpress   Up
```

WordPress was accessed through the browser at:

```text
http://localhost:8081
```

I completed the WordPress setup.

To verify persistence, I removed the containers and network:

```bash
# Stop and remove the WordPress and MySQL containers
sudo docker compose down

# This removes the containers and network but keeps the named volume
```

I then started the application again:

```bash
# Start WordPress and MySQL again
sudo docker compose up -d

# This recreates the containers using the existing named volume
```

WordPress was opened again in the browser and the existing WordPress data was verified after the restart.

---

## Task 4: Compose Commands

### Start services in detached mode

```bash
# Start all Compose services in detached mode
sudo docker compose up -d

# This starts the services in the background
```

### View running services

```bash
# Show the running Compose services
sudo docker compose ps

# This displays the service status and port mappings
```

Actual output:

```text
NAME                            IMAGE              SERVICE     STATUS         PORTS
wordpress-compose-db-1          mysql:8.0          db          Up             3306/tcp, 33060/tcp
wordpress-compose-wordpress-1   wordpress:latest   wordpress   Up             0.0.0.0:8081->80/tcp
```

### View logs of all services

```bash
# View logs from all Compose services
sudo docker compose logs

# This displays logs from WordPress and MySQL
```

The logs showed MySQL becoming ready for connections and WordPress starting successfully.

### View logs of a specific service

```bash
# View logs only from the WordPress service
sudo docker compose logs wordpress

# This displays logs for the WordPress container
```

### Stop services without removing them

```bash
# Stop the Compose services without removing the containers
sudo docker compose stop

# This stops the containers but keeps them available
```

The services were then started again:

```bash
# Start the existing stopped containers
sudo docker compose start

# This starts the existing Compose containers again
```

### Remove everything

```bash
# Remove the Compose containers and network
sudo docker compose down

# This removes the containers and network
```

### Rebuild images

```bash
# Attempt to rebuild the Compose services
sudo docker compose build

# This checks whether any services need to be rebuilt
```

Actual output:

```text
WARN[0000] No services to build
```

The Compose file uses existing images directly, so there were no services configured with a build context.

---

## Task 5: Environment Variables

I first defined environment variables directly inside the Compose file.

The WordPress service used:

```text
WORDPRESS_DB_HOST
WORDPRESS_DB_USER
WORDPRESS_DB_PASSWORD
WORDPRESS_DB_NAME
```

The MySQL service used:

```text
MYSQL_DATABASE
MYSQL_USER
MYSQL_PASSWORD
MYSQL_ROOT_PASSWORD
```

I then created a `.env` file containing the values:

```text
WORDPRESS_DB_USER=wordpress
WORDPRESS_DB_PASSWORD=wordpress123
WORDPRESS_DB_NAME=wordpress
MYSQL_ROOT_PASSWORD=root123
MYSQL_DATABASE=wordpress
MYSQL_USER=wordpress
MYSQL_PASSWORD=wordpress123
```

The Compose file was updated to reference the `.env` variables:

```yaml
services:
  wordpress:
    image: wordpress:latest
    ports:
      - "8081:80"
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: ${WORDPRESS_DB_USER}
      WORDPRESS_DB_PASSWORD: ${WORDPRESS_DB_PASSWORD}
      WORDPRESS_DB_NAME: ${WORDPRESS_DB_NAME}

  db:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
    volumes:
      - wordpress-db-data:/var/lib/mysql

volumes:
  wordpress-db-data:
```

I verified that Docker Compose picked up the variables:

```bash
# Verify the final Compose configuration and environment variables
sudo docker compose config

# This displays the resolved Compose configuration
```

The output showed the environment variables resolved correctly, including:

```text
WORDPRESS_DB_HOST: db:3306
WORDPRESS_DB_NAME: wordpress
WORDPRESS_DB_PASSWORD: wordpress123
WORDPRESS_DB_USER: wordpress
MYSQL_DATABASE: wordpress
MYSQL_PASSWORD: wordpress123
MYSQL_ROOT_PASSWORD: root123
MYSQL_USER: wordpress
```

Finally, I started the services again and verified that both WordPress and MySQL were running.

```bash
# Start the final Compose application
sudo docker compose up -d

# Verify both services
sudo docker compose ps
```

Actual services:

```text
NAME                            IMAGE              SERVICE     STATUS
wordpress-compose-db-1          mysql:8.0          db          Up
wordpress-compose-wordpress-1   wordpress:latest   wordpress   Up
```

---

## 5 Key Takeaways

1. **Docker Compose manages multiple containers** using a single YAML file.
2. **Compose automatically creates a network**, allowing services to communicate using their service names.
3. **Named volumes provide persistent data**, even when Compose containers are removed.
4. **`docker compose` commands** make it easy to start, stop, inspect, view logs, and remove multi-container applications.
5. **Environment variables and `.env` files** keep Compose configuration flexible and easier to manage.
