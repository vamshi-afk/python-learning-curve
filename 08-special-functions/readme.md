## 🗂 Topics Covered
- Special functions in Python
- ASCII code

---

## 🧠 Notes

### 🔸 Special Functions in Python

#### ➤ `zip()`
- Takes multiple iterable objects and aggregates them into a single iterator of tuples, pairing elements by position.
- Stops at the shortest iterable if their lengths differ.

#### ➤ `filter()`
- Constructs an iterator from elements of an iterable for which a specified function returns `True`.
- Used to selectively process items based on a condition.
- **Syntax:** `filter(function, iterable)`

#### ➤ `lambda`
- A small anonymous function defined using the `lambda` keyword.
- Can have any number of arguments but only one expression.
- Commonly used for short, throwaway functions.
- **Syntax:** `lambda arguments: expression`

#### ➤ `map()`
- Applies a specified function to each item of an iterable.
- Returns a `map` object (iterator) that can be converted into a list or used in a loop.
- **Syntax:** `map(function, iterable)`

---

### 🔸 ASCII Code

#### ➤ `ord()`
- Returns the ASCII (or Unicode) code of a character.  
  Example: `ord('A') → 65`

#### ➤ `chr()`
- Converts an ASCII code to its corresponding character.  
  Example: `chr(65) → 'A'`
