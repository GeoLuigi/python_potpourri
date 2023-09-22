# Geoshapes

Geoshapes is a Python module that provides classes for working with various geometric shapes. It allows you to create and perform calculations on regular polygons, circles, and cylinders.

## Installation

To use Geoshapes, simply copy the `geometry.py` file into your project directory.

## Usage

Import the module into your Python script using the `import` statement:

```python
import geoshapes
```

### Regular Polygons

The module includes a `RegularPolygon` class that represents a regular polygon with a specified number of sides. You can create instances of this class and perform calculations on them.

Example usage:

```python
polygon = geoshapes.RegularPolygon(5.0, 6)  # Create a regular hexagon
print(polygon)  # Output: "I'm a 6 sides polygon with 5.0 of base"
print(polygon.area)  # Output the area of the polygon
print(polygon.perimeter)  # Output the perimeter of the polygon
```

### Circles

The module also includes a `Circle` class for working with circles. You can create instances of this class and perform calculations on them.

Example usage:

```python
circle = geoshapes.Circle(3.0)  # Create a circle with radius 3.0
print(circle)  # Output: "I'm a circle with radius = 3.0"
print(circle.area)  # Output the area of the circle
print(circle.perimeter)  # Output the perimeter of the circle
```

### Cylinders

The `Cylinder` class extends the `Circle` class to represent a cylinder. You can create instances of this class and perform calculations on them.

Example usage:

```python
cylinder = geoshapes.Cylinder(2.0, 5.0)  # Create a cylinder with radius 2.0 and height 5.0
print(cylinder)  # Output: "I'm a cylinder with radius = 2.0 and height = 5.0"
print(cylinder.area)  # Output the surface area of the cylinder
print(cylinder.volume)  # Output the volume of the cylinder
```

## Modifying the Code

Feel free to modify the code according to your needs and use it in your projects. Geoshapes is designed to be flexible and customizable.

## Author

Geoshapes is developed and maintained by Jorge Hurtado.

## License

This module is licensed under the MIT License.
