from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
import time

USERNAME = YOUR_USERNAME
PASSWORD = YOUR_PASSWORD
DESIRED_JOB = YOUR_DESIRED_JOB


#To keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.linkedin.com/feed/")

#Sign in
sign_in_link = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_link.click()

#Entering Username and password
username = driver.find_element(By.ID, "username")
username.send_keys(USERNAME)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)

#Signed in
sing_in_button = driver.find_element(By.CLASS_NAME, "login__form_action_container")
sing_in_button.click()

#CAPTCHA - Solve it manually
# captcha_done = input("Captcha done ?\nType Y or N: ").lower()
# time.sleep(5)

#Search and apply for the jobs
# if captcha_done == "y":
time.sleep(20)
try:

    jobs_icon = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]')
    jobs_icon.click()
    time.sleep(2)

    #Search for the desired job
    jobs_search_box = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
    jobs_search_box.send_keys(DESIRED_JOB)
    time.sleep(4)
    jobs_search_box.send_keys(Keys.ENTER)

    #Filter the easy applications
    time.sleep(4)
    filters = driver.find_element(By.CSS_SELECTOR,".search-reusables__all-filters-pill-button")
    filters.click()
    time.sleep(2)
    easy_apply_button = driver.find_element(By.CLASS_NAME, "artdeco-toggle")
    easy_apply_button.click()


    # Get the list of all desired jobs
    def get_jobs():
        return driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container li")

    #Apply for the job
    count = 0
    for i in range(15):

        job = get_jobs()[count]
        driver.execute_script("arguments[0].scrollIntoView();", job)
        job.click()
        time.sleep(3)
        job_save_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button')
        job_save_button.click()
        count += 5

except NoSuchElementException:
        print("Element not found .\nMay be the page have not loaded completely yet.")


