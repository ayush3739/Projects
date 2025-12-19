from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os,time,requests
load_dotenv('.env')

web_link="https://appbrewery.github.io/Zillow-Clone/"
form_link=os.getenv('form_link')
profile_path="C:/Users/ayush/AppData/Local/Google/Chrome/User Data/profile 4/"

response=requests.get(web_link)
#print(response.text)
soup=BeautifulSoup(response.text,'html.parser')

links= [i.get('href') for i in soup.select(".StyledPropertyCardDataWrapper a")] 
print(f"there are {len(links)} in total")

address=[i.get_text() for i in soup.select('.StyledPropertyCardDataWrapper a address')]
address_list=[i.replace(" | ", " ").strip() for i in address]
print("address lists is created")

price=[i.get_text().replace("/mo", "").split("+")[0] for i in soup.select('.StyledPropertyCardDataWrapper span')]
print(price)
print("price list is created.")


print("fillig the form")
print(form_link)
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)


for i in range(len(links)):
    driver.get(form_link)
    time.sleep(1.5)
    in_address=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    in_address.send_keys(address_list[i])

    in_price=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    in_price.send_keys(price[i])

    in_link=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    in_link.send_keys(links[i])

    submit_button=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()

    print(f"filled the from {i+1} times")
    
    if (i+1)==len(links):
        print(f"filled the form with all the data and with Total Entries:: {i+1}/{len(links)}")
    
# def open_spreadsheet():
#     chrome_option=webdriver.ChromeOptions()
#     chrome_option.add_experimental_option('detach',True)
#     chrome_option.add_argument(f'--user-data-dir={profile_path}')

#     driver=webdriver.Chrome(options=chrome_option)
#     driver.get(os.getenv("spreadsheet"))
