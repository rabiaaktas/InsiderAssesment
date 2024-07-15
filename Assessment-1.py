from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def take_screenshot(driver, ss_counter):
    screenshot_path = f"{ss_counter}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")


def insider_automation_assessment(browser_name):
    ss_counter = 1
    try:
        if browser_name == 'chrome':
            driver = webdriver.Chrome()
        elif browser_name == 'firefox':
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        driver.maximize_window()
        driver.implicitly_wait(15)

        driver.get('https://useinsider.com/')
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@id='navbarDropdownMenuLink' and contains(text(),'Company')]"))
        )

        company_element = driver.find_element(By.XPATH, "//a[@id='navbarDropdownMenuLink' and contains(text(),'Company')]")
        company_element.click()

        career = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Careers'))
        )
        print("Drop-down menu opened")
        career.click()
        print("Clicked on Careers link")

        teams = driver.find_elements(By.XPATH, "//*[contains(@class,'job-item')]")
        print("Teams part is here")

        locations = driver.find_element(By.ID, "location-slider")
        driver.execute_script("arguments[0].scrollIntoView(true);", locations)
        print("Locations part is here")

        life = driver.find_element(By.CLASS_NAME, "elementor-swiper")
        driver.execute_script("arguments[0].scrollIntoView(true);", life)
        print("'Life at Insider' part is here")

    except Exception as e:
        take_screenshot(driver, ss_counter)
        ss_counter += 1
        print(f"Exception occurred: {str(e)}")

    finally:
        driver.quit()


if __name__ == '__main__':
    for browser_name in ['chrome','firefox']:
        insider_automation_assessment(browser_name)
