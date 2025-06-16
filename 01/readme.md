# 📘 Topics Learned

- Introduction to Python
- Data Types in Python
- `id()` in Python
- Lists, Tuples, Sets, Dictionaries
- Type Conversion
- `map()`, `split()`
- `.format()`

---

# 🧠 Notes

## 🔹 split()

- Splits a string into a list of substrings based on a delimiter.
- Example:
  
  ```
  "a,b,c".split(",")  # ['a', 'b', 'c']

## 🔹 Reversing Lists and Tuples

* Use slicing with `[::-1]` to reverse.
* Example:

  ```
  my_list[::-1]
  my_tuple[::-1]
  ```

## 🔹 Set Operations

* `add()`: Adds a single item to the set.
* `update()`: Adds multiple items to the set.
* `discard()`: Removes an item if it exists; does nothing if it doesn’t.
* `remove()`: Removes an item; raises an error if the item doesn’t exist.
* Symmetric Difference (`a ^ b`): Returns elements present in either set but not both.
* `isdisjoint()`: Returns `True` if two sets have **no elements in common**.
* Subset (`<=`): Checks if all elements of the first set are in the second.
* Proper Subset (`<`): Like subset but excludes equality.
* Superset (`>=`): Checks if the first set contains all elements of the second.
* Proper Superset (`>`): Like superset but excludes equality.
* `sorted()`: Returns a sorted list of set elements without brackets (unlike printing a set).

## 🔹 Dictionary Operations

* To safely `pop` or `get` with a fallback, use:

  ```
  dict.pop(key, fallback_operation)
  ```
* Example:

  ```
  d = {'a': 1}
  d.pop('b', None)  # Returns None instead of raising an error
  ```

## 🔹 Empty Collections

* Empty set: `s = set()`
* Empty dictionary: `d = {}`
