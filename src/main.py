from selenium import webdriver
from dotenv import load_dotenv
from datetime import datetime
import time
import os

# Import self-defined functions
from util.helpers import print_with_timestamp
from util.login_to_game import login_to_game
from util.check_money_at_hand import get_current_money
from util.check_if_in_jail import get_jail_status
from tasks.commit_crime import commit_crime
from tasks.rob_random_player import rob_random_player
from tasks.deposit_money import deposit_all_money
from tasks.jailbreak_highest_bounty import jailbreak_highest_bounty

in_jail = False
logged_in = False
last_crime_time = time.time() - 180  # Ensure the first crime is attempted immediately
last_robbery_time = time.time() - 900  # Ensure the first robbery is attempted immediately
last_deposit_time = time.time() - 1800  # Ensure the first deposit is attempted immediately
money_collected_this_session = 0 # Keep track of the money collected in this session

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
    in_jail = get_jail_status(driver)
    # Check if the player is in jail and wait until the time is up
    if in_jail[0]: # The first element of the tuple is a boolean indicating if the player is in jail
        time_left = get_jail_status(driver)[1] # The second element of the tuple is the time left in jail
        time.sleep(time_left)

    else:
        # Commit a crime if possible.
        if time.time() - last_crime_time > 180:
            commit_crime(driver)
            last_crime_time = time.time()

        # Rob a random player if possible.
        if time.time() - last_robbery_time > 900:
            rob_random_player(driver)
            last_robbery_time = time.time()

        # Jailbreak the player with the highest bounty.
        successfull_jailbreak = jailbreak_highest_bounty(driver)
        
        if(not successfull_jailbreak):
            exit(1)
