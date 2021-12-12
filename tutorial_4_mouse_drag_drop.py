from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# melakukan drag & drop dengan menggunakan nilai x offset dan y offset

driver = webdriver.Chrome(
    r'C:\Users\navisha\Desktop\selenium_basic\tutorial_selenium\test\driver\chromedriver.exe')
driver.get(
    'http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

# membuat object action/tindakan
action = ActionChains(driver=driver)

# element
drag = driver.find_element(
    By.XPATH, '//div[@id="dropContent"]/div[contains(@id, "box")][5]')
drop = driver.find_element(
    By.XPATH, '//div[@id="countries"]/div[contains(@id, "box")][5]')

# mendapatkan nilai offset element drop
x_off = drop.location.get('x')
y_off = drop.location.get('y')
print((x_off))  # lihat nilainya di console
print((y_off))  # lihat nilainya di console

# melakukan dragdropby ke element drop
action.drag_and_drop_by_offset(drag, xoffset=x_off, yoffset=y_off).perform()
