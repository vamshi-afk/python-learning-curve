## Python - Loops and Flow Control (Interview Questions)

### Q1. What is an infinite loop, and how can it occur in Python?

An infinite loop continues executing because its termination condition never becomes False.

```python
while True:
    print("Infinite Loop")
```

Prevent infinite loops by ensuring the condition eventually evaluates to False or use a `break` statement.

---

### Q2. Explain the difference between for and while loops in Python.

| Feature     | for Loop                      | while Loop                   |
| ----------- | ----------------------------- | ---------------------------- |
| Purpose     | Iterates over a sequence      | Runs based on a condition    |
| Termination | Ends after sequence completes | Ends when condition is False |
| Use Case    | Known iteration count         | Uncertain iteration count    |

---

### Q3. How does Python’s range() function work in a for loop?

`range()` generates a sequence of numbers:

* `range(stop)`
* `range(start, stop)`
* `range(start, stop, step)`

```python
for i in range(1, 10, 2):
    print(i)  # Outputs: 1, 3, 5, 7, 9
```

---

### Q4. What is the difference between xrange and range functions?

* In Python 3: Only `range()` exists and acts like `xrange()` from Python 2 (lazy evaluation).
* In Python 2:

  * `range()` returns a list.
  * `xrange()` returns a generator.

---

### Q5. What is the purpose of the break statement?

Terminates the loop immediately.

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

### Q6. Differentiate between break and continue statements in Python.

| Feature | break               | continue                |
| ------- | ------------------- | ----------------------- |
| Purpose | Exits loop entirely | Skips current iteration |
| Effect  | Ends loop           | Moves to next iteration |

---

### Q7. Can a for loop in Python iterate over non-sequential data types?

Yes. It works with any iterable like strings, sets, and dictionaries.

```python
d = {'a': 1, 'b': 2}
for key in d:
    print(key)
```

---

### Q8. What are the common errors in loops?

* Infinite loops
* Modifying the iterable during iteration
* Off-by-one errors
* Misplaced indentation

---

### Q9. What is a nested loop, and when is it used?

A loop inside another loop, typically used for 2D structures.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

### Q10. Write a program to print a multiplication table using loops.

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()
```

---

### Q11. How do you iterate through a dictionary’s keys and values?

```python
my_dict = {'a': 1, 'b': 2}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
```

---

### Q12. What is the difference between iter() and next() in Python?

| Function | Description                       |
| -------- | --------------------------------- |
| `iter()` | Converts object to an iterator    |
| `next()` | Retrieves next item from iterator |

---

### Q13. How do you iterate over multiple sequences in parallel?

Use `zip()`:

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for x, y in zip(list1, list2):
    print(x, y)
```

---

### Q14. What are the different types of for loops in Python?

* Sequence iteration
* Range-based iteration
* Using `enumerate()` for index tracking

```python
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)
```

---

### Q15. What is the purpose of the else clause in a loop in Python?

The `else` block runs only if the loop wasn't exited by a `break`.

```python
for i in range(5):
    if i == 3:
        break
else:
    print("Loop completed without break")
```

---

### Q16. What is short-circuiting in Python?

Short-circuiting skips evaluation if result is known from the first operand.

* `and`: Stops if first is False.
* `or`: Stops if first is True.

```python
x = 0
if x != 0 and (10 / x) > 1:
    print("Safe")
```

---

### Q17. Difference between `is` and `==` in Python?

| Operator | Compares        |
| -------- | --------------- |
| `==`     | Values          |
| `is`     | Object identity |

```python
a = [1, 2]
b = [1, 2]
print(a == b)  # True
print(a is b)  # False
```

---

### Q18. How to find the first occurrence of a value in a list using a loop?

```python
lst = [1, 2, 3, 4, 5]
for i, val in enumerate(lst):
    if val == 3:
        print(f"Found 3 at index {i}")
        break
```

---

### Q19. Common errors when iterating a list:

* `IndexError`: Accessing invalid indices
* `ValueError`: Performing invalid operations on values

---

### Q20. Write a program to print a pyramid pattern of stars.

```python
def print_pyramid(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "*" * (2*i-1))

print_pyramid(5)
```

---

### Q21. Benefits of `for` loops over `while` loops:

* Ideal for known iteration counts
* Cleaner syntax with sequences

---

### Q22. How does Python support conditional (ternary) expressions?

```python
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)
```

---

### Q23. Difference between for and while loop conditions:

* `for`: Automatically iterates over a collection
* `while`: Manually checks a condition each time

---

### Q24. Pitfalls of using `break` and how to avoid them:

* May cause unintended exits from loop
* Prefer clear logic, avoid nested breaks when possible

---

### Q25. Performance concerns with nested loops:

* Can result in high time complexity (O(n^2) or worse)

**Optimizations:**

* Reduce operations in inner loop
* Use sets/dicts for faster lookups
* Apply efficient algorithms

---
