from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from util.helpers import print_with_timestamp


def rob_random_player(driver: WebDriver) -> bool:
    try:
        # Click on "Utpressing"
        blackmail_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?p=blackmail' and contains(text(), 'Utpressing')]")
        )
        )
        blackmail_link.click()

        # Click on "Tilfeldig spiller"
        random_player_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='selectDiv blackmailPlayer selectLeft' and contains(text(), 'Tilfeldig spiller')]")
        )
        )
        random_player_button.click()

        # Click the submit button to perform the robbery
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Utfør utpressing']")
        )
        )
        submit_button.click()
        print_with_timestamp("Robbery performed successfully. 15-minute timer started.")
        return True
    except:
        print_with_timestamp("Failed to rob a player or in jail.")
        return False
