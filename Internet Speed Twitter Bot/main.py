from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
from dotenv import load_dotenv
import os,time
load_dotenv('.env')

user_email=os.getenv('user_id')
user_pass=os.getenv('user_pass')
PROMISED_DOWN=50
PROMISED_UP=10


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        # ✅ Use the working subprofile "Profile 4\\Default"
        profile_path = r"C:\Users\ayush\AppData\Local\Google\Chrome\User Data\Profile 4\Default"
        self.chrome_options.add_argument(f"--user-data-dir={profile_path}")

        # Initialize Chrome WebDriver
        self.driver = webdriver.Chrome(options=self.chrome_options)

        # Internet speed placeholders
        self.down =0
        self.Up =0
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(4)
        # accept_button = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        # accept_button.click()

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(45)
        self.down= float(self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.Up= float(self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

        print("down: ",self.down)
        print("Up: ",self.Up)    

    def tweet_at_provider(self):
        print("opening the Tweeter Website ")
        self.driver.get("https://x.com/home")
        time.sleep(5)

        # username_fill = WebDriverWait(self.driver, 10).until(
        #     ec.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))
        # )
        # username_fill.send_keys(user_email)
        post_fill=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet=f"Hey Internet Provider, why is my internet speed {self.down}down/{self.Up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        post_fill.send_keys(tweet)

        time.sleep(2)
        post_button=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post_button.click()
        print("----tweeted the post----")

        # time.sleep(3)
        # self.driver.close()
    def delete_the_post(self):
        try:
            print("deleting the post ")
            time.sleep(7)
            option=WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[5]/section/div/div/div[2]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div/div/button/div/div')))
            option.click()

            time.sleep(2)
            delete_button=self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div[1]/div[2]')
            delete_button.click()

            time.sleep(2)
            del_popup=self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/button[1]/div/span/span')
            del_popup.click()
        except(KeyError):
            print(f"error coming{KeyError}")

Twitter_bot=InternetSpeedTwitterBot() 
Twitter_bot.get_internet_speed()
if PROMISED_DOWN>Twitter_bot.down or PROMISED_UP>Twitter_bot.Up:
    Twitter_bot.tweet_at_provider()
    #Twitter_bot.delete_the_post()
