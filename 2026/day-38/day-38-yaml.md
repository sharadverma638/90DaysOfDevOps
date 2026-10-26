# YAML Basics

---

## Task 1: Key-Value Pairs

Created `person.yaml` with basic YAML key-value pairs:

```yaml
name: Sharad
role: DevOps Learner
experience_years: 0
learning: true
```

The `learning` value is a boolean because it is written as `true`, not `"true"`.

---

## Task 2: Lists

Added five DevOps tools and hobbies to `person.yaml`.

```yaml
tools:
  - Git
  - Docker
  - GitHub Actions
  - Kubernetes
  - Terraform

hobbies: [coding, reading, learning]
```

### Two ways to write a list in YAML

1. **Block style**

```yaml
tools:
  - Git
  - Docker
  - Kubernetes
```

2. **Inline style**

```yaml
hobbies: [coding, reading, learning]
```

---

## Task 3: Nested Objects

Created `server.yaml` with nested server and database configuration.

```yaml
server:
  name: devops-app-server
  ip: 192.168.1.10
  port: 8080

database:
  host: db.internal
  name: hospital_management
  credentials:
    user: app_user
    password: devops123
```

YAML uses indentation to represent nested objects.

YAML uses **spaces**, not tabs. Using a tab for indentation causes a YAML validation/parsing error.

---

## Task 4: Multi-line Strings

Used both YAML multiline styles in `server.yaml`.

### `|` Block Style

```yaml
startup_script: |
  #!/bin/bash
  echo "Starting application server"
  systemctl start nginx
```

The `|` style **preserves newlines**.

It is useful for scripts, configuration blocks, or text where the original line structure matters.

### `>` Fold Style

```yaml
startup_script_folded: >
  echo "Starting application server"
  echo "Checking required services"
  echo "Startup configuration loaded"
```

The `>` style **folds the lines into a single line**.

It is useful when the content should be treated as one continuous string.

---

## Task 5: Validate YAML

Installed `yamllint` and validated both YAML files.

```bash
yamllint person.yaml
yamllint server.yaml
```

I also intentionally broke the indentation to check the validation error.

After fixing the indentation, the YAML files were validated again.

---

## Task 6: Spot the Difference

### Correct

```yaml
name: devops
tools:
  - docker
  - kubernetes
```

### Broken

```yaml
name: devops
tools:
- docker
  - kubernetes
```

The problem is **inconsistent indentation**.

The list items under `tools` should have the same indentation level.

Correct version:

```yaml
name: devops
tools:
  - docker
  - kubernetes
```

---

## What I Learned

1. YAML depends heavily on **indentation** and uses spaces instead of tabs.
2. YAML lists can be written using **block style** or **inline style**.
3. The `|` style preserves newlines, while the `>` style folds multiline text into a single line.
