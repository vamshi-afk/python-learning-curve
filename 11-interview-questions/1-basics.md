## Python Basics - Data Types and Operators (Interview Questions)

### Q1. What is Python, and what are some of its key features?

Python is a high-level, interpreted programming language known for its readability and versatility.

**Key Features:**

* **Readable Syntax:** Clean and easy to understand.
* **Interpreted:** Executes code line-by-line.
* **Dynamic Typing:** No need to declare variable types explicitly.
* **Rich Libraries:** Includes packages like NumPy, Pandas, Django.
* **Cross-Platform:** Works across major OS platforms.

---

### Q2. Difference between Python 2 and Python 3?

* **Print Statement:**

  * Python 3: `print("Hello")`
  * Python 2: `print "Hello"`
* **Division:**

  * Python 3: `5 / 2` → `2.5`
  * Python 2: `5 / 2` → `2`
* **String Handling:** Python 3 uses Unicode by default.
* **Status:** Python 2 is deprecated since 2020.

---

### Q3. How is memory managed in Python?

* **Heap Allocation:** Memory is allocated from a private heap.
* **Reference Counting:** Tracks object usage.
* **Garbage Collector:** Automatically frees unused memory.

```python
a = [1, 2, 3]
b = a
# Reference count increases

del a  # One reference removed
```

---

### Q4. What is PEP 8 and why is it important?

PEP 8 is the official Python style guide promoting readable and consistent code.

```python
def add(a, b):
    return a + b
```

---

### Q5. What are Python's data types?

* **Numbers:** `int`, `float`, `complex`
* **Sequences:** `str`, `list`, `tuple`
* **Mappings:** `dict`
* **Sets:** `set`, `frozenset`
* **Boolean:** `bool`
* **Binary:** `bytes`, `bytearray`, `memoryview`
* **None:** `NoneType`

---

### Q6. Difference between list and tuple?

| Feature     | List            | Tuple                          |
| ----------- | --------------- | ------------------------------ |
| Mutable     | Yes             | No                             |
| Syntax      | `[1, 2, 3]`     | `(1, 2, 3)`                    |
| Performance | Slower          | Faster                         |
| Use Case    | Changeable data | Fixed data                     |
| Methods     | Many            | Few                            |
| Hashable    | No              | Yes (if elements are hashable) |

---

### Q7. Difference between strings and lists?

* **Strings:** Immutable and store characters.
* **Lists:** Mutable and can store various data types.

---

### Q8. What is the Walrus Operator?

Allows assignment within expressions.

```python
if (name := input("Enter name: ")):
    print(name)
```

*Introduced in Python 3.8*

---

### Q9. Interpreter vs Compiler in Python?

* **Interpreter:** Executes code line-by-line.
* **Compiler:** Converts whole code into machine code before execution.

---

### Q10. Shallow vs Deep Copy?

| Feature        | Shallow Copy   | Deep Copy    |
| -------------- | -------------- | ------------ |
| Reference      | Shared         | Independent  |
| Nested Objects | Not duplicated | Fully copied |

```python
import copy
copy.copy(obj)  # Shallow
copy.deepcopy(obj)  # Deep
```

---

### Q11. Mutable vs Immutable Types?

| Type       | Mutable        | Immutable             |
| ---------- | -------------- | --------------------- |
| Examples   | `list`, `dict` | `int`, `str`, `tuple` |
| Changeable | Yes            | No                    |

---

### Q12. Common Data Structures in Python

* **List:** Ordered, mutable.
* **Tuple:** Ordered, immutable.
* **Set:** Unordered, unique.
* **Dict:** Key-value pairs.

---

### Q13. Duplicate of Q11.

---

### Q14. Difference between `is` and `==`

* **`==`**: Compares values.
* **`is`**: Compares identities.

```python
a = [1, 2]
b = [1, 2]
print(a == b)  # True
print(a is b)  # False
```

---

### Q15. Type Conversion in Python

* **Implicit:** Automatically done.
* **Explicit:** Done using functions like `int()`, `float()`.

---

### Q16. Numeric Types

* `int`, `float`, `complex`

---

### Q17. Dictionary vs List

| Feature   | Dictionary      | List             |
| --------- | --------------- | ---------------- |
| Access    | Via key         | Via index        |
| Structure | Key-value pairs | Ordered elements |

---

### Q18. Difference between `/` and `//`

* `/` performs float division
* `//` performs floor division

---

### Q19. Operator Precedence Example

```python
result = 2 + 3 * 4  # 14
```

Precedence: `()`, `**`, `* / // %`, `+ -`, comparisons

---

### Q20. Logical vs Bitwise Operators

| Type    | Examples    |         |
| ------- | ----------- | ------- |
| Logical | `and`, `or` |         |
| Bitwise | `&`, \`     | `, `^\` |

---

### Q21. Difference between `+` and `+=`

* `+`: Creates a new object.
* `+=`: Modifies object in-place if mutable.

---

### Q22. Is Indentation Required?

Yes. It is syntactically significant.

---

### Q23. Common Escape Sequences

* `\n`: New line
* `\t`: Tab
* `\"`, `\'`: Quotes

---

### Q24. Difference: `None`, `False`, `0`

* `None == 0` → False
* `False == 0` → True

---

### Q25. Bytes vs Bytearray

| Feature | Bytes | Bytearray |
| ------- | ----- | --------- |
| Mutable | No    | Yes       |

```python
b = b"hello"
ba = bytearray(b)
ba[0] = 72
```
