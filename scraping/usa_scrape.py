import csv
import logging
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def write_to_csv(file_name, data):
    """Write trend data to a CSV file."""
    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Bio', 'Hits'])
        for trend in data:
            writer.writerow(trend)


def fetch_trends():
    """Fetch Google daily trends."""
    trends = []
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    browser = webdriver.Firefox(options=options)

    try:
        browser.get(
            'https://trends.google.com/trends/trendingsearches/daily?geo=US')
        feed_list_wrappers = browser.find_elements(
            By.CLASS_NAME, 'feed-list-wrapper')

        # Cleaning to be done in the Database layer using dbt, e.g. bio contains random characters
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
    print(trends)
    return trends


def main():
    """Main function."""
    try:
        current_date = date.today()
        csv_name = f'{current_date}_daily_trends_usa.csv'
        trends_data = fetch_trends()

        if trends_data:
            write_to_csv(csv_name, trends_data)
    except FileNotFoundError as e:
        logging.error(f"FileNotFoundError: {str(e)}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
