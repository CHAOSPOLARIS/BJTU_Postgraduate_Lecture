from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://XXXXXXXXXXXXXXXXXXX")
while 1==1:
    try:
        driver.find_element(By.CSS_SELECTOR, ".fbi_input").send_keys("Your name")
        driver.find_element(By.CSS_SELECTOR, ".wrapper").click()
        driver.find_element(By.CSS_SELECTOR, ".is_focus > .fbi_input").send_keys("Your student ID")
        driver.find_element(By.ID, "form_submit").click()
        if driver.find_element(By.ID, "form_submit"):
            print('success')
            break
    except:
        print('wait')
