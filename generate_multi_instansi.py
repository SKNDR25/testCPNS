import json

# ==============================================================================
# SCRIPT GENERATOR BANK SOAL MULTI-INSTANSI UNTUK CAT CPNS
# Memproduksi:
# 1. SKD Nasional (110 Soal Penuh Standar BKN)
# 2. SKB IT Spesifik Instansi:
#    - Kementerian Keuangan (Kemenkeu)
#    - Badan Siber dan Sandi Negara (BSSN)
#    - Kementerian Komunikasi dan Digital (Kemkomdigi)
#    - Badan Kepegawaian Negara (BKN)
#    - Kementerian Hukum dan HAM (Kemenkumham)
#    - Pemerintah Daerah (Pemprov / Pemkab / Pemkot)
# ==============================================================================

# Baca dulu 110 Soal SKD dari generator sebelumnya agar tetap utuh dan lengkap
from generate_bank_soal import all_skd_questions

instansi_packets = {
    # -------------------------------------------------------------
    # 1. KEMENTERIAN KEUANGAN (KEMENKEU)
    # Fokus: Sistem Perbendaharaan (SPAN), Core Tax Administration System (CTAS),
    # Keamanan Finansial, Integritas Transaksi ACID, Arsitektur Big Data Fiskal
    # -------------------------------------------------------------
    "skb_kemenkeu": {
        "title": "SKB IT - Kementerian Keuangan (Kemenkeu)",
        "instansi": "Kementerian Keuangan RI",
        "description": "Fokus pengujian: Sistem Perbendaharaan dan Anggaran Negara (SPAN), Core Tax, Transaksi Finansial (ACID), Audit TI, dan Keamanan Data Pajak/Bea Cukai.",
        "timeMinutes": 90,
        "passingGrades": {"total": 0},
        "questions": [
            {
                "id": "kemenkeu_1", "instansi": "Kemenkeu", "category": "Sistem Informasi Keuangan Negara", "subcategory": "SPAN & MPN",
                "question": "Dalam arsitektur Sistem Perbendaharaan dan Anggaran Negara (SPAN) di Kementerian Keuangan, modul yang bertanggung jawab memastikan bahwa setiap pengeluaran anggaran negara tidak melebihi alokasi Daftar Isian Pelaksanaan Anggaran (DIPA) yang telah ditetapkan adalah...",
                "options": {
                    "A": "Modul Komitmen (Commitment Management)",
                    "B": "Modul Pembayaran (Payment Management)",
                    "C": "Modul Kas (Cash Management)",
                    "D": "Modul Piutang (Receivables Management)",
                    "E": "Modul Buku Besar dan Pelaporan (General Ledger)"
                },
                "answer": "A",
                "explanation": "Modul Komitmen pada SPAN bertugas mengunci alokasi pagu anggaran sebelum kontrak atau pesanan diterbitkan, sehingga mencegah terjadinya pengeluaran yang melebihi batas DIPA (defisit pagu)."
            },
            {
                "id": "kemenkeu_2", "instansi": "Kemenkeu", "category": "Manajemen Basis Data Transaksional", "subcategory": "ACID Properties",
                "question": "Sistem Pembayaran Pajak Online Kemenkeu harus memastikan bahwa pemotongan saldo rekening wajib pajak dan pencatatan kas penerimaan negara terjadi secara simultan dan tidak boleh terjadi kondisi uang terpotong namun status belum terbayar. Prinsip ACID yang paling krusial menjamin hal ini adalah...",
                "options": {
                    "A": "Atomicity",
                    "B": "Consistency",
                    "C": "Isolation",
                    "D": "Durability",
                    "E": "Scalability"
                },
                "answer": "A",
                "explanation": "Prinsip Atomicity (All or Nothing) menjamin bahwa seluruh rangkaian operasi transaksi harus berhasil seutuhnya, atau jika terjadi kegagalan di tengah jalan, seluruh operasi akan di-rollback ke kondisi awal."
            },
            {
                "id": "kemenkeu_3", "instansi": "Kemenkeu", "category": "Rekayasa Sistem Informasi Perpajakan", "subcategory": "Core Tax System",
                "question": "Dalam implementasi Pembaruan Sistem Inti Administrasi Perpajakan (PSIAP/Core Tax Administration System) di Ditjen Pajak Kemenkeu, konsep interoperabilitas data pihak ketiga (ILAP - Instansi, Lembaga, Asosiasi, dan Pihak Lain) diwujudkan melalui arsitektur...",
                "options": {
                    "A": "Pengiriman berkas fisik bertanda tangan basah setiap akhir tahun",
                    "B": "Penyalinan basis data secara manual menggunakan media penyimpanan USB",
                    "C": "Enterprise Service Bus (ESB) dan RESTful API Gateway yang aman dengan enkripsi pertukaran data end-to-end",
                    "D": "Pengunggahan data lewat email publik tanpa otentikasi",
                    "E": "Menyatukan seluruh server perbankan ke dalam satu ruang server fisik Ditjen Pajak"
                },
                "answer": "C",
                "explanation": "Interoperabilitas data pihak ketiga pada Core Tax Kemenkeu memanfaatkan API Gateway dan ESB dengan protokol enkripsi tinggi untuk pertukaran data finansial secara otomatis, aman, dan standar."
            },
            {
                "id": "kemenkeu_4", "instansi": "Kemenkeu", "category": "Keamanan Data Finansial", "subcategory": "Kriptografi & PCI-DSS",
                "question": "Untuk melindungi data nomor rekening dan riwayat transaksi wajib pajak saat disimpan di basis data server Kemenkeu (Data-at-Rest), standar enkripsi simetris yang direkomendasikan secara global adalah...",
                "options": {
                    "A": "DES 56-bit",
                    "B": "AES-256 (Advanced Encryption Standard)",
                    "C": "MD5 Hashing",
                    "D": "Base64 Encoding",
                    "E": "ROT13"
                },
                "answer": "B",
                "explanation": "AES-256 adalah standar emas enkripsi simetris yang sangat aman dan menjadi standar industri keuangan serta instansi pertahanan untuk melindungi Data-at-Rest. MD5 dan Base64 bukan algoritma enkripsi yang aman."
            },
            {
                "id": "kemenkeu_5", "instansi": "Kemenkeu", "category": "Audit & Tata Kelola TI", "subcategory": "Disaster Recovery",
                "question": "Pusat Data dan Teknologi Informasi (Pusentei) Kemenkeu menetapkan bahwa jika terjadi bencana pada data center utama, sistem transaksi APBN harus dapat kembali beroperasi dalam waktu maksimal 30 menit dengan kehilangan data maksimal 5 menit transaksi terakhir. Parameter '30 menit' dan '5 menit' tersebut secara berturut-turut disebut...",
                "options": {
                    "A": "RPO (Recovery Point Objective) dan RTO (Recovery Time Objective)",
                    "B": "RTO (Recovery Time Objective) dan RPO (Recovery Point Objective)",
                    "C": "MTBF (Mean Time Between Failures) dan MTTR",
                    "D": "SLA (Service Level Agreement) dan OLA",
                    "E": "Throughput dan Latency"
                },
                "answer": "B",
                "explanation": "RTO (Recovery Time Objective) adalah batas waktu maksimal pemulihan sistem setelah insiden (30 menit). RPO (Recovery Point Objective) adalah batas toleransi kehilangan data diukur dalam rentang waktu kejadian (5 menit)."
            }
        ]
    },

    # -------------------------------------------------------------
    # 2. BADAN SIBER DAN SANDI NEGARA (BSSN)
    # Fokus: Keamanan Siber Nasional, Incident Response (CSIRT), Kriptografi,
    # Forensik Digital, Analisis Malware, Penetration Testing, ISO 27001
    # -------------------------------------------------------------
    "skb_bssn": {
        "title": "SKB IT - Badan Siber dan Sandi Negara (BSSN)",
        "instansi": "Badan Siber dan Sandi Negara (BSSN)",
        "description": "Fokus pengujian: Computer Security Incident Response Team (CSIRT), Kriptografi, Forensik Digital, Penetrasi Jaringan, Deteksi Kerentanan, dan Keamanan Infrastruktur Informasi Vital.",
        "timeMinutes": 90,
        "passingGrades": {"total": 0},
        "questions": [
            {
                "id": "bssn_1", "instansi": "BSSN", "category": "Incident Response & CSIRT", "subcategory": "NIST SP 800-61",
                "question": "Berdasarkan pedoman penanganan insiden siber NIST SP 800-61 yang diadopsi oleh Tim Tanggap Insiden Siber BSSN (Pusat Kontak Siber CSIRT), urutan tahapan penanganan insiden siber yang benar adalah...",
                "options": {
                    "A": "Detection -> Preparation -> Eradication -> Containment -> Recovery",
                    "B": "Preparation -> Detection & Analysis -> Containment, Eradication & Recovery -> Post-Incident Activity",
                    "C": "Containment -> Analysis -> Preparation -> Eradication -> Reporting",
                    "D": "Recovery -> Eradication -> Detection -> Preparation -> Audit",
                    "E": "Investigation -> Arrest -> Patching -> Reporting"
                },
                "answer": "B",
                "explanation": "Siklus hidup penanganan insiden standar NIST dan BSSN meliputi 4 fase utama: 1. Preparation, 2. Detection and Analysis, 3. Containment, Eradication, and Recovery, 4. Post-Incident Activity (Lessons Learned)."
            },
            {
                "id": "bssn_2", "instansi": "BSSN", "category": "Kriptografi & Persandian", "subcategory": "Asymmetric Key & Digital Signature",
                "question": "Dalam skema tanda tangan elektronik tersertifikasi (Balai Sertifikasi Elektronik / BSrE BSSN), untuk membuktikan keaslian dokumen dan nir-penyangkalan (non-repudiation), dokumen ditandatangani menggunakan...",
                "options": {
                    "A": "Kunci Publik (Public Key) penandatangan",
                    "B": "Kunci Privat (Private Key) penandatangan",
                    "C": "Kunci Publik penerima dokumen",
                    "D": "Kunci Rahasia bersama (Pre-shared key)",
                    "E": "Sertifikat SSL milik browser penerima"
                },
                "answer": "B",
                "explanation": "Tanda tangan digital dibentuk dengan mengenkripsi hash dokumen menggunakan Kunci Privat milik pemilik sertifikat. Pihak lain memverifikasi keabsahannya menggunakan Kunci Publik milik penandatangan."
            },
            {
                "id": "bssn_3", "instansi": "BSSN", "category": "Forensik Digital", "subcategory": "Chain of Custody & RAM Dump",
                "question": "Ketika seorang analis forensik siber BSSN menangani sebuah server yang sedang aktif diserang peretas, urutan pengambilan bukti digital berdasarkan prinsip 'Order of Volatility' (dari yang paling mudah menguap/hilang) adalah...",
                "options": {
                    "A": "Harddisk HDD -> Flashdisk -> RAM -> Log Firewall",
                    "B": "Register CPU & Cache -> Memori RAM -> Status Jaringan & Routing Table -> File Disk -> Media Backup",
                    "C": "File Disk -> RAM -> BIOS Config -> Kabel Jaringan",
                    "D": "Backup Tape -> Register CPU -> Harddisk -> RAM",
                    "E": "Rekaman CCTV -> Memory RAM -> CPU -> Harddisk"
                },
                "answer": "B",
                "explanation": "Order of Volatility (RFC 3227): Bukti yang paling mudah hilang harus diamankan terlebih dahulu: 1. Register/Cache, 2. Memory RAM, 3. Routing table & ARP cache, 4. Temporary file system, 5. Disk storage, 6. Backup tape."
            },
            {
                "id": "bssn_4", "instansi": "BSSN", "category": "Keamanan Jaringan & Pertahanan", "subcategory": "Firewall & IDS/IPS",
                "question": "Perangkat keamanan jaringan yang tidak hanya menganalisis port dan IP header, melainkan mampu menginspeksi muatan data pada Application Layer (Layer 7) untuk mendeteksi serangan injeksi SQL atau signature malware secara real-time disebut...",
                "options": {
                    "A": "Packet Filtering Firewall Tradisional",
                    "B": "Circuit-level Gateway",
                    "C": "Next-Generation Firewall (NGFW) / Deep Packet Inspection",
                    "D": "Network Address Translation (NAT) Router",
                    "E": "Unmanaged Switch"
                },
                "answer": "C",
                "explanation": "Next-Generation Firewall (NGFW) menggabungkan firewall konvensional dengan kemampuan Deep Packet Inspection (DPI), Intrusion Prevention System (IPS), dan deteksi aplikasi di Layer 7 OSI."
            },
            {
                "id": "bssn_5", "instansi": "BSSN", "category": "Analisis Kerentanan Siber", "subcategory": "CVSS & Remediasi",
                "question": "Dalam sistem penilaian kerentanan keamanan Common Vulnerability Scoring System (CVSS v3.1), sebuah kerentanan yang diberi skor 9.8 diklasifikasikan ke dalam tingkat keparahan (Severity Level)...",
                "options": {
                    "A": "Low",
                    "B": "Medium",
                    "C": "High",
                    "D": "Critical",
                    "E": "Informational"
                },
                "answer": "D",
                "explanation": "Rentang skala CVSS v3.1: 0.1-3.9 (Low), 4.0-6.9 (Medium), 7.0-8.9 (High), dan 9.0-10.0 (Critical). Skor 9.8 masuk ke dalam kategori Critical yang membutuhkan penanganan darurat segera."
            }
        ]
    },

    # -------------------------------------------------------------
    # 3. KEMENTERIAN KOMUNIKASI DAN DIGITAL (KEMKOMDIGI)
    # Fokus: Arsitektur SPBE Nasional, Pusat Data Nasional (PDN), UU ITE & PDP,
    # Infrastruktur Telekomunikasi, Interoperabilitas Layanan Digital Publik
    # -------------------------------------------------------------
    "skb_kemkomdigi": {
        "title": "SKB IT - Kementerian Komunikasi dan Digital (Kemkomdigi)",
        "instansi": "Kementerian Komunikasi dan Digital (Kemkomdigi)",
        "description": "Fokus pengujian: Arsitektur SPBE Nasional, Pusat Data Nasional (PDN), UU Perlindungan Data Pribadi (UU PDP), Tata Kelola Spektrum Frekuensi, dan Transformasi Digital Pemerintahan.",
        "timeMinutes": 90,
        "passingGrades": {"total": 0},
        "questions": [
            {
                "id": "komdigi_1", "instansi": "Kemkomdigi", "category": "Regulasi & Kedaulatan Digital", "subcategory": "UU PDP No. 27/2022",
                "question": "Berdasarkan Undang-Undang Nomor 27 Tahun 2022 tentang Perlindungan Data Pribadi (UU PDP), pihak yang memproses Data Pribadi untuk dan atas nama Pengendali Data Pribadi disebut...",
                "options": {
                    "A": "Subjek Data Pribadi",
                    "B": "Prosesor Data Pribadi",
                    "C": "Petugas Perlindungan Data (DPO)",
                    "D": "Auditor Sistem Informasi Independen",
                    "E": "Otoritas Pengawas Persaingan Usaha"
                },
                "answer": "B",
                "explanation": "UU PDP membedakan antara Pengendali Data Pribadi (menentukan tujuan dan kendali pemrosesan) dan Prosesor Data Pribadi (pihak yang melakukan pemrosesan data untuk dan atas nama Pengendali)."
            },
            {
                "id": "komdigi_2", "instansi": "Kemkomdigi", "category": "Infrastruktur Digital Nasional", "subcategory": "Pusat Data Nasional (PDN)",
                "question": "Konsep Pusat Data Nasional (PDN) yang dikelola oleh Kemkomdigi menerapkan model komputasi awan pemerintah (Government Cloud). Karakteristik utama dari penyatuan pusat data ini bagi efisiensi birokrasi adalah...",
                "options": {
                    "A": "Mewajibkan setiap dinas daerah membeli server fisik baru setiap semester",
                    "B": "Konsolidasi infrastruktur server, eliminasi duplikasi anggaran pengadaan data center di ratusan instansi, dan standarisasi keamanan terpusat",
                    "C": "Menghapus seluruh koneksi internet di instansi pemerintah daerah",
                    "D": "Memusatkan seluruh pegawai IT pemerintah di kantor Kemkomdigi Jakarta",
                    "E": "Menggunakan server gratisan tanpa Service Level Agreement (SLA)"
                },
                "answer": "B",
                "explanation": "PDN bertujuan mengonsolidasikan ribuan pusat data instansi pemerintah yang tersebar dan tidak terstandar menjadi infrastruktur terpadu demi efisiensi anggaran negara, skalabilitas, dan keamanan informasi."
            },
            {
                "id": "komdigi_3", "instansi": "Kemkomdigi", "category": "Tata Kelola SPBE Nasional", "subcategory": "Interoperabilitas Data",
                "question": "Dalam Keputusan Menkominfo / Perpres SPBE mengenai Bagi Pakai Data Nasional, standar format pertukaran data terstruktur yang ringan, independen terhadap bahasa pemrograman, dan umum digunakan untuk RESTful Web Service antaraplikasi pemerintah adalah...",
                "options": {
                    "A": "JSON (JavaScript Object Notation)",
                    "B": "DOCX",
                    "C": "PDF/A",
                    "D": "EXE",
                    "E": "SWF"
                },
                "answer": "A",
                "explanation": "JSON adalah format pertukaran data standar terbuka yang ringan, mudah dibaca manusia dan mesin, serta menjadi format de facto untuk interoperabilitas API modern antaraplikasi SPBE."
            },
            {
                "id": "komdigi_4", "instansi": "Kemkomdigi", "category": "Jaringan Telekomunikasi & Spektrum", "subcategory": "Teknologi 5G & IoT",
                "question": "Teknologi jaringan seluler generasi kelima (5G) yang dialokasikan Kemkomdigi untuk mendukung Smart City dan otomasi industri memiliki tiga pilar fitur utama, yaitu eMBB, URLLC, dan mMTC. Makna dari URLLC adalah...",
                "options": {
                    "A": "Kecepatan download video ultra tinggi untuk smartphone pribadi",
                    "B": "Komunikasi latensi ultra rendah dan keandalan tinggi (Ultra-Reliable Low-Latency Communication) untuk kendali jarak jauh dan misi kritis",
                    "C": "Koneksi khusus radio amatir pedesaan",
                    "D": "Pemutusan koneksi otomatis saat jaringan padat",
                    "E": "Enkripsi tanpa kata sandi"
                },
                "answer": "B",
                "explanation": "URLLC (Ultra-Reliable and Low Latency Communications) dirancang untuk komunikasi instan dengan latensi di bawah 1 milidetik, cocok untuk operasi kritis seperti bedah jarak jauh, kendaraan otonom, dan kontrol jaringan listrik pintar."
            },
            {
                "id": "komdigi_5", "instansi": "Kemkomdigi", "category": "Keamanan Konten & Literasi Digital", "subcategory": "DNS Filtering & Trust Positif",
                "question": "Sistem penanganan konten negatif di internet yang dioperasikan oleh Kemkomdigi untuk mencegah akses ke situs perjudian online, phishing, dan pornografi bekerja pada lapisan resolusi alamat web yang disebut...",
                "options": {
                    "A": "DNS Filtering (Sistem Trust Positif / DNS Nawala)",
                    "B": "Manipulasi Kabel Fiber Optik Bawah Laut",
                    "C": "Pemblokiran nomor IMEI seluruh smartphone",
                    "D": "Penghentian daya listrik gardu BTS",
                    "E": "Pemasangan chip pengawas di komputer warga"
                },
                "answer": "A",
                "explanation": "Kemkomdigi mengoperasikan DNS Filtering terintegrasi (database Trust Positif / AIS) yang memetakan domain bermasalah ke IP pemblokiran sehingga akses ke server terlarang dicegah sejak proses resolusi domain."
            }
        ]
    },

    # -------------------------------------------------------------
    # 4. BADAN KEPEGAWAIAN NEGARA (BKN)
    # Fokus: Arsitektur CAT BKN, Sistem Informasi ASN (SIASN), Manajemen Database
    # Kepegawaian Nasional, Keamanan Ujian Daring, MyASN
    # -------------------------------------------------------------
    "skb_bkn": {
        "title": "SKB IT - Badan Kepegawaian Negara (BKN)",
        "instansi": "Badan Kepegawaian Negara (BKN)",
        "description": "Fokus pengujian: Arsitektur Sistem CAT BKN (Jaringan Kiosk, Enkripsi Soal), SIASN (Sistem Informasi ASN Terpadu), Manajemen Data Pokok ASN, dan Integrasi MyASN.",
        "timeMinutes": 90,
        "passingGrades": {"total": 0},
        "questions": [
            {
                "id": "bkn_1", "instansi": "BKN", "category": "Arsitektur Sistem CAT", "subcategory": "Infrastruktur Jaringan Ujian CAT",
                "question": "Untuk menjamin kerahasiaan dan integritas bank soal serta mencegah kebocoran selama ujian seleksi CPNS berlangsung, arsitektur jaringan pada titik lokasi (tilok) CAT BKN dirancang menggunakan topologi...",
                "options": {
                    "A": "Jaringan terbuka dengan akses Wi-Fi publik tanpa password",
                    "B": "Jaringan tertutup lokal (LAN terisolasi / Local Offline Server) yang terhubung ke server pusat BKN melalui VPN terenkripsi khusus saat sinkronisasi soal dan hasil",
                    "C": "Server yang di-hosting di media sosial publik",
                    "D": "Koneksi peer-to-peer antar perangkat peserta ujian",
                    "E": "Tiap komputer peserta dipasangi modem GSM pribadi"
                },
                "answer": "B",
                "explanation": "Sistem CAT BKN menggunakan jaringan lokal yang terisolasi total dari internet umum di ruang tes. Soal dikirim secara terenkripsi melalui kanal VPN aman dari server pusat BKN ke server lokal titik lokasi."
            },
            {
                "id": "bkn_2", "instansi": "BKN", "category": "Sistem Informasi ASN (SIASN)", "subcategory": "Integrasi Layanan Digital Kepegawaian",
                "question": "SIASN BKN mengintegrasikan layanan kenaikan pangkat, mutasi, dan pensiun seluruh PNS se-Indonesia. Pola arsitektur basis data yang menjamin data riwayat jabatan ASN tetap konsisten di seluruh instansi pemerintah daerah dan pusat adalah...",
                "options": {
                    "A": "Setiap instansi membuat format database sendiri yang tidak kompatibel",
                    "B": "Single Identity Number berbasis NIP dengan database terpusat yang dapat diakses melalui Single Sign-On (SSO) dan API terstandar",
                    "C": "Pencatatan manual di buku kas instansi masing-masing",
                    "D": "Pengiriman berkas riwayat PNS lewat flashdisk kurir setiap bulan",
                    "E": "Database diunggah di situs cloud publik tanpa autentikasi"
                },
                "answer": "B",
                "explanation": "SIASN menerapkan prinsip Satu Data ASN dengan Single Identity Number (NIP unik) yang terhubung secara terpusat dengan layanan web service, sehingga pergerakan mutasi, pangkat, dan pensiun terkelola secara realtime dan konsisten."
            },
            {
                "id": "bkn_3", "instansi": "BKN", "category": "Keamanan & Integritas Ujian", "subcategory": "Live Score Streaming",
                "question": "Salah satu keunggulan transparansi sistem CAT BKN adalah penayangan skor ujian secara langsung (Live Score) di kanal YouTube resmi. Dari sudut pandang arsitektur perangkat lunak, bagaimana cara BKN menampilkan live score tanpa membebani server utama ujian CAT?",
                "options": {
                    "A": "Streaming langsung membaca basis data produksi utama setiap detik",
                    "B": "Menggunakan mekanisme data replication / read-only replica atau caching layer terpisah untuk server display publik, sehingga lalu lintas penonton tidak mengganggu performa server transaksi ujian",
                    "C": "Petugas mengetik ulang skor peserta satu per satu di notepad",
                    "D": "Kamera merekam layar peserta langsung dari belakang kursi",
                    "E": "Menyuruh penonton masuk ke dalam ruang ujian untuk melihat monitor peserta"
                },
                "answer": "B",
                "explanation": "Prinsip arsitektur sistem memisahkan Read/Write traffic (Database Transactional Ujian) dari Public Read Traffic (Live Score). Replikasi basis data atau database streamer khusus digunakan agar beban streaming ribuan penonton tidak memperlambat respon ujian peserta."
            },
            {
                "id": "bkn_4", "instansi": "BKN", "category": "Aplikasi Mobile MyASN", "subcategory": "Otentikasi & Keamanan Pengguna",
                "question": "Aplikasi MyASN BKN memungkinkan ASN mengakses data profil, e-KPE, dan kenaikan pangkat dari smartphone. Protokol otentikasi standar terbuka yang digunakan untuk mengamankan login terpusat (Single Sign-On) pada aplikasi mobile pemerintah adalah...",
                "options": {
                    "A": "OAuth 2.0 / OpenID Connect",
                    "B": "Telnet tanpa password",
                    "C": "HTTP Basic Auth plaintext",
                    "D": "FTP Anonymous",
                    "E": "SNMP v1"
                },
                "answer": "A",
                "explanation": "OAuth 2.0 dan OpenID Connect (OIDC) adalah standar industri modern untuk otentikasi dan otorisasi Single Sign-On (SSO) pada aplikasi web dan mobile pemerintah."
            },
            {
                "id": "bkn_5", "instansi": "BKN", "category": "Manajemen Data Kepegawaian", "subcategory": "Query SQL & Pelaporan",
                "question": "Seorang Pranata Komputer di BKN diminta menyajikan data jumlah ASN yang akan memasuki batas usia pensiun (58 tahun) dalam 12 bulan ke depan berdasarkan kolom tanggal_lahir. Klausul fungsi SQL yang paling tepat digunakan adalah...",
                "options": {
                    "A": "WHERE DATEDIFF(YEAR, tanggal_lahir, GETDATE()) >= 57",
                    "B": "WHERE tanggal_lahir IS NULL",
                    "C": "ORDER BY RAND()",
                    "D": "GROUP BY nama_lengkap",
                    "E": "DROP TABLE pegawai"
                },
                "answer": "A",
                "explanation": "Fungsi DATEDIFF atau penambahan interval tahun pada kolom tanggal lahir digunakan untuk memfilter pegawai yang telah mencapai usia batas pensiun dalam rentang 1 tahun ke depan."
            }
        ]
    },

    # -------------------------------------------------------------
    # 5. KEMENTERIAN HUKUM DAN HAM (KEMENKUMHAM)
    # Fokus: Sistem Informasi Manajemen Keimigrasian (SIMKIM), Sistem Database
    # Pemasyarakatan (SDP), Layanan AHU Online, Perlindungan Kekayaan Intelektual
    # -------------------------------------------------------------
    "skb_kemenkumham": {
        "title": "SKB IT - Kementerian Hukum dan HAM (Kemenkumham)",
        "instansi": "Kementerian Hukum dan HAM RI",
        "description": "Fokus pengujian: Sistem Informasi Manajemen Keimigrasian (SIMKIM - Autogate, Paspor Biometrik), Sistem Database Pemasyarakatan (SDP), dan AHU Online.",
        "timeMinutes": 90,
        "passingGrades": {"total": 0},
        "questions": [
            {
                "id": "kumham_1", "instansi": "Kemenkumham", "category": "Sistem Informasi Keimigrasian", "subcategory": "SIMKIM & Autogate",
                "question": "Pintu perlintasan imigrasi otomatis (Autogate) di bandara internasional yang terhubung ke SIMKIM Kemenkumham melakukan verifikasi identitas pelintas menggunakan teknologi pengenalan biometrik berupa...",
                "options": {
                    "A": "Pencocokan sidik jari dan pengenalan wajah (Face Recognition) dengan chip e-paspor dan database cekal",
                    "B": "Pencocokan kartu nama kertas",
                    "C": "Pemeriksaan tanda tangan basah secara manual",
                    "D": "Pengukuran tinggi badan saja",
                    "E": "Pengecekan warna baju pelintas"
                },
                "answer": "A",
                "explanation": "Autogate memindai e-paspor melalui chip RFID (ICAO Doc 9303) lalu membandingkan data biometrik wajah dan sidik jari penumpang secara real-time dengan kamera/sensor untuk memastikan kesesuaian dan mengecek daftar cegah-tangkal."
            },
            {
                "id": "kumham_2", "instansi": "Kemenkumham", "category": "Sistem Database Pemasyarakatan (SDP)", "subcategory": "Manajemen Data Tahanan",
                "question": "Sistem Database Pemasyarakatan (SDP) di Ditjen Pemasyarakatan mengelola remisi, pembebasan bersyarat, dan pemindahan warga binaan. Fitur penjaminan integritas data penting dalam SDP untuk mencegah manipulasi perhitungan sisa masa tahanan adalah...",
                "options": {
                    "A": "Setiap petugas bebas mengedit masa tahanan tanpa pencatatan log",
                    "B": "Audit Trail (Log aktivitas sistem terenkripsi) dan validasi otomatis perhitungan remisi berdasarkan peraturan perundangan",
                    "C": "Menyimpan data narapidana di file spreadsheet tanpa password",
                    "D": "Menghapus data narapidana setelah jam 5 sore",
                    "E": "Membagikan akun admin ke seluruh keluarga narapidana"
                },
                "answer": "B",
                "explanation": "Sistem informasi sensitif seperti SDP wajib memiliki Audit Trail (catatan log riwayat aktivitas yang tidak dapat diubah) serta algoritma perhitungan hak integrasi otomatis berbasis aturan baku untuk menutup celah korupsi/pungli."
            },
            {
                "id": "kumham_3", "instansi": "Kemenkumham", "category": "Layanan Administrasi Hukum Umum", "subcategory": "AHU Online & Notariat",
                "question": "Sistem AHU Online memfasilitasi pengesahan badan hukum PT secara elektronik dalam hitungan menit. Mekanisme pengamanan dokumen Surat Keputusan (SK) Pengesahan Badan Hukum yang diterbitkan agar tidak dapat dipalsukan adalah...",
                "options": {
                    "A": "Mencetak dokumen di kertas berharga dengan cap lilin saja",
                    "B": "Penyematan QR Code dinamis dan Tanda Tangan Elektronik (TTE) tersertifikasi yang dapat diverifikasi keasliannya secara daring",
                    "C": "Mengharuskan pemohon datang ke kantor kementerian di Jakarta",
                    "D": "Menyimpan dokumen asli di dalam amplop tertutup tanpa kode",
                    "E": "Mewajibkan pemohon menandatangani dokumen dengan tinta emas"
                },
                "answer": "B",
                "explanation": "Dokumen elektronik resmi pemerintah seperti SK Kemenkumham menggunakan Sertifikat Elektronik / TTE dan QR Code verifikatif yang terhubung ke server validasi keabsahan dokumen negara."
            },
            {
                "id": "kumham_4", "instansi": "Kemenkumham", "category": "Kekayaan Intelektual", "subcategory": "Sistem Paten & Hak Cipta Daring",
                "question": "Pada sistem pendaftaran Hak Kekayaan Intelektual (DJKI Online), sistem harus mampu melakukan penelusuran kemiripan merek (Trademark Similarity Search). Algoritma pencocokan teks yang umum digunakan untuk mendeteksi kesamaan fonetik pengucapan merek adalah...",
                "options": {
                    "A": "Soundex atau Metaphone",
                    "B": "Bubble Sort",
                    "C": "Dijkstra Algorithm",
                    "D": "Round Robin",
                    "E": "Binary Search Tree"
                },
                "answer": "A",
                "explanation": "Soundex dan Metaphone adalah algoritma fonetik yang mengindeks kata berdasarkan bunyi pengucapannya dalam bahasa inggris/internasional, sangat efektif mendeteksi merek yang ditulis berbeda namun terdengar sama."
            },
            {
                "id": "kumham_5", "instansi": "Kemenkumham", "category": "Keamanan Jaringan Lembaga", "subcategory": "Perlindungan Data Rahasia",
                "question": "Dalam mengamankan jalur komunikasi transmisi data paspor dan biometrik warga negara antara kantor imigrasi di perbatasan dengan pusat data Kemenkeu/Kemenkumham di Jakarta, teknologi tunneling terenkripsi yang wajib digunakan adalah...",
                "options": {
                    "A": "IPSec VPN (Virtual Private Network) dengan enkripsi AES",
                    "B": "Koneksi HTTP biasa tanpa sertifikat SSL",
                    "C": "Jaringan radio walkie-talkie konvensional",
                    "D": "Pengiriman SMS blast publik",
                    "E": "Koneksi FTP tanpa enkripsi"
                },
                "answer": "A",
                "explanation": "IPSec VPN menciptakan terowongan komunikasi data yang dienkripsi secara ketat di layer jaringan (Layer 3), menjamin kerahasiaan data lintas wilayah pulau terpencil ke pusat data nasional."
            }
        ]
    },

    # -------------------------------------------------------------
    # 6. PEMERINTAH DAERAH (PEMPROV / PEMKAB / PEMKOT)
    # Fokus: Smart City, Sistem Informasi Pemerintahan Daerah (SIPD Kemendagri),
    # Sistem Administrasi Kependudukan (SIAK), Layanan Publik Daerah (SuperApps)
    # -------------------------------------------------------------
    "skb_pemda": {
        "title": "SKB IT - Pemerintah Daerah (Pemprov / Pemkab / Pemkot)",
        "instansi": "Pemerintah Daerah",
        "description": "Fokus pengujian: Sistem Informasi Pemerintahan Daerah (SIPD), Smart City, Sistem Administrasi Kependudukan (SIAK), Integrasi Layanan Publik Daerah, dan SPBE Lokal.",
        "timeMinutes": 90,
        "passingGrades": {"total": 0},
        "questions": [
            {
                "id": "pemda_1", "instansi": "Pemerintah Daerah", "category": "Pengelolaan Keuangan Daerah", "subcategory": "SIPD Kemendagri",
                "question": "Pemerintah Daerah diwajibkan menyusun perencanaan pembangunan (e-Planning) dan penganggaran (e-Budgeting) secara terintegrasi melalui Sistem Informasi Pemerintahan Daerah (SIPD) yang dikembangkan oleh Kemendagri. Tujuan utama dari integrasi sistem ini adalah...",
                "options": {
                    "A": "Memberi keleluasaan setiap dinas membuat pos anggaran siluman di luar Musrenbang",
                    "B": "Menyelaraskan perencanaan pembangunan daerah dengan RKPD dan APBD secara transparan, serta memudahkan pengawasan realisasi belanja daerah oleh pemerintah pusat",
                    "C": "Menghapus peran DPRD dalam pembahasan anggaran",
                    "D": "Mewajibkan warga membayar retribusi dua kali lipat",
                    "E": "Menyulitkan proses pencairan bantuan sosial"
                },
                "answer": "B",
                "explanation": "SIPD bertujuan menyatukan data perencanaan dan keuangan seluruh Pemda se-Indonesia agar transparan, akuntabel, dan selaras antara Rencana Kerja Pemerintah Daerah (RKPD) dengan APBD."
            },
            {
                "id": "pemda_2", "instansi": "Pemerintah Daerah", "category": "Smart City & IoT", "subcategory": "Command Center Daerah",
                "question": "Banyak pemerintah kota/kabupaten membangun Command Center untuk memantau kemacetan lalu lintas, genangan banjir, dan pengaduan masyarakat secara real-time. Teknologi sensor IoT yang digunakan untuk memantau ketinggian air sungai secara otomatis disebut...",
                "options": {
                    "A": "Sensor Ultrasonik / Radar Water Level Sensor",
                    "B": "Termometer badan manual",
                    "C": "Kertas lakmus pengukur pH",
                    "D": "Alat pengukur tensi darah",
                    "E": "Scanner barcode minimarket"
                },
                "answer": "A",
                "explanation": "Sensor ketinggian air berbasis ultrasonik atau radar memancarkan gelombang untuk mengukur jarak permukaan air dan mengirimkan data telemetri secara nirkabel ke Command Center pemda."
            },
            {
                "id": "pemda_3", "instansi": "Pemerintah Daerah", "category": "Layanan Kependudukan", "subcategory": "SIAK Terpusat & KTP Digital (IKD)",
                "question": "Transformasi Sistem Informasi Administrasi Kependudukan (SIAK) menjadi SIAK Terpusat oleh Ditjen Dukcapil Kemendagri di seluruh Dinas Dukcapil Pemda bertujuan untuk...",
                "options": {
                    "A": "Mencegah duplikasi data kependudukan (NIK ganda) dan mempercepat verifikasi data identitas warga antarinstansi secara realtime",
                    "B": "Mengharuskan pencetakan e-KTP diulang setiap satu tahun sekali",
                    "C": "Menyimpan data warga di server komputer kelurahan secara terpisah tanpa jaringan",
                    "D": "Menjual data nomor telepon warga kepada pengiklan swasta",
                    "E": "Membatasi perpindahan domisili warga antarprovinsi"
                },
                "answer": "A",
                "explanation": "SIAK Terpusat meniadakan server data lokal di dinas kabupaten/kota yang rawan tidak sinkron, sehingga database menjadi tunggal di pusat data nasional dan mencegah terbitnya NIK ganda."
            },
            {
                "id": "pemda_4", "instansi": "Pemerintah Daerah", "category": "Layanan Publik Digital", "subcategory": "Kanal Pengaduan Warga (SP4N-LAPOR!)",
                "question": "Platform nasional yang wajib diintegrasikan oleh seluruh Pemerintah Daerah untuk mengelola aspirasi dan keluhan pengaduan pelayanan publik masyarakat adalah...",
                "options": {
                    "A": "SP4N-LAPOR!",
                    "B": "TikTok Live",
                    "C": "Marketplace E-Commerce",
                    "D": "Sistem Pembelian Game Online",
                    "E": "Situs Web Berita Hiburan"
                },
                "answer": "A",
                "explanation": "SP4N-LAPOR! (Sistem Pengelolaan Pengaduan Pelayanan Publik Nasional) adalah kanal resmi satu pintu yang dikelola KemenPANRB, Ombudsman, dan Kemkomdigi untuk mengawasi tindak lanjut aduan warga di setiap Pemda."
            },
            {
                "id": "pemda_5", "instansi": "Pemerintah Daerah", "category": "Pengembangan SuperApps Pemda", "subcategory": "Arsitektur Microservices",
                "question": "Pemerintah Daerah ingin menggabungkan puluhan aplikasi dinas yang terpisah-pisah (kesehatan, pajak daerah, perizinan, pengaduan) ke dalam satu aplikasi mobile tunggal (SuperApp). Pola arsitektur perangkat lunak yang paling cocok agar setiap modul dinas dapat dikembangkan dan diperbarui secara independen tanpa mengganggu modul lain adalah...",
                "options": {
                    "A": "Monolith raksasa yang disatukan dalam satu file kode besar",
                    "B": "Microservices Architecture dengan API Gateway",
                    "C": "Program batch berbasis DOS",
                    "D": "Aplikasi client-server Visual Basic 6 tanpa jaringan",
                    "E": "Situs web statis HTML tanpa database"
                },
                "answer": "B",
                "explanation": "Arsitektur Microservices memungkinkan setiap modul fungsional layanan dinas berjalan sebagai layanan independen yang terhubung melalui API Gateway, memberikan skalabilitas dan keandalan tinggi bagi SuperApp daerah."
            }
        ]
    }
}

# Format Bank Soal Terpadu
full_bank_soal = {
    # Paket 1: SKD Nasional (110 Soal Penuh)
    "skd": {
        "title": "Simulasi Resmi CAT BKN - SKD (110 Soal Full)",
        "instansi": "Nasional (Seluruh Instansi)",
        "description": "30 TWK, 35 TIU, 45 TKP skala 1-5 dengan ambang batas resmi BKN.",
        "timeMinutes": 100,
        "passingGrades": {
            "twk": 65,
            "tiu": 80,
            "tkp": 166
        },
        "questions": all_skd_questions
    }
}

# Masukkan paket-paket SKB Instansi
for key, p in instansi_packets.items():
    # Pastikan setiap soal memiliki points default jika belum terpasang
    for q in p["questions"]:
        if "points" not in q:
            ans = q["answer"]
            q["points"] = {opt: (5 if opt == ans else 0) for opt in ["A", "B", "C", "D", "E"]}
    full_bank_soal[key] = p

# Tulis ke file data_soal.js
js_content = "/**\n * BANK SOAL MULTI-INSTANSI CAT CPNS (SKD NASIONAL & SKB SPESIFIK INSTANSI)\n */\nwindow.BANK_SOAL = " + json.dumps(full_bank_soal, indent=2, ensure_ascii=False) + ";\n"

with open("d:\\CPNS\\data_soal.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Sukses meng-generate data_soal.js multi-instansi!")
for k, v in full_bank_soal.items():
    print(f"- [{k}] {v['title']}: {len(v['questions'])} soal")
