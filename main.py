import traceback

from selenium import webdriver

import parametrs
from services import steps

URL = 'https://trendsales.dk/sell'


def sales_scrapper(open_browser=True, save_sale=False, tries=1, wait_time=10):
    flag = False
    for t in range(tries):
        try:
            if not open_browser:
                options = webdriver.ChromeOptions()
                options.add_argument('headless')
                browser = webdriver.Chrome(options=options)
            else:
                browser = webdriver.Chrome()
            browser.get(url=URL)

            steps.accept_cookie(browser,wait_time)

            steps.login(browser, wait_time, parametrs.LOGIN, parametrs.PASSWORD)

            steps.photo_adding(browser, wait_time, [parametrs.FIRST_PHOTO_PATH, parametrs.SECOND_PHOTO_PATH, parametrs.THIRD_PHOTO_PATH])

            steps.sex_adding(browser, wait_time, parametrs.SEX)

            steps.size_adding(browser, wait_time, parametrs.SIZE)

            for i in range(5):
                try:
                    steps.brand_adding(browser, wait_time, parametrs.BRAND)
                    brand_flag = True
                except Exception as e:
                    brand_flag = False
                if brand_flag:
                    break

            steps.color_adding(browser, wait_time, parametrs.COLOR)

            steps.shabbiness_adding(browser, wait_time, parametrs.SHABBINESS)

            steps.description_adding(browser, wait_time, parametrs.DESCRIPTION)

            steps.price_adding(browser, wait_time, parametrs.FIRST_PRICE, parametrs.YOUR_PRICE)

            steps.sales_method_adding(browser, wait_time, parametrs.SALES_METHODS)

            steps.data_confirming(browser, wait_time)

            steps.territorial_position_adding(browser, wait_time, parametrs.ADDRESS, parametrs.POST_NUMBER, parametrs.BY)

            if save_sale:
                steps.sales_confirming(browser, wait_time)

            flag = True
        except Exception:
            print(f"attempt № {t} failed with error:")
            print(traceback.format_exc())
        finally:
            browser.quit()
        if flag:
            print(f'attempt № {t} completed successfully')
            break

sales_scrapper()