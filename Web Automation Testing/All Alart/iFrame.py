from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Md Sadikur Rahman\\Desktop\\SQA  Trainning\\Python\\pythonProject\\Driver\\chromedriver.exe")

class SwitchIframe():
    def iframe(self):
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/iframe")
        time.sleep(3)

        driver.switch_to.frame('mce_0_ifr')
        paragraph = driver.find_element(By.XPATH,'//*[@id="tinymce"]/p')
        paragraph.clear()
        paragraph.send_keys("Python selenium iframe test automation")
        time.sleep(3)
        driver.close()

test_obj = SwitchIframe()
test_obj.iframe()
