# Docker Compose: Real-World Multi-Container Apps

---

## Task 1: Build Your Own App Stack

Created a 3-service Docker Compose application with:

* Flask web application
* MySQL database
* Redis cache

### Flask Application

`app/app.py`

```python
from flask import Flask
import os
import mysql.connector
import redis

app = Flask(__name__)

@app.route("/")
def home():
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "devops"),
        password=os.getenv("DB_PASSWORD", "devops123"),
        database=os.getenv("DB_NAME", "devops")
    )

    cache = redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=6379
    )

    db.close()

    return "Hello from Flask! Database and Redis are connected."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### Dockerfile

`app/Dockerfile`

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Compose Stack

The Compose file created the web, database and Redis services.

```yaml
services:
  web:
    build: ./app
    ports:
      - "5000:5000"
    environment:
      DB_HOST: db
      DB_USER: devops
      DB_PASSWORD: devops123
      DB_NAME: devops
      REDIS_HOST: redis

  db:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: devops
      MYSQL_USER: devops
      MYSQL_PASSWORD: devops123
      MYSQL_ROOT_PASSWORD: root123

  redis:
    image: redis:alpine
```

### Result

All three services started successfully.

| Service | Image             | Status  |
| ------- | ----------------- | ------- |
| web     | day34-compose-web | Running |
| db      | mysql:8.0         | Running |
| redis   | redis             | Running |

The Flask application was exposed on port `5000`.

---

## Task 2: depends_on & Healthchecks

Added a database healthcheck and configured the web service to wait for the database to become healthy.

```yaml
depends_on:
  db:
    condition: service_healthy
```

Database healthcheck:

```yaml
healthcheck:
  test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-uroot", "-proot123"]
  interval: 5s
  timeout: 5s
  retries: 10
```

The stack was brought down and started again.

### Result

```text
day34-compose-db-1       Up 6 seconds (healthy)
day34-compose-redis-1    Up 6 seconds
day34-compose-web-1      Up Less than a second
```

Database health check returned:

```text
healthy
```

The web service was configured to wait for the database healthcheck.

---

## Task 3: Restart Policies

First, `restart: always` was added to the database service.

The database container was manually killed and the container was checked after waiting for the restart.

The test was then repeated using:

```yaml
restart: on-failure
```

### Result

The database container was recreated and became healthy when the Compose stack was brought up again.

| `restart: always`                                     | `restart: on-failure`                                      |
| ----------------------------------------------------- | ---------------------------------------------------------- |
| Restarts the container regardless of its exit status. | Restarts the container when it exits because of a failure. |

---

## Task 4: Custom Dockerfiles in Compose

The web service uses:

```yaml
build: ./app
```

A code change was made to the Flask application:

```text
Hello from Flask! Database and Redis are connected. Code updated!
```

The application was rebuilt and restarted with:

```bash
# Rebuild the web image and restart the Compose services.
sudo docker compose up -d --build

# Check the status of all services.
sudo docker compose ps
```

### Result

The image was rebuilt successfully.

```text
[+] Building 2.0s (12/12) FINISHED
✔ Image day34-compose-web Built
```

All three services were running after the rebuild.

---

## Task 5: Named Networks & Volumes

An explicit network, named database volume and service labels were added.

### Named Network

```yaml
networks:
  app-network:
    name: day34-app-network
```

### Named Volume

```yaml
volumes:
  db-data:
    name: day34-db-data
```

The database service uses the volume:

```yaml
volumes:
  - db-data:/var/lib/mysql
```

### Service Labels

Labels were added to the services for organization.

Example for the web service:

```yaml
labels:
  com.90days.service: "web"
  com.90days.category: "application"
```

### Result

The named network was created:

```text
day34-app-network    bridge    local
```

The named volume was created:

```text
day34-db-data
```

The web service labels were verified successfully:

```json
{
  "com.90days.category": "application",
  "com.90days.service": "web"
}
```

All three services were running after recreating the stack.

---

## Task 6: Scaling Bonus

The web service was scaled to 3 replicas using:

```bash
# Try to scale the web service to three replicas.
sudo docker compose up -d --scale web=3
```

### Result

The first web container was already using host port `5000`.

The second replica failed to start because it also attempted to bind the same host port:

```text
Error response from daemon:
failed to set up container networking:
Bind for 0.0.0.0:5000 failed:
port is already allocated
```

The scaling test showed that simple scaling does not work when every replica uses the same host port mapping:

```yaml
ports:
  - "5000:5000"
```

Only one container can bind host port `5000` at the same time.

---

## Key Takeaways

1. Docker Compose can run multiple services such as a web app, MySQL and Redis together.
2. `depends_on` with a healthcheck can control when a dependent service starts.
3. Restart policies such as `always` and `on-failure` control how containers are restarted.
4. Compose can build application images directly from a custom Dockerfile.
5. Named networks, volumes and labels help manage communication, persistent data and service organization.
6. Scaling a service with a fixed host port can cause a port conflict when multiple replicas try to use the same port.
