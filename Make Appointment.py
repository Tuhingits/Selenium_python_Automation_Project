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

    # Make Appointment
driver.find_element(By.ID,"btn-make-appointment").click()


# Enter Credential For Login

driver.find_element(By.ID,"txt-username").send_keys("John Doe")
driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")

driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/form/div[4]/div/button").click()

# Book An Appoinment

driver.find_element(By.ID,"combo_facility").click()
driver.find_element(By.XPATH,"/html/body/section/div/div/form/div[1]/div/select/option[2]").click()

#for Checkbox
driver.find_element(By.ID,"chk_hospotal_readmission").click()

#for radio Button
driver.find_element(By.ID,"radio_program_medicaid").click()

#for date Picker  dd/mm/yy
driver.find_element(By.ID,"txt_visit_date").click()

Date_time="June 2023"

while True:
    Date = driver.find_element(By.XPATH, "/html/body/div/div[1]/table/thead/tr[2]/th[2]").text

    if Date_time==Date:
        break
    else:
        driver.find_element(By.XPATH,"/html/body/div/div[1]/table/thead/tr[2]/th[3]").click()

# fixed date

Fixed_Date: str="9"
dates=driver.find_elements(By.XPATH,"/html/body/div/div[1]/table/tbody/tr/td")

for element in dates:
    if element.text==Fixed_Date:
        element.click()
        break

driver.find_element(By.ID,"txt_comment").send_keys("I need a appoinment for checkup.please give me feedback email")
driver.find_element(By.ID,"btn-book-appointment").click()

Actual_title=driver.title
Expected_title="CURA Healthcare Service"
if Actual_title==Expected_title:
    print("Test Case Pass")
else:
    print("test Case Fail")

driver.close()



