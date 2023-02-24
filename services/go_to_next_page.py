from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import consts


def go_to_next_page(browser):
    btn_to_next_page = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, consts.SELECTOR_BTN_TO_NEXT_PAGE)))
    btn_to_next_page.click()
