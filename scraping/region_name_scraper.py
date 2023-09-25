"""
This module contains the main functionality for setting up a browser instance, fetching region names
from the specified URL, and logging the results. 

Functions:
    - main(): Initiates the browser, fetches region names, logs them, and then closes the browser.
"""

import logging

from typing import List

from selenium.webdriver import Firefox

from utils.region_name_utls.browser_setup__utils import browser_setup
from utils.region_name_utls.fetch_region_names__utils import fetch_region_names

def main() -> None:
    """
    Main function to initiate the browser setup,
    fetches the region names and logs the output returned for them.
    
    Raises:
        Any exceptions that gets raised by browser_setup and fetch_region_names.
    """
    browser: Firefox = browser_setup()
    if browser:
        regions: List[str] = fetch_region_names(browser)
        for region in regions:
            logging.info("Region: %s", region)
    logging.info('Closing the browser...')
    browser.quit()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
