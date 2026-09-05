# Networking Concepts: DNS, IP, Subnets and Ports

---

## Task 1: DNS - How Names Become IPs

When I type `google.com` in a browser, the browser needs to find the IP address of the domain. DNS resolves the domain name to an IP address. The browser can then connect to the server using the returned IP address.

### DNS Record Types

* `A` - Maps a domain name to an IPv4 address.
* `AAAA` - Maps a domain name to an IPv6 address.
* `CNAME` - Maps one domain name to another domain name.
* `MX` - Specifies the mail servers for a domain.
* `NS` - Specifies the authoritative name servers for a domain.

```bash
# Task 1: Check DNS information for google.com
dig google.com

# Shows DNS records including A records and TTL
```

### A Record and TTL

* A records returned:

  * `192.178.173.139`
  * `192.178.173.113`
  * `192.178.173.138`
  * `192.178.173.101`
  * `192.178.173.102`
  * `192.178.173.100`
* TTL: `90 seconds`

The DNS query completed successfully with status `NOERROR`.

---

## Task 2: IP Addressing

### What is an IPv4 address?

An IPv4 address is a 32-bit address used to identify a device on a network. It is divided into four octets separated by dots.

Example:

`192.168.1.10`

Each octet can have a value from `0` to `255`.

### Public vs Private IP

* Public IP - Used for communication over the internet.
* Private IP - Used inside private networks.

### Private IP Ranges

* `10.0.0.0/8`
* `172.16.0.0/12`
* `192.168.0.0/16`

```bash
# Task 2: Check IP addresses on my machine
ip addr show

# Shows network interfaces and their assigned IP addresses
```

### Private IP

From my network environment, my private IP is:

`10.46.98.205`

---

## Task 3: CIDR and Subnetting

### What does `/24` mean?

In `192.168.1.0/24`, `/24` means that 24 bits are used for the network portion and 8 bits are available for hosts.

### Why do we subnet?

Subnetting divides a larger network into smaller networks. This makes IP address management, organization, security, and network planning easier.

### CIDR Table

| CIDR  | Subnet Mask       | Total IPs | Usable Hosts |
| ----- | ----------------- | --------- | ------------ |
| `/24` | `255.255.255.0`   | `256`     | `254`        |
| `/16` | `255.255.0.0`     | `65,536`  | `65,534`     |
| `/28` | `255.255.255.240` | `16`      | `14`         |

---

## Task 4: Ports - The Doors to Services

A port is a logical number used to identify a specific network service on a device. Ports allow multiple services to use the same IP address.

### Common Ports

| Port    | Service |
| ------- | ------- |
| `22`    | SSH     |
| `80`    | HTTP    |
| `443`   | HTTPS   |
| `53`    | DNS     |
| `3306`  | MySQL   |
| `6379`  | Redis   |
| `27017` | MongoDB |

```bash
# Task 4: Check listening ports and services
ss -tulpn

# Shows listening TCP and UDP ports
```

### Listening Ports Found

1. Port `80` - HTTP
2. Port `53` - DNS

My `ss -tulpn` output also showed port `631`, which is commonly used for printing services.

---

## Task 5: Putting It Together

### Question 1

**You run `curl http://myapp.com:8080` - what networking concepts from today are involved?**

DNS resolves `myapp.com` to an IP address. Port `8080` identifies the application service, and HTTP is used to communicate with that service.

### Question 2

**Your app can't reach a database at `10.0.1.50:3306` - what would you check first?**

I would first check whether the database is running and listening on port `3306`. Then I would check network connectivity and firewall rules between the application and database.

---

## What I Learned

* Learned how DNS resolves domain names into IP addresses.
* Learned the difference between public and private IP addresses.
* Learned how CIDR and subnetting are used to divide networks.
* Learned common network ports and how to check listening services using `ss`.
