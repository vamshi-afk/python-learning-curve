## Strings and Lists – Python Interview Questions

### Q1. What does the `swapcase()` method do?

It creates a new string with uppercase letters converted to lowercase and vice versa.

```python
text = "PythonRocks"
print(text.swapcase())  # Output: "pYTHONrOCKS"
```

---

### Q2. How are strings stored in memory compared to lists?

* **Strings**: Stored in a contiguous block of memory. Python may optimize using *string interning*.
* **Lists**: Dynamic arrays that store references to objects, not the objects themselves.

---

### Q3. What is the purpose of negative indexing?

Negative indices access elements starting from the end of the sequence.

| Example         | Result |
| --------------- | ------ |
| `"abc"[-1]`     | `'c'`  |
| `[1, 2, 3][-2]` | `2`    |

---

### Q4. What’s the difference between lists and tuples?

| Property    | List            | Tuple                          |
| ----------- | --------------- | ------------------------------ |
| Mutability  | Mutable         | Immutable                      |
| Syntax      | `[1, 2]`        | `(1, 2)`                       |
| Use Case    | Changing data   | Fixed/grouped data             |
| Performance | Slightly slower | Slightly faster                |
| Hashable    | No              | Yes (if elements are hashable) |

---

### Q5. How do `count()` and `index()` differ?

* `count()` returns how many times an item occurs.
* `index()` returns the position of the first occurrence.

```python
"banana".count('a')  # 3
[1, 2, 1].index(1)   # 0
```

---

### Q6. Difference between `remove()` and `pop()` in lists?

| Method     | Works On      | Returns | Raises Error If   |
| ---------- | ------------- | ------- | ----------------- |
| `remove()` | Element value | None    | Element not found |
| `pop()`    | Index         | Element | Index is invalid  |

---

### Q7. How to find the intersection of two lists without using sets?

```python
def intersect(a, b):
    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1
    result = []
    for x in b:
        if freq.get(x, 0) > 0:
            result.append(x)
            freq[x] -= 1
    return result
```

---

### Q8. How does slicing work on strings?

Slicing uses the format: `string[start:end:step]`

* `start`: where to begin (inclusive)
* `end`: where to stop (exclusive)
* `step`: how many indices to skip

---

### Q9. What are some common string operations?

* **Concatenation**: `'a' + 'b'`, `"".join([...])`
* **Search**: `'sub' in s`, `s.find('x')`
* **Case Changes**: `upper()`, `lower()`, `capitalize()`
* **Trimming**: `strip()`, `rstrip()`, `lstrip()`

---

### Q10. What is a list comprehension?

A short syntax for creating lists.

```python
evens = [x for x in range(10) if x % 2 == 0]
```

---

### Q11. Difference between `sort()` and `sorted()`?

| Feature        | `sort()` (method) | `sorted()` (function) |
| -------------- | ----------------- | --------------------- |
| Modifies List? | Yes (in-place)    | No (returns new list) |
| Input Type     | List only         | Any iterable          |

---

### Q12. Difference between `split()` and `rsplit()`?

* `split()` starts splitting from the left.
* `rsplit()` starts splitting from the right.

Both default to splitting on whitespace.

---

### Q13. Common list methods?

* `append()`, `extend()`, `insert()`
* `remove()`, `pop()`, `clear()`
* `sort()`, `reverse()`, `index()`

---

### Q14. What is string interning?

Python reuses memory for identical immutable strings to save space and speed up comparisons.

---

### Q15. How to flatten a nested list in one line?

```python
flat = [item for sub in nested_list for item in sub]
```

---

### Q16. Why are strings immutable?

Modifying a string creates a new object. Benefits:

* Thread-safe
* Hashable (usable as dict keys)
* Interning optimizations

---

### Q17. How does Python optimize string memory?

Through interning and pooling of identical strings to reduce duplicate allocations.

---

### Q18. `+` vs `.join()` for concatenating strings?

* `+` is okay for small operations but inefficient in loops.
* `.join()` is faster for merging many strings.

---

### Q19. Can different strings have the same hash?

Yes, but it's rare. Hash collisions are possible but uncommon.

---

### Q20. Why can strings be dictionary keys?

Because they are immutable and hashable. Lists can't be used as keys since they’re mutable.

---

### Q21. How are strings compared in Python?

Strings are compared lexicographically using Unicode values.

```python
"abc" < "xyz"  # True
```

---

### Q22. What is pickling?

* **Pickling**: Convert Python object to byte stream.
* **Unpickling**: Restore object from byte stream.

Used for saving or transmitting Python data.

---

### Q23. What is the time complexity of `append()` in lists?

* Amortized O(1)
* Occasionally O(n) if the list resizes

---

### Q24. Why do lists store references?

To efficiently manage memory and allow storing different data types without duplication.

---

### Q25. Compare strings and lists in Python.

| Feature       | Strings              | Lists                     |
| ------------- | -------------------- | ------------------------- |
| Mutability    | Immutable            | Mutable                   |
| Data Type     | Characters only      | Mixed types               |
| Syntax        | `"text"`             | `[1, 2, 3]`               |
| Modification  | Not allowed          | Supported                 |
| Hashable      | Yes                  | No                        |
| Common Use    | Text                 | Collections of elements   |
| Concatenation | `+`, `join()`        | `+`, `extend()`           |
| Methods       | `split()`, `upper()` | `append()`, `pop()`, etc. |

---