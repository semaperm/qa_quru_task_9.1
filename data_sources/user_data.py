from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    user_number: str
    birthday_date: dict[str:str]
    subject: str
    hobbies: dict[str:bool]
    file: str
    address: str
    state: str
    city: str


user_for_registration = User(
    first_name="Sema",
    last_name="Semenov",
    email="sema@test.ru",
    gender="Male",
    user_number="0123456789",
    birthday_date={'year': '1995', 'month': 'September', 'day': '13'},
    subject="Maths",
    hobbies={"Sports": True, "Reading": False, "Music": False},
    file="Proverka.jpg",
    address="Perm",
    state="NCR",
    city="Delhi"
)