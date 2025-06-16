## 📘 Topics Covered

- OOP (Object-Oriented Programming)

---

## 🧠 Notes

### 🧱 Core OOP Concepts

#### ✅ Class and Objects

- A class serves as a blueprint for creating objects, which are individual instances of that class.

#### ✅ Constructor (`__init__`)

- A special method used to initialize objects when they are created.
- In Python, the `__init__` method serves as the constructor.
- It sets up the initial state of an object by assigning values to its data members.

#### ✅ `self` Keyword

- `self` is a special reference used within class methods to refer to the current instance of the class.

#### ✅ Attribute Resolution

- If both class and object have an attribute with the same name, the object attribute takes priority for that instance.

---

### 🔐 Encapsulation

- **Protected Members**:
  - Prefix with a single underscore `_var`
  - Indicates intended internal use (not enforced by Python)

- **Private Members**:
  - Prefix with double underscores `__var`
  - Restricts access via name mangling

- **Encapsulation**:
  - Restricting access to data members.
  - Ensures only necessary parts are exposed publicly.

---

### 🎭 Abstraction

- Hiding complex implementation details, exposing only necessary functionality.

#### Abstract Classes:

- Allow defining methods that must be created within any child class.
- Cannot be instantiated directly.
- Can have both abstract and concrete methods.
- Concrete subclasses must implement all abstract methods.
- If not, the subclass also becomes abstract.

---

### 🔧 Decorators

- A decorator is a function that takes another function as an argument and enhances its behavior.
- Declared using: `@decoratorFunctionName`

---

### 🧩 Attributes and Methods

#### ✅ Class Attributes

- Shared by all instances of a class.
- Defined within the class but **outside** any instance methods.

#### ✅ Instance Attributes

- Unique to each instance.
- Usually defined within the `__init__` method.

---

### 🏷️ Class vs Static Methods

#### ✅ Class Methods

- Bound to the class, not the instance.
- Use `@classmethod` decorator.
- First parameter is `cls` (refers to the class).
- Can modify or access class attributes.

#### ✅ Static Methods

- Do not access or modify class or instance attributes.
- Use `@staticmethod` decorator.
- Utility functions related to the class.

---

### 🧬 Inheritance

- Allows one class to inherit attributes and methods from another.
- Promotes code reusability.

#### 📚 Types of Inheritance:

1. **Single Inheritance**  
   One base class → One derived class.

2. **Multilevel Inheritance**  
   A derived class is a base class for another class.

3. **Multiple Inheritance**  
   A class inherits from more than one base class.

4. **Hierarchical Inheritance**  
   Multiple classes inherit from one base class.

5. **Hybrid Inheritance**  
   Combination of two or more types.

---

### 🔁 Method Overriding

- A subclass redefines a method of its superclass.
- The method must have the same name and parameters.
- Python uses **Method Resolution Order (MRO)** to determine which method to execute.

#### `super()` Function

- Accesses methods and properties of the superclass.
- Used to extend or modify superclass behavior from a subclass.

---

### 🔄 Polymorphism

#### ✅ Static Polymorphism

- **Compile-time polymorphism** (common in C++/Java).
- Achieved using **function overloading** (not directly supported in Python).

#### ✅ Dynamic Polymorphism

- **Runtime polymorphism** — supported naturally in Python.
- A single function can accept different types of input.

#### ✅ Operator Overloading

- A form of polymorphism.
- Enables the same operator to behave differently depending on the context or operand types.
