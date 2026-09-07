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