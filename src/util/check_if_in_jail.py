from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple
from util.helpers import print_with_timestamp

def get_jail_status(driver: WebDriver) -> Tuple[bool, int]:
    '''
    Check if the player is currently in jail and returns the time left in jail.

    Args:
        driver: WebDriver instance from Selenium Manager.

    Returns:
        A tuple (is_in_jail, time_left_in_seconds).
    '''
    try:
        # Click on "Fengsel"
        jail_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?p=jail' and contains(text(), 'Fengsel')]"))
        )
        jail_link.click()

        # Check if the jail element indicating time left is present
        jail_time_element = driver.find_elements(By.XPATH, "//div[@class='defpadding']//span[@id='js_countdown']")
        if jail_time_element:
            time_left_text = jail_time_element[0].text
            time_parts = time_left_text.split()
            minutes = 0
            seconds = 0

            if 'minutt' in time_parts:
                minutes = int(time_parts[0])
                seconds = int(time_parts[-2])
            else:
                seconds = int(time_parts[0])

            total_time_left = (minutes * 60) + seconds
            print_with_timestamp(f"You are currently in jail for: {minutes} minute(s) and {seconds} second(s).")
            return (True, total_time_left)
        else:
            print_with_timestamp("You are not in jail.")
            return (False, 0)
    except:
        print_with_timestamp("Failed to check jail status.")
        return (False, 0)
