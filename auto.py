from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

search = input("Enter a word:")
# Initialize the web driver and navigate to the YouTube homepage
driver = webdriver.Chrome()
# Find the search box and enter the keyword
driver.get("https://www.youtube.com")
search_box = driver.find_element(By.NAME, "search_query")  # Find the search box
search_box.send_keys(search)
search_box.send_keys(Keys.RETURN)

# Wait for the page to load and display the search results
time.sleep(20)

# Print the titles of the top 10 videos in the search results
videos = driver.find_elements(By.CSS_SELECTOR, ".text-wrapper.style-scope.ytd-video-renderer")
# for video in videos[:10]:
#     print(video.get_attribute("title"))

# Close the web driver
driver.quit()
