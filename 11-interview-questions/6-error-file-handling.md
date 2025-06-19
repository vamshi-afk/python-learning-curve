## Error Handling and File Handling (Interview Questions)

### Q1. What is the difference between `try-except` and `try-except-finally` blocks in Python?

* `try-except`: Used to catch and handle exceptions that occur in the `try` block.
* `try-except-finally`: Ensures that the `finally` block always executes, used for cleanup actions.

---

### Q2. Can you catch multiple exceptions in a single `except` block? Provide an example.

Yes.

```python
try:
    x = 1 / 0
except (ZeroDivisionError, TypeError) as e:
    print(f"Error: {e}")
```

---

### Q3. How to delete a file using Python?

* `os.remove()`
* `os.unlink()`

---

### Q4. What are Exception Groups in Python?

Introduced in Python 3.11 to handle multiple exceptions:

```python
try:
    raise ExceptionGroup('Example', (
        TypeError('Example TypeError'),
        ValueError('Example ValueError'),
        KeyError('Example KeyError'),
        AttributeError('Example AttributeError')
    ))
except* TypeError:
    ...
except* ValueError as e:
    ...
except* (KeyError, AttributeError) as e:
    ...
```

---

### Q5. What is the difference between `read()`, `readline()`, and `readlines()`?

* `read()`: Entire file as a string.
* `readline()`: One line at a time.
* `readlines()`: List of all lines.

---

### Q6. What is the `assert` keyword?

Used for debugging. Raises `AssertionError` if condition is false.

```python
assert 2 + 2 == 4  # OK
assert 2 + 2 == 5  # Raises AssertionError
```

---

### Q7. What are the file modes in Python?

| Mode | Description         |
| ---- | ------------------- |
| 'r'  | Read (default)      |
| 'w'  | Write (overwrite)   |
| 'a'  | Append              |
| 'b'  | Binary mode         |
| 'x'  | Exclusive creation  |
| 't'  | Text mode (default) |
| 'r+' | Read and write      |
| 'w+' | Write and read      |
| 'a+' | Append and read     |

---

### Q8. What is the `with` statement used for in exception handling?

Manages resources automatically, e.g.:

```python
with open("file.txt", "r") as f:
    content = f.read()
```

---

### Q9. Difference between `flush()` and `close()`?

* `flush()`: Writes buffer to file.
* `close()`: Flushes and closes file.

---

### Q10. Common exceptions in Python:

* `ZeroDivisionError`
* `ValueError`
* `IndexError`
* `FileNotFoundError`
* `TypeError`
* `KeyError`

---

### Q11. `read()` vs `readlines()`:

| Feature      | `read()`     | `readlines()`   |
| ------------ | ------------ | --------------- |
| Returns      | String       | List of strings |
| File Pointer | End          | End             |
| Use Case     | Full content | Line-by-line    |

---

### Q12. Binary vs Text Files:

* Text: Human-readable, encoded (e.g. UTF-8).
* Binary: Non-readable, raw data.

---

### Q13. Syntax Errors vs Exceptions:

* Syntax Errors: Detected before execution.
* Exceptions: Runtime errors.

---

### Q14. How to create a custom exception?

```python
class MyException(Exception):
    pass
```

---

### Q15. How to handle file-related exceptions?

```python
try:
    with open("nonexistent.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Other error: {e}")
```

---

### Q16. What is a generic `except` block?

Catches all exceptions. Use with caution:

```python
try:
    ...
except:
    print("Something went wrong")
```

---

### Q17. How to write to a file?

```python
with open("file.txt", "w") as f:
    f.write("Hello")
```

---

### Q18. Ensure a file is properly closed?

Use `with` statement:

```python
with open("example.txt", "r") as file:
    content = file.read()
```

---

### Q19. What is `seek()` used for?

Moves file pointer to a specific position.

---

### Q20. How to write multiple lines?

```python
lines = ["Line 1\n", "Line 2\n"]
with open("file.txt", "w") as f:
    f.writelines(lines)
```

---

### Q21. Role of `else` in exception handling:

Runs only if no exception occurs in `try`.

---

### Q22. How to log exceptions?

Use the `logging` module:

```python
import logging
logging.exception("Exception occurred")
```

---

### Q23. Purpose of `sys.exc_info()`?

Returns info about the current exception.

---

### Q24. Handling exceptions in specific order:

Always place more specific exceptions before general ones.

---

### Q25. Custom error messages when raising exceptions:

```python
raise ValueError("This is a custom error message")
```

---