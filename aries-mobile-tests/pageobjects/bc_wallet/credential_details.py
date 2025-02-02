import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.basepage import BasePage


# These classes can inherit from a BasePage to do common setup and functions
class CredentialDetailsPage(BasePage):
    """Credential Details page object"""
    
    # Locators
    on_this_page_text_locator = "Credential Details"
    revocation_dismiss_locator = (AppiumBy.ID, "com.ariesbifold:id/Okay")
    revocation_message_locator = (AppiumBy.ID, "com.ariesbifold:id/BodyText")
    revocation_status_locator = (AppiumBy.ID, "com.ariesbifold:id/Revoked")
    revocation_info_locator = (AppiumBy.ID, "com.ariesbifold:id/RevocationInfo")


    def on_this_page(self):
        return super().on_this_page(self.on_this_page_text_locator)

    def select_revocation_dismiss(self):
        if self.on_this_page():
            self.find_by(self.revocation_dismiss_locator).click()
        else:
            raise Exception(f"App not on the {type(self)} page")

    def select_revocation_info(self):
        if self.on_this_page():
            self.find_by(self.revocation_dismiss_locator).click()
        else:
            raise Exception(f"App not on the {type(self)} page")

    def get_revocation_message_details(self):
        if self.on_this_page():
            message_element = self.find_by(self.revocation_message_locator)
            return message_element.text
        else:
            raise Exception(f"App not on the {type(self)} page")

    def is_credential_revoked(self):
        if self.on_this_page():
            if self.find_by(self.revocation_status_locator):
                return True
            else:
                return False
        else:
            raise Exception(f"App not on the {type(self)} page")