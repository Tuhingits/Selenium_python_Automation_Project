from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome("D:\\Selenium_Web_Driver\\New folder\\chromedriver_win32\\chromedriver.exe",
                          chrome_options=options)
# Opening YouTube In Chrome Browser
driver.get("https://www.youtube.com//")
# Maximise Browser Window
driver.maximize_window()

driver.implicitly_wait(30)
# Find Searchbox
driver.find_element(By.NAME, "search_query").click()
# Enter Search Data into Searchbox
driver.find_element(By.NAME, "search_query").send_keys("Automation testing")
# Click Search Icon
driver.find_element(By.ID, "search-icon-legacy").click()

# Scroll To find Desire Data
location: WebElement = driver.find_element(By.LINK_TEXT, "GET INTO WORLD")
driver.execute_script("arguments[0].scrollIntoView();",location)

# Click Targeted Video
driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[3]/div[1]").click()

# click for go to channel
driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a").click()

Actual_title = driver.title
Expected_title ="GET INTO WORLD - YouTube"

if Actual_title==Expected_title:
    print("Test Case Pass")
else:
    print("Test Case Fail")

# For closing Browser
driver.close()




