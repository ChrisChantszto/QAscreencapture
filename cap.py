from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = Firefox()

driver.set_window_size(1300, 800)

driver.get(url)
url = ""
time.sleep(10)
driver.save_screenshot(#test.png)
print("hi")

actions = []
actions = driver.find_elements(By.CLASS_NAME, #string classname )

count = 0
for e in actions:
    print(e)
    e.click()
    time.sleep(5)
    print("test" + str(count) + ".png")
    driver.save_screenshot("test" + str(count) + ".png")
    count += 1
