from faker import Faker
from faker.providers import internet
import re

class FakeInputData:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(FakeInputData, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.fake = Faker()
        self.fake.add_provider(internet)
        self.email = self.fake.email()
        self.password = self.fake.password()
        self.existing_email = "test_account@test.com"
        self.existing_password = "testpassword"
        self.name = self.fake.name()
        self.date_day = "1"
        self.date_month = "1"
        self.date_year = "1990"
        self.firstname = self.fake.first_name()
        self.lastname = self.fake.last_name()
        self.company = self.fake.company()
        self.address = self.fake.address()
        self.address2 = self.fake.address()
        self.country = "United States"
        self.state = self.fake.state()
        self.city = self.fake.city()
        self.zipcode = self.fake.zipcode()
        self.phone = self.fake.phone_number()
        self.file = "./data/test.txt"
        self.sentence = self.fake.sentence()
        self.search_text = 'blue'
        self.search_term = re.compile('blue', re.IGNORECASE)