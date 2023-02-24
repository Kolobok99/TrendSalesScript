import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import consts
from .go_to_next_page import go_to_next_page


def accept_cookie(browser, wait_time):
    btn_accept_cookie = WebDriverWait(browser, wait_time).until(
        EC.element_to_be_clickable((By.ID, consts.ID_BTN_ACCEPT_COOKIE)))
    btn_accept_cookie.click()


def login(browser, wait_time, login, password):
    btn_to_login = WebDriverWait(browser, wait_time).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, consts.SELECTOR_BTN_TO_LOGIN)))
    btn_to_login.click()

    WebDriverWait(browser, wait_time).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, consts.SELECTOR_FORM_LOGIN)))

    login_form = browser.find_elements(By.CSS_SELECTOR, consts.SELECTOR_FORM_LOGIN)
    login_form[0].send_keys(login)
    login_form[1].send_keys(password)

    btn_submit_login = browser.find_element(By.CSS_SELECTOR, consts.SELECTOR_BTN_SUBMIT_LOGIN)
    btn_submit_login.click()




def photo_adding(browser, wait_time, photos_path: list):
    first_photo = photos_path.pop(0)
    btn_to_add_photo = WebDriverWait(browser, wait_time).until(
        EC.element_to_be_clickable(((By.CSS_SELECTOR, consts.SELECTOR_BTN_TO_ADD_FIRST_PHOTO))))
    btn_to_add_photo.click()

    input_photo = WebDriverWait(browser, wait_time).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, consts.SELECTOR_INPUT_FIRST_PHOTO)))

    input_photo.send_keys(first_photo)

    for photo in photos_path:
        btn_to_add_others_photo = WebDriverWait(browser, wait_time).until(
            EC.element_to_be_clickable(((By.CSS_SELECTOR, consts.SELECTOR_BTN_ADD_OTHERS_PHOTO))))
        btn_to_add_others_photo.click()

        WebDriverWait(browser, wait_time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, consts.SELECTOR_INPUT_FIRST_PHOTO)))
        input_next_photo = browser.find_elements(By.CSS_SELECTOR, consts.SELECTOR_INPUT_FIRST_PHOTO)
        input_next_photo[1].send_keys(photo)

        time.sleep(1)

    go_to_next_page(browser)


def sex_adding(browser, wait_time, sex):
    xpath_sex_btn = consts.get_xpath_btn_sex(sex)
    who_is_btn = WebDriverWait(browser, wait_time).until(EC.element_to_be_clickable((By.XPATH, xpath_sex_btn)))
    who_is_btn.click()
    time.sleep(1)

    go_to_next_page(browser)


def size_adding(browser, wait_time, size):
    xpath_btn_size = consts.get_xpath_btn_size(size)
    btn_size = WebDriverWait(browser, wait_time).until(EC.presence_of_element_located((By.XPATH, xpath_btn_size)))
    btn_size.click()

    go_to_next_page(browser)


def brand_adding(browser, wait_time, brand):
    find_brand_input = WebDriverWait(browser, wait_time) \
        .until(EC.presence_of_element_located((By.CSS_SELECTOR, consts.SELECTOR_INPUT_FIND_BRAND)))
    find_brand_input.send_keys(Keys.CONTROL + "A")
    for b in brand:
        find_brand_input.send_keys(b)
        time.sleep(0.3)
    # time.sleep(10)
    find_brand_input.send_keys(Keys.ESCAPE)

    xpath_brand_li_btn = consts.get_xpath_btn_li_brand(brand)
    brand_li = WebDriverWait(browser, wait_time).until(
        EC.presence_of_element_located((By.XPATH, xpath_brand_li_btn)))
    brand_li.click()

    go_to_next_page(browser)


def color_adding(browser, wait_time, color):
    xpath_btn_color = consts.get_xpath_btn_color(color)
    btn_color = WebDriverWait(browser, wait_time).until(EC.presence_of_element_located((By.XPATH, xpath_btn_color)))
    btn_color.click()

    go_to_next_page(browser)


def shabbiness_adding(browser,wait_time, shabbiness):
    xpath_btn_gender_shabbiness = consts.get_btn_shabbiness(shabbiness)
    btn_shabbiness = WebDriverWait(browser, wait_time).until(
        EC.presence_of_element_located((By.XPATH, xpath_btn_gender_shabbiness)))
    btn_shabbiness.click()

    go_to_next_page(browser)


def description_adding(browser, wait_time, description):
    description_textarea = WebDriverWait(browser, wait_time).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, consts.SELECTOR_TEXT_AREA_DESCRIPTION)))

    description_textarea.click()
    description_textarea.send_keys(description)

    go_to_next_page(browser)


def price_adding(browser, wait_time, your_price, first_price):
    WebDriverWait(browser, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, consts.SELECTOR_FORM_PRICES)))

    input_prices = browser.find_elements(By.CSS_SELECTOR, consts.SELECTOR_FORM_PRICES)

    input_prices[0].send_keys(your_price)
    input_prices[1].send_keys(first_price)

    go_to_next_page(browser)


def sales_method_adding(browser, wait_time, methods):
    if len(methods) == 2:
        btn_sales_method_pick_up = WebDriverWait(browser, wait_time).until(
            EC.presence_of_element_located((By.XPATH, consts.XPATH_BTN_SALES_METHOD_PICK_UP_BTN)))
        btn_sales_method_pick_up.click()
    elif methods[0] == 'PICK_UP':
        btn_sales_method_ask = WebDriverWait(browser, wait_time).until(
            EC.presence_of_element_located((By.XPATH, consts.XPATH_BTN_SALES_METHOD_ASK)))
        btn_sales_method_ask.click()
    elif methods[0] == 'AKS':
        pass
    go_to_next_page(browser)


def data_confirming(browser, wait_time,):
    btn_confirm_selling = WebDriverWait(browser, wait_time).until(
        EC.presence_of_element_located((By.XPATH, consts.XPATH_BTN_CONFIRM_SALE)))
    btn_confirm_selling.click()


def territorial_position_adding(browser, wait_time, address, post_number, by):

    address_input = WebDriverWait(browser, wait_time).until(
        EC.presence_of_element_located((By.XPATH, consts.XPATH_INPUT_ADDRESS)))
    post_number_input = WebDriverWait(browser, wait_time).until(
        EC.presence_of_element_located((By.XPATH, consts.XPATH_INPUT_POST_NUMBER)))
    by_input = WebDriverWait(browser, wait_time).until(EC.presence_of_element_located((By.XPATH, consts.XPATH_INPUT_BY)))

    address_input.send_keys(Keys.CONTROL + "A")
    address_input.send_keys(address)

    post_number_input.send_keys(Keys.CONTROL + "A")
    post_number_input.send_keys(post_number)
    #
    by_input.send_keys(Keys.CONTROL + "A")
    by_input.send_keys(by)


def sales_confirming(browser, wait_time):
    gem_span_btn = WebDriverWait(browser, wait_time).until(
        EC.presence_of_element_located((By.XPATH, consts.XPATH_SPAN_BTN_GEM)))
    gem_span_btn.click()