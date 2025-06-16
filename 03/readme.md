# 📘 Topics I Learned

- Operators
- Control Flow Statements

---

# 🧠 Notes

## Operator

### 🔹 Short-Circuiting in Python

- Python stops evaluating an expression as soon as the overall result is determined.
  - For example, in a logical `and`, if the first operand is `False`, the second is **not evaluated**.
- Short-circuiting improves efficiency by avoiding unnecessary evaluations.
- It also helps prevent errors, especially when the second expression depends on the first.

### 🔹 Other Notes on Operators

- An **empty string** is treated as `False` in a boolean context.
- **Identity Operators** compare the memory locations of two objects.
- Even if two lists have the **same content**, they occupy **different memory locations**.
- **Left Shift (`<<`)**:
  - Multiplies a number by \(2^x\), where \(x\) is the number of shifts.
  - Shifts bits to the left.
- **Right Shift (`>>`)**:
  - Divides a number by \(2^x\), where \(x\) is the number of shifts.
  - Shifts bits to the right.
- **1's Complement**:
  - Inverts all bits.
- **2's Complement**:
  - Obtained by adding 1 to the Least Significant Bit (LSB) after taking 1's complement.
