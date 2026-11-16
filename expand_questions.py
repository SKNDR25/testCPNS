import json
from generate_bank_soal import all_skd_questions

# ==============================================================================
# EXPANDER BANK SOAL SKB MULTI-INSTANSI (SOAL LENGKAP & MENDALAM)
# ==============================================================================

# Soal Tambahan Kemkomdigi (Menjadi 25 Soal Lengkap)
kemkomdigi_extended = [
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
        "explanation": "UU PDP membedakan antara Pengendali Data Pribadi (pihak yang menentukan tujuan dan kendali pemrosesan) dan Prosesor Data Pribadi (pihak yang memproses data untuk dan atas nama Pengendali)."
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
    },
    {
        "id": "komdigi_6", "instansi": "Kemkomdigi", "category": "Regulasi & Kedaulatan Digital", "subcategory": "UU PDP No. 27/2022",
        "question": "Menurut UU PDP Pasal 46, apabila terjadi kegagalan pelindungan data pribadi (data breach), Pengendali Data Pribadi wajib menyampaikan pemberitahuan tertulis kepada Subjek Data dan lembaga otoritas pengawas dalam jangka waktu maksimal...",
        "options": {
            "A": "1 x 24 jam",
            "B": "2 x 24 jam",
            "C": "3 x 24 jam (72 jam)",
            "D": "7 x 24 jam",
            "E": "30 hari kerja"
        },
        "answer": "C",
        "explanation": "Pasal 46 UU PDP menetapkan bahwa dalam hal terjadi kegagalan pelindungan Data Pribadi, Pengendali Data Pribadi wajib memberitahukan secara tertulis maksimal 3 x 24 jam (72 jam) kepada Subjek Data dan lembaga terkait."
    },
    {
        "id": "komdigi_7", "instansi": "Kemkomdigi", "category": "Regulasi & Kedaulatan Digital", "subcategory": "Data Protection Officer (DPO)",
        "question": "UU PDP mewajibkan penunjukan Pejabat atau Petugas Pelindungan Data Pribadi (Data Protection Officer / DPO) pada Pengendali Data dalam kondisi tertentu, salah satunya adalah ketika...",
        "options": {
            "A": "Perusahaan hanya memiliki kurang dari 5 orang karyawan",
            "B": "Kegiatan pokok Pengendali Data melibatkan pemrosesan data pribadi dalam skala besar dan/atau pemrosesan data pribadi yang bersifat spesifik (sensitif)",
            "C": "Instansi tersebut tidak pernah terhubung ke internet",
            "D": "Pengendali data hanya menggunakan formulir kertas manual",
            "E": "Semua pengguna aplikasi adalah warga negara asing"
        },
        "answer": "B",
        "explanation": "DPO wajib ditunjuk jika pemrosesan untuk kepentingan pelayanan publik, kegiatan pokok melibatkan pemantauan data teratur berskala besar, atau memproses data pribadi spesifik (kesehatan, biometrik, keuangan, data anak)."
    },
    {
        "id": "komdigi_8", "instansi": "Kemkomdigi", "category": "Tata Kelola SPBE Nasional", "subcategory": "Sistem Penghubung Layanan Pemerintah (SPLP)",
        "question": "Dalam Perpres No. 95/2018, Sistem Penghubung Layanan Pemerintah (SPLP) berfungsi sebagai...",
        "options": {
            "A": "Aplikasi pesan singkat antarpegawai kantor",
            "B": "Infrastruktur integrasi (Service Bus / API Hub) nasional yang menghubungkan dan mengalirkan data antar-layanan SPBE di seluruh K/L/D",
            "C": "Pengganti fungsi router di kantor kelurahan",
            "D": "Perangkat keras printer bersama untuk kementerian",
            "E": "Platform siaran radio publik"
        },
        "answer": "B",
        "explanation": "SPLP adalah perangkat integrasi yang berfungsi melakukan translasi format, routing, pertukaran data (interoperabilitas), dan orkestrasi layanan antar instansi pemerintah pusat dan daerah secara aman."
    },
    {
        "id": "komdigi_9", "instansi": "Kemkomdigi", "category": "Infrastruktur Telekomunikasi", "subcategory": "Palapa Ring & SATRIA-1",
        "question": "Proyek strategis nasional berupa jaringan tulang punggung (backbone) serat optik nasional yang menjangkau seluruh kabupaten/kota di Indonesia hingga wilayah 3T dinamakan...",
        "options": {
            "A": "Palapa Ring",
            "B": "IndoSat-1",
            "C": "Nusantara Net",
            "D": "Garuda Cable",
            "E": "Khatulistiwa Fiber"
        },
        "answer": "A",
        "explanation": "Palapa Ring adalah proyek pembangunan jaringan serat optik nasional sepanjang puluhan ribu kilometer melintasi darat dan dasar laut yang menghubungkan 514 kabupaten/kota di Indonesia."
    },
    {
        "id": "komdigi_10", "instansi": "Kemkomdigi", "category": "Infrastruktur Telekomunikasi", "subcategory": "Satelit SATRIA-1",
        "question": "Satelit Republik Indonesia (SATRIA-1) yang diluncurkan Kemkomdigi beroperasi menggunakan teknologi High Throughput Satellite (HTS) dengan kapasitas 150 Gbps. Fungsi utama satelit ini adalah...",
        "options": {
            "A": "Menyediakan akses internet pita lebar (broadband) bagi titik layanan publik (sekolah, puskesmas, kantor desa) di wilayah 3T yang belum terjangkau serat optik",
            "B": "Memata-matai siaran televisi negara tetangga",
            "C": "Menyimpan seluruh database server perbankan swasta",
            "D": "Menggantikan seluruh menara BTS seluler di kota besar",
            "E": "Menyiarkan iklan komersial ke luar angkasa"
        },
        "answer": "A",
        "explanation": "SATRIA-1 difokuskan untuk konektivitas layanan publik gratis di ribuan titik fasilitas pendidikan (sekolah), fasilitas kesehatan (puskesmas), dan kantor pemerintahan di daerah terluar, terdepan, dan tertinggal (3T)."
    },
    {
        "id": "komdigi_11", "instansi": "Kemkomdigi", "category": "Manajemen Spektrum Frekuensi", "subcategory": "Analog Switch Off (ASO)",
        "question": "Peralihan siaran televisi analog ke siaran digital (Analog Switch Off / ASO) yang diselesaikan oleh Kemkomdigi menghasilkan pembebasan pita frekuensi sebesar 112 MHz pada rentang 700 MHz. Pita frekuensi yang dibebaskan ini disebut...",
        "options": {
            "A": "Digital Dividend",
            "B": "Analog Waste",
            "C": "Dark Fiber",
            "D": "Carrier Frequency",
            "E": "Sideband"
        },
        "answer": "A",
        "explanation": "Digital Dividend adalah spektrum frekuensi radio 700 MHz yang berhasil dihemat melalui migrasi siaran TV analog ke digital (DVB-T2). Spektrum emas ini dialihkan untuk mempercepat perluasan internet 4G/5G berkecepatan tinggi."
    },
    {
        "id": "komdigi_12", "instansi": "Kemkomdigi", "category": "Infrastruktur Digital Nasional", "subcategory": "Cloud Computing (NIST)",
        "question": "Model layanan komputasi awan pada Pusat Data Nasional di mana instansi pemerintah menyewa infrastruktur komputasi berupa Virtual Machine (vCPU, RAM, Storage, dan Jaringan) dan instansi bertanggung jawab mengelola OS serta aplikasi sendiri disebut...",
        "options": {
            "A": "IaaS (Infrastructure as a Service)",
            "B": "PaaS (Platform as a Service)",
            "C": "SaaS (Software as a Service)",
            "D": "FaaS (Function as a Service)",
            "E": "DaaS (Desktop as a Service)"
        },
        "answer": "A",
        "explanation": "IaaS menyediakan sumber daya komputasi mentah (compute, storage, networking). Penyewa (instansi) bebas menginstal dan mengkonfigurasi sistem operasi, runtime, dan aplikasi di atas VM tersebut."
    },
    {
        "id": "komdigi_13", "instansi": "Kemkomdigi", "category": "Infrastruktur Digital Nasional", "subcategory": "Disaster Recovery Center (DRC)",
        "question": "Dalam standar Pusat Data Nasional Kemkomdigi, fasilitas DRC (Disaster Recovery Center) wajib dibangun dengan kriteria geografis tertentu, yaitu...",
        "options": {
            "A": "Tepat bersebelahan di ruangan yang sama dengan data center utama",
            "B": "Berada pada zona risiko bencana geologis yang berbeda dan terpisah jarak aman dari data center utama dengan konektivitas serat optik redundan",
            "C": "Di rumah pribadi pimpinan instansi",
            "D": "Di luar negeri tanpa koordinasi keamanan",
            "E": "Di atas kapal laut yang terus berpindah-pindah"
        },
        "answer": "B",
        "explanation": "DRC harus berada pada lempeng/zona geografis berbeda untuk memastikan bila terjadi gempa bumi, banjir, atau bencana besar pada Data Center primer, fasilitas DRC tetap beroperasi dan data tidak musnah."
    },
    {
        "id": "komdigi_14", "instansi": "Kemkomdigi", "category": "Regulasi & Kedaulatan Digital", "subcategory": "UU ITE & Tanda Tangan Elektronik",
        "question": "Berdasarkan UU ITE dan PP No. 71/2019, Tanda Tangan Elektronik (TTE) Tersertifikasi wajib dibuat menggunakan jasa...",
        "options": {
            "A": "Penyelenggara Sertifikasi Elektronik (PSrE) Indonesia yang berinduk ke Kemkomdigi",
            "B": "Notaris konvensional di kantor cabang daerah",
            "C": "Aplikasi edit foto smartphone gratisan",
            "D": "Warnet terdekat",
            "E": "Penyedia tanda tangan dari luar negeri yang tidak terdaftar"
        },
        "answer": "A",
        "explanation": "TTE tersertifikasi memiliki kekuatan hukum tertinggi dan nilai pembuktian kuat karena diterbitkan oleh PSrE Indonesia yang diakui dan diawasi langsung oleh pemerintah melalui Kemkomdigi (Root CA Indonesia)."
    },
    {
        "id": "komdigi_15", "instansi": "Kemkomdigi", "category": "Smart City & Digital Society", "subcategory": "Gerakan Menuju 100 Smart City",
        "question": "Dalam Masterplan Gerakan Menuju 100 Smart City yang diinisiasi Kemkomdigi, terdapat 6 pilar utama. Pilar yang berkaitan dengan pemanfaatan teknologi informasi untuk meningkatkan akuntabilitas birokrasi dan transparansi pelayanan publik disebut...",
        "options": {
            "A": "Smart Governance",
            "B": "Smart Economy",
            "C": "Smart Living",
            "D": "Smart Mobility",
            "E": "Smart Environment"
        },
        "answer": "A",
        "explanation": "Smart Governance berfokus pada digitalisasi tata kelola birokrasi, keterbukaan informasi publik, efisiensi administrasi pemerintahan, dan penyediaan layanan terpadu bagi warga."
    },
    {
        "id": "komdigi_16", "instansi": "Kemkomdigi", "category": "Keamanan Konten & Literasi Digital", "subcategory": "Mesin Pengais Konten (AIS)",
        "question": "Kemkomdigi mengoperasikan sistem mesin pengais (crawler) berbasis kecerdasan buatan bernama AIS. Tugas utama dari sistem AIS ini adalah...",
        "options": {
            "A": "Mendeteksi secara otomatis keberadaan konten terlarang (pornografi, judi online, radikalisme, hoaks) di jutaan situs internet dan media sosial secara masif",
            "B": "Menghapus akun email pribadi seluruh warga negara",
            "C": "Mengirimkan pesan promosi pulsa ke semua nomor telepon",
            "D": "Memperlambat koneksi internet pada malam hari",
            "E": "Mengurangi saldo rekening bank peretas secara otomatis"
        },
        "answer": "A",
        "explanation": "Mesin AIS Kemkomdigi menggunakan algoritma machine learning dan web crawler berkecepatan tinggi untuk menelusuri, mengenali pola URL/gambar/teks negatif, dan mengantrekan temuan untuk verifikasi pemblokiran."
    },
    {
        "id": "komdigi_17", "instansi": "Kemkomdigi", "category": "Tata Kelola SPBE Nasional", "subcategory": "Satu Data Indonesia (Perpres 39/2019)",
        "question": "Sesuai Perpres No. 39 Tahun 2019 tentang Satu Data Indonesia, prinsip utama yang harus dipenuhi oleh setiap data yang dihasilkan oleh produsen data pemerintah adalah...",
        "options": {
            "A": "Memenuhi Standar Data, memiliki Metadata, memenuhi Interoperabilitas Data, dan menggunakan Kode Referensi/Data Induk",
            "B": "Disimpan dalam format rahasia yang tidak dapat dibaca siapa pun",
            "C": "Dijual kepada perusahaan riset internasional dengan harga tertinggi",
            "D": "Dicetak dalam kertas formulir rangkap lima",
            "E": "Dihapus secara berkala setiap 30 hari"
        },
        "answer": "A",
        "explanation": "4 Prinsip Satu Data Indonesia: 1. Standar Data (definisi konsep & ukuran), 2. Metadata (informasi pelacak konteks data), 3. Interoperabilitas (mudah dibagi-pakaikan antar sistem), 4. Kode Referensi/Data Induk tunggal."
    },
    {
        "id": "komdigi_18", "instansi": "Kemkomdigi", "category": "Jaringan Telekomunikasi & Spektrum", "subcategory": "Internet Protocol IPv6",
        "question": "Kemkomdigi mendorong percepatan adopsi IPv6 di seluruh infrastruktur digital instansi pemerintah dan ISP. Alasan fundamental migrasi dari IPv4 ke IPv6 adalah...",
        "options": {
            "A": "IPv4 telah habis ruang alamatnya (hanya ~4,3 miliar IP), sedangkan IPv6 memiliki ruang alamat 128-bit yang sangat melimpah untuk miliaran perangkat IoT masa depan",
            "B": "IPv6 tidak membutuhkan router atau kabel",
            "C": "IPv4 hanya bisa digunakan untuk browsing teks tanpa gambar",
            "D": "IPv6 membuat koneksi komputer menjadi gratis selamanya",
            "E": "IPv4 dilarang oleh undang-undang telekomunikasi internasional"
        },
        "answer": "A",
        "explanation": "Alamat IPv4 (32-bit) telah habis secara global. IPv6 (128-bit) menyediakan 2^128 alamat unik (sekitar 3,4 x 10^38), menjamin setiap perangkat pintar, sensor smart city, dan server memiliki alamat IP publik sendiri."
    },
    {
        "id": "komdigi_19", "instansi": "Kemkomdigi", "category": "Infrastruktur Digital Nasional", "subcategory": "Standar Data Center TIA-942",
        "question": "Menurut standar data center internasional ANSI/TIA-942, kualifikasi 'Tier IV' (Fault Tolerant) mensyaratkan tingkat ketersediaan (uptime availability) tahunan minimum sebesar...",
        "options": {
            "A": "99,995% (toleransi downtime maksimal kurang dari 26 menit per tahun)",
            "B": "95,000%",
            "C": "90,000%",
            "D": "80,000%",
            "E": "50,000%"
        },
        "answer": "A",
        "explanation": "Tier IV adalah tingkat keandalan tertinggi: Fault Tolerant dengan jalur daya dan pendingin redundan (2N+1), menjamin uptime 99,995% (downtime tahunan maksimal 26,3 menit)."
    },
    {
        "id": "komdigi_20", "instansi": "Kemkomdigi", "category": "Regulasi & Kedaulatan Digital", "subcategory": "Penyelenggara Sistem Elektronik (PSE)",
        "question": "Berdasarkan Permenkominfo No. 5/2020, seluruh Penyelenggara Sistem Elektronik (PSE) Lingkup Privat baik domestik maupun asing wajib mendaftarkan sistemnya ke Kemkomdigi. Dampak hukum bagi PSE yang tidak mendaftar adalah...",
        "options": {
            "A": "Pemutusan akses (pemblokiran) sistem elektronik di wilayah hukum Indonesia",
            "B": "Pemberian subsidi kuota internet dari pemerintah",
            "C": "Pengambilalihan saham perusahaan oleh kementerian",
            "D": "Kewajiban menghapus seluruh kode program",
            "E": "Penutupan rekening bank pribadi seluruh direksi"
        },
        "answer": "A",
        "explanation": "Sanksi administratif bagi PSE privat yang tidak mendaftar ke portal layanan Kemkomdigi dimulai dari teguran tertulis, denda administratif, hingga sanksi pemutusan akses (takedown/blokir akses jaringan)."
    }
]

# Tambahkan soal instansi lainnya (Kemenkeu, BSSN, BKN, Kumham, Pemda) ke 10-15 soal masing-masing
# Kita perbarui dict instansi
from generate_multi_instansi import instansi_packets

# Update Kemkomdigi dengan soal panjang
instansi_packets["skb_kemkomdigi"]["questions"] = kemkomdigi_extended

# Format Bank Soal Terpadu
full_bank_soal = {
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

for key, p in instansi_packets.items():
    for q in p["questions"]:
        if "points" not in q:
            ans = q["answer"]
            q["points"] = {opt: (5 if opt == ans else 0) for opt in ["A", "B", "C", "D", "E"]}
    full_bank_soal[key] = p

js_content = "/**\n * BANK SOAL MULTI-INSTANSI CAT CPNS (SKD NASIONAL & SKB SPESIFIK INSTANSI)\n */\nwindow.BANK_SOAL = " + json.dumps(full_bank_soal, indent=2, ensure_ascii=False) + ";\n"

with open("d:\\CPNS\\data_soal.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Berhasil mengupdate data_soal.js!")
for k, v in full_bank_soal.items():
    print(f"- [{k}] {v['title']}: {len(v['questions'])} soal")
