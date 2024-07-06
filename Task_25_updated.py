from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = r"D:\Python_HW\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the IMDB search page
def load_page(url):
    driver.get(url)
    driver.maximize_window()

##Expand the section##
def expand_page():
    expand = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-testid='adv-search-expand-all']")))
    actions = ActionChains(driver)
    actions.click(expand)
    actions.perform()

##Input for Name##
def name_input(name):
    driver.implicitly_wait(20)
    name_input = driver.find_element(By.CSS_SELECTOR, "input[name='name-text-input']")
    name_input.send_keys(name)

#Input for Birthdate##
def birthdate_input(startdate,enddate):
    driver.implicitly_wait(20)
    birth_date_start_input=driver.find_element(By.CSS_SELECTOR,"input[name='birth-date-start-input']")
    birth_date_start_input.send_keys(startdate)
    birth_date_end_input=driver.find_element(By.CSS_SELECTOR,"input[name='birth-date-end-input']")
    birth_date_end_input.send_keys(enddate)

#Input for Birthday##
def birthday_input(day):
    driver.implicitly_wait(20)
    birthday_input = driver.find_element(By.CSS_SELECTOR, "input[name='birthday-input']")
    actions = ActionChains(driver)
    actions.send_keys_to_element(birthday_input, day)
    actions.send_keys(Keys.RETURN)
    actions.perform()

##Input for Awards##
def award():
    driver.implicitly_wait(20)
    awards_input = driver.find_element(By.CSS_SELECTOR,"button[data-testid='test-chip-id-oscar_best_supporting_actress_winners']")
    actions = ActionChains(driver)
    actions.click(awards_input)
    actions.perform()

##Input for Topics##
def birth_place(birthplace):
    driver.implicitly_wait(20)
    topic_dropdown = driver.find_element(By.ID,"within-topic-dropdown-id")
    actions = ActionChains(driver)
    actions.click(topic_dropdown)
    actions.perform()
    selectoption = Select(topic_dropdown)
    selectoption.select_by_value(birthplace)

##Input for topictext##
def topic_text(country):
    topic_text_input=driver.find_element(By.CSS_SELECTOR,"input[name='within-topic-input']")
    actions = ActionChains(driver)
    actions.send_keys_to_element(topic_text_input,country)
    actions.send_keys(Keys.RETURN)
    actions.perform()

##Input for DeathDate##
def death_date(deathdate1,deathdate2):
    driver.implicitly_wait(20)
    death_date_start_input=driver.find_element(By.CSS_SELECTOR,"input[name='death-date-start-input']")
    death_date_start_input.send_keys(deathdate1)
    death_date_end_input=driver.find_element(By.CSS_SELECTOR,"input[name='death-date-end-input']")
    death_date_end_input.send_keys(deathdate2)

def gender_input():
    driver.implicitly_wait(20)
    gender_input = driver.find_element(By.CSS_SELECTOR, "button[data-testid='test-chip-id-FEMALE']")
    actions = ActionChains(driver)
    actions.click(gender_input)
    actions.perform()

##Input for Credit##
def credit_input(credit):
    driver.implicitly_wait(20)
    credit_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='autosuggest-input-test-id-filmography']")
    actions = ActionChains(driver)
    actions.click(credit_input)
    actions.send_keys_to_element(credit_input, credit)
    actions.pause(2)
    actions.send_keys(Keys.DOWN)
    actions.pause(2)
    actions.send_keys(Keys.ENTER)
    actions.perform()

##Input for adults##
def adult_name():
    adultnames_input=driver.find_element(By.CSS_SELECTOR,"input[id='include-adult-names']")
    actions = ActionChains(driver)
    actions.click(adultnames_input)
    actions.perform()

##See Results##
def seeresults():
    seeresults=driver.find_element(By.CSS_SELECTOR,"button[data-testid='adv-search-get-results']")
    seeresults.click()


def search_inputs():
    load_page("https://www.imdb.com/search/name/")
    expand_page()
    name_input("Audrey")
    birthdate_input("14071990","14072000")
    birthday_input("06-14")
    award()
    birth_place("BIRTH_PLACE")
    topic_text("United States")
    death_date("23092000","23092005")
    gender_input()
    credit_input("Holiday")
    adult_name()
    seeresults()
    driver.close()
    driver.quit()

result=search_inputs()