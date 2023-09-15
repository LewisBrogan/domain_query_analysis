from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from datetime import date

current_date = date.today()
csv_name = f'{current_date}_daily_trends_usa.csv'

headOption = webdriver.FirefoxOptions()
headOption.add_argument('-headless')
browser = webdriver.Firefox(options=headOption)


browser.get('https://trends.google.com/trends/trendingsearches/daily?geo=US')

feed_list_wrappers = browser.find_elements(By.CLASS_NAME,'feed-list-wrapper')
# returns 2 feed list arrays

feed_list_wrappers


trends = []

for feed_list_wrapper in feed_list_wrappers:
    details = feed_list_wrapper.find_elements(By.CLASS_NAME,'details')
    for detail in details:

        title = detail.find_element(By.CLASS_NAME, 'details-top').text
        bio = detail.find_element(By.CLASS_NAME, 'details-bottom').text
        hits = detail.find_element(By.XPATH,'..').find_element(By.CLASS_NAME,"search-count-title").text
        trends.append([title, bio, hits])
        #print('Title: ', title, '\n', 'Bio: ', bio, '\n', 'hits: ', hits)
        #print('\n Date: ', now)
        
  
        with open(csv_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Bio', 'Hits'])
            for trend in trends:
                writer.writerow(trend)