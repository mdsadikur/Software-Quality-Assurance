from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Md Sadikur Rahman\\Desktop\\SQA  Trainning\\Python\\pythonProject\\Driver\\chromedriver.exe")

class SwitchWindow():
    def test(self):
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/windows")

        time.sleep(3)
        parent_handle=driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH,'//*[@id="content"]/div/a').click()
        all_handles = driver.window_handles
        print(all_handles)
        time.sleep(3)

        for child_handle in all_handles:
            if child_handle not in parent_handle:
                driver.switch_to.window(child_handle)
                print(driver.title)
                driver.close()
                driver.quit()

test_object=SwitchWindow()
test_object.test()