"""
This module provides the `fetch_region_names` function, 
which is responsible for fetching region names from Google Trends daily trending searches.

The function uses Selenium to navigate the Google Trends website, interact with the UI elements,
and extract the relevant region names.

Functions:
    fetch_region_names(browser: Firefox) -> List[str]: Fetches region names from Google Trends.
"""

import logging

from typing import List

from httpcore import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

def fetch_region_names(browser: Firefox) -> List[str]:
    """Fetch region names from Google Trends daily trending searches.

    Args:
        browser (Firefox): An instance of the Firefox browser.

    Returns:
        List[str]: A list containing the region names.
    """
    region_list: List[str] = []
    try:
        url: str = 'https://trends.google.com/trends/trendingsearches/daily?geo=US'
        logging.info('Navigating to %s', url)
        browser.get(url)

        logging.debug('Looking for region buttons...')
        region_buttons: List[WebElement] = browser.find_elements(
            By.XPATH, "(//md-select-value[@class='_md-select-value']//span)[2]")
        if region_buttons:
            logging.info('Found region buttons. Clicking the first one...')
            region_buttons[0].click()

        logging.debug('Extracting region names...')
        region_names: List[WebElement] = browser.find_elements(By.XPATH, "//div[@class='_md-text']")
        if region_names:
            logging.info('Found %s regions.', len(region_names))
            for i in region_names:
                text: str = i.text
                region_list.append(text)
        else:
            logging.warning("No region names found.")
    except NoSuchElementException:
        logging.error('NoSuchElementException: Failed to find the expected element on the page.')
    except TimeoutException:
        logging.error('TimeoutException: Timed out waiting for an element.')
    except Exception as exception_logging: # pylint: disable=broad-except
        logging.error('An unexpected error occurred: %s', str(exception_logging))

    return region_list
