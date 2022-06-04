from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Md Sadikur Rahman\\Desktop\\SQA  Trainning\\Python\\pythonProject\\Driver\\chromedriver.exe")

class MouseHover():
    def test_hover(self):
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/hovers")
        time.sleep(3)

        user1 = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/img')

        actions = ActionChains(driver)
        actions.move_to_element(user1).perform()
        time.sleep(3)
        driver.close()

object = MouseHover()
object.test_hover()