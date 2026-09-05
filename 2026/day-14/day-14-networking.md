# Networking Fundamentals & Hands-on Checks

## Task

Get comfortable with core networking concepts and the commands used during troubleshooting.

Today I practiced basic networking concepts, checked connectivity, inspected listening ports, tested DNS resolution, checked an HTTP response, and performed a local port probe.

---

## Quick Concepts

### OSI vs TCP/IP

* The OSI model has 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application.
* The TCP/IP model has 4 layers: Link, Internet, Transport, and Application.

### Where Protocols Sit

* IP works at the Network layer in OSI and the Internet layer in TCP/IP.
* TCP and UDP work at the Transport layer.
* HTTP and HTTPS work at the Application layer.
* DNS works at the Application layer.

### Real Example

* `curl https://example.com` = Application layer over TCP over IP.

---

## Hands-on Checklist

### Identity

```bash
# Check the local IP address
hostname -I
```

**Observation:**
My local machine returned an IP address from the local network. This helped me identify the IP assigned to my system.

> Example: 192.168.1.10

### Reachability

```bash
# Check whether the target is reachable
ping google.com
```

**Observation:**
The target was reachable and replies were received successfully. The latency was low and there was no packet loss.

> Example: 64 bytes from google.com: icmp_seq=1 ttl=... time=...

### Path

```bash
# Check the network path to the target
traceroute google.com
```

```bash
# Alternative command
tracepath google.com
```

**Observation:**
The command showed multiple hops between my machine and the target. Some hops may not respond because of network or firewall restrictions.

### Ports

```bash
# Show listening TCP and UDP ports
ss -tulpn
```

**Observation:**
I found a listening service and checked its port.

> Example: SSH - Port 22

### Name Resolution

```bash
# Resolve the domain name
dig google.com
```

```bash
# Alternative command
nslookup google.com
```

**Observation:**
DNS successfully resolved `google.com` to an IP address.

> Example: 142.250.x.x

### HTTP Check

```bash
# Check the HTTP response headers
curl -I https://example.com
```

**Observation:**
The server returned a successful HTTP response.

> Example: HTTP/2 200

The `200` status code means the request was successful.

### Connections Snapshot

```bash
# Show a snapshot of network connections
netstat -an | head
```

**Observation:**
I checked the current connection states and roughly compared `ESTABLISHED` and `LISTEN` entries.

## Target

I used:

```text
google.com
```

for the ping, traceroute, and HTTP checks where possible.

---

## Mini Task: Port Probe & Interpret

### 1. Identify a Listening Port

```bash
# Find a listening port
ss -tulpn
```

I identified:

```text
Service: SSH
Port: 22
```

### 2. Test the Port

```bash
# Test the local SSH port
nc -zv localhost 22
```

**Result:**
The port was reachable because the SSH service was listening on port 22.

### 3. Interpret the Result

The port was reachable. If it was not reachable, my next checks would be the service status and firewall rules.

## Reflection

### Which command gives you the fastest signal when something is broken?

`ping` gives me a quick signal about basic network reachability and latency.

### What layer would you inspect next if DNS fails?

I would inspect the Application layer because DNS is an Application layer protocol. I would also check the configured DNS server and network connectivity.

### What layer would you inspect next if HTTP 500 shows up?

I would inspect the Application layer because HTTP is an Application layer protocol. An HTTP 500 usually points to a server-side application problem.

### Two follow-up checks I would run in a real incident

1. Check service status and listening ports.
2. Check firewall rules and application logs.
