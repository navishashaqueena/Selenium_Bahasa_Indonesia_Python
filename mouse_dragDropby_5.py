from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    r'C:\Users\navisha\Desktop\selenium_basic\tutorial_selenium\test\driver\chromedriver.exe')
driver.get(
    'http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-2.html')

# membuat object action/tindakan
action = ActionChains(driver=driver)

# element
drag = driver.find_elements(By.XPATH, '//div[contains(@id, "box")]')
drop = driver.find_element(By.XPATH, '//div[@id="dropBox"]')

# loop semua yang ada di drag
# kemudian di drop menggunankan action
for i in drag:
    action.drag_and_drop(i, drop).perform()
