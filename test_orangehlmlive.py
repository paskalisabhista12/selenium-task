from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome()
#     # driver.minimize_window()
#     yield driver
#     driver.quit()

def test_login_success():

    driver = webdriver.Chrome()

    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-text--h5"))
        )
    except:
        driver.quit()

    user_input = driver.find_elements(By.CLASS_NAME, "oxd-input")
    username_input = user_input[0]
    password_input = user_input[1]

    username_input.send_keys("Admin")
    password_input.send_keys("admin123")
    
    driver.find_element(By.CLASS_NAME, "oxd-button").click()    # Submit
    current_url = driver.current_url

    assert "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index" == current_url

    driver.quit()

@pytest.mark.parametrize("username, password", [
    ("Admin", "fun123"),
    ("admin", "admin"),
])

def test_login_failed(username, password):

    driver = webdriver.Chrome()

    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-text--h5"))
        )
    except:
        driver.quit()

    user_input = driver.find_elements(By.CLASS_NAME, "oxd-input")
    username_input = user_input[0]
    password_input = user_input[1]

    username_input.send_keys(username)
    password_input.send_keys(password)
    
    driver.find_element(By.CLASS_NAME, "oxd-button").click()    # Submit
    
    alert_text = "Invalid credentials"

    assert alert_text in driver.page_source

    driver.quit()

def test_admin_user_management_search():

    driver = webdriver.Chrome()

    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-text--h5"))
        )
    except:
        driver.quit()

    user_input = driver.find_elements(By.CLASS_NAME, "oxd-input")
    username_input = user_input[0]
    password_input = user_input[1]

    username_input.send_keys("Admin")
    password_input.send_keys("admin123")

    driver.find_element(By.CLASS_NAME, "oxd-button").click()    # Submit

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"))
        )
    except:
        driver.quit()

    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]"))
        )
    except:
        driver.quit()

    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]"))
        )
    except:
        driver.quit()

    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]").click()
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
    driver.implicitly_wait(2)
    current_url = driver.current_url

    assert "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers" == current_url

    driver.quit()

def test_add_user_success():
    driver = webdriver.Chrome()

    driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-text--h5"))
        )
    except:
        driver.quit()

    user_input = driver.find_elements(By.CLASS_NAME, "oxd-input")
    username_input = user_input[0]
    password_input = user_input[1]

    username_input.send_keys("Admin")
    password_input.send_keys("admin123")

    driver.find_element(By.CLASS_NAME, "oxd-button").click()    # Submit

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"))
        )
    except:
        driver.quit()

    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"))
        )
    except:
        driver.quit()

    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[1]/div[2]/i").click()
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click()
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[1]/div[2]/i").click()
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]").click()
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("a")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]").click()
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Orange")
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("password123")
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("password123")
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
    time.sleep(5)
    current_url = driver.current_url
    assert "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers" == current_url
    driver.quit()

def test_add_user_failed():
    driver = webdriver.Chrome()

    driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-text--h5"))
        )
    except:
        driver.quit()

    user_input = driver.find_elements(By.CLASS_NAME, "oxd-input")
    username_input = user_input[0]
    password_input = user_input[1]

    username_input.send_keys("Admin")
    password_input.send_keys("admin123")

    driver.find_element(By.CLASS_NAME, "oxd-button").click()    # Submit

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"))
        )
    except:
        driver.quit()

    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"))
        )
    except:
        driver.quit()

    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[1]/div[2]/i").click()
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click()
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[1]/div[2]/i").click()
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]").click()
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("a")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]").click()
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("test")
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("password123")
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("password123")
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
    time.sleep(3)
    current_url = driver.current_url
    assert "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser" == current_url
    driver.quit()