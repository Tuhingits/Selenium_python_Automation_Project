from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

serv = Service("D:\\Selenium_Web_Driver\\New folder\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv,chrome_options=option)
driver.maximize_window()

driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Cliclking menu-toggle for Showing logging button
driver.find_element(By.ID,"menu-toggle").click()

    #For going Loging Page
driver.find_element(By.XPATH,"/html/body/nav/ul/li[3]/a").click()
#For entering Username And Password By Using xpath

driver.find_element(By.ID,"txt-username").send_keys("John Doe")
driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")

driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/form/div[4]/div/button").click()

# Validation Test Case
Actual_title = driver.title
Expect_title = "CURA Healthcare Service"
if Actual_title==Expect_title:
    print("Login Test Pass")
else:
    print("Login Test Fail")

driver.close()
