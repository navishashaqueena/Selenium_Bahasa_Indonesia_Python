
# import semua library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# membuat driver
driver = webdriver.Chrome(
    r'C:\Users\navisha\Desktop\selenium_basic\tutorial_selenium\test\driver\chromedriver.exe')

# webpage
driver.get('https://en.wikipedia.org/wiki/Apress')

action = ActionChains(driver=driver)

# Fungsi key_down(value, web_element) bekerja dengan menekan tombol. Hal ini terutama digunakan dengan tombol pengubah, seperti Shift, Control, Alt, dan sebagainya.
# Fungsi  key_up (nilai, web_element)  melepaskan tombol pengubah ditekan. Biasanya digunakan setelah metode key_down.
# Fungsi send_keys_to_element(send_keys) metode mengirimkan penekanan tombol dari keyboard ke elemen web yang sedang dipilih. Dapat digunakan untuk satu tombol atau beberapa tombol.
# Sebagian besar waktu, tindakan keyboard digunakan bersama. Berikut ini adalah contoh singkat tindakan keyboard yang memilih dan menyalin teks dari halaman web.
# action secara merantai
# ActionChains(driver)\
#     .key_down(Keys.CONTROL)\
#     .send_keys("a")\
#     .key_up(Keys.CONTROL)\
#     .key_down(Keys.CONTROL)\
#     .send_keys("c")\
#     .key_up(Keys.CONTROL)\
#     .perform()

# kirim kunci ke element tertentu
# element pencarian wiki
search = driver.find_element_by_xpath(
    '//input[@class="vector-search-box-input"]')

# tulis di element search kemudian tekan enter
ActionChains(driver=driver)\
    .send_keys_to_element(search, 'soekarno')\
    .key_down(Keys.ENTER)\
    .perform()

# fungsi pause(secs), tindakan ditunda (dijeda) selama durasi waktu tertentu (dalam detik). Ini menampilkan elemen web sebelum melakukan tindakan.
# fungsi  reset_actions() Clears atau menghapus semua tindakan yang tersimpan yang berkaitan dengan elemen web. Tindakan dapat disimpan secara lokal atau remote end.
