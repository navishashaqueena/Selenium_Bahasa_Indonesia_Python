from selenium import webdriver
import time

# membuka browser chrome
driver = webdriver.Chrome(
    executable_path=r'C:\Users\navisha\Desktop\selenium_basic\tutorial_selenium\test\driver\chromedriver.exe')

# membuka browser firefox
# driver = webdriver.Chrome(
#     executable_path=r'C:\Users\navisha\Desktop\selenium_basic\tutorial_selenium\test\driver\geckodriver.exe')

# membuka halaman web
# jika halaman web dari local gunakan = driver.get('path lokal')
# jika halaman web dari server local gunakan = driver.get('http://localhost')
# driver.get('https://skillacademy.com/')

# memaksimalkan ukuran browser
# driver.maximize_window()

# browser ukuran fullscreen
# driver.fullscreen_window()


# mengatur ukuran tinggi dan lebar browser
# driver.set_window_size(height=500, width=400)

# mengatur posisi browser
# posisi x dan y dimulai dari (0,0) dari pojok kanan atas layar
# driver.set_window_position(x=500, y=400)

# mengatur posisi browser dengan posisi dan dimensi
# posisi x dan y sedangkan dimensi tinggi dan lebar
# driver.set_window_rect(x=30, y=30, height=500, width=450)

# untuk mengetahui posisi browser
# posisi_browser = driver.get_window_position()
# print(posisi_browser)  # akan mencetak posisi browser dalam dictionary

# untuk mengetahui ukuran browser
# akan mencetak ukuran browser dalam dictionary
# print(driver.get_window_size())


# untuk menavigasi halaman sebelum dan sesudah
# buka google
# driver.get('https://www.google.com/')
# buka skillacademy
driver.get('https://skillacademy.com/')
# kembali ke halaman sebelumnya 'google'
# driver.back()
# print('kembali ke halaman sebelumnya')
# forward ke halaman berikutnya
# driver.forward()
# print('pergi ke halaman berikutnya')

# menyegarkan halaman atau refresh
driver.refresh()


# menutup browser windows saat ini
# driver.close()

# menutup semua browser windows
time.sleep(5)
driver.quit()
