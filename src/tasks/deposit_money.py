from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from util.helpers import print_with_timestamp

def deposit_all_money(driver: WebDriver) -> bool:
    '''
    Deposit all money in the bank.

    Args:
        driver: WebDriver instance from Selenium Manager.

    '''
    try:
        # Click on "Bank"
        bank_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?p=bank' and contains(text(), 'Bank')]")
        )
        )
        bank_link.click()

        # Click the "Sett inn alt" button
        deposit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @name='depositAll' and @value='Sett inn alt']")
        )
        )
        deposit_button.click()
        print_with_timestamp("All money deposited successfully. 30-minute timer started.")
        return True
    except:
        print_with_timestamp("Failed to deposit money.")
        return False
