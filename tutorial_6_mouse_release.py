from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# melakukan drag & drop dengan menggunakan fungsi release
# ini paling efektif untuk melakukan drag drop
# release() melepaskan klik kiri mouse, jika tidak ada element web
# maka akan melepaskan pada posisinya saat ini

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

# melepaskan klik kiri mouse setelah melakukan beberapa tindakan yang diperlukan
# klik dan tahan element drop
action.click_and_hold(on_element=drag).perform()
# pindahkan ke element drag kemudian lepaskan/release
action.move_to_element(to_element=drop).release().perform()
