from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver import ActionChains


serv_obj=Service("C:\Drivers\chromedriver_win3\chromedriver.exe")
driver=webdriver.Chrome("service=serv_obj")

driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(10)
my_alert=driver.switch_to.alert
my_alert.accept()