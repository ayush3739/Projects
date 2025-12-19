from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

wiki_link="https://en.wikipedia.org/wiki/Main_Page"

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
# add this option so Chrome starts maximized
chrome_options.add_argument("--start-maximized")

driver=webdriver.Chrome(options=chrome_options)
# ensure the window is maximized (works as a fallback)
driver.maximize_window()

#Navigate to wikipedia
driver.get(wiki_link)

article_count_element = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# click the element
# article_count_element.click()
# get the text after clicking if needed
article_count = article_count_element.text

all_portal=driver.find_element(By.LINK_TEXT,value="Content portals")
#all_portal.click()

# Find the search <input> by name (stable: name="search")
search = driver.find_element(By.NAME, "search")
search.send_keys("Python",Keys.ENTER)

#driver.close()