from PageObject.BasePage import BasePage


class FormAuthenticationPage(BasePage):

    # XPath locators for elements on the Form Authentication Page
    username_input = "//input[@id='username']"
    password_input = "//input[@id='password']"
    login_button = "//button[@type='submit']"
    message = "//div[@id='flash']"
    heading = "//h2"
    logout_button = "//a[@href='/logout']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_heading(self) -> str:
        """
        Get the main heading of the Form Authentication page.
        :return: Main heading text.
        """
        return self.get_text(self.heading)

    def enter_username(self, username: str):
        """
        Enter the username in the input field.
        :param username: Username to enter.
        """
        self.enter_text(self.username_input,username)

    def enter_password(self, password: str):
        """
        Enter the password in the input field.
        :param password: Password to enter.
        """
        self.enter_text(self.password_input,password)

    def click_login(self):
        """
        Click the login button to submit the form.
        """
        self.click(self.login_button)

    def get_message(self) -> str:
        """
        Get the message displayed after login attempt.
        :return: Message text.
        """
        return self.get_text(self.message)

    def click_logout(self):
        """
        Click the logout button to log out of the application.
        """
        self.click(self.logout_button)