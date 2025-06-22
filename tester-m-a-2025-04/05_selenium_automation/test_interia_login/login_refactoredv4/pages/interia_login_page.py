from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class InteriaLoginPage:
    URL = "https://poczta.interia.pl/logowanie/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    RODO_ACCEPT_BUTTON = (By.CLASS_NAME, "rodo-popup-agree")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "btn--login")
    ERROR_MESSAGE = (By.CLASS_NAME, "form__error")

    def open(self):
        self.driver.get(self.URL)

    def accept_rodo(self):
        try:
            rodo_button = self.wait.until(EC.element_to_be_clickable(self.RODO_ACCEPT_BUTTON))
            rodo_button.click()
        except TimeoutException:
            pass

    def enter_email(self, email):
        email_input = self.wait.until(EC.presence_of_element_located(self.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, email, password):
        self.open()
        self.accept_rodo()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        error = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return error.text.strip()
