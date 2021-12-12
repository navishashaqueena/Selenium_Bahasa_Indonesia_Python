# PENJELASAN
# ActionChains mengotomatiskan interaksi mouse dan keyboard tingkat rendah dalam kasus uji
# perform() adalah fungsi penting yang memungkinkan semua tindakan oleh mouse dan keyboard diimplementasikan dilakukan. Semua fungsi ActionChains yang terkait dengan mouse dan keyboard hanya berfungsi saat fungsi perform() digunakan; jika tidak digunakan, maka fungsi ActionChain tidak menghasilkan tindakan pada halaman web.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# membuka browser chrome
driver = webdriver.Chrome(
    executable_path=r'C:\Users\navisha\Desktop\selenium_basic\tutorial_selenium\test\driver\chromedriver.exe')
# membuka url/halaman
# driver.get('https://skillacademy.com/')

# pergi ke Button/tombol
# web_element = driver.find_element_by_xpath(
#     '//div[@data-testid="header-login-button"]')

# klik element yang di seleksi diatas
# web_element.click()
# webdriver.ActionChains(driver=driver).click(web_element).perform()

# melakukan tindakan klik dan tahan di element web
# webdriver.ActionChains(driver=driver).click_and_hold(web_element).perform()

# melakukan tindakan klik kanan mouse
# time.sleep(5)
# gambar = driver.find_element_by_xpath('//img[@alt="Skill Academy Logo2x"]')
# webdriver.ActionChains(driver=driver).context_click(gambar).perform()

# klik 2 kali
driver.get('https://promo.skillacademy.com/payday')
navigasi = driver.find_element_by_xpath('//p[@class="uang-saku"]')
webdriver.ActionChains(driver=driver).double_click(navigasi).perform()
