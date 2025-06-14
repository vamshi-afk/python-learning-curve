# Topics Learned 
- Introduction to python
- Data types in python
- id() in python
- lists, tuples, sets, dictionaries
- type conversion
- map(), split()
- .format()

# Things I might forget
- split(): splits the string to a list of substrings by a delimitter
- reverse a list | tuple = [::-1]
- set operations 
    - add() adds single item whereas update() adds multiple
    - discard() removes an item if exits otherwise does nothing, remove() raises an error if the item doesnt exits
    - Symmetric Difference(a^b): returns elements present in either sets but not both
    - isdisjoint(): Returns True if the two sets have no elements in common.
    - Subset (<=): Checks if all elements of the first set are in the second set.
    - Proper Subset (<): Similar to subset but does not allow both sets to be equal.
    - Superset (>=): Checks if the first set contains all elements of the second set.
    - Proper Superset (>): Similar to superset but does not allow both sets to be.
    - *sorted() prints the set without brackets unlike regular sorted()
- dictionary operations
    - if you want to pop/get with fallback like in dictionary_question.py
        use dict.pop(value, fallback_operation)
- empty set: s=set(), empty dict: dict={}    
