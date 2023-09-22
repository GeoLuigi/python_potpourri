# Date Class Documentation

**Table of Contents**
- [Installation](#installation)
- [Usage](#usage)
- [Class Methods](#class-methods)
- [Properties](#properties)
- [Static Methods](#static-methods)
- [Example Usage](#example-usage)
- [Convert a date string to a 'Date' object](#convert-a-date-string-to-a-date-object)
- [Contributing](#contributing)
- [Author](#author)

## Installation
To use the Date class, follow these steps:

1. Ensure you have Python installed on your system (version 3.5 or above).
2. Copy the `date.py` file and include it in your project directory.

## Usage
To use the Date class in your Python code, you need to import it:
``python
from date import Date``

After importing the class, you can create instances of the Date class and perform various operations on them.

## Class Methods

The 'Date' class provides the following class methods:

-   `firstDayOfTheYear(year)`: Creates a Date object representing the first day of the specified year.
-   `lastDayOfTheYear(year)`: Creates a Date object representing the last day of the specified year.

## Properties

The Date class provides the following properties:

-   `isLeap`: Determines if the current year is a leap year.
-   `totalMonthDays`: Returns the total number of days in the current month.
-   `validDate`: Checks if the current date is valid.
-   `monthName`: Returns the name of the current month.

## Static Methods

The Date class provides the following static methods:

-   `areEqual(date1, date2)`: Compares two Date objects and checks if they represent the same date.
-   `isLater(date1, date2)`: Compares two Date objects and checks if date1 is later than date2.
-   `isPrevious(date1, date2)`: Compares two Date objects and checks if date1 is earlier than date2.
-   `leapYear(year)`: Checks if a given year is a leap year.
-   `difference(date1, date2)`: Calculates the difference in days between two dates.
-   `randomDate()`: Generates a random date.
-   `toDate(literal_date)`: Creates a Date object from a date string in literal format.

## Example Usage

Here's an example that demonstrates how to use the Date class:

    ```python
    from date import Date

    #Create a date object
    date1 = Date(12, 3, 2023)

    #Print the date
    print(date1)  # Output: 12 / 03 / 2023

    #Check if it's a leap year
    print(date1.isLeap)  # Output: False

    #Get the total days in the month
    print(date1.totalMonthDays)  # Output: 31

    #Check if the date is valid
    print(date1.validDate)  # Output: True

    #Get the name of the month
    print(date1.monthName)  # Output: March

    #Create another date object
    date2 = Date(1, 1, 2024)

    #Compare dates
    print(Date.areEqual(date1, date2))  # Output: False
    print(Date.isLater(date1, date2))  # Output: False
    print(Date.isPrevious(date1, date2))  # Output: True

    #Calculate the difference in days between dates
    print(Date.difference(date1, date2))  # Output: -295

    #Generate a random date
    random_date = Date.randomDate()
    print(random_date)  # Output: Random date in the format DD / MM / YYYY

    #Convert a date string to a 'Date' object
    date_string = "25 December 2023"
    converted_date = Date.toDate(date_string)
    print(converted_date)  # Output: 25 / 12 / 2023

These are just a few examples of how you can use the Date class to perform operations on dates. Refer to the class documentation above for a complete list of methods and properties available.

## Contributing

If you would like to contribute to the Date class, feel free to submit a pull request. Make sure to follow the existing coding style and include tests for any new functionality.

## Author

The code in this repository was written by:

**Jorge Luis Hurtado Goitia**

-   Email: [lhgjorge@gmail.com](mailto:lhgjorge@gmail.com)
-   LinkedIn: [linkedin.com/in/jorgeluishurtadogoitia](https://www.linkedin.com/in/jorgeluishurtadogoitia/)