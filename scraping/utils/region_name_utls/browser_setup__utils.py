"""
This module provides functionality to initialize and return a Firefox browser
instance with a headless configuration. 

It uses the Selenium package to interact with the browser and handles exceptions related to browser setup.

Attributes:
    None

Functions:
    browser_setup() -> Firefox: Initialize and return a Firefox browser instance with --headless configuration. # pylint: disable=line-too-long
"""

import logging

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.common.exceptions import WebDriverException

def browser_setup() -> Firefox:
    """Initialize and returns a Firefox browser instance with --headless configuration

    Returns:
        webdriver.Firefox: The instance of the Firefox browser.
        
    Raises:
        WebDriverException: If there's an issue Initializing the browser.
    """
    logging.info('Initializing browser with headless configuration...')
    try:
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        browser = webdriver.Firefox(options=options)
        return browser
    except WebDriverException as webdriver_exception_logging: # pylint: disable=broad-except
        logging.error("Error Initializing the browser: %e", webdriver_exception_logging)
        raise
