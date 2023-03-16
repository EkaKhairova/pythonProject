
from selenium import webdriver



def test_setup():
    global driver
    driver = webdriver.Chrome()

def test_reg():
    driver.get("https://shop.synctoskill.com")
    driver.maximize_window()
    driver.find_elements('xpath', "//a[@class='nav-link text-dark']")[0].click()
    driver.find_elements('xpath', "//i[@class='fa fa-user-plus']")[0].click()
    driver.find_element('xpath', "//input[@name='FullName']").send_keys("Dima")
    driver.find_element('xpath', "//input[@name='Email']").send_keys("dima95xa@gmail.com")
    driver.find_element('xpath', "//input[@name='Password']").send_keys("Qwerty**")
    driver.find_element('xpath', "//input[@name='PasswordConfirmation']").send_keys("Qwerty**")
    driver.find_element('xpath', "//input[@name='Phone']").send_keys("7(777)125-12-12")
    driver.find_element('xpath', "//input[@name='Address']").send_keys("Lenina 5")
    driver.find_element('xpath', "//input[@name='BirthDate']").send_keys("15.06.2000")
    driver.find_element('xpath', "//input[@value='Sign Up']").click()


def test_login():
    driver.get("https://shop.synctoskill.com")
    driver.find_elements("xpath", "//a[@class='nav-link text-dark']")[0].click()
    driver.find_element("xpath", "//input[@name='Email']").send_keys("dima95xa@gmail.com")
    driver.find_element("xpath", "//input[@name='Password']").send_keys("Qwerty**")
    driver.find_element("xpath", "//input[@value='Sign In']").click()
    email = driver.find_elements("xpath", "//a[@href='/Account/Profile']")[0].get_attribute("text").find("dima95xa@gmal.com")
    assert(email == 1)


