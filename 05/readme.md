# 📘 Topics Covered

- Functions

---

# 🧠 Notes

## 🔹 Default Arguments

- Default arguments are specified by assigning a value to a parameter in the function definition.
- Example:
   
  ```
  def greet(name="User"):
      print(f"Hello, {name}")
```

## 🔹 Keyword Arguments

* Arguments provided using the **parameter name**, allowing you to pass them in any order.
* Example:

  ```python
  def display(name, age):
      print(name, age)

  display(age=25, name="Alice")
  ```

## 🔹 Positional Arguments

* Arguments that must be provided **in the correct order** as defined in the function signature.
* Example:

  ```python
  def add(a, b):
      return a + b

  add(5, 10)  # Correct
  ```

## 🔹 Variable Length Arguments

Used when the number of arguments passed to a function is **not fixed**.

### ✅ Variable Length Positional Arguments (`*args`)

* Allows passing a varying number of **non-keyworded** arguments.
* Defined using `*parameter_name`.
* Example:

  ```python
  def total(*numbers):
      return sum(numbers)
  ```

### ✅ Variable Length Keyword Arguments (`**kwargs`)

* Allows passing a varying number of **keyworded** arguments.
* Defined using `**parameter_name`.
* Example:

  ```python
  def display_info(**info):
      for key, value in info.items():
          print(f"{key}: {value}")
  ```

## 🔹 Returning Multiple Values

* Python functions can return **multiple values** using tuples.
* Values can be assigned using **tuple unpacking**.
* Example:

  ```python
  def get_user():
      return "Alice", 30

  name, age = get_user()
  ```
