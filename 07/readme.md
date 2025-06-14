# Topics covered

- OOP (Object-Oriented Programming)

# Things I might forget

- A class serves as a blueprint for creating objects, which are individual instances of that class.
- A constructor is a special method used to initialize objects when they are created. In Python, the **init** method serves as the constructor. It sets up the initial state of an object by assigning values to its data members.
- self is a special reference used within class methods to refer to the current instance of the class.
- If both class and object have an attribute with the same name, the object attribute takes priority for that instance.
- **Protected Members**: Prefixing a variable name with a single underscore. This indicates that the member is intended for internal use within the class or its subclasses, but Python does not enforce this restriction.
- **Private Members**: Double underscores before a member name to make it private. This restricts access to the member from outside the class by performing name mangling.
- **Encapsulation**: Restricting access to the data members, ensuring that only necessary parts are exposed publicly.

- **Abstraction**: Hiding complex implementation details and only exposing the necessary functionality.
    - Abstract classes allow you to define methods that must be created within any child classes built from the abstract class.
    - Abstract classes cannot be instantiated.
    - Concrete subclasses must implement all abstract methods.
    - Abstract classes can have both abstract and concrete methods.
    - If a class does not implement all abstract methods, it becomes abstract.
- **Decorator**: A decorator is a function that takes another function as an argument and enhances the behavior of the passed function. You can Declare a Decorator using @decoratorFuntionName
- **Class Attributes** are shared by all instances of a class. They are defined within the class but outside any instance methods.
- **Instance Attributes** are unique to each instance of a class. They are usually defined within the **init** method.
- **Class methods** are methods that are bound to the class and not the instance of the class. They are used to modify or access class attributes. To create a class method, we use the @classmethod decorator.
- The first parameter of a class method is cls, which refers to the class itself. This allows the method to access and modify class attributes.
- **Static methods** are methods that belong to a class but do not access or modify the class or instance attributes. They are used to create utility functions that perform tasks related to the class but do not require access to class or instance data. Static methods are created using the @staticmethod decorator.

- **Inheritance**:
    - Allows one class to inherit attributes and methods from another class. This promotes code reusability and establishes a relationship between classes.

    **Types of Inheritance**:
    1. **Single Inheritance**: Single inheritance involves one base class and one derived class. The subclass inherits attributes and methods from the superclass.
    2. **Multilevel Inheritance**: Multilevel inheritance occurs when a class is derived from another derived class, forming a multi-level hierarchy. This means there is a chain of inheritance where a subclass becomes a superclass for another subclass.
    3. **Multi Inheritance**: To inherit from more than one base class. This means the derived class can have multiple superclass.
    4. **Hierarchical Inheritance**: Multiple derived classes inheriting from a single base class. This creates a hierarchy where several subclasses share the same superclass.
    5. **Hybrid Inheritance**: Combination of two or more types of inheritance.

- **Method Overriding**: Occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The method in the subclass has the same name and parameters as the one in the superclass. 
- Python follows the **Method Resolution Order (MRO)** to determine which method to execute when there are multiple methods with the same name in the inheritance hierarchy.
- The **super()** function is used to give access to methods and properties of a superclass from within a subclass. It allows the subclass to extend or modify the behavior of the superclass method.