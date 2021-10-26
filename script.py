import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc3Wp9C6pR2g4KpPgclcJCsN_U7jdc0rWRLk1R4jkj3uxyUpA/viewform")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerViewNumberedItemContainer:nth-child(1) input").send_keys("GeeTransit#3203")
driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerViewNumberedItemContainer:nth-child(2) input").send_keys("https://github.com/GeeTransit/intro-to-automation-with-selenium")
driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerViewNumberedItemContainer:nth-child(3) div.freebirdFormviewerComponentsQuestionRadioChoice:nth-child(2) div.freebirdThemedRadio").click()
driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerViewNumberedItemContainer:nth-child(4) div.freebirdFormviewerComponentsQuestionCheckboxChoice:nth-child(1) div.freebirdThemedCheckbox").click()
driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerViewNumberedItemContainer:nth-child(4) div.freebirdFormviewerComponentsQuestionCheckboxChoice:nth-child(3) div.freebirdThemedCheckbox").click()
driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerViewNumberedItemContainer:nth-child(5) input").send_keys("Option 2")
driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerViewNumberedItemContainer:nth-child(6) div.quantumWizMenuPaperselectOptionList div.freebirdThemedSelectOptionDarkerDisabled:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerViewNumberedItemContainer:nth-child(6) div.quantumWizMenuPaperselectPopup div.freebirdThemedSelectOptionDarkerDisabled:nth-child(4)").click()

driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerViewNavigationSubmitButton .appsMaterialWizButtonPaperbuttonLabel").click()
time.sleep(2)

driver.close()
