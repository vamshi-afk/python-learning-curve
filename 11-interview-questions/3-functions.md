## Functions and Special Functions – Python Interview Questions

### Q1. What is the purpose of functions in Python, and how do they support modularity?

Functions break a program into smaller reusable units. This encourages cleaner code, easier testing, and improved readability.

---

### Q2. How can a Python function return multiple values?

A function can return multiple values using a tuple or any iterable.

```python
def get_values():
    return 1, 2, 3

a, b, c = get_values()
```

---

### Q3. What are default parameters in Python?

Default parameters allow you to call a function without providing values for every argument.

```python
def greet(name, msg="Hello"):
    print(f"{msg}, {name}")
```

---

### Q4. How do keyword arguments work?

Keyword arguments let you specify arguments by name, not position.

```python
def display(name, role):
    print(f"{name} is a {role}")

display(role="Engineer", name="Sam")
```

---

### Q5. What are \*args and \*\*kwargs?

These allow variable numbers of arguments.

* `*args` collects positional arguments into a tuple.
* `**kwargs` collects keyword arguments into a dictionary.

```python
def demo(*args, **kwargs):
    print(args)
    print(kwargs)
```

---

### Q6. Is Python pass-by-reference or pass-by-value?

Python uses "pass-by-object-reference". Mutable objects can be modified, while immutable ones cannot.

---

### Q7. Difference between `map()` and `filter()`?

| Function   | Purpose                         | Output   |
| ---------- | ------------------------------- | -------- |
| `map()`    | Applies a function to each item | Iterator |
| `filter()` | Filters items using condition   | Iterator |

---

### Q8. How does Python handle ASCII?

* `ord('A')` → Converts character to ASCII (returns 65)
* `chr(65)` → Converts ASCII to character (returns 'A')

---

### Q9. What is a lambda function?

A compact anonymous function, often used for short operations.

```python
double = lambda x: x * 2
```

---

### Q10. What is the default return value of a function?

If not specified, a function returns `None`.

---

### Q11. Can functions return other functions?

Yes. Functions can return other functions, enabling dynamic behaviors and closures.

---

### Q12. What is recursion?

Recursion is a technique where a function calls itself. It’s useful for problems that can be broken down into smaller similar problems.

---

### Q13. What is scope in Python?

* **Local**: Within the function
* **Global**: Outside functions
* **Enclosed**: Between local and global
* **Built-in**: Python’s predefined names

---

### Q14. What is a docstring?

A docstring is a multi-line string used for documenting a function.

```python
def example():
    """This function does nothing."""
    pass

print(example.__doc__)
```

---

### Q15. Shallow vs Deep Copy?

* **Shallow Copy**: Duplicates only the outer object.
* **Deep Copy**: Duplicates both outer and nested objects.

---

### Q16. What are function annotations?

Metadata for parameters and return values.

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

### Q17. What is a higher-order function?

A function that takes or returns another function. Examples include `map`, `filter`, `reduce`.

---

### Q18. How does Python handle recursive function calls?

There’s a maximum recursion depth (default \~1000). Exceeding it causes a `RecursionError`.

---

### Q19. What is memoization?

Memoization caches the results of function calls to avoid repeated computation.

---

### Q20. What are decorators in Python?

Decorators are functions that modify the behavior of other functions.

```python
@decorator
def func():
    pass
```

---

### Q21. How can you debug Python code?

Use the `pdb` module:

```bash
python -m pdb your_script.py
```

---

### Q22. What does `zip()` do?

It combines multiple iterables into a single iterator of tuples.

```python
zip([1, 2], ['a', 'b'])  # → (1, 'a'), (2, 'b')
```

---

### Q23. What happens when `zip()` is used on iterables of different lengths?

It stops at the shortest iterable.

---

### Q24. Difference between `map()` and `filter()`?

* `map()` transforms data.
* `filter()` selects data based on a condition.

```python
map(lambda x: x**2, [1, 2])
filter(lambda x: x % 2 == 0, [1, 2, 3])
```

---

### Q25. Compare `zip()`, `map()`, and `filter()`.

| Function   | Use Case               |
| ---------- | ---------------------- |
| `zip()`    | Combine sequences      |
| `map()`    | Apply function to data |
| `filter()` | Select matching items  |

---
