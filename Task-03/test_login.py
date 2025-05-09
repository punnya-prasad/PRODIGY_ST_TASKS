from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL and credentials
URL = "https://www.saucedemo.com/"
VALID_USERS = ["standard_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]
PASSWORD = "secret_sauce"

def setup_driver():
    driver = webdriver.Chrome()  # Add path if not in PATH
    driver.get(URL)
    driver.maximize_window()
    return driver

def login(driver, username, password):
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

def test_positive_login():
    for user in VALID_USERS:
        driver = setup_driver()
        login(driver, user, PASSWORD)
        assert "inventory" in driver.current_url
        print(f"[PASS] Valid login for {user}")
        driver.quit()

def test_locked_out_user():
    driver = setup_driver()
    login(driver, "locked_out_user", PASSWORD)
    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "locked out" in error.lower()
    print("[PASS] Locked out user test passed.")
    driver.quit()

def test_invalid_credentials():
    driver = setup_driver()
    login(driver, "invalid_user", "wrong_pass")
    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "epic sadface" in error.lower()
    print("[PASS] Invalid login credentials test passed.")
    driver.quit()

def test_empty_fields():
    driver = setup_driver()
    login(driver, "", "")
    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "username is required" in error.lower()
    print("[PASS] Empty field login test passed.")
    driver.quit()

# Run all tests
if __name__ == "__main__":
    test_positive_login()
    test_locked_out_user()
    test_invalid_credentials()
    test_empty_fields()
