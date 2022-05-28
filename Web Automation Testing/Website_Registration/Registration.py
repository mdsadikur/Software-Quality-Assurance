from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Md Sadikur Rahman\\Desktop\\SQA  Trainning\\Python\\pythonProject\\Driver\\chromedriver.exe")

driver.get("https://sso.teachable.com/secure/9521/identity/sign_up/email")

driver.maximize_window()

driver.find_element(By.ID,"user_name").send_keys("Md Sadikur Rahman")
driver.find_element(By.NAME,"email").send_keys("sadikur.rahman3168@gmail.com")
driver.find_element(By.NAME,"password").send_keys("sadik3322")
#driver.find_element((By.XPATH,'//*[@id="allow_marketing_emails"]'))
driver.find_element(By.XPATH,"/html/body/main/div/form/div[6]/input").click()
