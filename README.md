Nama : Najwa Salsabil

NPM : 2506588701

Kelas : PBP A

### Tugas 1
1. Saya memakai elemen HTML5 secara konsisten:<section> buat tiap blok konten utama (Profile, Skills, Experience, Education, Projects, Achievements), <article> buat item yang berdiri sendiri dan bisa diulang (tiap skill group, tiap project card, tiap achievement card), <nav> buat navigasi, <time> buat tahun di timeline Experience, dan <dl>/<dt>/<dd> buat data NPM dan Program. Elemen-elemen ini membantu banget karena browser dan screen reader jadi ngerti struktur halaman tanpa saya harus nulis banyak <div> generik, misalnya <article> nunjukkin ke browser bahwa tiap project card itu konten yang punya makna sendiri, bukan cuma pembungkus visual. Saya sengaja tidak memakai <aside> karena semua konten di halaman ini memang bagian utama dari portofolio, bukan info tambahan/sampingan.

2. Tantangan terbesar ada di dua tempat: (1) navigasi header yang jumlah link-nya bertambah tiap saya nambah section baru (dari 1 jadi 6 link), di layar sempit ini gampang overflow, jadi saya memakai flex-wrap biar link pindah baris otomatis daripada dipotong; (2) layout timeline di Experience, karena kombinasi grid dua kolom (bulet + tahun) harus tetap proporsional walau lebar layar berubah, saya sesuaikan lebar kolom gridnya lewat media query, bukan cuma menyembunyikan elemen. Cara saya evaluasi elemen mana yang perlu diprioritaskan: konten yang paling penting buat identitas (nama, foto) saya pertahankan urutannya duluan di mobile, sementara elemen dekoratif atau data sekunder (kayak grid multi-kolom di Skills/Projects) saya biarkan collapse jadi satu kolom karena itu gak mengorbankan keterbacaan.

3. Batasan paling kerasa: semua konten masih hardcoded di HTML, jadi kalau aku mau update satu pencapaian baru, saya harus edit langsung ke source code dan deploy ulang, gak ada cara buat nge-update dari luar. Saya juga gak bisa nyimpen data secara dinamis karena belum ada backend/database. Ke depannya, fungsionalitas dinamis yang paling ingin aku tambahkan adalah backend sederhana supaya konten Experience/Projects/Achievements bisa di-manage lewat admin panel atau database, dan form kontak yang beneran ngirim email/tersimpan, bukan cuma mailto: link.

AI Disclosure & Refleksi:
Dalam pengerjaan tugas pembuatan portofolio ini, saya mengerjakannya secara mandiri tanpa menggunakan bantuan generative AI untuk menghasilkan kode. Proses pemecahan masalah saya lakukan dengan membaca materi perkuliahan, memeriksa sintaks secara manual, serta melakukan riset mandiri melalui Google dan dokumentasi web. 

Riset mandiri tersebut sering saya lakukan terutama untuk hal-hal seputar CSS. CSS memiliki cakupan konsep dan properti yang sangat luas di baliknya, mulai dari tata letak (flexbox/grid), styling responsif, hingga penyesuaian detail komponen visual. Ketika menemukan kendala tampilan atau styling yang tidak sesuai ekspektasi, saya mencari referensi implementasi properti CSS yang tepat di mesin pencari, lalu menganalisis dan menerapkannya sendiri ke dalam kode proyek.

### Tugas 2
1. Ketika pengguna mengetik URL, misalnya /projects/, browser mengirim request ke server Django. Request ini pertama kali diterima oleh urls.py milik proyek (portofolio/urls.py), yang isinya cuma meneruskan semua path kosong ("") ke include("main.urls") — jadi proyek ini gak langsung menentukan view mana yang dipanggil, dia cuma "melempar" ke konfigurasi routing aplikasi main. Di dalam main/urls.py, Django mencocokkan sisa path (projects/) dengan pola yang terdaftar, dan menemukan path("projects/", show_projects, name="show_projects"), sehingga fungsi show_projects di main/views.py yang dipanggil.

Di dalam show_projects, view mengambil seluruh data dari model lewat Project.objects.all(), lalu membungkusnya ke dalam sebuah context (dictionary) bersama data lain seperti name. View kemudian memanggil render(request, "projects.html", context), yang artinya Django mengambil berkas template projects.html, mengganti semua {{ ... }} dan menjalankan {% for %}/{% if %} di dalamnya menggunakan data dari context, lalu menghasilkan HTML jadi. HTML inilah yang dikembalikan sebagai response ke browser dan ditampilkan ke pengguna.

Jadi alurnya: Browser → portofolio/urls.py → main/urls.py → show_projects (view) → Project (model) → kembali ke view sebagai context → projects.html (template) → HTML response → Browser.

2. Kalau data ditulis langsung di HTML, setiap kali ada proyek baru yang ingin ditambahkan, maka harus buka dan edit file template secara manual, lalu deploy ulang seluruh aplikasi. Dengan menyimpan data di model, menambah proyek baru cukup dengan menambahkan satu baris data ke database (lewat Django admin atau shell), tanpa menyentuh kode sama sekali. Ini juga bikin data lebih konsisten dan gampang diproses, misalnya kalau suatu saat aku mau menampilkan proyek diurutkan berdasarkan tanggal terbaru, atau memfilter proyek berdasarkan kategori, itu bisa dilakukan langsung lewat query di level model/view, tanpa perlu mengubah struktur HTML satu per satu. Pemisahan ini juga membuat template murni berurusan dengan tampilan saja, sehingga kalau nanti aku ganti desainnya total, logika pengambilan data di view tidak perlu ikut berubah.

3. makemigrations itu langkah untuk membuat catatan perubahan, perintah ini membaca perubahan yang aku buat di models.py (misalnya menambah model Project dan Achievement), lalu menghasilkan berkas migrasi baru (0002_achievement_project.py) yang berisi instruksi perubahan tersebut. Berkas ini belum benar-benar mengubah apa pun di database, dia cuma "rencana" yang tercatat.

migrate itu langkah untuk menjalankan rencana tersebut, perintah ini membaca semua berkas migrasi yang belum diterapkan, lalu benar-benar mengeksekusi perubahan itu ke skema database (misalnya membuat tabel main_project dan main_achievement yang sebelumnya belum ada).

Contoh nyata yang mengharuskan aku menjalankan keduanya: saat aku menambahkan model Project dan Achievement baru ke models.py di tugas ini. Karena struktur tabelnya benar-benar baru (belum pernah ada di database sebelumnya), aku wajib jalankan python manage.py makemigrations dulu supaya Django tahu ada tabel baru yang perlu dibuat, lalu python manage.py migrate supaya tabel itu benar-benar terbentuk di db.sqlite3 dan siap diisi data.

AI Disclosure & Refleksi
Dalam pengerjaan Individual Assignment 2 ini, saya **tidak menggunakan bantuan tools Artificial Intelligence (AI)** sama sekali, baik berupa LLM (seperti ChatGPT, Claude, atau Gemini) maupun AI coding assistant (seperti GitHub Copilot). 

Seluruh proses implementasi—mulai dari pendefinisian model, penulisan fungsi views, pembuatan template HTML dengan Django Template Language (DTL), konfigurasi URL routing, hingga penulisan unit test—dikerjakan secara mandiri dengan merujuk pada:
1. Materi dan kode latihan Tutorial 02 Pemrograman Berbasis Platform (PBP).
2. Dokumentasi resmi Django (Django Documentation).
3. Catatan serta slide perkuliahan PBP Fasilkom UI.