class LoginPage:
    log_in = "//a[@class='nav-link text-dark']"
    register_filed = "//i[@class='fa fa-user-plus']"
    name_filed = "//input[@name='FullName']"
    password_confirm_filed = "//input[@name='PasswordConfirmation']"
    email_filed = "//input[@name='Email']"
    password_filed = "//input[@name='Password']"
    phone_filed = "//input[@name='Phone']"
    log_in_button = "//input[@value='Sign In']"
    sign_in_button = "//input[@value='Sign Up']"
    user_profile_name = "//a[@href='/Account/Profile']"
    address_filed = "//input[@name='Address']"
    birth_day_filed = "//input[@name='BirthDate']"

    def startpage(self):
        self.get("https://shop.synctoskill.com")

