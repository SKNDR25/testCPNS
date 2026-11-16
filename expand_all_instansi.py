import json

# Buka file data_soal.js yang sudah ada
with open("d:\\CPNS\\data_soal.js", "r", encoding="utf-8") as f:
    text = f.read()

# Ekstrak JSON
json_str = text.replace("/**\n * BANK SOAL MULTI-INSTANSI CAT CPNS (SKD NASIONAL & SKB SPESIFIK INSTANSI)\n */\nwindow.BANK_SOAL = ", "").rstrip(";\n")
data = json.loads(json_str)

# Tambahan Soal Kemenkeu (hingga 15 soal)
kemenkeu_more = [
    {
        "id": "kemenkeu_6", "instansi": "Kemenkeu", "category": "Basis Data & Data Warehouse", "subcategory": "ETL & OLAP",
        "question": "Kementerian Keuangan mengolah data penerimaan pajak dan bea cukai dari jutaan transaksi untuk keperluan analisis eksekutif Menteri Keuangan. Sistem basis data yang dioptimalkan khusus untuk kueri agregasi analitis berkecepatan tinggi (bukan transaksi harian) disebut...",
        "options": {
            "A": "OLTP (Online Transaction Processing)",
            "B": "OLAP (Online Analytical Processing) / Data Warehouse",
            "C": "Microsoft Access",
            "D": "Flat File CSV manual",
            "E": "SQLite lokal di komputer staf"
        },
        "answer": "B",
        "explanation": "OLAP dan Data Warehouse dirancang khusus dengan skema bintang/snowflake untuk membaca dan menganalisis tren data agregat dalam volume besar secara cepat tanpa membebani basis data transaksional (OLTP)."
    },
    {
        "id": "kemenkeu_7", "instansi": "Kemenkeu", "category": "Sistem Informasi Keuangan Negara", "subcategory": "SAKTI",
        "question": "Sistem Aplikasi Keuangan Tingkat Instansi (SAKTI) digunakan oleh seluruh Satuan Kerja (Satker) kementerian/lembaga untuk mengelola keuangan APBN. SAKTI mengintegrasikan siklus pengelolaan anggaran yang meliputi tiga tahapan utama, yaitu...",
        "options": {
            "A": "Penganggaran, Pelaksanaan, dan Pertanggungjawaban/Pelaporan",
            "B": "Peminjaman, Pengeluaran, dan Penghapusan",
            "C": "Perekrutan, Penggajian, dan Pemecatan",
            "D": "Perencanaan, Pengawasan, dan Penyitaan",
            "E": "Tender, Lelang, dan Penjualan Aset"
        },
        "answer": "A",
        "explanation": "SAKTI mengintegrasikan seluruh proses bisnis pengelolaan keuangan Satker dari hulu ke hilir: Tahap Perencanaan/Penganggaran, Tahap Pelaksanaan Anggaran (komitmen, pembayaran, bendahara), hingga Pelaporan (akuntansi & buku besar)."
    },
    {
        "id": "kemenkeu_8", "instansi": "Kemenkeu", "category": "Audit Sistem Informasi", "subcategory": "COBIT & Internal Control",
        "question": "Dalam audit sistem teknologi informasi perbendaharaan negara, pengendalian internal yang berfungsi mendeteksi anomali atau ketidakwajaran saat transaksi berlangsung (misalnya deteksi duplikasi nomor rekening penerima bantuan) disebut...",
        "options": {
            "A": "Preventive Control (Pengendalian Pencegahan)",
            "B": "Detective Control (Pengendalian Pendeteksian)",
            "C": "Corrective Control (Pengendalian Pemulihan)",
            "D": "Compensating Control",
            "E": "Physical Control"
        },
        "answer": "B",
        "explanation": "Detective Control bertugas menemukan dan mengidentifikasi kesalahan, anomali, atau kecurangan sesaat setelah atau saat peristiwa tersebut terjadi, memicu peringatan untuk penanganan lebih lanjut."
    },
    {
        "id": "kemenkeu_9", "instansi": "Kemenkeu", "category": "Keamanan Finansial", "subcategory": "Non-Repudiation & Audit Trail",
        "question": "Untuk mencegah pejabat penandatangan Surat Perintah Membayar (SPM) menyangkal bahwa ia telah menyetujui pencairan dana negara miliaran rupiah, sistem aplikasi keuangan negara menerapkan prinsip...",
        "options": {
            "A": "Nir-penyangkalan (Non-repudiation) dengan Tanda Tangan Elektronik Tersertifikasi dan Timestamping",
            "B": "Pemberian cap stempel basah di atas layar monitor",
            "C": "Konfirmasi lisan via panggilan telepon santai",
            "D": "Penggunaan akun bersama (shared account) satu ruangan",
            "E": "Penghapusan log login setiap malam hari"
        },
        "answer": "A",
        "explanation": "Non-repudiation memastikan pihak pengirim/penyetuju transaksi tidak dapat menyangkal tindakannya berkat sertifikat digital unik, kunci privat, dan catatan audit trail yang sah secara hukum."
    },
    {
        "id": "kemenkeu_10", "instansi": "Kemenkeu", "category": "Arsitektur High Availability", "subcategory": "Load Balancing",
        "question": "Portal pelaporan SPT Tahunan daring (e-Filing Pajak) mengalami lonjakan akses hingga jutaan wajib pajak secara bersamaan pada akhir bulan Maret. Teknik arsitektur server yang membagi lalu lintas request secara merata ke puluhan server web di backend disebut...",
        "options": {
            "A": "Load Balancing",
            "B": "Overclocking Processor",
            "C": "Disk Defragmentation",
            "D": "Port Forwarding tunggal",
            "E": "Peer-to-Peer Sharing"
        },
        "answer": "A",
        "explanation": "Load Balancer mendistribusikan beban lalu lintas jaringan secara cerdas (algoritma Round Robin, Least Connections, dll.) ke beberapa web server farm untuk mencegah kegagalan satu titik (single point of failure) saat lonjakan traffic."
    }
]

# Tambahan Soal BSSN (hingga 15 soal)
bssn_more = [
    {
        "id": "bssn_6", "instansi": "BSSN", "category": "Analisis Malware", "subcategory": "Sandbox & Reverse Engineering",
        "question": "Seorang analis keamanan siber BSSN mendapatkan sampel berkas executable (.exe) mencurigakan yang diduga sebagai ransomware penyandera data pemerintah. Metode analisis dinamis yang aman untuk mengamati perilaku berkas tersebut tanpa membahayakan jaringan riil adalah...",
        "options": {
            "A": "Menjalankan berkas tersebut di lingkungan Virtual Machine terisolasi (Sandbox)",
            "B": "Mengeklik berkas langsung di komputer server produksi",
            "C": "Mengirimkan berkas tersebut via email ke seluruh pegawai instansi",
            "D": "Mengunggah berkas ke website publik kantor",
            "E": "Mencetak kode biner berkas di atas kertas"
        },
        "answer": "A",
        "explanation": "Dynamic Malware Analysis dilakukan di dalam lingkungan Sandbox (VM terisolasi tanpa akses ke jaringan produksi) untuk memantau aktivitas proses, modifikasi registry, dan koneksi command-and-control (C2) secara aman."
    },
    {
        "id": "bssn_7", "instansi": "BSSN", "category": "Keamanan Jaringan & Web", "subcategory": "Man-in-the-Middle (MitM)",
        "question": "Serangan siber di mana peretas menyusup di antara komunikasi peramban pengguna dan server web pemerintah dengan memalsukan Certificate Authority (CA) sehingga seluruh data sensitif dapat didekripsi disebut...",
        "options": {
            "A": "Man-in-the-Middle (MitM) Attack",
            "B": "Brute Force Attack",
            "C": "Buffer Overflow",
            "D": "SQL Injection",
            "E": "DDoS Amplification"
        },
        "answer": "A",
        "explanation": "MitM Attack terjadi ketika penyerang memposisikan dirinya di tengah aliran komunikasi antara dua pihak untuk menyadap, mencuri, atau memanipulasi data yang sedang transit (in-transit)."
    },
    {
        "id": "bssn_8", "instansi": "BSSN", "category": "Kriptografi & Hashing", "subcategory": "Salt & Password Hashing",
        "question": "Dalam menyimpan password pengguna pada basis data aplikasi sistem informasi instansi, praktik keamanan terbaik yang direkomendasikan BSSN adalah...",
        "options": {
            "A": "Menyimpan password dalam bentuk teks terbuka (Plaintext)",
            "B": "Menggunakan fungsi hash kriptografis yang lambat dan aman dengan penambahan garam unik (Salted Hash) seperti bcrypt atau Argon2",
            "C": "Menyimpan dalam format MD5 tanpa salt",
            "D": "Mengenkripsi menggunakan kode Caesar Cipher sederhana",
            "E": "Menyimpan password di file teks catatan di desktop admin"
        },
        "answer": "B",
        "explanation": "Fungsi hashing adaptif modern seperti bcrypt atau Argon2 yang dipadukan dengan Salt (string acak unik) melindungi password dari serangan Rainbow Table dan cracking berbasis akselerasi GPU."
    },
    {
        "id": "bssn_9", "instansi": "BSSN", "category": "Tata Kelola Keamanan Informasi", "subcategory": "ISO/IEC 27001",
        "question": "Standar internasional mengenai Sistem Manajemen Keamanan Informasi (SMKI) yang diwajibkan oleh BSSN untuk diterapkan pada seluruh Penyelenggara Infrastruktur Informasi Vital (IIV) adalah...",
        "options": {
            "A": "ISO/IEC 27001",
            "B": "ISO 9001",
            "C": "ISO 14001",
            "D": "ISO 45001",
            "E": "ISO 22000"
        },
        "answer": "A",
        "explanation": "ISO/IEC 27001 adalah standar global baku untuk merancang, mengimplementasikan, memelihara, dan terus meningkatkan Sistem Manajemen Keamanan Informasi (Information Security Management System - ISMS)."
    },
    {
        "id": "bssn_10", "instansi": "BSSN", "category": "Penetration Testing & Red Teaming", "subcategory": "Zero-Day Vulnerability",
        "question": "Istilah dalam keamanan siber untuk kerentanan perangkat lunak yang belum diketahui oleh pengembangnya atau belum memiliki patch/tambalan resmi saat serangan terjadi dinamakan...",
        "options": {
            "A": "Zero-Day Vulnerability",
            "B": "Legacy Bug",
            "C": "Open Source Glitch",
            "D": "False Positive",
            "E": "Deprecated Feature"
        },
        "answer": "A",
        "explanation": "Zero-Day Vulnerability adalah celah keamanan baru yang belum dipublikasikan atau belum memiliki perbaikan keamanan (patch) dari vendor pengembang, sehingga memiliki tingkat risiko eksploitasi yang sangat tinggi."
    }
]

# Tambahan Soal BKN (hingga 15 soal)
bkn_more = [
    {
        "id": "bkn_6", "instansi": "BKN", "category": "Arsitektur Sistem CAT", "subcategory": "Integritas & Anti-Joki",
        "question": "Pada pelaksanaan seleksi CPNS di titik lokasi (tilok) BKN, sistem registrasi peserta dilengkapi dengan teknologi pemindai wajah (Face Recognition) yang dicocokkan langsung dengan database Dukcapil. Tujuan utama penerapan fitur ini adalah...",
        "options": {
            "A": "Membuat foto peserta untuk kartu ucapan selamat",
            "B": "Mencegah praktik perjokian dan memastikan bahwa orang yang duduk di kursi ujian adalah pelamar yang sesungguhnya",
            "C": "Mengukur suhu tubuh peserta yang sedang sakit",
            "D": "Menentukan urutan tempat duduk peserta secara alfabetis",
            "E": "Mendeteksi tingkat ketegangan psikologis peserta"
        },
        "answer": "B",
        "explanation": "Face Recognition pada tahap registrasi pra-ujian CAT BKN bertujuan memvalidasi keaslian identitas peserta secara biometrik dengan data KTP/Dukcapil untuk mengeliminasi potensi joki ujian."
    },
    {
        "id": "bkn_7", "instansi": "BKN", "category": "Sistem Informasi ASN (SIASN)", "subcategory": "Kenaikan Pangkat Otomatis (KPO)",
        "question": "Layanan Kenaikan Pangkat Otomatis (KPO) dan Penetapan Pensiun Otomatis (PPO) pada SIASN BKN memanfaatkan mekanisme pertukaran data tanpa kertas (paperless). Konsep rekayasa perangkat lunak yang memungkinkan data SK Jabatan dari daerah langsung terverifikasi tanpa entri ulang di pusat adalah...",
        "options": {
            "A": "Interoperabilitas Data Berbasis API dan Dokumen Digital Terotentikasi",
            "B": "Pengiriman fotokopi berkas legalisir basah via kantor pos",
            "C": "Pengunggahan foto selfie pejabat ke media sosial",
            "D": "Pencetakan berkas di kertas karbon rangkap tiga",
            "E": "Penggunaan mesin faks manual"
        },
        "answer": "A",
        "explanation": "KPO dan PPO memanfaatkan integrasi API antara SIMPEG Instansi Daerah dengan SIASN BKN, di mana berkas PDF telah ditandatangani secara digital (TTE) sehingga validasi berlangsung otomatis dan paperless."
    },
    {
        "id": "bkn_8", "instansi": "BKN", "category": "Basis Data ASN", "subcategory": "Integritas Relasional & Foreign Key",
        "question": "Pada basis data kepegawaian nasional BKN, tabel 'riwayat_pendidikan' terhubung dengan tabel utama 'pegawai' melalui kolom 'nip'. Untuk mencegah penghapusan data pegawai yang masih memiliki riwayat pendidikan aktif secara tidak sengaja, aturan constraint yang diterapkan pada Foreign Key adalah...",
        "options": {
            "A": "ON DELETE RESTRICT (atau ON DELETE NO ACTION)",
            "B": "ON DELETE CASCADE tanpa konfirmasi",
            "C": "DROP DATABASE",
            "D": "TRUNCATE TABLE",
            "E": "ALLOW NULL bebas"
        },
        "answer": "A",
        "explanation": "Constraint ON DELETE RESTRICT menolak operasi penghapusan pada record induk jika masih ada record anak (child) yang merujuk kepadanya, menjaga integritas referensial data penting."
    },
    {
        "id": "bkn_9", "instansi": "BKN", "category": "Arsitektur Kiosk Mode", "subcategory": "CAT Browser Lockdown",
        "question": "Aplikasi client CAT BKN yang berjalan di komputer peserta dikonfigurasi dalam mode 'Kiosk / Lockdown Browser'. Fitur pengamanan utama dari browser jenis ini adalah...",
        "options": {
            "A": "Memungkinkan peserta browsing internet dan membuka WhatsApp",
            "B": "Mengunci akses desktop, menonaktifkan tombol pintas (Alt+Tab, Ctrl+C, WinKey), dan memblokir aplikasi lain agar peserta fokus hanya pada layar ujian",
            "C": "Mempercepat koneksi game online di komputer peserta",
            "D": "Menghapus sistem operasi Windows setiap kali ujian selesai",
            "E": "Menyembunyikan soal ujian dari monitor peserta"
        },
        "answer": "B",
        "explanation": "Kiosk/Lockdown Browser mengisolasi lingkungan pengujian: mencegah peralihan tab, mematikan fungsi clipboard, memblokir hotkey sistem operasi, dan mendeteksi multi-display untuk menjaga kejujuran ujian."
    },
    {
        "id": "bkn_10", "instansi": "BKN", "category": "Manajemen Layanan TI", "subcategory": "Helpdesk & Service Desk",
        "question": "BKN mengoperasikan portal Helpdesk SSCASN untuk menangani ribuan kendala pelamar (NIK tidak ditemukan, salah akreditasi, data ganda). Metrik SLA (Service Level Agreement) yang mengukur kecepatan waktu petugas merespons tiket pertama kali disebut...",
        "options": {
            "A": "First Response Time (FRT)",
            "B": "Mean Time to Failure (MTTF)",
            "C": "Bandwidth Utilization",
            "D": "Ping RTT",
            "E": "Clock Speed"
        },
        "answer": "A",
        "explanation": "First Response Time (FRT) adalah durasi waktu dari saat tiket keluhan diajukan oleh pengguna hingga staf helpdesk memberikan tanggapan/solusi pertama kali."
    }
]

# Tambahan Soal Kumham (hingga 15 soal)
kumham_more = [
    {
        "id": "kumham_6", "instansi": "Kemenkumham", "category": "Sistem Informasi Keimigrasian", "subcategory": "Visa on Arrival Online (e-VoA)",
        "question": "Layanan e-VoA (Electronic Visa on Arrival) di Ditjen Imigrasi Kemenkumham memproses pembayaran penerimaan negara bukan pajak (PNBP) visa turis asing secara real-time. Standar protokol pembayaran internasional yang wajib dipenuhi oleh sistem gateway pembayaran kartu kredit tersebut adalah...",
        "options": {
            "A": "PCI-DSS (Payment Card Industry Data Security Standard)",
            "B": "SNI Mainan Anak",
            "C": "ISO 14001 Manajemen Lingkungan",
            "D": "Gaya Penulisan APA",
            "E": "Sertifikat Halal"
        },
        "answer": "A",
        "explanation": "PCI-DSS adalah standar keamanan internasional wajib bagi setiap sistem pemrosesan transaksi kartu pembayaran (Visa, Mastercard, JCB) untuk melindungi data pemegang kartu dari kebocoran."
    },
    {
        "id": "kumham_7", "instansi": "Kemenkumham", "category": "Sistem Database Pemasyarakatan", "subcategory": "Biometrik Tahanan",
        "question": "Di dalam lapas dan rutan, sistem identifikasi narapidana menggunakan pemindai biometrik sidik jari AFIS (Automated Fingerprint Identification System). Standar format digital internasional untuk interoperabilitas data sidik jari antar-penegak hukum (Polri, Kejaksaan, Kemenkumham) adalah...",
        "options": {
            "A": "ANSI/NIST-ITL atau WSQ (Wavelet Scalar Quantization)",
            "B": "MP3 Audio",
            "C": "GIF Animasi",
            "D": "RTF Document",
            "E": "AVI Video"
        },
        "answer": "A",
        "explanation": "Format kompresi WSQ dan standar ANSI/NIST-ITL dirancang khusus oleh FBI dan NIST untuk menyimpan dan mengompres citra sidik jari resolusi tinggi (500 DPI) tanpa kehilangan detail minutiae kunci."
    },
    {
        "id": "kumham_8", "instansi": "Kemenkumham", "category": "Sistem AHU Online", "subcategory": "High Traffic & Concurrency",
        "question": "Notaris di seluruh Indonesia mengakses AHU Online secara serentak setiap pagi hari untuk memesan nama perseroan terbatas (PT). Untuk mencegah dua notaris memesan nama perusahaan perseroan yang sama persis pada detik yang bersamaan, mekanisme basis data yang wajib diimplementasikan adalah...",
        "options": {
            "A": "Database Locking (Pessimistic / Optimistic Locking) dan Unique Constraint pada kolom nama_pt",
            "B": "Menghapus database setiap 10 menit",
            "C": "Membiarkan data ganda tersimpan lalu dihapus manual bulan depan",
            "D": "Meminta notaris melempar koin undian",
            "E": "Mematikan koneksi internet notaris yang kedua"
        },
        "answer": "A",
        "explanation": "Concurrency Control dengan mekanisme locking dan Unique Constraint di level basis data memastikan integritas transaksi: transaksi pertama mengunci nama, dan transaksi kedua otomatis ditolak karena nama sudah dipesan."
    },
    {
        "id": "kumham_9", "instansi": "Kemenkumham", "category": "Jaringan & Infrastruktur", "subcategory": "CCTV & IoT Pengawasan Lapas",
        "question": "Sistem CCTV pemantauan cerdas di Lembaga Pemasyarakatan Kemenkumham dilengkapi fitur analitik video pintar (Smart Video Analytics). Kemampuan AI yang paling berguna untuk mencegah pelarian warga binaan pada malam hari adalah...",
        "options": {
            "A": "Virtual Perimeter Intrusion Detection (Deteksi Penyeberangan Garis Batas Pagar)",
            "B": "Perekaman video gerak lambat untuk film hiburan",
            "C": "Pemutaran musik otomatis di lorong",
            "D": "Pembersihan lensa kamera otomatis setiap detik",
            "E": "Pengubahan warna video menjadi hitam putih"
        },
        "answer": "A",
        "explanation": "Virtual Perimeter Intrusion Detection dan Tripwire Analytics secara otomatis membunyikan alarm peringatan di ruang kontrol seketika ada objek manusia melintasi batas pagar terlarang pada jam istirahat malam."
    },
    {
        "id": "kumham_10", "instansi": "Kemenkumham", "category": "Kekayaan Intelektual", "subcategory": "Manajemen Arsip Dokumen Digital",
        "question": "Sistem e-Paten di Ditjen Kekayaan Intelektual menyimpan jutaan berkas gambar teknik dan deskripsi invensi dalam format PDF/A. Keunggulan format PDF/A (Archival) dibandingkan format PDF standar untuk preservasi dokumen jangka panjang adalah...",
        "options": {
            "A": "Font, gambar, dan profil warna tertanam secara mandiri (self-contained) sehingga dokumen dijamin dapat dibuka identik puluhan tahun ke depan tanpa bergantung font luar",
            "B": "Ukurannya selalu di bawah 1 KB",
            "C": "Dapat mengedit teks otomatis dengan kecerdasan buatan",
            "D": "Menghapus file secara otomatis setelah 5 tahun",
            "E": "Hanya bisa dibuka di perangkat smartphone tertentu"
        },
        "answer": "A",
        "explanation": "PDF/A (ISO 19005) adalah varian PDF khusus pengarsipan digital jangka panjang yang melarang fitur eksternal (font eksternal, javascript) demi menjamin keterbacaan dokumen hingga puluhan tahun mendatang."
    }
]

# Tambahan Soal Pemda (hingga 15 soal)
pemda_more = [
    {
        "id": "pemda_6", "instansi": "Pemerintah Daerah", "category": "Pengelolaan Jaringan Daerah", "subcategory": "Metropolitan Area Network (MAN)",
        "question": "Dinas Kominfo Pemda membangun jaringan intra-pemerintah daerah (Intranet Pemda) yang menghubungkan seluruh kantor dinas, kecamatan, hingga puskesmas dalam satu wilayah kota. Skala cakupan jaringan komputer ini diklasifikasikan sebagai...",
        "options": {
            "A": "PAN (Personal Area Network)",
            "B": "LAN (Local Area Network)",
            "C": "MAN (Metropolitan Area Network)",
            "D": "WAN Global",
            "E": "SAN (Storage Area Network)"
        },
        "answer": "C",
        "explanation": "MAN (Metropolitan Area Network) mencakup wilayah geografis seluas satu kota atau kabupaten, mengintegrasikan berbagai jaringan lokal (LAN) OPD menjadi satu jaringan intra-pemerintah daerah."
    },
    {
        "id": "pemda_7", "instansi": "Pemerintah Daerah", "category": "Smart City & Geospasial", "subcategory": "WebGIS Pemda",
        "question": "Pemerintah Daerah memanfaatkan WebGIS (Sistem Informasi Geografis berbasis web) untuk pemetaan zona tata ruang (RTRW), sebaran titik kemiskinan, dan Pajak Bumi dan Bangunan (PBB). Format data spasial vektor yang paling umum digunakan dalam pertukaran data WebGIS adalah...",
        "options": {
            "A": "GeoJSON atau Shapefile (.shp)",
            "B": "MP4 Video",
            "C": "WAV Audio",
            "D": "EXE Application",
            "E": "DOCX Word"
        },
        "answer": "A",
        "explanation": "GeoJSON dan Shapefile (.shp) adalah format standar terbuka untuk merepresentasikan fitur geografis berupa titik (point), garis (linestring), dan poligon (polygon) beserta atribut datanya pada aplikasi peta digital."
    },
    {
        "id": "pemda_8", "instansi": "Pemerintah Daerah", "category": "Sistem Informasi Manajemen Kepegawaian Daerah", "subcategory": "Absensi Geotagging & Spoofing",
        "question": "Aplikasi absensi ASN mobile yang dikembangkan Diskominfo Pemda kerap dicurangi pegawai nakal dengan menggunakan aplikasi Fake GPS (lokasi palsu). Teknik pengamanan perangkat lunak yang paling efektif untuk mencegah manipulasi lokasi ini adalah...",
        "options": {
            "A": "Mendeteksi flag 'Mock Location' di sistem operasi Android, mengecek integritas status root/jailbreak, dan memverifikasi BSSID sinyal Wi-Fi kantor",
            "B": "Menghapus aplikasi kamera di ponsel pegawai",
            "C": "Menyuruh pegawai mengirim foto selfie via SMS",
            "D": "Menyita smartphone seluruh ASN",
            "E": "Mematikan GPS satelit kota"
        },
        "answer": "A",
        "explanation": "Aplikasi mobile modern mendeteksi status mock location API pada Android SDK, memeriksa integritas runtime (Root detection), serta memvalidasi kesesuaian lokasi GPS dengan BSSID Wi-Fi resmi kantor."
    },
    {
        "id": "pemda_9", "instansi": "Pemerintah Daerah", "category": "Layanan Kependudukan", "subcategory": "Identitas Kependudukan Digital (IKD)",
        "question": "Aplikasi Identitas Kependudukan Digital (IKD / KTP Digital) yang diterapkan Disdukcapil Pemda menampilkan data KTP, KK, dan akta kelahiran di smartphone warga. Protokol keamanan yang digunakan untuk melindungi transmisi QR Code verifikasi identitas agar tidak mudah disalin penipu adalah...",
        "options": {
            "A": "Time-based Dynamic QR Code (QR Code yang berganti otomatis setiap 90 detik dan terenkripsi)",
            "B": "QR Code statis dicetak di stiker kertas",
            "C": "Foto KTP biasa tanpa enkripsi",
            "D": "Nomor NIK ditulis dengan spidol di layar",
            "E": "Tangkapan layar (screenshot) bebas"
        },
        "answer": "A",
        "explanation": "Dynamic QR Code pada IKD memiliki masa kedaluwarsa singkat (time-to-live) dan data payload terenkripsi, mencegah tangkapan layar (screenshot) digunakan oleh pihak yang tidak berhak."
    },
    {
        "id": "pemda_10", "instansi": "Pemerintah Daerah", "category": "Tata Kelola SPBE Pemda", "subcategory": "Evaluasi SPBE KemenPANRB",
        "question": "Dalam Evaluasi Sistem Pemerintahan Berbasis Elektronik (SPBE) yang dinilai setiap tahun oleh KemenPANRB, predikat 'Sangat Baik' (Indeks > 3.5) pada instansi Pemerintah Daerah mencerminkan bahwa...",
        "options": {
            "A": "Pemda memiliki ratusan aplikasi terpisah yang dibuat oleh setiap dinas tanpa integrasi",
            "B": "Layanan SPBE Pemda telah terpadu (terintegrasi antar-OPD), terukur kinerjanya, memiliki tata kelola kolaboratif, dan berdampak nyata bagi kepuasan masyarakat",
            "C": "Pemda membeli server termahal tanpa ada yang menggunakannya",
            "D": "Seluruh pegawai Pemda memiliki akun media sosial resmi",
            "E": "Pemda tidak lagi menggunakan komputer dalam bekerja"
        },
        "answer": "B",
        "explanation": "Indeks SPBE tinggi mengukur tingkat kematangan (maturity level) integrasi layanan, keterpaduan tata kelola, kebijakan internal, dan efektivitas layanan digital bagi publik (bukan jumlah banyaknya aplikasi yang terfragmentasi)."
    }
]

# Masukkan ke dalam dictionary
data["skb_kemenkeu"]["questions"].extend(kemenkeu_more)
data["skb_bssn"]["questions"].extend(bssn_more)
data["skb_bkn"]["questions"].extend(bkn_more)
data["skb_kemenkumham"]["questions"].extend(kumham_more)
data["skb_pemda"]["questions"].extend(pemda_more)

# Pastikan setiap soal memiliki points default
for key in data:
    for q in data[key]["questions"]:
        if "points" not in q:
            ans = q["answer"]
            q["points"] = {opt: (5 if opt == ans else 0) for opt in ["A", "B", "C", "D", "E"]}

js_content = "/**\n * BANK SOAL MULTI-INSTANSI CAT CPNS (SKD NASIONAL & SKB SPESIFIK INSTANSI)\n */\nwindow.BANK_SOAL = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"

with open("d:\\CPNS\\data_soal.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Update berhasil!")
for k, v in data.items():
    print(f"- [{k}] {v['title']}: {len(v['questions'])} soal")
