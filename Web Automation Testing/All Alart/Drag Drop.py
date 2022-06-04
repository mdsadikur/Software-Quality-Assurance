from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Md Sadikur Rahman\\Desktop\\SQA  Trainning\\Python\\pythonProject\\Driver\\chromedriver.exe")

class DragDrope():
    def test_dragdrop(self):
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        time.sleep(3)

        fromElement = driver.find_element(By.XPATH,'//*[@id="column-a"]')
        toElement = driver.find_element(By.XPATH,'//*[@id="column-b"]')

        action = ActionChains(driver)
        action.drag_and_drop(fromElement,toElement).perform()
        time.sleep(2)
        driver.close()

object = DragDrope()
object.test_dragdrop()
