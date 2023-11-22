from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ------------------------- CONSTANTS -------------------------- #
PROMISED_DOWN = 1500
PROMISED_UP = 1000
TWITTER_EMAIL = "_____"
TWITTER_PASSWORD = "_____"


# ------------------------- SELENIUM SETUP -------------------------- #

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# ------------------------- CLASS SETUP -------------------------- #


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(5)
        start_test = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_test.click()

        # timeout until speed test is over
        time.sleep(45)
        download_speed = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span',
        ).text
        upload_speed = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span',
        ).text
        print(f"down: {download_speed}, up: {upload_speed}")

    def tweet_at_provider(self):
        # click log in button
        self.driver.get("https://twitter.com/i/flow/signup")
        time.sleep(5)

        log_in = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[7]/span[2]/span/span',
        )
        log_in.click()

        # input email in textbox
        time.sleep(2)
        email_box = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input',
        )
        email_box.send_keys(TWITTER_EMAIL)
        email_box.send_keys(Keys.ENTER)

        # enter password in textbox
        time.sleep(2)
        password_box = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input',
        )
        password_box.send_keys(TWITTER_PASSWORD)
        password_box.send_keys(Keys.ENTER)

        # compose tweet
        time.sleep(5)
        compose_tweet = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a',
        )
        compose_tweet.click()

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        compose_tweet.send_keys(tweet)
        time.sleep(3)

        post_tweet = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div/div/span/span',
        )
        post_tweet.click()

        time.sleep(3)
        self.driver.quit()
