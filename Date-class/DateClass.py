import random
def monthDays(month: int, year: int):
    '''
    This function returns the number of days a specific month has, taking into account if the year is a leap year.

    Parameters:
        month (int): The month for which to determine the number of days.
        year (int): The year in which the month falls.

    Returns:
        int: The number of days in the specified month.

    Notes:
        - The function considers leap years when calculating the number of days in February.
        - For leap years, February has 29 days; otherwise, it has 28 days.
        - The month parameter should be an integer from 1 to 12, representing the months of the year.
        - The year parameter should be a valid integer year.

    Example:
        month_days = monthDays(2, 2023)
        print(month_days)
        # Output: 28
    '''
    month_days = {1  : 31,
                  2  : 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28,
                  3  : 31,
                  4  : 30,
                  5  : 31,
                  6  : 30,
                  7  : 31,
                  8  : 31,
                  9  : 30,
                  10 : 31,
                  11 : 30,
                  12 : 31}
    return month_days.get(month)

class Date(object):
    """
    Represents a date in the Gregorian calendar.

    The Date class provides various methods and properties to manipulate and work with dates,
    including date validation, date comparison, date arithmetic, and more.

    Attributes:
        day (int): The day component of the date.
        month (int): The month component of the date.
        year (int): The year component of the date.

    Methods:
        __init__(self, day=1, month=1, year=1): Initializes a new Date object with the given day, month, and year.
        __str__(self): Returns a string representation of the date.
        isLeap(self): Checks if the year is a leap year.
        totalMonthDays(self): Returns the total number of days in the month.
        validDate(self): Checks if the date is valid.
        monthName(self): Returns the name of the month.
        areEqual(date1, date2): Checks if two dates are equal.
        isLater(date1, date2): Checks if date1 is later than date2.
        isPrevious(date1, date2): Checks if date1 is earlier than date2.
        firstDayOfTheYear(cls, year): Creates a Date object representing the first day of the specified year.
        lastDayOfTheYear(cls, year): Creates a Date object representing the last day of the specified year.
        plusDay(self): Increments the date by one day.
        minusDay(self): Decrements the date by one day.
        copy(cls, date_object): Creates a copy of the given Date object.
        leapYear(year): Checks if a year is a leap year.
        difference(date1, date2): Calculates the difference in days between two dates.
        randomDate(cls): Creates a random valid date.
        toDate(cls, literal_date): Converts a string with the format "dd Month YYYY" to a Date object.
        """
    month_names = { 1: 'January',
                    2: 'February',
                    3: 'March',
                    4: 'April',
                    5: 'May',
                    6: 'June',
                    7: 'July',
                    8: 'August',
                    9: 'September',
                   10: 'October',
                   11: 'November',
                   12: 'December'}

    def __init__(self, day: int = 1, month: int = 1, year: int = 1):
        self.day = day
        self.month = month
        self.year = year
        if not self.validDate:
            raise ValueError('Invalid date introduced!')
            
    def __str__(self):
        day = str(self.day).zfill(2)
        month = str(self.month).zfill(2)
        year = str(self.year).zfill(4)

        return f'{day} / {month} / {year}'
    
    @property
    def isLeap(self):
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)
    
    @property
    def totalMonthDays(self):
        month_days = {1  : 31,
                      2  : 29 if self.isLeap else 28,
                      3  : 31,
                      4  : 30,
                      5  : 31,
                      6  : 30,
                      7  : 31,
                      8  : 31,
                      9  : 30,
                      10 : 31,
                      11 : 30,
                      12 : 31}     
        return month_days.get(self.month)
    
    @property
    def validDate(self):
        if not 1 <= self.month <= 12:
            return False

        if not 1 <= self.day <= self.totalMonthDays:
            return False

        return True

    @property
    def monthName(self):
        return self.month_names.get(self.month)
    
    @staticmethod
    def areEqual(date1, date2):
        return date1.day == date2.day and date1.month == date2.month and date1.year == date2.year

    @staticmethod
    def isLater(date1, date2):
        return (date1.year, date1.month, date1.day) > (date2.year, date2.month, date2.day)
    
    @staticmethod
    def isPrevious(date1, date2):
        return (date1.year, date1.month, date1.day) < (date2.year, date2.month, date2.day)

    @classmethod
    def firstDayOfTheYear(cls, year:int):
        return cls(1, 1, year)

    @classmethod
    def lastDayOfTheYear(cls, year:int):
        return cls(31, 12, year)


    def plusDay(self):
        self.day += 1

        if self.day > self.totalMonthDays:
            self.day = 1
            self.month += 1

            if self.month > 12:
                self.month = 1
                self.year += 1
         
    def minusDay(self):
        self.day -= 1

        if self.day == 0:
            self.day = self.totalMonthDays
            self.month -= 1

            if self.month == 0:
                self.month = 12
                self.year -= 1

    @classmethod
    def copy(cls, date_object):
        return cls(date_object.day, date_object.month, date_object.year)

    @staticmethod
    def leapYear(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) 

    @staticmethod
    def difference(date1, date2):  
        days_of_difference = 0

        #Resorting the dates, initial date = minor date
        if Date.isLater(date1, date2):
            initial_date = date2
            final_date = date1
        else:
            initial_date = date1
            final_date = date2
        
    
        initial_month = initial_date.month
        
        if initial_month == 12:
            initial_year = initial_date.year + 1
        else:
            initial_year = initial_date.year

        #starting to iterate years and months
        for year in range(initial_year, final_date.year + 1):

            if days_of_difference == 0: #Only for the first iteration
                if initial_date.month == final_date.month and initial_date.year == final_date.year:
                    days_of_difference += final_date.day - initial_date.day
                    break
                
                #Adding the rest of the days to obtain a complete month                           
                if initial_date.month != final_date.month or initial_date.year != final_date.year:    
                    days_of_difference += monthDays(initial_month, initial_date.year) - initial_date.day
                    if initial_month != 12:
                        initial_month += 1  
                    else: 
                        initial_month = 1
                    
            #Objective month for the iteration loop        
            if year == final_date.year:
                objective_month = final_date.month    
            else:
                objective_month = 12
                    
            for month in range(initial_month , objective_month + 1):
                if year == final_date.year and month == final_date.month:
                    days_of_difference += final_date.day
                    break
                
                days_of_difference += monthDays(month, year)
                if month == 12:
                    initial_month = 1
                    break
        
        return days_of_difference

    @classmethod
    def randomDate(cls):
        year = random.randrange(1, 3001)
        month = random.randrange(1, 13) 
        day = random.randrange(1, monthDays(month, year))

        return cls(day, month, year)
    
    @classmethod
    def toDate(cls, literal_date:str):
        parts = literal_date.split(' ')
        if len(parts) != 3 or parts[1].capitalize() not in cls.month_names.values():
            raise ValueError('Invalid format introduced!')

        day = int(parts[0])
        year = int(parts[2])
        month = next(key for key, value in cls.month_names.items() if value == parts[1].capitalize())
        return cls(day, month, year)