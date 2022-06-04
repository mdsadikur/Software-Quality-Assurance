from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Md Sadikur Rahman\\Desktop\\SQA  Trainning\\Python\\pythonProject\\Driver\\chromedriver.exe")

class Screenshot():
    def test_screenshot(self):
        driver.maximize_window()
        driver.get("https://www.daraz.com.bd/")
        time.sleep(3)

        driver.get_screenshot_as_file("C:\\Users\\Md Sadikur Rahman\\Desktop\\SQA  Trainning\\Python\\pythonProject\\All Alart\\Screenshots\\daraz.png")
        driver.close()

test_obj = Screenshot()
test_obj.test_screenshot()


