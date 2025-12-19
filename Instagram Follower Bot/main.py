from selenium import webdriver
from selenium.webdriver.common.by import By
    
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from dotenv import load_dotenv
import os,time
load_dotenv('.env')

username=os.getenv('user_name')
password=os.getenv('password') 
Search="codinganddecoding"

profile_path="Your chrome profile path"


class InstaFollower:
    def __init__(self):
        self.chrome_option=webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option('detach',True)
        self.chrome_option.add_argument(f'--user-data-dir={profile_path}')

        self.driver=webdriver.Chrome(options=self.chrome_option)
    
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')

        time.sleep(2)
        print(username)
        in_username=self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        in_username.send_keys(username)

        in_pass=self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        in_pass.send_keys(password)

        login_button=self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div[1]/div[3]/button')
        login_button.click()

        
        # Click "Not now" and ignore Save-login info prompt
        try:
            time.sleep(2.1)
            save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
            if save_login_prompt:
                save_login_prompt.click()
        except:
            pass

    
        
    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{Search}/")

        time.sleep(2)

        followers_button = self.driver.find_element(By.XPATH, "//a[contains(@href, '/followers')]")
        followers_button.click()
        time.sleep(4)
        self.modal=self.driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range(2):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.modal)
            time.sleep(2)
        ''' Another method for scrolling (put in a for loop)
        modal.send_keys(Keys.END)

        time.sleep(2)
        '''

    # Follow method
    def follow(self):
        time.sleep(1)
        follow_buttons = self.modal.find_elements(By.XPATH, ".//button[contains(., 'Follow')]")
        total=len(follow_buttons)
        followed=0
        following=0
        requested=0
        print(f"Found {total} follow buttons")  

        for button in follow_buttons:
            try:
                if button.text=="Following":
                    following+=1
                if button.text=="Requested":
                    requested+=1
                if button.text == "Follow":  
                    button.click()
                    time.sleep(0.5)
                    followed+=1
                         
            except (ElementClickInterceptedException):
                continue
        print(f"Followed: {followed}, Already following: {following}, Requested: {requested}\n Total:({followed+following+requested}/{total})")


object=InstaFollower()
#object.login()
object.find_followers()

object.follow()
