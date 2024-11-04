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

        # Check if the success message appears
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='successBox']//span[contains(text(), 'Vellykket')]")
            ))

            # Extract the amount of money stolen using a regex to match numbers with commas
            amount_element = driver.find_element(By.XPATH, "//div[@class='successBox']//span[normalize-space(.) and translate(., ',', '') = translate(., ',', '')*1]")
            amount_text = amount_element.text.replace(',', '')  # Remove any commas
            amount_stolen = int(amount_text)

            print_with_timestamp(f"💰 Rob random person, money stolen: \033[1;32m{amount_stolen} kr\033[0m - Next attempt in 15 minutes.")
            return amount_stolen
        except:
            # No success box means the crime failed
            print_with_timestamp(f"😕 Rob random person, no money stolen: \033[1;31m0kr\033[0m - Next attempt in 15 minutes.")
            return 0

    except:
        print_with_timestamp("Failed to rob a player or in jail.")
        return 0
