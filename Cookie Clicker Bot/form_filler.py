from selenium import webdriver
from selenium.webdriver.common.by import By

challenge_link="http://secure-retreat-92358.herokuapp.com/"

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver=webdriver.Chrome(options=chrome_options)
driver.get(challenge_link)

f_name=driver.find_element(By.NAME,value="fName")
L_name=driver.find_element(By.NAME,value="lName")
Email=driver.find_element(By.NAME,value="email")


f_name.send_keys("Hexon")
L_name.send_keys("Param")
Email.send_keys("Fakeemail@wiki.com")

Button=driver.find_element(By.CSS_SELECTOR,value="form button")
Button.click()