from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math





try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    time.sleep(10)

    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)



    first_input = browser.find_element(By.ID, "answer")
    first_input.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()