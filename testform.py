from selenium import webdriver

emails = 'faliaamalia5@gmail.com'
passw = 'Abcderaya5'
konf = 'Abcderaya5'
namad = 'Falia'
namab = 'Amalia'
telp = '087887900345'
kota = 'KOTA TANGERANG'

driver = webdriver.Chrome()
driver.get('https://www.cermati.com/gabung')
email1 = driver.find_element_by_name('email')
email1.send_keys(emails)

sandii = driver.find_element_by_name('password')
sandii.send_keys(passw)

konfirmasi = driver.find_element_by_name('confirmPassword')
konfirmasi.send_keys(konf)

namadpn = driver.find_element_by_name('firstName')
namadpn.send_keys(namad)

namablkg = driver.find_element_by_name('lastName')
namablkg.send_keys(namab)

telpn = driver.find_element_by_name('mobilePhone')
telpn.send_keys(telp)

kotaa = driver.find_element_by_name('residenceCity')
kotaa.send_keys(kota)

pilih = driver.find_element_by_class_name('autocomplete-list-item highlighted')
pilih.send_keys(kota)

daftar = driver.find_element_by_name('sign-up.submit')
daftar.click()

#element.send_keys(KEY.RETURN)
#driver.quit()
#time.sleep()