# TUTORIAL SELENIUM MENGGUNAKAN PYTHON 
*By Rifki Arisandi Pratama*

*My Website [https://navisha-pratama.com/](https://navisha-pratama.com/)*

*My Youtube [navisha-pratama](https://www.youtube.com/channel/UCS5FYSLD95fvdLzWw8PW4-A/featured)*



# ELEMENT WEB

### Pencari ID
Metode atau fungsi ini adalah salah satu locator yang paling banyak digunakan. ID adalah atribut unik di halaman web HTML dan cenderung tidak terpengaruh oleh perubahan.

Menurut W3C, setiap elemen harus memiliki ID unik; namun, browser mengizinkan pengecualian untuk aturan ini. Pengecualian ini memungkinkan elemen yang berbeda memiliki nama ID yang sama atau tanpa ID, itulah sebabnya Selenium memiliki delapan pencari. Berikut sintaksnya.
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
HTML diatas, tag form adalah satu-satunya elemen yang memiliki atribut ID. Atribut ID tag formulir bernama EmployeeForm.contoh :

`Employee_form = driver.find_element_by_id ('EmployeeForm')`

Dengan menggunakan metode ini, Anda dapat dengan mudah menemukan elemen jika atribut ID diketahui. Jika beberapa elemen memiliki nama atribut ID yang sama, maka ID pertama yang cocok akan dikembalikan. Jika tidak ada kecocokan, maka pengecualian dipanggil. Pengecualian ini dikenal sebagai 

`NoSuchElementException`

## Pencari Nama

atribut `name` adalah atribut banyak digunakan, mungkin tidak didefinisikan secara unik. Atribut `name` biasanya merupakan elemen input pada formulir (tetapi juga digunakan dalam bidang teks dan tombol). Atribut `name` meneruskan semua nilai yang sesuai ke server saat tindakan kirim dilakukan pada formulir.

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
Ada dua tag input dengan atribut `name`. Tag (elemen) input pertama dan kedua memiliki `employee_name` sebagai atribut `name` dan elemen `email` mudah ditemukan, sebagai berikut.

```
# element pertama
employee = driver.find_element_by_name('employee_name')
# element kedua
email = driver.find_element_by_name('email')
```

Dalam setiap kasus, pencari nama dicocokkan dengan elemen pertama pada halaman sumber HTML. Jika tidak ada elemen pada halaman yang cocok, maka `NoSuchElementException` akan dipanggil.
Dalam kasus beberapa elemen dengan nama yang sama sebagai atribut, locator memilih elemen pertama pada halaman HTML dengan nama yang ditentukan secara tepat.

`next = driver.find_element_by_name('next')`

## Pencari XPath
XPath digunakan dalam bahasa XML untuk menemukan node yang menavigasi melalui elemen dan atribut. Jalur dibuat dari ekspresi yang terkait dengan node tertentu. HTML juga mendukung implementasi XML menggunakan XHTML. Dengan tidak adanya ID dan nama, sulit untuk menemukan elemen. Dalam situasi ini, pencari XPaths mengidentifikasi elemen dengan tautannya. Ini adalah pencari lokasi ketiga yang paling banyak digunakan setelah ID dan nama. Ada beberapa cara untuk menemukan tautan karena mereka berada dalam struktur seperti pohon.

Sintaks umum untuk XPath adalah

`xpath =//tag_name[@attribute_name= 'value']`
### Keterangan :
1.  `//` : Mendefinisikan direktori/tag saat ini (satu garis miring digunakan untuk jalur absolut)
2. `tag_name` : Mendefinisikan nama tag untuk jalur yang ditentukan
3. `@` : Menentukan atribut yang akan dipilih
4. `attribute_name` : Menentukan nama atribut; nama atribut node
5. `value` : Mendefinisikan nilai dari atribut yang ditentukan

## XPath Cheat 
### DASAR-DASAR
```<!DOCTYPE html>
<html lang="en">

<head>
    <title>XPath and CSS Selectors</title>
</head>

<body>
    <h1>XPath expressions simplified</h1>
    <div class="intro">
        <p> I'm paragraph within a div with a class set to intro <span id="location">I'm a span with ID set to location
                and i'm within a paragraph</span> </p>
        <p id="outside">I'm a paragraph with ID set to outside and i'm within a div with a class set to intro</p>
    </div>
    <p>Hi i'm placed immediately after a div with a class set to intro </p> <span class='intro'>Div with a class
        attribute set to intro </span>
    <ul id="items">
        <li data-identifier="7">Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
        <li>Item 4</li>
    </ul> <a href="https://www.google.com">Google</a> <a href="http://www.google.fr">Google France</a>
    <p class='bold italic'>Hi, I have two classes</p>
    <p class='bold'>Hi i'm bold</p>
</body>

</html>
```
Elemen adalah tag dalam markup HTML.
Contoh:
tag `p`  alias paragragh disebut elemen. Untuk memilih elemen apa pun dari halaman web HTML, kami cukup menggunakan sintaks berikut:
Contoh:
Untuk memilih semua elemen `p` kita dapat menggunakan pemilih XPath berikut:
`//P`
Meskipun pendekatan ini bekerja dengan baik, tidak disarankan untuk menggunakannya, karena jika misalnya kita hanya ingin memilih `p` elemen yang ada di dalam `div` pertama dengan atribut kelas sama dengan `intro` pendekatan ini tidak akan menjadi solusi terbaik, inilah mengapa kami selalu memilih untuk menargetkan elemen baik dengan atribut `class`, `id` , atau berdasarkan posisinya sehingga kami dapat membatasi cakupan ekspresi XPath.

### IDENTITAS KELAS
Jadi untuk memilih elemen apa pun berdasarkan nilai atribut kelasnya, kami menggunakan sintaks berikut:

`//elementName[@attributeName=’value’]`

Contoh:
Katakanlah kita ingin memilih elemen `p` yang ada di dalam  `div`  dengan atribut class sama dengan `intro` dalam hal ini kita menggunakan ekspresi XPath berikut:

`//div[@class=’intro’]/text()`

Jika kita ingin memilih elemen `p` dengan `id` sama dengan `outside` kita dapat menggunakan ekspresi XPath berikut:
`//p[@id='outside']/text()`

> INGAT:
> Harap dicatat, nilai atribut kelas yang sama persis dapat diberikan ke lebih dari satu elemen, dan `id` hanya dapat diberikan ke dan hanya satu elemen.

Terkadang kita juga ingin memilih elemen berdasarkan atribut asing yang tidak termasuk dalam standar markup HTML. Misalnya untuk memilih elemen `li` dengan atribut `data-identifier` sama dengan `7` dalam hal ini kita menggunakan ekspresi XPath berikut:

`//li[@data-identifier=”7”]`

Terkadang elemen yang ingin kita pilih memang memiliki dua kelas, misalnya untuk memilih elemen `p` dengan atribut class sama dengan `bold` dan `italic` dalam hal ini kita menggunakan ekspresi XPath berikut:

`//p[@class=’bold italic’]`

ATAU:
Meskipun elemen tersebut memiliki dua kelas, misalnya, kita dapat mencari substring di dalam nilai atribut kelas dengan menggunakan fungsi `contains()`.

`//p[contains(@class, ‘italic’)]`

> INGAT:
> Fungsi contains membutuhkan dua argumen:
> 1.	Yang pertama adalah tempat pencarian, apakah pada nilai atribut class , id atau yang lainnya.
> 2.	Argumen kedua adalah nilai yang Anda cari.
> 3.	Nilai yang Anda cari juga peka huruf besar/kecil, jadi berhati - hatilah!

### Pencarian nilai

Katakanlah Anda ingin memilih semua elemen `a`di mana `href` nilai atribut dimulai dengan `https` dan bukan `http` , dalam hal ini kita dapat menggunakan ekspresi XPath berikut:

`//a[starts-with(@href, 'http')]`

Jadi mencari teks yang muncul di awal kita menggunakan fungsi `starts-with()` yang mengambil argumen yang sama dengan fungsi `contains()`.

Sekarang jika Anda ingin mencari nilai di akhir, kami menggunakan fungsi `ends-with()`, namun, fungsi ini tidak didukung pada XPath versi 1.0 yang merupakan versi yang digunakan oleh sebagian besar browser dan LXML.

Terakhir jika kita ingin mencari nilai tertentu di antara kita menggunakan fungsi `contains()` seperti yang dijelaskan sebelumnya.

Jika Anda ingin mendapatkan teks dari elemen tertentu, Anda dapat menggunakan fungsi `text()`, misalnya, untuk mendapatkan elemen teks dari `p` elemen dengan `id` sama dengan `outside` kami menggunakan ekspresi XPath berikut:

`//p[@id=”outside”]/text()`

### Posisinya
Oke, misalkan Anda ingin mendapatkan elemen `li` kedua dari `ul` elemen dengan `id` sama dengan `outside`, dalam hal ini Anda dapat menggunakan ekspresi XPath berikut:

`//ul[@id=”items”]/li[2]`

Namun, jika Anda ingin memilih item daftar kedua tetapi Anda juga ingin membuat elemen teksnya menjadi `Item 2`, dalam hal ini Anda dapat menggunakan ekspresi XPath berikut:

`//ul[@id=”items”]/li[position() = 2 and text() = “Item 2”]`

Perhatikan dalam hal ini saya menggunakan fungsi `position()` , fungsi `text()` ditambah operator logika `and`.

Ada operator logika `and` ada juga operator logika `or`.
>INGAT:
>Di XPath semua yang kita tulis di dalam [] dikenal sebagai predikat/kondisi.

### XPath axis/sumbu
Di XPath, sumbu digunakan untuk mencari elemen berdasarkan hubungannya dengan elemen lain, kami memiliki beberapa sumbu yang dapat kami gunakan untuk menavigasi ke atas dan ke bawah di markup HTML.
Semua sumbu di XPath menggunakan sintaks berikut: 
`ElementName::axis`

XPath axis (NAIK)
- Parent
- Axis/sumbu parent digunakan untuk mendapatkan parent dari elemen tertentu, misalnya mendapatkan parent dari `p` elemen dengan `id` sama dengan `outside` kami menggunakan ekspresi XPath berikut:

    `//p[@id="outside"]/parent::node()`

- Fungsi `node()` di XPath digunakan untuk mendapatkan `elemen` apapun jenisnya.
- Nenek moyang/ancestor
- Sumbu ancestor dapat digunakan untuk semua ancestor dari elemen tertentu, misalnya untuk mendapatkan ancestor ( parent , grand parent , ...) dari elemen `p` dengan `id` sama dengan `outside` kami menggunakan ekspresi XPath berikut:

`//p[@id="outside"]/ancestor::node()`

- sebelumnya /preceding
Di XPath sumbu sebelumnya/preceding akan mendapatkan semua elemen yang mendahului elemen tidak termasuk nenek moyangnya/ancestor.
- Saudara sebelumnya/preceding-sibling
Pada XPath sumbu preceding-sibling akan mendapatkan saudara yang mendahului suatu elemen, dengan kata lain akan mengembalikan saudara yang berada di atas elemen tertentu.
Sumbu XPath (TURUN)
Untuk turun pada markup HTML kita juga memiliki 4 sumbu yaitu: 
- Sumbu child yang akan mendapatkan anak-anak dari elemen tertentu
- Sumbu following yang akan mengembalikan semua elemen yang berada setelah tag penutup elemen tertentu.
- Sumbu following-sibling yang akan mengembalikan semua elemen setelah tag penutup suatu elemen tetapi elemen -elemen ini harus memiliki induk yang sama.
- Sumbu descendant yang akan mendapatkan turunan dari elemen tertentu.

Jika ada dua element tapi kita ingin salah satunya maka bungkus elemen dengan `()` diikuti dengan `[]` untuk memilih indexnya, misalnya kita ingin memilih elemen time:
`(//time)[1]` # element time index ke 1
