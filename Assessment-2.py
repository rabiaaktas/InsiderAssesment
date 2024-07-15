from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def take_screenshot(driver, ss_counter):
    screenshot_path = f"{ss_counter}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

def insiderAutomationAssestment(browser_name):
    ss_counter = 1
    try:
        if browser_name == 'chrome':
            driver = webdriver.Chrome()
        elif browser_name == 'firefox':
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        
        driver.maximize_window()
        driver.get("https://useinsider.com/careers/quality-assurance/")

        allJobs = driver.find_element(By.LINK_TEXT, 'See all QA jobs')
        allJobs.click()

        WebDriverWait(driver,20).until(
            EC.presence_of_element_located((By.XPATH, '//span[@title="Quality Assurance"]'))
        )

        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "filter-by-location"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", select_element)

        dropdown_element = driver.find_element(By.ID,"select2-filter-by-location-container")
        time.sleep(5)
        dropdown_element.click()
        time.sleep(5)

        dropDownMenu = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, 'select2-filter-by-location-results'))
        )
        if dropDownMenu.is_displayed() and dropDownMenu.is_enabled():
            clickOnOption = driver.find_element(By.XPATH,"//li[contains(@id, 'Istanbul, Turkey')]")
            driver.execute_script("arguments[0].focus();", clickOnOption)
            clickOnOption.click()
            textTest = driver.find_element(By.ID,"select2-filter-by-location-container").text
            print(textTest)
            time.sleep(5)

        position_list = driver.find_element(By.ID,'jobs-list')
        driver.execute_script("arguments[0].scrollIntoView(true);", position_list)

        job_posts = driver.find_elements(By.XPATH,"//*[contains(@class,'position-list-item-wrapper')]")
        print("Job Post Count:: " , len(job_posts))
        action_chains = ActionChains(driver)

        for index in range(1, len(job_posts) + 1):

            job_post = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'position-list-item-wrapper')])[" + str(index) + "]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", job_post)
            action_chains.move_to_element(job_post).perform()

            role_button = driver.find_element(By.XPATH, "(//a[text()='View Role'])[" + str(index) + "]")            
            role_button.click()
            
            time.sleep(5)  
            
            driver.switch_to.window(driver.window_handles[1])
            current_url = driver.current_url
            print("Current URL:", current_url)
            
            domain = current_url.split('/')[2]
            print(domain)

            if domain == "job.levers.co":
                print("Job application page opened successfully")
            else:
                driver.save_screenshot("application_page_not_opened.png")

            driver.close()
            driver.switch_to.window(driver.window_handles[0])
      
    except Exception as e:
        take_screenshot(driver, ss_counter)
        ss_counter += 1
        print(f"Exception occurred: {str(e)}")

    finally:
        driver.quit()

if __name__ == '__main__':
    for browsername in ['chrome','firefox']:
        insiderAutomationAssestment(browsername)

    
    




