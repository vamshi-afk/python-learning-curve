## 📘 Topics Learned

- `print()`
- `input()`

---

## 🧠 Notes

### 🔹 print()

- **`sep=''`**: Specifies the separator between multiple objects in the `print()` function.  
  - Default is a space `' '`.  
  - Example: `print('a', 'b', 'c', sep='-')` outputs: `a-b-c`.
- **`end=''`**: Specifies what to print at the end of the output.  
  - Default is a newline character `'\n'`.  
  - Example: `print('Hello', end='!')` outputs: `Hello!` without moving to a new line.

### 🔹 input()

- The `input()` function **always returns a string**.
- Use `int()` (or other type casts) to convert the input to the required data type.  
  - Example: `age = int(input("Enter your age: "))`
