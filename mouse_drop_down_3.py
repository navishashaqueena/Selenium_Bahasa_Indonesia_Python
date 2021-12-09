from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    executable_path=r'C:\Users\navisha\Desktop\selenium_basic\tutorial_selenium\test\driver\chromedriver.exe')

driver.get('https://skillacademy.com/')

# drop_down = driver.find_element_by_xpath(
#     '//div[@data-testid="dropdown-category"]')
# ActionChains(driver=driver).move_to_element(drop_down).perform()

# menunggu sampai submenu ditampilkan
# WebDriverWait(driver=driver, timeout=3).until(
#     EC.visibility_of_element_located((By.LINK_TEXT, 'Pemasaran')))
# klik pilihan
# driver.find_element_by_link_text('Pemasaran').click()

# menggerakkan mouse dari offset x ke offset y dari posisi saat ini
# membuat variabel x dan y
x = 268
y = 66
webdriver.ActionChains(driver=driver).move_by_offset(
    xoffset=x, yoffset=y).perform()
