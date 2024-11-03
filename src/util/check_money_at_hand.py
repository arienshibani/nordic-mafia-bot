from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from util.helpers import print_with_timestamp

# Function to get current money and store it in a variable
def get_current_money(driver: WebDriver) -> int:
    try:
        money_element = driver.find_element(By.XPATH, "//li[@id='money_hand']//span[@class='value']/span")
        current_money = int(money_element.text.replace(',', '').replace('.', ''))  # Handle formatting
        print_with_timestamp(f"Current money checked: {current_money} kr")
        return current_money
    except:
        print_with_timestamp("Failed to retrieve current money.")
        return 0