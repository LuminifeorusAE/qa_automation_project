import random

from faker import Faker
from data.data import Person

faker = Faker()
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker.first_name() + " " + faker.last_name(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        age=random.randint(18, 90),
        salary=random.randint(80000, 500000),
        departament=faker.job(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address()
    )
