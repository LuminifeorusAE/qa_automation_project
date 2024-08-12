import random
from datetime import datetime, timedelta

from faker import Faker
from data.data import Person, Color, Date

faker = Faker()
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker.first_name() + " " + faker.last_name(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        age=random.randint(18, 90),
        salary=random.randint(80000, 500000),
        department=faker.job(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address(),
        mobile_number=faker.msisdn(),
    )


def generated_file():
    path = rf'C:\Users\David\PycharmProjects\qa_automation_project\filetest{random.randint(0, 999)}.txt'
    file = open(path, "w+")
    file.write(f"Hello World{random.randint(0, 999)}")
    file.close()
    return file.name, path


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generate_random_time():
    start_time = datetime.strptime("00:00", "%H:%M")
    end_time = datetime.strptime("23:45", "%H:%M")
    delta = timedelta(minutes=15)
    random_time = start_time + timedelta(minutes=random.randint(0, (end_time - start_time).seconds // 60 // 15) * 15)
    return random_time.strftime("%H:%M")


def generate_date():
    yield Date(
        year=faker.year(),
        month=faker.month_name(),
        day=faker.day_of_month(),
        time=generate_random_time()
    )

# def denerate_subject(value=None):
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
