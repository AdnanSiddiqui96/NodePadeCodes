from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the YouTube website
driver.get("https://www.youtube.com/")

# Find the search bar and enter the search query
search_bar = driver.find_element_by_name("search_query")
search_bar.send_keys("Python Programming")
search_bar.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(5)

# Find the first search result and click on it
video_link = driver.find_element_by_xpath('//*[@id="contents"]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a')
video_link.click()

# Wait for the video to load
time.sleep(5)

# Play the video
play_button = driver.find_element_by_xpath('//*[@id="movie_player"]/div[30]/div[2]/div[1]/button')
play_button.click()
