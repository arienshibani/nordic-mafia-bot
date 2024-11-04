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
        jail_time_element = driver.find_elements(By.XPATH, "//div[@class='blockInstance blockInstanceWide']//div[@class='defpadding']//span[@id='js_countdown']")
        if jail_time_element:
            # Extract minutes and seconds from the nested spans
            minutes_element = jail_time_element[0].find_element(By.XPATH, ".//span[1]").text
            seconds_element = jail_time_element[0].find_element(By.XPATH, ".//span[2]").text

            # Convert to total time in seconds
            total_time_in_seconds = int(minutes_element) * 60 + int(seconds_element)
            print_with_timestamp(f"You are currently in jail for {minutes_element} minute(s) and {seconds_element} second(s), totaling {total_time_in_seconds} seconds.")
            return (True, total_time_in_seconds)
        else:
            print_with_timestamp("You are not in jail.")
            return (False, 0)
    except Exception as e:
        print_with_timestamp(f"Failed to check jail status. Error: {e}")
        return (False, 0)
