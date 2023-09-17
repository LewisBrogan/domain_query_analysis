from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import logging

def fetch_trends(region):

    region_url_map = {
        'us': 'US',
        'uk': 'GB',
    }

    """Fetch Google daily trends."""
    logging.info('Browser opened...')
    trends = []
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    browser = webdriver.Firefox(options=options)

    try:
        logging.info(f'Fetching trends for {region}...')
        region_code = region_url_map[region]
        url = f'https://trends.google.com/trends/trendingsearches/daily?geo={region_code}'
        browser.get(url)

        feed_list_wrappers = browser.find_elements(
            By.CLASS_NAME, 'feed-list-wrapper')

        # Cleaning to be done in the Database layer using dbt, e.g. bio contains random characters
        logging.info('Data fetched...')
        for feed_list_wrapper in feed_list_wrappers:
            details = feed_list_wrapper.find_elements(By.CLASS_NAME, 'details')
            for detail in details:
                title = detail.find_element(By.CLASS_NAME, 'details-top').text
                bio = detail.find_element(By.CLASS_NAME, 'details-bottom').text
                hits = detail.find_element(By.XPATH, '..').find_element(
                    By.CLASS_NAME, "search-count-title").text
                trends.append([title, bio, hits])

    except NoSuchElementException as e:
        logging.error(f"NoSuchElementException: {str(e)}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
    finally:
        browser.quit()
    # print(trends)
    return trends