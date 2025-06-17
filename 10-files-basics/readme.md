## 🗂 Topics Covered
- File Handling in Python

---

## 📘 File Handling in Python

File I/O (Input/Output) allows your Python programs to **read from** and **write to** files on your computer. This is essential for tasks like:
- Saving data
- Reading configuration files
- Processing large datasets

---

### 📂 Opening Files

To work with files, use the `open()` function:

```python
file = open('example.txt', 'r')
````

* `'example.txt'` is the file name
* `'r'` is the mode (read mode in this case)

---

### 🔧 File Modes

| Mode  | Description                                              |
| ----- | -------------------------------------------------------- |
| `'r'` | Read mode – opens file for reading                       |
| `'w'` | Write mode – opens file for writing, truncates if exists |
| `'a'` | Append mode – adds to the end of the file                |
| `'b'` | Binary mode – for binary files like images               |
| `'+'` | Update mode – allows reading and writing                 |

---

### 📖 Reading from Files

Common methods:

* `read()` – Reads the entire file
* `readline()` – Reads one line at a time
* `readlines()` – Reads all lines into a list

```python
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()
```

---

### ✍️ Writing to Files

Use `'w'` (write) or `'a'` (append) mode:

```python
file = open('example.txt', 'w')
file.write('Hello, World!')
file.close()
```

---

### 🔒 Closing Files

Always close files after you're done:

```python
file.close()
```

---

### ✅ Using `with` Statement

The `with` statement automatically handles file closing, even if an error occurs:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

---

### 🚨 Handling Exceptions

Use `try-except` to manage errors like missing files:

```python
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('The file does not exist.')
```

---

### 🛠️ File Methods Summary

| Method                 | Description                        |
| ---------------------- | ---------------------------------- |
| `read(size)`           | Reads `size` bytes from the file   |
| `readline()`           | Reads the next line                |
| `readlines()`          | Reads all lines and returns a list |
| `write(string)`        | Writes a string                    |
| `writelines(list)`     | Writes a list of strings           |
| `seek(offset, whence)` | Moves file cursor                  |
| `tell()`               | Returns current cursor position    |

---

## 🔍 Detailed Explanation of File Methods

### 🔹 `read(size)`

Reads a specific number of bytes:

```python
with open('example.txt', 'r') as file:
    content = file.read(5)
    print(content)
```

---

### 🔹 `readline()`

Reads the next line each time it's called:

```python
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()
```

---

### 🔹 `readlines()`

Reads all lines into a list:

```python
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
```

---

### 🔹 `write(string)`

Writes a string to the file:

```python
with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a new line.')
```

---

### 🔹 `writelines(list)`

Writes a list of strings:

```python
lines = ['First line\n', 'Second line\n', 'Third line\n']
with open('example.txt', 'w') as file:
    file.writelines(lines)
```

---

### 🔹 `seek(offset, whence)`

Moves the file cursor:

* `offset`: number of bytes
* `whence`: reference point

  * `0`: Beginning
  * `1`: Current position
  * `2`: End of file

```python
with open('example.txt', 'r') as file:
    file.seek(10, 0)  # Move to 10th byte
    content = file.read()
    print(content)
```

---

### 🔹 `tell()`

Returns the current file cursor position:

```python
with open('example.txt', 'r') as file:
    print(file.tell())   # Output: 0
    file.read(5)
    print(file.tell())   # Output: 5
```
