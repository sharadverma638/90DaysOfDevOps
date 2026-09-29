# Docker Volumes and Networking

---

## Task 1: The Problem

I started a MySQL container without attaching any volume.

```bash
# Start MySQL without a volume
sudo docker run -d --name day32-mysql-test -e MYSQL_ROOT_PASSWORD=devops123 mysql:8.0

# Create a database and table inside the container
sudo docker exec -it day32-mysql-test mysql -uroot -pdevops123
```

I created a database named `devops_test`, a `users` table, and inserted a user.

```text
mysql> SELECT * FROM users;
+----+--------+
| id | name   |
+----+--------+
|  1 | Sharad |
+----+--------+
```

I then stopped and removed the container and created a new MySQL container without a volume.

```bash
# Stop and remove the old container
sudo docker stop day32-mysql-test
sudo docker rm day32-mysql-test

# Start a new MySQL container without the old container data
sudo docker run -d --name day32-mysql-test -e MYSQL_ROOT_PASSWORD=devops123 mysql:8.0

# Check the databases in the new container
sudo docker exec -it day32-mysql-test mysql -uroot -pdevops123 -e "SHOW DATABASES;"
```

The `devops_test` database was no longer present.

```text
Database
information_schema
mysql
performance_schema
sys
```

**Result:** The data was lost because the container was removed and no volume was attached. Container storage is temporary.

---

## Task 2: Named Volumes

I created a named Docker volume and attached it to MySQL.

```bash
# Create a named volume for MySQL data
sudo docker volume create day32-mysql-data

# Start MySQL with the named volume
sudo docker run -d \
  --name day32-mysql-volume \
  -e MYSQL_ROOT_PASSWORD=devops123 \
  -v day32-mysql-data:/var/lib/mysql \
  mysql:8.0
```

I created a database and inserted data.

```text
mysql> SELECT * FROM users;
+----+--------+
| id | name   |
+----+--------+
|  1 | Sharad |
+----+--------+
```

I stopped and removed the container, then created a new container using the same volume.

```bash
# Verify Docker volumes
sudo docker volume ls

# Inspect the named volume
sudo docker volume inspect day32-mysql-data

# Stop and remove the old container
sudo docker stop day32-mysql-volume
sudo docker rm day32-mysql-volume

# Start a new MySQL container using the same volume
sudo docker run -d \
  --name day32-mysql-volume \
  -e MYSQL_ROOT_PASSWORD=devops123 \
  -v day32-mysql-data:/var/lib/mysql \
  mysql:8.0

# Verify that the old data is still available
sudo docker exec day32-mysql-volume \
  mysql -uroot -pdevops123 \
  -e "SELECT * FROM devops_persistent.users;"
```

Actual result:

```text
id	name
1	Sharad
```

**Result:** The data remained available because the data was stored in the named volume instead of the container's writable layer.

### Named Volume vs Bind Mount

| Named Volume                                  | Bind Mount                                      |
| --------------------------------------------- | ----------------------------------------------- |
| Managed by Docker                             | Uses a specific host path                       |
| Good for persistent application data          | Good when the host needs direct access to files |
| Example: `-v day32-mysql-data:/var/lib/mysql` | Example: `-v ~/day32-bind-mount:/data`          |

---

## Task 3: Bind Mounts

I created a directory on the host and mounted it into an Ubuntu container.

```bash
# Create a directory on the host
mkdir -p ~/day32-bind-mount

# Create a test file on the host
echo "Hello from the host machine" > ~/day32-bind-mount/test.txt

# Start an Ubuntu container with a bind mount
sudo docker run -d \
  --name day32-bind-test \
  -v ~/day32-bind-mount:/data \
  ubuntu \
  sleep infinity

# Read the host file from inside the container
sudo docker exec day32-bind-test cat /data/test.txt
```

Actual output:

```text
Hello from the host machine
```

I also created a file from inside the container.

```bash
# Create a file from inside the container
sudo docker exec day32-bind-test \
  bash -c 'echo "Created inside the container" > /data/container.txt'

# Read the file from the host
cat ~/day32-bind-mount/container.txt
```

Actual output:

```text
Created inside the container
```

I then modified the host-mounted file from inside the container.

```bash
# Append data to the mounted file
sudo docker exec day32-bind-test \
  bash -c 'echo "Updated from inside the container" >> /data/test.txt'

# Check the updated file on the host
cat ~/day32-bind-mount/test.txt
```

Actual output:

```text
Hello from the host machine
Updated from inside the container
```

**Result:** Changes made inside the container were visible on the host because both locations point to the same mounted directory.

---

## Task 4: Docker Networking Basics

I listed the Docker networks available on the machine.

```bash
# List Docker networks
sudo docker network ls
```

Actual output:

```text
NETWORK ID     NAME      DRIVER    SCOPE
08b093fd07b0   bridge    bridge    local
1eb998fd7cce   host      host      local
8f581d7051c3   none      null      local
```

I inspected the default `bridge` network.

```bash
# Inspect the default bridge network
sudo docker network inspect bridge
```

The bridge network used:

```text
Subnet: 172.17.0.0/16
Gateway: 172.17.0.1
```

The containers had these IP addresses:

```text
day32-bind-test: 172.17.0.3
devops-web:      172.17.0.2
```

I checked the IP address of the container directly.

```bash
# Get the IP address of the container
sudo docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' day32-bind-test
```

Actual output:

```text
172.17.0.3
```

The first ping attempt failed because the Ubuntu image did not have `ping` installed.

```text
exec: "ping": executable file not found in $PATH
```

After installing `iputils-ping`, I tested communication using the container IP.

```bash
# Test communication using the container IP
sudo docker exec day32-bind-test ping -c 3 172.17.0.2
```

Actual result:

```text
3 packets transmitted, 3 received, 0% packet loss
```

**Result:** Containers on the default bridge were able to communicate using their IP addresses.

**Note:** Name-based communication on the default bridge was not tested separately.

---

## Task 5: Custom Networks

I created a custom Docker bridge network.

```bash
# Create a custom Docker network
sudo docker network create day32-network

# Start the application container on the custom network
sudo docker run -d \
  --name day32-app \
  --network day32-network \
  ubuntu \
  sleep infinity

# Start the client container on the same custom network
sudo docker run -d \
  --name day32-client \
  --network day32-network \
  ubuntu \
  sleep infinity
```

I installed `ping` in the client container and tested communication using the container name.

```bash
# Test name-based communication between containers
sudo docker exec day32-client ping -c 3 day32-app
```

Actual output:

```text
PING day32-app (172.18.0.2) 56(84) bytes of data.
64 bytes from day32-app.day32-network (172.18.0.2): ...
64 bytes from day32-app.day32-network (172.18.0.2): ...
64 bytes from day32-app.day32-network (172.18.0.2): ...

3 packets transmitted, 3 received, 0% packet loss
```

**Result:** The custom network provided automatic name resolution between containers.

The default `bridge` network does not provide the same user-defined DNS-based container name resolution. Custom networks are designed to make container-to-container communication easier using container names.

---

## Task 6: Put It Together

I created a MySQL database container and an application client container on the same custom network.

```bash
# Start MySQL on the custom network
sudo docker run -d \
  --name day32-mysql \
  --network day32-network \
  -e MYSQL_ROOT_PASSWORD=devops123 \
  mysql:8.0

# Start the client container on the same network
sudo docker run -d \
  --name day32-db-client \
  --network day32-network \
  ubuntu \
  sleep infinity

# Install the MySQL client
sudo docker exec day32-db-client apt-get update
sudo docker exec day32-db-client apt-get install -y default-mysql-client
```

I connected to MySQL using the database container name.

```bash
# Connect to MySQL using the container name
sudo docker exec day32-db-client \
  mysql -h day32-mysql -uroot -pdevops123 \
  -e "SELECT VERSION();"
```

Actual output:

```text
mysql: [Warning] Using a password on the command line interface can be insecure.
VERSION()
8.0.46
```

**Result:** The client container successfully resolved `day32-mysql` by name and connected to MySQL over the custom Docker network.

**Note:** The MySQL container used for this final connection was not started with the named volume. The named volume requirement was completed separately in Task 2.

---

## 5 Key Takeaways

1. **Containers are ephemeral**, so important data can be lost when a container is removed.
2. **Named volumes provide persistent storage** that can survive container removal.
3. **Bind mounts connect host directories to containers**, allowing changes to be shared between the host and container.
4. **Custom Docker networks provide container name resolution**, making container-to-container communication easier.
5. **Containers on the same custom network can communicate using container names**, which is useful for application and database communication.
