
# Подтверждение куков
ID_BTN_ACCEPT_COOKIE = 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll'
SELECTOR_BTN_TO_LOGIN = '.btn.btn--white.btn--no-shadow.login__btn > span'

# Авторизация
SELECTOR_FORM_LOGIN = '.outlinedInputField__input'
SELECTOR_BTN_SUBMIT_LOGIN = '.login__btn > span'

SELECTOR_AUTH_ERROR = '.validationErrText'

# Кнопка перехода к следующей стр. добавления товара
SELECTOR_BTN_TO_NEXT_PAGE = '.btn-continue'

# Добавление фотографий
SELECTOR_BTN_TO_ADD_FIRST_PHOTO = '.sell-pictures__btn'
SELECTOR_INPUT_FIRST_PHOTO = "input[type='file']"
SELECTOR_BTN_ADD_OTHERS_PHOTO = '.image-placeholder.image-placeholder--small.image-placeholder--media'

# Добавление пола
def get_xpath_btn_sex(sex):
    XPATH_BTN_WHO_IS = f"//span[text()='{sex}']"
    return XPATH_BTN_WHO_IS

# Добавление размера
def get_xpath_btn_size(size):
    XPATH_BTN_SIZE = f"//span[text()='{size}']"
    return XPATH_BTN_SIZE


# Добавление брэнда
SELECTOR_INPUT_FIND_BRAND = 'input.outlinedsearchselectfield__input'


def get_xpath_btn_li_brand(brand):
    XPATH_BTN_LI_BRAND = f"//li[text()='{brand}']"
    return XPATH_BTN_LI_BRAND


# Добавление цвета
def get_xpath_btn_color(color):
    XPATH_BTN_COLOR = f"//span[text()='{color}']//preceding-sibling::button"
    return XPATH_BTN_COLOR


# Добавление поношенности
def get_btn_shabbiness(shabbiness):
    XPATH_BTN_SHABBINESS = f"//div[text()='{shabbiness}']//following-sibling::div[contains(@class, 'svgicon')]"
    return XPATH_BTN_SHABBINESS

# Добавление описания
SELECTOR_TEXT_AREA_DESCRIPTION = '.outlinedInputField__textarea'

# Добавление цены
SELECTOR_FORM_PRICES = '.outlinedInputField__input'


# Способ продажи
ask = 'Fragt'
pick_up = 'Afhentning'

def get_sales_method_btn(method):
    XPATH_BTN_SALES_METHOD = f"//span[text()='{method}']//following-sibling::span//child::label[contains(@class, 'toggle-input__label')]"
    return XPATH_BTN_SALES_METHOD

XPATH_BTN_SALES_METHOD_ASK = get_sales_method_btn(ask)
XPATH_BTN_SALES_METHOD_PICK_UP_BTN = get_sales_method_btn(pick_up)

# Подтверждение данных продажи
XPATH_BTN_CONFIRM_SALE = "//button[text()='Opret annonce']"

# Ввод территориальных данных
XPATH_INPUT_ADDRESS = "//div[text()='Adresse*']//following-sibling::input"
XPATH_INPUT_POST_NUMBER = "//div[text()='Postnummer *']//following-sibling::input"
XPATH_INPUT_BY = "//div[text()='By*']//following-sibling::input"

# Подтверждение территориальных данных
XPATH_SPAN_BTN_GEM = "//span[text()='Gem']"
