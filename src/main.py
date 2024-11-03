from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# Set up WebDriver (no need to specify the path, Selenium Manager handles it)
driver = webdriver.Chrome()

# Open the game website
driver.get('https://www.nordicmafia.org')  # Replace with the actual game URL

# Wait for the cookie popup and click the "Avvis alle" button if present
try:
    reject_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Avvis alle')]")
    )
    )
    reject_button.click()
except:
    print("No cookie popup found or already dismissed.")

# Wait for the login button to be present and click it
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/login' and contains(text(), 'Logg inn')]")
)
)
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
WebDriverWait(driver, 10).until(
    EC.url_changes('https://www.nordicmafia.org/login')
)

# Function to commit a crime
def commit_crime():
    try:
        # Click on "Kriminalitet"
        kriminalitet_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?p=kriminalitet' and contains(text(), 'Kriminalitet')]")
        )
        )
        kriminalitet_link.click()

        # Click on "Jack en spilleautomat"
        jack_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//td[contains(text(), 'Jack en spilleautomat')]")
        )
        )
        jack_button.click()
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Crime committed successfully. 3-minute timer started.")
        return True
    except:
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Failed to commit a crime or in jail.")
        return False

# Function to rob a random player
def rob_random_player():
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
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Robbery performed successfully. 15-minute timer started.")
        return True
    except:
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Failed to rob a player or in jail.")
        return False

# Main loop to commit a crime every 3 minutes and rob a player every 15 minutes
in_jail = False
last_crime_time = time.time() - 180  # Ensure the first crime is attempted immediately
last_robbery_time = time.time() - 900  # Ensure the first robbery is attempted immediately

while True:
    current_time = time.time()
    if not in_jail:
        # Check if it's time to commit a crime (3 minutes passed)
        if current_time - last_crime_time >= 180:
            success = commit_crime()
            if success:
                last_crime_time = time.time()  # Reset the timer for the next crime
            else:
                in_jail = True  # Assume being in jail if crime fails

        # Check if it's time to rob a player (15 minutes passed)
        if current_time - last_robbery_time >= 900:
            robbery_success = rob_random_player()
            if robbery_success:
                last_robbery_time = time.time()  # Reset the timer for the next robbery
    else:
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - In jail. Waiting for release...")
        time.sleep(60)  # Wait 1 minute before checking again

# Close the browser when done
driver.quit()
