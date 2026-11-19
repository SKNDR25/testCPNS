# 🇮🇩 Simulasi CAT CPNS & SKB IT Multi-Instansi
### Platform Latihan Mandiri Berbasis Standar Resmi CAT BKN

Platform web simulasi ujian **Computer Assisted Test (CAT)** mandiri berbasis standar Badan Kepegawaian Negara (BKN) untuk persiapan seleksi Calon Pegawai Negeri Sipil (CPNS) dan Pegawai Pemerintah dengan Perjanjian Kerja (PPPK). 

Dilengkapi dengan **Bank Soal Autentik (710 Soal Berdasar Regulasi & Standar Resmi)**, sistem penilaian *Passing Grade* otomatis, analisis performa real-time, penyimpanan sesi otomatis (*auto-save/resume*), dan mode kiosk/layar penuh.

---

## 📑 Daftar Isi
- [Fitur Utama](#-fitur-utama)
- [Struktur & Cakupan Bank Soal (710 Soal)](#-struktur--cakupan-bank-soal-710-soal)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Panduan Instalasi & Cara Penggunaan](#-panduan-instalasi--cara-penggunaan)
  - [1. Penggunaan Langsung (Offline / Standalone)](#1-penggunaan-langsung-offline--standalone)
  - [2. Menjalankan via Server Lokal (Opsional)](#2-menjalankan-via-server-lokal-opsional)
- [Panduan Fitur Aplikasi](#-panduan-fitur-aplikasi)
- [Struktur Direktori](#-struktur-direktori)
- [Kontribusi & Manajemen Soal](#-kontribusi--manajemen-soal)
- [Lisensi](#-lisensi)

---

## 🌟 Fitur Utama

### 1. Pilihan 2 Mode Latihan Fleksibel
* ⏱️ **Mode Simulasi CAT Resmi:** Replikasi persis kondisi ujian asli: timer hitung mundur (90/100 menit), pembahasan terkunci selama ujian, indikator status ragu-ragu, dan evaluasi kelulusan passing grade resmi di akhir sesi.
* 📖 **Mode Belajar Mandiri (Study Mode):** Belajar santai tanpa tekanan waktu: begitu peserta memilih opsi A–E, status **Benar (Hijau)** atau **Salah (Merah)** beserta kunci jawaban resmi dan pembahasan komprehensif langsung terbuka seketika di bawah soal. Grid nomor otomatis menandai hijau (benar) atau merah (salah).

### 2. Antarmuka Realistis Standar CAT BKN
* **Pengalaman Ujian Autentik:** Tampilan antarmuka, warna tema, timer hitung mundur, panel nomor soal, dan indikator status dirancang menyerupai terminal tes BKN asli.
* **Auto-Save & Resume Sesi:** Sesi ujian tersimpan otomatis di *LocalStorage* setiap beberapa detik. Jika browser tidak sengaja tertutup atau halaman ter-refresh, progres pengerjaan dan sisa waktu tidak hilang.
* **Hentikan Sesi (Keluar):** Tombol pembatalan/penghentian sesi ujian kapan saja dengan konfirmasi modal yang aman.
* **Aksesibilitas & Kiosk Mode:**
  * Kontrol ukuran teks soal (`A-`, `A`, `A+`) untuk kenyamanan membaca.
  * Tombol **Layar Penuh (⛶ Fullscreen)** untuk meminimalkan distraksi saat mengerjakan ujian.
* **Acak Soal & Pilihan Jawaban:** Tersedia opsi *checkbox* untuk mengacak urutan soal (*Shuffle Questions*) dan mengacak pilihan jawaban (*Shuffle Options*) A–E.
* **Navigasi Cepat (Quick Jump):** Tombol pintas untuk langsung melompat ke sub-kategori:
  * Pada SKD: `[TWK (1-30)]`, `[TIU (31-65)]`, `[TKP (66-110)]`.
  * Pada SKB: Berdasarkan rumpun kompetensi teknis instansi.

### 3. Evaluasi & Pembahasan Mendalam
* **Skor & Kelulusan Passing Grade Otomatis:** Perhitungan nilai SKD instan mengacu pada PermenPAN-RB terbaru (TWK: min 65, TIU: min 80, TKP: min 166). Penilaian TKP menggunakan pembobotan asli skala 1–5.
* **Filter Pembahasan:** Di layar hasil, peserta dapat meninjau:
  * `Semua Soal`
  * `Hanya Jawaban Salah` (untuk evaluasi kelemahan materi)
  * `Hanya Jawaban Benar`
  * `Soal yang Ditandai Ragu-Ragu`
* **Pencarian Pembahasan Cepat:** Fitur kotak pencarian langsung untuk mencari topik atau kata kunci tertentu dari soal yang telah dikerjakan.
* **Rujukan Regulasi Jelas:** Setiap butir soal dilengkapi landasan hukum eksplisit (UU, Perpres, PermenPAN-RB, Permendagri, PMK, NIST, ISO, dll.).

### 3. Dashboard Riwayat & Statistik
* Rekapitulasi jumlah ujian yang diselesaikan, skor rata-rata, tingkat kelulusan passing grade (%), dan skor tertinggi.
* Tabel riwayat pengerjaan lengkap dengan tanggal, paket ujian, rincian skor, dan status kelulusan.

### 4. Manajemen Bank Soal (CRUD & JSON Import/Export)
* **Tambah Soal Kustom:** Form input langsung dari browser untuk menambahkan soal baru (pilihan ganda standar A–E maupun skala TKP 1–5).
* **Ekspor & Impor JSON:** Kemudahan mencadangkan bank soal atau berbagi paket soal baru antar pengguna.

---

## 📚 Struktur & Cakupan Bank Soal (766 Soal 100% Unik Bebas Duplikat)

Seluruh soal dalam aplikasi ini disusun secara sistematis berdasarkan regulasi resmi pemerintah dan standar industri, dan **telah melalui proses audit deduplikasi ketat (100% Unik, 0 Duplikat)**. Dengan mengaktifkan fitur **"🔀 Acak Urutan Soal (Shuffle Questions)"**, sistem akan mengambil sampel acak segar sesuai standar ujian BKN (SKD: 110 soal; SKB: 100 soal) sehingga simulasi setiap sesi menjadi variatif tanpa pengulangan soal yang sama:

| No | Paket Ujian | Total Bank Soal | Sampel Ujian Resmi | Alokasi Waktu | Standar Rujukan & Fokus Materi |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | **SKD Nasional (Resmi CAT BKN)** | **160 Soal** | **110 Soal** | 100 Menit | **KepmenPAN-RB No. 321/2024**:<br>• TWK 50 Soal (Pancasila, UUD 1945 Amandemen, NKRI, Sejarah Perjuangan, Tipikor KPK, Bela Negara)<br>• TIU 50 Soal (Silogisme, Analitis, Deret Angka, Aritmatika Sosial, Kecepatan, Figural)<br>• TKP 60 Soal (Pelayanan Publik, Jejaring Kerja, Sosial Budaya, TIK, Profesionalisme, Anti Radikalisme - Skala 1–5) |
| 2 | **SKB IT - Kemkomdigi** | **101 Soal** | **100 Soal** | 90 Menit | • **UU No. 27/2022 (PDP)** & **UU No. 1/2024 (ITE)**<br>• **SE Menkominfo No. 9/2023 (Etika AI)** & Permenkominfo 5/2020 (PSE Privat)<br>• Pusat Data Nasional (PDN Cloud ISO 27017), Spektrum Frekuensi 5G, DNS Filtering |
| 3 | **SKB IT - Kementerian Keuangan** | **101 Soal** | **100 Soal** | 90 Menit | • Sistem Perbendaharaan dan Anggaran Negara (**SPAN**)<br>• Pembaruan Sistem Inti Administrasi Perpajakan (**CoreTax/PSIAP**)<br>• Aplikasi **SAKTI**, Modul Penerimaan Negara (**MPN G3**), PMK No. 155/2017, ACID Database |
| 4 | **SKB IT - BSSN** | **101 Soal** | **100 Soal** | 90 Menit | • Manajemen Krisis Siber (**Perpres No. 47/2023**)<br>• Manajemen Insiden Keamanan Siber (**NIST SP 800-61 Rev 2**)<br>• Indeks KAMI BSSN, Bukti Forensik Digital (**RFC 3227**), Kriptografi Asimetris, Zero Trust |
| 5 | **SKB IT - Badan Kepegawaian Negara (BKN)** | **101 Soal** | **100 Soal** | 90 Menit | • Prosedur Seleksi CAT BKN LAN Kiosk (**Perka BKN No. 8/2022**)<br>• Manajemen Talenta ASN 9-Box Grid (**PermenPAN-RB No. 3/2020**)<br>• Sistem Informasi ASN Terintegrasi (**SIASN**), NIP 18 Digit, MyASN OAuth 2.0 |
| 6 | **SKB IT - Kemenkumham** | **101 Soal** | **100 Soal** | 90 Menit | • Paspor Elektronik & Autogate (**ICAO Doc 9303 Part 11 PA/CA**)<br>• Sistem Database Pemasyarakatan (**SDP**) & Biometrik Warga Binaan<br>• AHU Online, e-Paten DJKI, Sertifikasi Tanda Tangan Elektronik BSrE |
| 7 | **SKB IT - Pemerintah Daerah (Pemda)** | **101 Soal** | **100 Soal** | 90 Menit | • Hak Akses Data Kependudukan (**Permendagri No. 104/2019**)<br>• Pedoman Pencatatan Nama Dokumen (**Permendagri No. 73/2022**)<br>• Sistem Informasi Pemerintahan Daerah (**SIPD Permendagri 70/2019**)<br>• SIAK Terpusat Web-based & IKD di Kecamatan, Smart City 6 Dimensi |

---

## 🛠 Teknologi yang Digunakan

* **Frontend:** Pure HTML5, CSS3 (Modern Flexbox, CSS Grid, Custom CSS Variables), Vanilla JavaScript (ES6+).
* **Storage:** Browser `localStorage` API (Zero Server Setup, Privacy-Safe, Offline-Ready).
* **Generators:** Python 3 Scripting untuk perakitan bank soal berbasis struktur JSON/JS.
* **Zero Dependency:** Tanpa framework berat (React/Vue/Angular), tanpa Node.js build step yang rumit — aplikasi langsung berjalan di peramban web modern apa pun.

---

## 🚀 Panduan Instalasi & Cara Penggunaan

### 1. Penggunaan Langsung (Offline / Standalone)
Aplikasi ini dirancang *plug-and-play*:
1. Unduh atau clone repositori ini:
   ```bash
   git clone https://github.com/SKNDR25/testCPNS.git
   ```
2. Buka folder hasil clone.
3. Klik ganda file **`index.html`** untuk langsung menjalankannya di peramban favorit Anda (Google Chrome, Microsoft Edge, Mozilla Firefox, Brave, Safari, dll.).

### 2. Menjalankan via Server Lokal (Opsional)
Jika Anda ingin menjalankan aplikasi melalui web server lokal:

* **Menggunakan Python (Semua OS):**
  ```bash
  python -m http.server 8080
  ```
  Lalu buka peramban di `http://localhost:8080`.

* **Menggunakan Node.js (`npx serve`):**
  ```bash
  npx serve .
  ```

* **Menggunakan Laragon / XAMPP:**
  Pindahkan folder ini ke dalam direktori `www` (Laragon) atau `htdocs` (XAMPP), lalu akses melalui `http://localhost/testCPNS`.

---

## 💡 Panduan Fitur Aplikasi

1. **Memulai Ujian:**
   * Di Beranda, pilih kategori ujian: **SKD (Seleksi Kompetensi Dasar)** atau **SKB IT (Pilih salah satu dari 6 instansi)**.
   * Atur opsi tambahan jika diinginkan: centang *"Acak Urutan Soal"* atau *"Acak Pilihan Jawaban"*.
   * Klik **"Mulai Simulasi CAT Sekarang »"**.
2. **Saat Mengerjakan Ujian:**
   * Klik opsi jawaban A, B, C, D, atau E. Jawaban akan langsung tersimpan.
   * Gunakan tombol **"Ragu-Ragu"** jika belum yakin pada suatu soal (indikator nomor akan berwarna kuning).
   * Gunakan tombol navigasi nomor atau **"Quick Jump"** untuk berpindah antar kategori.
   * Anda dapat menggunakan tombol **`A-` / `A+`** untuk memperbesar tulisan atau **`⛶ Layar Penuh`** untuk mode kiosk.
   * Jika ada urusan mendesak, klik tombol **`⏹ Hentikan Sesi (Keluar)`** untuk menghentikan tes dan kembali ke menu utama.
3. **Melihat Hasil & Pembahasan:**
   * Klik **"Selesai Ujian"** pada nomor terakhir atau melalui sidebar.
   * Konfirmasi pada jendela dialog pop-up.
   * Hasil nilai instan, persentase ketercapaian passing grade, dan grafik performa akan ditampilkan.
   * Gulir ke bawah untuk membaca pembahasan mendalam beserta rujukan undang-undang dan standarnya.
4. **Mengelola Bank Soal & Ekspor/Impor:**
   * Buka tab **"⚙️ Kelola Bank Soal"** pada navbar atas.
   * Klik **"Tambah Soal Baru"** untuk memasukkan latihan soal buatan sendiri.
   * Klik **"Ekspor JSON"** untuk membuat backup seluruh bank soal.

---

## 📁 Struktur Direktori

```text
testCPNS/
├── index.html                 # Antarmuka web utama (Dashboard, Kiosk Exam, Result View)
├── style.css                  # Desain visual, tema resmi CAT BKN, dan tata letak responsif
├── app.js                     # Mesin logika: Timer, Shuffler, Scoring, Auto-Save, CRUD
├── data_soal.js               # Bank soal inti: 710 soal SKD & SKB IT Multi-Instansi
├── build_all_instansi_100.py  # Script master pembuat 100 soal per instansi
├── generate_bank_soal.py      # Generator paket soal SKD nasional
├── .gitignore                 # Daftar berkas yang diabaikan Git
└── README.md                  # Dokumentasi panduan instalasi dan penggunaan
```

---

## 🤝 Kontribusi & Manajemen Soal

Ingin menambahkan paket soal instansi lain (misal: Kementerian ESDM, ATR/BPN, Kejaksaan Agung) atau mengoreksi rujukan materi?
1. Fork repositori ini.
2. Buat branch fitur baru (`git checkout -b fitur/tambah-instansi`).
3. Tambahkan paket soal pada `data_soal.js` sesuai format skema data yang ada.
4. Commit perubahan Anda (`git commit -m 'Menambahkan paket soal SKB Kejaksaan'`).
5. Push ke branch (`git push origin fitur/tambah-instansi`).
6. Ajukan **Pull Request**.

---

## 📄 Lisensi

Proyek ini dirancang untuk tujuan edukasi dan persiapan seleksi aparatur sipil negara di Indonesia. Bebas digunakan, dipelajari, dan dikembangkan secara mandiri.
