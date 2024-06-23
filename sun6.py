from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.select import Select

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    time.sleep(10)
    browser.get(link)


    a = browser.find_element(By.ID, "num1")
    a1 = a.text


    b = browser.find_element(By.ID, "num2")
    b1 = b.text

    sum = (int(a1) + int(b1))

    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(str(sum))



    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()