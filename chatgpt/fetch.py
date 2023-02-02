from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# URL for the YouTube video
url = "https://www.youtube.com/watch?v=WfDN1SDeFUQ"

# Start a web driver (e.g. Chrome)
driver = webdriver.Chrome()

# Load the YouTube video page
driver.get(url)

# Scroll down to load more comments
while True:
    try:
        load_more_button = driver.find_element(by=By.XPATH,value='//*[@id="more"]')
        # find_element_by_xpath('//*[@id="more"]')
        load_more_button.click()
    except:
        print('break')
        break

# Extract the comments
comments = driver.find_elements(by=By.XPATH,value='//*[@id="content-text"]')
comments = [comment.text for comment in comments]

# Print the extracted comments
for comment in comments:
    print(comment)

# Close the web driver
driver.quit()
