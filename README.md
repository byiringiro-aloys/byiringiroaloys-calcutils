# calcutils-byiringiroaloys

A simple Python math utility package providing basic arithmetic and statistical helper functions.

**Version:** 0.1.0  
**Author:** Aloys Byiringiro  
**License:** MIT

---

## Installation

Install from TestPyPI using pip:

```bash
pip install -i https://test.pypi.org/simple/ calcutils-byiringiroaloys
```

![Package on TestPyPI](resources/package_preview:site.png)

![Installation](resources/package_installation.png)

---

## Usage

> **Note:** The install name (`calcutils-byiringiroaloys`) and the import name (`calcutils`) are different.

### Import the package

```python
import calcutils
```

Or import specific functions directly:

```python
from calcutils import add, subtract, multiply, divide, average
```

Or import from the module itself:

```python
from calcutils.operations import add, divide
```

---

## Functions

### `add(num1, num2)`
Returns the sum of two numbers.

```python
from calcutils import add

result = add(5, 3)
print(result)  # 8
```

---

### `subtract(big_num1, small_num2)`
Returns the difference between two numbers.

```python
from calcutils import subtract

result = subtract(10, 4)
print(result)  # 6
```

---

### `multiply(num1, num2)`
Returns the product of two numbers.

```python
from calcutils import multiply

result = multiply(3, 7)
print(result)  # 21
```

---

### `divide(num1, num2)`
Returns the result of dividing `num1` by `num2`.  
Returns an error string if `num2` is zero — it does **not** raise an exception.

```python
from calcutils import divide

print(divide(10, 2))   # 5.0
print(divide(5, 0))    # Error: Can not divide by Zero.
```

---

### `average(numbers)`
Returns the arithmetic mean of a list of numbers. Returns `0.0` for an empty list.

```python
from calcutils import average

result = average([1, 2, 3, 4, 5])
print(result)  # 3.0

print(average([]))  # 0.0
```

---

## Example

```python
from calcutils import add, subtract, multiply, divide, average

print("Addition:", add(5, 3))           # 8
print("Subtraction:", subtract(10, 4))  # 6
print("Multiplication:", multiply(3, 7))# 21
print("Division:", divide(10, 2))       # 5.0
print("Division by zero:", divide(5, 0))# Error: Can not divide by Zero.
print("Average:", average([1, 2, 3]))   # 2.0
```

![Package execution](resources/package_execution.png)

---

## Notes

- All arithmetic functions (`add`, `subtract`, `multiply`, `divide`) accept two numbers (int or float).
- `divide` handles zero division gracefully by returning an error string rather than raising an exception.
- `average` accepts a list of numbers of any length.

---

## Links

- [TestPyPI](https://test.pypi.org/project/calcutils-byiringiroaloys/)
- [GitHub](https://github.com/byiringiro-aloys/byiringiroaloys-calcutils)
