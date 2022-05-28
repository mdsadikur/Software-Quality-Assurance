from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Md Sadikur Rahman\\Desktop\\SQA  Trainning\\Python\\pythonProject\\Driver\\chromedriver.exe")

driver.get("https://sso.teachable.com/secure/9521/identity/login/password?wizard_id=cpeWR-lw5exwGejigYLX4rQWdd-Dh44CIGZqWZSDf8GMODVuu727wno1q0FCiFLMXw0kRdYkOB49pySeAeRRow")

driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("mdsadikurrahman26@gmail.com")


driver.find_element(By.NAME,"password").send_keys("sadik3322")

driver.find_element(By.XPATH,"/html/body/main/div/form/div[4]/input").click()
