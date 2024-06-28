
from faker import Faker
from data.data import Person

faker = Faker()
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker.first_name() + " " + faker.last_name(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address()
    )