# File IO Practice

## 1. Create the File

```bash
touch notes.txt
```

**Use:** Creates an empty text file.

## 2. Write to the File

```bash
echo "Dog" > notes.txt
```

**Use:** Writes `Dog` to the file.

**Output:**

```bash
Dog
```

## 3. Append to the File

```bash
echo "Cat" >> notes.txt
```

**Use:** Adds `Cat` to the end of the file.

**Output:**

```bash
Dog
Cat
```

## 4. Write and Display

```bash
echo "Mouse" | tee -a notes.txt
```

**Use:** Adds `Mouse` to the file and displays it.

**Output:**

```bash
Mouse
```

## 5. Read the Full File

```bash
cat notes.txt
```

**Use:** Displays the complete file.

**Output:**

```bash
Dog
Cat
Mouse
```

## 6. Read First 2 Lines

```bash
head -n 2 notes.txt
```

**Use:** Displays the first two lines.

**Output:**

```bash
Dog
Cat
```

## 7. Read Last 2 Lines

```bash
tail -n 2 notes.txt
```

**Use:** Displays the last two lines.

**Output:**

```bash
Cat
Mouse
```

## Key Takeaways

* **Create:** `touch` creates a new file.
* **Write:** `>` writes new content to a file.
* **Append:** `>>` adds content without removing existing content.
* **Read:** `cat`, `head` and `tail` are used to read file content.
* **tee:** Writes content to a file and displays it on the terminal.
