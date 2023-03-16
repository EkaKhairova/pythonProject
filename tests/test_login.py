import allure
from selenium import webdriver
from page_object.login_page import LoginPage

@allure.description("Проверка работы команды setup при запуске")
@allure.title("Проверка работы команды запускающей остальные тестын")
@allure.severity(severity_level="BLOCKER")

def test_setup():
    global driver
    driver = webdriver.Chrome()


@allure.description("Проверка возможности заполнения полей при регистрации в системе")
@allure.testcase("https://shop.synctoskill.com", "STS5")
@allure.title("Проверка возможности регистрации в системе")
@allure.severity(severity_level="BLOCKER")



def test_reg():
    LoginPage.startpage(driver)
    driver.maximize_window()
    driver.find_elements('xpath', LoginPage.log_in)[0].click()
    driver.find_elements('xpath', LoginPage.register_filed)[0].click()
    driver.find_element('xpath', LoginPage.name_filed).send_keys("Dima")
    driver.find_element('xpath', LoginPage.email_filed).send_keys("dima95xa@gmail.com")
    driver.find_element('xpath', LoginPage.password_filed).send_keys("Qwerty**")
    driver.find_element('xpath', LoginPage.password_confirm_filed).send_keys("Qwerty**")
    driver.find_element('xpath', LoginPage.phone_filed).send_keys("7(777)125-12-12")
    driver.find_element('xpath', LoginPage.address_filed).send_keys("Lenina 5")
    driver.find_element('xpath', LoginPage.birth_day_filed).send_keys("15.06.2000")
    driver.find_element('xpath', LoginPage.sign_in_button).click()


@allure.description("Проверка возможности заполнения полей при авторизации в системе")
@allure.testcase("https://shop.synctoskill.com", "STS5")
@allure.title("Проверка возможности авторизации в системе")
@allure.severity(severity_level="BLOCKER")

def test_login():
    LoginPage.startpage(driver)
    driver.find_elements("xpath", LoginPage.log_in)[0].click()
    driver.find_element("xpath", LoginPage.email_filed).send_keys("dima95xa@gmail.com")
    driver.find_element("xpath", LoginPage.password_filed).send_keys("Qwerty**")
    driver.find_element("xpath", LoginPage.log_in_button).click()
    email = driver.find_elements("xpath", LoginPage.user_profile_name)[0].get_attribute("text").find("dima95xa@gmail.com")
    assert(email != 1)


 assert response.status_code == 200
