from cgi import print_form
import email
from secrets import choice
import pandas as pd
import openpyxl
import random
from datetime import datetime, timedelta
import requests
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data/"
male_name = pd.DataFrame(pd.read_excel( DATA_DIR / "name_male.xlsx"))
female_name = pd.DataFrame(pd.read_excel( DATA_DIR / "name_female.xlsx"))
male_surname = pd.DataFrame(pd.read_excel(DATA_DIR / "surname_male.xlsx"))
female_surname = pd.DataFrame(pd.read_excel(DATA_DIR / "surname_female.xlsx"))
mail_provider = pd.DataFrame(pd.read_excel(DATA_DIR / "mail_provider.xlsx"))
job_list = pd.DataFrame(pd.read_excel(DATA_DIR / "job_list.xlsx"))
citys_list = pd.DataFrame(pd.read_excel(DATA_DIR / "citys_poland.xlsx"))


class Person():
    def __init__(self) -> None:
        self.gender = self.get_gender()

        if self.gender == "male":
            self.name = self.get_random_male_name()
        else:
            self.name = self.get_random_female_name()

        if self.gender == "male":
            self.surname = self.get_random_male_surname()
        else:
            self.surname = self.get_random_female_surname()
        self.age, self.birthday_date = self.get_random_birthsday()
        self.email = self.genarate_email(self.name, self.surname)
        self.job = self.generate_job_title()
        self.weight = self.get_random_weight()
        self.phone = self.generate_mobile_phone_number()
        self.photo = self.get_photo(self.gender, self.age)
        self.place_of_birth = self.get_place_of_birth()

    def get_gender(self):
        if random.randint(0, 1) == 0:
            return "male"
        else:
            return "female"

    def get_random_male_name(self):
        return male_name["name"][random.randint(0, male_name.shape[0] - 1)].capitalize()

    def get_random_female_name(self):
        return female_name["name"][random.randint(0, female_name.shape[0] - 1)].capitalize()

    def get_random_male_surname(self):
        return male_surname["surname"][random.randint(0, male_surname.shape[0] - 1)].capitalize()

    def get_random_female_surname(self):
        return female_surname["surname"][random.randint(0, female_surname.shape[0] - 1)].capitalize()

    def genarate_email(self, name, surname):
        email = mail_provider["name"][random.randint(
            0, mail_provider.shape[0]-1)]
        emal_adress = f"{name}.{surname}@{email}".lower()
        return emal_adress

    def generate_job_title(self):
        job = job_list["job"][random.randint(0, job_list.shape[0] - 1)]
        if self.age > 62:
            job = "emeryt"
        return job

    def get_random_weight(self):
        if self.gender == "male":
            return round(random.gauss(85, 10), 1)
        else:
            return round(random.gauss(75, 10), 1)

    def get_random_age(self):
        age = round(random.gauss(41, 18))
        if age < 18:
            age = 18
        return age

    def get_random_date_between(self, start, end):

        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(0, int_delta)
        return start + timedelta(seconds=random_second)

    def get_random_birthsday(self):
        now = datetime.now()
        age = self.get_random_age()
        d1 = datetime.strptime(
            f"{now.day}/{now.month}/{now.year - age - 1} {now.hour}:{now.second}", "%d/%m/%Y %H:%M")
        d2 = datetime.strptime(
            f"{now.day}/{now.month}/{now.year - age} {now.hour}:{now.second}", "%d/%m/%Y %H:%M")
        birthsday = self.get_random_date_between(d1, d2)
        return age, birthsday.strftime("%d.%m.%Y %H:%M")

    def generate_mobile_phone_number(self):
        prefix = random.choice(
            [45, 50, 51, 53, 57, 60, 66, 69, 72, 73, 78, 79, 88])
        rand_num = [random.randint(0, 9) for number in range(0, 7)]
        rand_num.insert(0, prefix)
        phone_number = ""
        for i in rand_num:
            phone_number += str(i)
        return phone_number

    def get_photo(self, gender, age):
        query = {"gender": gender, "minimum_age": age-4, "maximum_age": age+4}
        response = requests.get("https://fakeface.rest/face/json", params=query)
        data = response.json()
        return data["image_url"]
    
    def get_place_of_birth(self):
        return citys_list["city"][random.randint(0, male_name.shape[0] - 1)].capitalize()




if __name__ == "__main__":
    person = Person()
    print(person.__dict__)
    print(DATA_DIR)