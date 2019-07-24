from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

button = browser.find_element_by_tag_name("button")

WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000")
    )

button.click()

num = browser.find_element_by_id("input_value").text
y = calc(num)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

button = browser.find_element_by_id("solve")
button.click()