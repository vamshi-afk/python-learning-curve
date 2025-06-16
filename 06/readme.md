# 📘 Topics Covered

In-depth understanding and solved problems on the following topics:

- String
- List
- Tuple

---

# 🧵 String

- **`ord()`**: Returns the integer representing the Unicode of the given character.
- **`chr()`**: Returns the character corresponding to a given integer.
- **Escape Sequences**:
  - Used to include special characters.
  - Represented using a backslash (`\`) before the special character.
- **Raw Strings**:
  - Special type of string that does not process escape sequences.
  - Useful when dealing with file paths or strings with many backslashes.
  - Defined using `r` or `R` before the string, e.g., `r"path\to\file"`.
- **Formatted Strings**:
  - Allow variables to be inserted efficiently using `f""` syntax.
  - Example: `f"Hello, {name}!"`
- **`in` Operator**:
  - Checks if a substring exists within another string.
  - Returns `True` if found, otherwise `False`.
- **Immutability**:
  - Strings are immutable in Python.
  - Concatenation creates a new string object each time.
- **Capitalization**:
  - `capitalize()`: Capitalizes only the **first letter** of the string.
  - `title()`: Capitalizes the **first letter of each word** in a string.

---

# 📋 List

- To add multiple elements, use loops.
- Tuples (which are immutable) can be added to lists using `append()`.
- Unlike sets, lists **can contain other lists** as elements.

### 🔨 List Methods

- **`del`**:
  - A keyword used to delete variables or items from a list **by index**.
  - Example: `del my_list[2]`

- **`remove()`**:
  - Removes the **first occurrence** of a specified value from the list.
  - Example: `my_list.remove("apple")`

- **`pop()`**:
  - Removes and returns an item **at a specified index**.
  - If no index is specified, it removes and returns the **last item**.
  - Example: `my_list.pop()` or `my_list.pop(1)`

---

# 🔗 Tuple

*(Notes for Tuple section not provided, can be added later if needed.)*
