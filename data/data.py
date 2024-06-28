from dataclasses import dataclass
from faker import Faker


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
