import random
from datetime import datetime, timedelta
from faker import Faker
from data.data import Person, Color, Date

# Initialize a Faker instance to generate fake data like names, addresses, etc.
faker = Faker()
# Seed the random number generator for Faker to produce reproducible results.
Faker.seed()


def generated_person():
    """
    Generator function to yield a randomly generated Person object.

    The Person object is populated with fake data such as full name,
    first name, last name, age, salary, job, email, addresses, and mobile number.

    Yields:
        Person: An instance of the Person class with randomly generated attributes.
    """
    yield Person(
        full_name=faker.first_name() + " " + faker.last_name(),
        # Generate a full name by combining first and last names
        first_name=faker.first_name(),  # Generate a first name
        last_name=faker.last_name(),  # Generate a last name
        age=random.randint(18, 90),  # Random age between 18 and 90
        salary=random.randint(80000, 500000),  # Random salary between 80,000 and 500,000
        department=faker.job(),  # Generate a random job title
        email=faker.email(),  # Generate a random email address
        current_address=faker.address(),  # Generate a random current address
        permanent_address=faker.address(),  # Generate a random permanent address
        mobile_number=faker.msisdn(),  # Generate a random mobile number in the MSISDN format
    )


def generated_file():
    """
    Function to generate a text file with random content and return its name and path.

    The file contains "Hello World" followed by a random number between 0 and 999.
    It is saved at a randomly named location.

    Returns:
        tuple: A tuple containing the name of the file and the path where it is saved.
    """
    # Define the path for the new file, including a random number in the file name.
    path = rf'C:\Users\David\PycharmProjects\qa_automation_project\filetest{random.randint(0, 999)}.txt'
    # Open the file in write-plus mode (creates the file if it doesn't exist).
    file = open(path, "w+")
    # Write "Hello World" followed by a random number into the file.
    file.write(f"Hello World{random.randint(0, 999)}")
    # Close the file after writing.
    file.close()
    # Return the file name and the path to where it is stored.
    return file.name, path


def generated_color():
    """
    Generator function to yield a Color object containing a list of color names.

    Yields:
        Color: An instance of the Color class with a list of predefined color names.
    """
    yield Color(
        # List of predefined colors
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black",
                    "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generate_random_time():
    """
    Function to generate a random time between 00:00 and 23:45 in 15-minute intervals.

    Returns:
        str: A string representing the randomly generated time in the format 'HH:MM'.
    """
    # Define the start time (00:00) and end time (23:45).
    start_time = datetime.strptime("00:00", "%H:%M")
    end_time = datetime.strptime("23:45", "%H:%M")
    # Define the time interval (15 minutes).
    timedelta(minutes=15)
    # Generate a random time within the range, ensuring it's a multiple of 15 minutes.
    random_time = start_time + timedelta(minutes=random.randint(0, (end_time - start_time).seconds // 60 // 15) * 15)
    # Return the formatted time as a string (HH:MM).
    return random_time.strftime("%H:%M")


def generate_date():
    """
    Generator function to yield a Date object with random day, month, year, and time.

    Yields:
        Date: An instance of the Date class with randomly generated date and time attributes.
    """
    yield Date(
        year=faker.year(),  # Generate a random year
        month=faker.month_name(),  # Generate a random month name
        day=faker.day_of_month(),  # Generate a random day of the month
        time=generate_random_time()  # Generate a random time in 15-minute intervals
    )

# def generate_subject(value=None):
#     subjects = [
#         {
#         value: 1,
#         subject: "Hindi"
#         value: 2,
#         subject: "English"
#     , {
#         value: 3,
#         subject: "Maths"
#     }, {
#         value: 4,
#         subject: "Physics"
#     }, {
#         value: 5,
#         subject: "Chemistry"
#     }, {
#         value: 6,
#         subject: "Biology"
#     }, {
#         value: 7,
#         subject: "Computer Science"
#     }, {
#         value: 8,
#         subject: "Commerce"
#     }, {
#         value: 9,
#         subject: "Accounting"
#     }, {
#         value: 10,
#         subject: "Economics"
#     }, {
#         value: 11,
#         subject: "Arts"
#     }, {
#         value: 12,
#         subject: "Social Studies"
#     }, {
#         value: 13,
#         subject: "History"
#     }, {
#         value: 14,
#         subject: "Civics"
#     }
#     ]
