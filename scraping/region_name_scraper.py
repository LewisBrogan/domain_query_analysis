from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import logging

def main():

    logging.info('Browser opened...')
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    browser = webdriver.Firefox(options=options)

    try:
        url = f'https://trends.google.com/trends/trendingsearches/daily?geo=US'
        browser.get(url)

        region_buttons = browser.find_elements(By.XPATH, "(//md-select-value[@class='_md-select-value']//span)[2]")
        if region_buttons:
            region_buttons[0].click()

        region_names = browser.find_elements(By.XPATH, "//div[@class='_md-text']")
        if region_names:
            for i in region_names:
                text = i.text
                print(f"Region: {text}")
        else:
            print("No region names found.")

        # (//div[@class='_md-text'])[2] / 

        # trending_feed_tabs = browser.find_elements(
        #     By.CLASS_NAME, 'trending-feed-tabs')
        # print(f'Fending feed tabs: {trending_feed_tabs}')

    except NoSuchElementException as e:
        logging.error(f"NoSuchElementException: {str(e)}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
    finally:
        browser.quit()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()