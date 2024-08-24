from dataclasses import dataclass


# Define a class to store personal information using the @dataclass decorator.
# The @dataclass decorator automatically generates special methods like __init__, __repr__, etc.
@dataclass
class Person:
    """
       A data class to represent a person's information.

       Attributes:
       ----------
       full_name : str
           The full name of the person.
       first_name : str
           The first name of the person.
       last_name : str
           The last name of the person.
       age : int
           The age of the person.
       salary : int
           The salary of the person.
       department : str
           The department in which the person works.
       email : str
           The email address of the person.
       current_address : str
           The current residential address of the person.
       permanent_address : str
           The permanent residential address of the person.
       mobile_number : str
           The mobile phone number of the person.
    """
    # Store personal information for a person
    full_name: str = None  # The full name of the person
    first_name: str = None  # First name of the person
    last_name: str = None  # Last name of the person
    age: int = None  # Age of the person
    salary: int = None  # Salary of the person
    department: str = None  # Department where the person works
    email: str = None  # Email address of the person
    current_address: str = None  # Current residential address of the person
    permanent_address: str = None  # Permanent residential address of the person
    mobile_number: str = None  # Mobile phone number of the person


# Define a class to store color information.
@dataclass
class Color:
    """
       A data class to represent color information.

       Attributes:
       ----------
       color_name : list
           A list containing names of colors.
    """
    # Store a list of color names
    color_name: list = None  # A list of color names


# Define a class to store date information.
@dataclass
class Date:
    """
        A data class to represent date information.

        Attributes:
        ----------
        day : str
            The day of the date.
        month : str
            The month of the date.
        year : str
            The year of the date.
        time : str
            The time associated with the date.
    """
    # Store day, month, year, and time details for a specific date
    day: str = None  # Day of the date
    month: str = None  # Month of the date
    year: str = None  # Year of the date
    time: str = None  # Time associated with the date
