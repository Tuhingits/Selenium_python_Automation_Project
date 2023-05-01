import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.implicitly_wait(30)

driver.get("http://frontend.iou.ac/")


driver.find_element(By.XPATH, "//div/div[2]/div/button[2]").click()

driver.find_element(By.XPATH, "//div/div[4]/div/div/div/div/div[1]/button[2]").click()

# Enter credential for reg
driver.find_element(By.ID, "email").send_keys("test12@gmail.com")
driver.find_element(By.ID, "id_password").send_keys("123456")
driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div/div/div/div/div[3]/form/div[3]/div/input").send_keys("123456")
driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div/div/div/div/div[3]/form/button").click()
driver.find_element(By.ID, "otp").send_keys("1234")
driver.find_element(By.ID, "otp").click()
