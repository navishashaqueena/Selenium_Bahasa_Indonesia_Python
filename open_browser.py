from selenium import webdriver

# membuka browser chrome
driver = webdriver.Chrome(
    executable_path=r'C:\Users\navisha\Desktop\selenium_basic\tutorial_selenium\test\driver\chromedriver.exe')

# membuka browser firefox
# driver = webdriver.Chrome(
#     executable_path=r'C:\Users\navisha\Desktop\selenium_basic\tutorial_selenium\test\driver\geckodriver.exe')

# membuka halaman web
driver.get('https://skillacademy.com/')

# memaksimalkan ukuran browser
driver.maximize_window()

# browser ukuran fullscreen
driver.fullscreen_window()

# menutup browser windows saat ini
driver.close()

# menutup semua browser windows
# driver.quit()
