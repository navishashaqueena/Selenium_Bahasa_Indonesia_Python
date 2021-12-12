# ELEMENT WEB

## Pencari ID
### Metode atau fungsi ini adalah salah satu locator yang paling banyak digunakan. ID adalah atribut unik di halaman web HTML dan cenderung tidak terpengaruh oleh perubahan.
### Menurut W3C, setiap elemen harus memiliki ID unik; namun, browser mengizinkan pengecualian untuk aturan ini. Pengecualian ini memungkinkan elemen yang berbeda memiliki nama ID yang sama atau tanpa ID, itulah sebabnya Selenium memiliki delapan pencari. Berikut sintaksnya.
`var_name = find_element_by_id ('id_attribute')`
### CONTOH HTML

```
<html>
<body>
<form id="EmployeeForm">
<input name="employee_name"type="text"/>
<input name="email"type="email"/>
<input name="next"type="submit" value="Login"/>
</form>
</body>
</html>
```
### HTML diatas, tag form adalah satu-satunya elemen yang memiliki atribut ID. Atribut ID tag formulir bernama EmployeeForm.contoh :

`Employee_form = driver.find_element_by_id ('EmployeeForm')`

### Dengan menggunakan metode ini, Anda dapat dengan mudah menemukan elemen jika atribut ID diketahui. Jika beberapa elemen memiliki nama atribut ID yang sama, maka ID pertama yang cocok akan dikembalikan. Jika tidak ada kecocokan, maka pengecualian dipanggil. Pengecualian ini dikenal sebagai 

`NoSuchElementException`

## Pencari Nama

### atribut `name` adalah atribut banyak digunakan, mungkin tidak didefinisikan secara unik. Atribut `name` biasanya merupakan elemen input pada formulir (tetapi juga digunakan dalam bidang teks dan tombol). Atribut `name` meneruskan semua nilai yang sesuai ke server saat tindakan kirim dilakukan pada formulir.

`var_name = find_element_by_name ('nama_atribut')`

### Contoh HTML

```
<html>
<body>
<form id="EmployeeForm">
<input name="employee_name" type="text" /><!--1st element-->
<input name="email" type="email" /><!--2nd element-->
<input name="next" type="submit" value="Login" /><!--3rd element-->
<input name="next" type="button" value="Clear" /><!--4th element-->
</form>
</body>
</html>
```
### Ada dua tag input dengan atribut `name`. Tag (elemen) input pertama dan kedua memiliki `employee_name` sebagai atribut `name` dan elemen `email` mudah ditemukan, sebagai berikut.

```
# element pertama
employee = driver.find_element_by_name('employee_name')
# element kedua
email = driver.find_element_by_name('email')
```

### Dalam setiap kasus, pencari nama dicocokkan dengan elemen pertama pada halaman sumber HTML. Jika tidak ada elemen pada halaman yang cocok, maka `NoSuchElementException` akan dipanggil.
### Dalam kasus beberapa elemen dengan nama yang sama sebagai atribut, locator memilih elemen pertama pada halaman HTML dengan nama yang ditentukan secara tepat.

`next = driver.find_element_by_name('next')`

## Pencari XPath
### XPath digunakan dalam bahasa XML untuk menemukan node yang menavigasi melalui elemen dan atribut. Jalur dibuat dari ekspresi yang terkait dengan node tertentu. HTML juga mendukung implementasi XML menggunakan XHTML. Dengan tidak adanya ID dan nama, sulit untuk menemukan elemen. Dalam situasi ini, pencari XPaths mengidentifikasi elemen dengan tautannya. Ini adalah pencari lokasi ketiga yang paling banyak digunakan setelah ID dan nama. Ada beberapa cara untuk menemukan tautan karena mereka berada dalam struktur seperti pohon.
### Sintaks umum untuk XPath adalah

`xpath =//tag_name[@attribute_name= 'value']`
### Keterangan :
1.  `//` : Mendefinisikan direktori/tag saat ini (satu garis miring digunakan untuk jalur absolut)
2. `tag_name` : Mendefinisikan nama tag untuk jalur yang ditentukan
3. `@` : Menentukan atribut yang akan dipilih
4. `attribute_name` : Menentukan nama atribut; nama atribut node
5. `value` : Mendefinisikan nilai dari atribut yang ditentukan
