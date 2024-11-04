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
            EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?p=jail' and contains(text(), 'Fengsel')]"))
        )
        
        jail_link.click()

        # Find the first row in the jail table and save player name and bounty
        player_name = driver.find_element(By.XPATH, "//table[@class='def_table def_table_left coloringTable']//tr[2]//td[1]//span").text
        bounty = driver.find_element(By.XPATH, "//table[@class='def_table def_table_left coloringTable']//tr[2]//td[3]").text

        # Click "Bryt ut" link
        breakout_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//table[@class='def_table def_table_left coloringTable']//tr[2]//a[contains(text(), 'Bryt ut')]"))
        )

        breakout_link.click()

        # Wait for a few seconds for the page to update
        time.sleep(5)

        # Check if the error box indicating "Brukeren er ikke i fengsel" is present
        error_present = driver.find_elements(By.XPATH, "//div[@class='errorBox' and contains(., 'Brukeren er ikke i fengsel.')]")
        if error_present:
            print_with_timestamp(f"Attempted jailbreak, but the user {player_name} with bounty {bounty} is not in jail.")
            return False

        print_with_timestamp(f"Attempted to break out the player {player_name} with bounty {bounty}.")
        return True

    except Exception as e:
        print_with_timestamp(f"Failed to attempt jailbreak or no bounties available. Error: {e}")
        return False