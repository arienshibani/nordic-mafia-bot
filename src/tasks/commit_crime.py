from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from util.helpers import print_with_timestamp

def commit_crime(driver: WebDriver, crime_to_commit: str = "Ran en gammel dame") -> int:
    '''
    Navigates to the "Kriminalitet" page and commits a crime. The default crime is "Ran en gammel dame".

    Args:
        driver: WebDriver instance from Selenium Manager.
        crime_to_commit: The crime to commit. Defaults to "Ran en gammel dame". Possible crimes are:
            - "Ran en gammel dame"
            - "Jack en spilleautomat"
            - "Ran en bensinstasjon"
            - "Ran en postbank"
            - "Ran en verditransport"

    Returns:
        The amount of money stolen as an integer if successful, otherwise 0.
    '''

    # Make sure the crime_to_commit is one of the available crimes
    possible_crimes = [
        "Ran en gammel dame",
        "Jack en spilleautomat",
        "Ran en bensinstasjon",
        "Ran en postbank",
        "Ran en verditransport"
    ]

    if crime_to_commit not in possible_crimes:
        print_with_timestamp(f"Invalid crime in config: {crime_to_commit}. Defaulting to 'Ran en gammel dame'.")
        crime_to_commit = "Ran en gammel dame"

    try:
        # Click on "Kriminalitet"
        kriminalitet_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?p=kriminalitet' and contains(text(), 'Kriminalitet')]"))
        )
        kriminalitet_link.click()

        # Click on the crime button
        crime_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//td[contains(text(), '{crime_to_commit}')]")))

        crime_button.click()

        print_with_timestamp("Crime committed.")
        return 0
    except Exception as e:
        print_with_timestamp(f"Unable to commit the crime. Error: {e}")

        return 0
