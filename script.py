import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc3Wp9C6pR2g4KpPgclcJCsN_U7jdc0rWRLk1R4jkj3uxyUpA/viewform")
time.sleep(2)

questions = driver.find_elements(By.CSS_SELECTOR, "div.freebirdFormviewerViewNumberedItemContainer")
questions[0].find_element(By.CSS_SELECTOR, "input").send_keys("GeeTransit#3203")
questions[1].find_element(By.CSS_SELECTOR, "input").send_keys("https://github.com/GeeTransit/intro-to-automation-with-selenium")
questions[2].find_elements(By.CSS_SELECTOR, "div.freebirdFormviewerComponentsQuestionRadioChoice")[1].find_element(By.CSS_SELECTOR, "div.freebirdThemedRadio").click()
questions[3].find_elements(By.CSS_SELECTOR, "div.freebirdFormviewerComponentsQuestionCheckboxChoice")[0].find_element(By.CSS_SELECTOR, "div.freebirdThemedCheckbox").click()
questions[3].find_elements(By.CSS_SELECTOR, "div.freebirdFormviewerComponentsQuestionCheckboxChoice")[2].find_element(By.CSS_SELECTOR, "div.freebirdThemedCheckbox").click()
questions[4].find_element(By.CSS_SELECTOR, "input").send_keys("Option 2")
questions[5].find_elements(By.CSS_SELECTOR, "div.quantumWizMenuPaperselectOptionList div.freebirdThemedSelectOptionDarkerDisabled")[0].click()
questions[5].find_elements(By.CSS_SELECTOR, "div.quantumWizMenuPaperselectPopup div.freebirdThemedSelectOptionDarkerDisabled")[2].click()

driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerViewNavigationSubmitButton .appsMaterialWizButtonPaperbuttonLabel").click()
time.sleep(2)

driver.close()
