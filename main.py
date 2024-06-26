from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math





try:
    link = ("http://suninjuly.github.io/explicit_wait2.html")
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    def calc(x):
       return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)


    first_input = browser.find_element(By.ID, "answer")
    first_input.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

