## Python – Object-Oriented Programming (OOP) Interview Questions

### Q1. What does method overriding mean in Python?

When a subclass redefines a method from its parent class with the same name and parameters, it overrides the original behavior.

---

### Q2. How do instance methods, class methods, and static methods differ?

* **Instance methods**: Use `self`, work with individual objects.
* **Class methods**: Use `cls`, work at the class level.
* **Static methods**: Don’t access instance or class data; general utility methods.

---

### Q3. Is multiple inheritance supported in Python?

Yes, Python allows a class to inherit from multiple base classes.

---

### Q4. What is polymorphism in Python?

Polymorphism lets objects of different types respond to the same method in their own way.

---

### Q5. What is monkey patching?

It means changing or extending classes/modules at runtime without modifying the source code.

---

### Q6. What is the role of `__init__()`?

It's the constructor method called when a class is instantiated, used to initialize attributes.

---

### Q7. How is encapsulation done in Python?

By using naming conventions:

* `var`: public
* `_var`: protected (by convention)
* `__var`: private (via name mangling)

---

### Q8. What happens if a class method is called from an instance?

Python automatically passes the class (`cls`) as the first argument.

---

### Q9. What is the purpose of `__new__`?

`__new__` creates the object in memory; it's called before `__init__`.

---

### Q10. How do `@property` and `property()` differ?

* `@property`: Decorator syntax for getter.
* `property()`: Function for creating getters, setters, and deleters explicitly.

---

### Q11. Compare composition and inheritance.

* **Inheritance**: Defines a "is-a" relationship.
* **Composition**: Embeds one class inside another for a "has-a" relationship.

---

### Q12. What is the diamond problem and how does Python resolve it?

It’s an ambiguity in multiple inheritance. Python solves it using Method Resolution Order (MRO) with the C3 linearization algorithm.

---

### Q13. What’s the difference between `del obj` and `obj = None`?

* `del obj`: Removes the reference entirely.
* `obj = None`: Keeps the name but points to `None`.

---

### Q14. What is duck typing?

“If it walks like a duck and quacks like a duck…” Python checks for behavior, not explicit type.

---

### Q15. How is method resolution handled with multiple inheritance?

Python follows MRO (Method Resolution Order), which can be seen using `Class.__mro__` or `Class.mro()`.

---

### Q16. Difference between `__init__` and `__call__`?

* `__init__`: Initializes a new object.
* `__call__`: Lets an instance be invoked as a function.

---

### Q17. How can immutability be achieved in a Python class?

* Use `__slots__` to limit attributes
* Avoid defining setters
* Override `__setattr__` to prevent changes

---

### Q18. Compare `classmethod` and `staticmethod`.

* `classmethod(cls)`: Gets class reference.
* `staticmethod()`: Independent utility, no class or instance reference.

---

### Q19. Can a class inherit from both `object` and another class?

Yes, but in Python 3 it’s redundant—all classes inherit from `object` by default.

---

### Q20. Difference between class and instance variables?

* **Class variables**: Shared across all instances.
* **Instance variables**: Unique to each object.

---

### Q21. What is a metaclass?

A class that defines how other classes behave. It’s the "class of a class."

---

### Q22. What does OOP mean in Python?

Object-Oriented Programming is a model that focuses on:

* Encapsulation
* Abstraction
* Inheritance
* Polymorphism

---

### Q23. What is the difference between `self` and `cls`?

* `self`: Refers to the object instance.
* `cls`: Refers to the class itself.

---

### Q24. Can Python have multiple constructors?

Not directly. You can use default values or define class methods like `@classmethod` to simulate them.

---

### Q25. How does Python handle access to private and protected members?

* `_name`: Treated as protected (by convention).
* `__name`: Considered private via name mangling (e.g., `_ClassName__name`).

---