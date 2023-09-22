
# Vector Module

The Vector module provides classes to create and manipulate 2D and 3D vectors.

## Installation

To use the Vector module, you can simply include the `vector.py` file in your project directory or import it as a module.

```
python
from vector import Vector2D, Vector3D
```

## Usage

### 2D Vector

To create a 2D vector, initialize an instance of the `Vector2D` class by specifying the x and y coordinates.

```python
vector_2d = Vector2D(3, 4)
print(vector_2d)  # Output: (3, 4)
```

You can perform various operations on 2D vectors, such as adding, subtracting, scalar multiplication, calculating the dot product, and finding the distance between vectors.

```python
vector_1 = Vector2D(1, 2)
vector_2 = Vector2D(3, 4)

addition = Vector2D.add(vector_1, vector_2)
print(addition)  # Output: (4, 6)

subtraction = Vector2D.subtract(vector_1, vector_2)
print(subtraction)  # Output: (-2, -2)

scalar_product = vector_1.scalar_prod(2)
print(scalar_product)  # Output: (2, 4)

dot_product = Vector2D.dot_product(vector_1, vector_2)
print(dot_product)  # Output: 11

distance = Vector2D.distance(vector_1, vector_2)
print(distance)  # Output: 2.8284271247461903
```

### 3D Vector

The `Vector3D` class extends the functionality of `Vector2D` to include a z coordinate. You can create a 3D vector by providing the x, y, and z coordinates.

```python
vector_3d = Vector3D(1, 2, 3)
print(vector_3d)  # Output: (1, 2, 3)
```

Similar to 2D vectors, you can perform operations on 3D vectors, including addition, subtraction, scalar multiplication, dot product calculation, and distance calculation.

```python
vector_1 = Vector3D(1, 2, 3)
vector_2 = Vector3D(4, 5, 6)

addition = Vector3D.add(vector_1, vector_2)
print(addition)  # Output: (5, 7, 9)

subtraction = Vector3D.subtract(vector_1, vector_2)
print(subtraction)  # Output: (-3, -3, -3)

scalar_product = vector_1.scalar_prod(2)
print(scalar_product)  # Output: (2, 4, 6)

dot_product = Vector3D.dot_product(vector_1, vector_2)
print(dot_product)  # Output: 32

distance = Vector3D.distance(vector_1, vector_2)
print(distance)  # Output: 5.196152422706632
```

## Author

This Vector module was created by Jorge Luis Hurtado Goitia.

Feel free to reach out to me if you have any questions or feedback.
