import requests
import allure
from faker import Faker

fake = Faker()



@allure.description("API Проверка возможности заполнения полей при регистрации в системе")
@allure.title("API Проверка возможности регистрации в системе")
@allure.severity(severity_level="BLOCKER")



def test_api():

    temp_email = fake.ascii_company_email()
    name = fake.name()
    address = fake.address()
    date = fake.date()
    password = fake.password()

    header = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    body = {
       "password": password,
       "passwordConfirmation": password,
       "email": temp_email,
       "fullName": name,
       "birthDate": date,
       "address": address,
       "phone": "string"
    }

    response = requests.post("https://shop.synctoskill.com/api/AccountApi/register", headers=header, json=body)
    print(temp_email)
    print(name)
    print(address)
    print(date)
    print(password)

    


