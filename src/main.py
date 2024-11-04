from selenium import webdriver
from dotenv import load_dotenv
from datetime import datetime
import time
import os
import random

# Import self-defined functions
from util.helpers import print_with_timestamp
from util.login_to_game import login_to_game
from util.check_money_at_hand import get_current_money
from util.check_if_in_jail import get_jail_status
from tasks.commit_crime import commit_crime
from tasks.rob_random_player import rob_random_player
from tasks.deposit_money import deposit_all_money
from tasks.jailbreak_highest_bounty import jailbreak_highest_bounty

# Global variables
in_jail = False
logged_in = False
money_collected_this_session = 0

# Time tracking variables
last_crime_time = time.time() - 180  # Ensure the first crime is attempted immediately
last_robbery_time = time.time() - 900  # Ensure the first robbery is attempted immediately
last_deposit_time = time.time() - 1800  # Ensure the first deposit is attempted immediately


# Load environment variables from .env file. Replace with actual file path.
load_dotenv()
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# Set up WebDriver (no need to specify the path, Selenium Manager handles it)
driver = webdriver.Chrome()
# Open the game website
driver.get('https://www.nordicmafia.org')  # Replace with the actual game URL

logged_in = login_to_game(driver, username, password)

while logged_in:
    time.sleep(random.uniform(3, 6))
    if time.time() - last_robbery_time > 900:
        rob_random_player(driver)
        last_robbery_time = time.time()

    time.sleep(random.uniform(2, 6))
    if time.time() - last_crime_time > 180:
        commit_crime(driver, "Jack en spilleautomat")
        last_crime_time = time.time()

    time.sleep(random.uniform(3, 6))
    if time.time() - last_deposit_time > 360:
        money_collected_this_session += deposit_all_money(driver)
        last_deposit_time = time.time()

    # Jailbreak the player with the highest bounty.