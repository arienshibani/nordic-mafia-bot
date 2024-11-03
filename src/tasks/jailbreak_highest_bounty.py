from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from util.helpers import print_with_timestamp
import time


def jailbreak_highest_bounty(driver: WebDriver) -> bool:
    '''
    Visit the jail page and attempt to break out the player with the highest bounty. If the jailbreak fails, the player will be put in jail.

    Args:
        driver: WebDriver instance from Selenium Manager.
    '''

    try:
        # Click on "Fengsel"
        jail_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?p=jail' and contains(text(), 'Fengsel')]")
        )
        )
        jail_link.click()

        # Find the first row in the jail table and click "Bryt ut" link
        breakout_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//table[@class='def_table def_table_left coloringTable']//tr[2]//a[contains(text(), 'Bryt ut')]")
        ))


        breakout_link.click()

        # Check if the jailbreak failed or someone else broke them out first
        time.sleep(5)  # Wait for page update
        print_with_timestamp("Attempted to break out the player with the highest bounty.")
        return True

    except:
        print_with_timestamp("Failed to attempt jailbreak or no bounties available.")
        return False
