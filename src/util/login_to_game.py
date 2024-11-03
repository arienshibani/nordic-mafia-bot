from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from util.helpers import print_with_timestamp

def login_to_game(driver: WebDriver, username: str, password: str) -> bool:
    '''
    Logs in to the game using the provided credentials.

    Args:
        driver: WebDriver instance from Selenium Manager.
        username: The username to use for login. Provided by .env file.
        password: The password to use for login. Provided by .env file.

    '''
    # Wait for the cookie popup and click the "Avvis alle" button if present
    try:
        reject_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Avvis alle')]"))
        )
        reject_button.click()
    except:
        print_with_timestamp("No cookie popup found or already dismissed.")

    # Wait for the login button to be present and click it
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login' and contains(text(), 'Logg inn')]")))
    login_button.click()

    # Wait for the login form to appear and fill in the credentials
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )

    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')
    username_input.send_keys(username)
    password_input.send_keys(password)

    # Find and click the submit button
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Logg inn')]")
    submit_button.click()

    # Wait to ensure login completes and stay on the page
    WebDriverWait(driver, 10).until(EC.url_changes('https://www.nordicmafia.org/login'))
    return True