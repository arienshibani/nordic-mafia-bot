from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from util.helpers import print_with_timestamp

def deposit_all_money(driver: WebDriver) -> int:
    '''
    Deposit all money in the bank and return the amount deposited.

    Args:
        driver: WebDriver instance from Selenium Manager.

    Returns:
        The amount of money deposited as an integer.
    '''
    try:
        # Click on "Bank"
        bank_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?p=bank' and contains(text(), 'Bank')]"))
        )

        bank_link.click()

        # Wait for the money element to be visible and get the inner span value
        money_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@id='money_hand']/span"))
        )
        amount_to_deposit = int(money_element.text.replace(',', '').replace(' ', ''))

        # Click the "Sett inn alt" button
        deposit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @name='depositAll' and @value='Sett inn alt']"))
        )

        deposit_button.click()
        print_with_timestamp(f"🏦 Deposited \033[1;33m{amount_to_deposit}\033[0m kr in the bank account.")

        return amount_to_deposit

    except Exception as e:
        print_with_timestamp(f"❌ Error: Failed to deposit money: {e}")
        return 0
