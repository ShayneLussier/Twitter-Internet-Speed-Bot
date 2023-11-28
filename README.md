# Twitter-Internet-Speed-Bot

Test your internet connection speed and tweet at your internet service provider if the speeds are lower than advertised.

## Usage

Users must enter their advertised download and upload speeds (in megabytes MB) as well as their X/twitter credentials.
```python
# ------------------------- CONSTANTS -------------------------- #
PROMISED_DOWN = 1500
PROMISED_UP = 1000
TWITTER_EMAIL = "_____"
TWITTER_PASSWORD = "_____"
```

In the `def tweet_at_provider(self):` function. Users can @mention their isp in the message. The current code tweets into the void!😄
```python
tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
compose_tweet.send_keys(tweet)
```

## Warning

If selenium crashes when launching a browser, it might be because it can't find the path to your webdriver in your directory. Fix with the following code:
```python
from selenium import webdriver

# Path to your WebDriver
driver_path = '/path/to/your/webdriver'
# Initialize the browser driver (for example, Chrome)
driver = webdriver.Chrome(executable_path=driver_path) 
```
