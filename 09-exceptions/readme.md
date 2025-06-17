## 🗂 Topics Covered
- Errors
- Exception

---

## 🧠 Notes

---

### ⚠️ Errors

#### ➤ Syntax Error
- Occurs when the Python code violates the language's grammar rules.
- Prevents the code from being parsed correctly.

#### ➤ Runtime Error
- Happens during the execution of the program.
- Unlike syntax errors, runtime errors occur after the code has been successfully parsed.

#### ➤ Logical Error
- Occurs when the program runs without crashing but produces incorrect results.
- These errors are often harder to detect because the code doesn't throw an exception.

#### ➤ Common Runtime Errors
- **NameError**: When the code tries to use a variable or function name that hasn't been defined.
- **TypeError**: When an operation or function is applied to an object of inappropriate type.
- **IndexError**: When you try to access an index that is out of range for a list or other indexed collection.
- **KeyError**: When a dictionary key is not found in the set of existing keys.
- **AttributeError**: When you try to access an attribute or method that doesn't exist for a particular object.
- **IndentationError**: When the code is not properly indented.
- **ImportError**: When Python cannot find the module you are trying to import.
- **ValueError**: When you try to perform an operation on a value that has the correct type but an inappropriate value.

---

### 🚧 Exceptions

- Exception handling is a mechanism that allows you to manage errors that occur during the execution of a program.
- Instead of the program crashing when an error occurs, exception handling enables you to handle the error gracefully and continue running the program.
- An exception is an event that disrupts the normal flow of a program's instructions.
- When an error occurs, Python raises an exception, which can be caught and handled using exception handling techniques.

#### 🔹 Core Components of Exception Handling
- **`try` block**: Tests a block of code for errors.
- **`except` block**: Handles the error. If an error occurs in the try block, this block is executed.
- **`else` block** *(optional)*: Runs if no exceptions are raised in the try block.
- **`finally` block**: Contains code that will run no matter what, whether an exception occurs or not. Commonly used for cleanup (e.g., closing files).

#### 💡 Best Practices
- **Be specific**: Catch specific exceptions rather than using a general exception to avoid hiding bugs.
- **Use `finally` for cleanup**: Always release resources properly.
- **Avoid empty `except` blocks**: Handle exceptions appropriately instead of leaving them empty.
- **Log exceptions**: Helps in debugging and maintaining your code.

