from selenium import webdriver

PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://jakhongirs.me")

# driver.close()  # will close current tab
driver.quit()  # will close entire browser

page_title = driver.title
print(page_title)
