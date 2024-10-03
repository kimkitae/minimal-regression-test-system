import pytest
from appium import webdriver
import allure

# 테스트 케이스 로드
def load_test_cases():
    with open('test_cases.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]

# WebDriver 설정
@pytest.fixture(scope="module")
def driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",  # Appium 2.0에서는 명시적으로 필요
        "appPackage": "com.example.app",
        "appActivity": "com.example.app.MainActivity"
    }
    driver = webdriver.Remote('http://appium:4723', desired_caps)
    yield driver
    driver.quit()

# 테스트 함수 생성
@pytest.mark.parametrize('test_case', load_test_cases())
def test_app(driver, test_case):
    with allure.step(test_case):
        # 각 테스트 케이스에 대한 테스트 로직을 구현합니다.
        assert driver.find_element_by_id('com.example.app:id/main_view').is_displayed()
