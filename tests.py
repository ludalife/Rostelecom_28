import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from settings import valid_password, valid_email, valid_account, valid_phone
from conftest import valid_phone

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(r"C:\Users\User\Downloads\chromedriver.exe")
    pytest.driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=9328d728-dc48-451d-82b6-676f9b041ee6&theme&auth_type')

    yield

    pytest.driver.quit()


# №1 Вход на сайт
@pytest.mark.parametrize('phone', valid_phone)
def test_valid_auth(phone, password=valid_password):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'kc-login').click()

# №2 Невалидный номера телефона
def test_invalid_phone():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    pytest.driver.find_element(By.ID, 'username').send_keys('89214455577')
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()

# №3 Невалидный пароль
def test_invalid_password():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'password').send_keys('lkkkkliilss')
    pytest.driver.find_element(By.ID, 'kc-login').click()

# №4 Yевалиднsq логин
def test_invalid_login():
    WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-login')))
    pytest.driver.find_element(By.ID, 't-btn-tab-login').send_keys('rtkid_167837800312')
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()


# №5 Вход черезкнопку enter
def test_log_in_by_enter_btn():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    login = pytest.driver.find_element(By.ID, 'username')
    login.clear()
    login.send_keys(valid_email)
    password = pytest.driver.find_element(By.ID, 'password')
    password.clear()
    password.send_keys(valid_password)
    password.send_keys(Keys.RETURN)


# №6 Кнопка "Забыл пароль" 
def test_forgot_password_btn():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'forgot_password')))
    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'reset').click()

# №7 Номер лицевого счета в поле email
def test_email_btn():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_account)
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()

# №8 Номер лицевого счета в поле login
def test_login_btn():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-login')))
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_account)
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()

# №9 Кнопка "Лицевой счет"
def test_personal_account_btn():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls')))
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_account)
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()


# №10 Некорректный логина, превышающий допустимую длину 
def test_login_long_line():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-login')))
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.find_element(By.ID, 'username').send_keys('kkkkkkkkkkkkkkkkkkkkjgggggsdlklklklklklklklklklklklkllkjhfffffffffffffffdddddddttt')
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()



# №11 Некорректный логин 
def test_login_not_ASCII_symbols():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-login')))
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.find_element(By.ID, 'username').send_keys('{|\\/*()-_=+`~?"№;!@#$%^&:[]}')
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()


# №12 Лицевй счет китайскими иероглифами
def test_account_chinese_chars():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-login')))
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.find_element(By.ID, 'username').send_keys('的之大来以个中上们一是不了人我在有他这为')
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()


# №13 Кнопка "Зарегистрироваться"
def test_registration_btn():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    pytest.driver.find_element(By.ID, 'kc-register').click()
    pytest.driver.find_element(By.NAME, 'firstName').send_keys('Людмила')
    pytest.driver.find_element(By.NAME, 'lastName').send_keys('Плесовских')
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input').send_keys('Екатеринбург')
    pytest.driver.find_element(By.ID, 'address').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    pytest.driver.find_element(By.NAME, 'register').click()


# №14 Поле "Запомнить меня"
def test_check_mark():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/label/span[1]').click()
    pytest.driver.find_element(By.ID, 'kc-login').click()


# 15 Кнопка "Вернуться назад"
def test_reset_back_btn():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'forgot_password')))
    pytest.driver.find_element(By.ID, 'forgot_password').click()
    # pytest.driver.find_element(By.ID, 'username').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'reset-back').click()

