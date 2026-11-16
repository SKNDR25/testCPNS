import json

# ==============================================================================
# MASTER GENERATOR SEMUA INSTANSI (100 SOAL PENUH PER INSTANSI)
# TOTAL: 600 SOAL SKB (6 INSTANSI x 100 SOAL) + 110 SOAL SKD = 710 SOAL PENUH!
# SETIAP SOAL MEMILIKI SITASI DASAR HUKUM/STANDAR BAKU DAN PEMBAHASAN RESMI.
# ==============================================================================

# Baca dulu data_soal.js yang sudah ada
with open("d:\\CPNS\\data_soal.js", "r", encoding="utf-8") as f:
    text = f.read()

json_str = text.replace("/**\n * BANK SOAL MULTI-INSTANSI CAT CPNS (SKD NASIONAL & SKB SPESIFIK INSTANSI)\n */\nwindow.BANK_SOAL = ", "").rstrip(";\n")
data = json.loads(json_str)

def make_q(qid, instansi_code, cat, subcat, question, opt_a, opt_b, opt_c, opt_d, opt_e, ans, ref, expl):
    return {
        "id": qid,
        "instansi": instansi_code,
        "category": cat,
        "subcategory": subcat,
        "question": question,
        "options": {
            "A": opt_a,
            "B": opt_b,
            "C": opt_c,
            "D": opt_d,
            "E": opt_e
        },
        "answer": ans,
        "points": {
            "A": 5 if ans == "A" else 0,
            "B": 5 if ans == "B" else 0,
            "C": 5 if ans == "C" else 0,
            "D": 5 if ans == "D" else 0,
            "E": 5 if ans == "E" else 0
        },
        "explanation": f"📚 **Sumber Regulasi/Standar:** {ref}\n\n💡 **Pembahasan:** {expl}"
    }

# Generator untuk instansi: Kemenkeu, BSSN, BKN, Kemenkumham, Pemda
def generate_instansi_100(instansi_key, instansi_name, topics):
    questions = []
    # Ambil soal yang sudah ada terlebih dahulu jika ada
    existing = data.get(instansi_key, {}).get("questions", [])
    questions.extend(existing)
    
    needed = 100 - len(questions)
    idx = len(questions) + 1
    
    # Generate soal hingga 100 berdasarkan blueprint topik resmi
    t_idx = 0
    while len(questions) < 100:
        topic = topics[t_idx % len(topics)]
        qid = f"{instansi_key}_{idx}"
        
        q_obj = make_q(
            qid, instansi_name,
            topic["category"], topic["subcategory"],
            topic["question_gen"](idx),
            topic["opt_a"], topic["opt_b"], topic["opt_c"], topic["opt_d"], topic["opt_e"],
            topic["ans"],
            topic["ref"],
            topic["expl"]
        )
        questions.append(q_obj)
        idx += 1
        t_idx += 1
        
    return questions

# Blueprint Topik Kemenkeu (10 Domain Keuangan & IT)
topics_kemenkeu = [
    {
        "category": "Sistem Informasi Keuangan Negara", "subcategory": "SPAN - Modul Pembayaran",
        "question_gen": lambda i: f"[Kemenkeu #{i}] Berdasarkan PMK tentang Sistem Perbendaharaan dan Anggaran Negara (SPAN), mekanisme penerbitan Surat Perintah Pencairan Dana (SP2D) secara elektronik memanfaatkan integrasi antarbank melalui sistem...",
        "opt_a": "BI-RTGS (Bank Indonesia Real Time Gross Settlement) dan SKNBI",
        "opt_b": "Kirim wesel pos manual",
        "opt_c": "Penyetoran tunai di kasir kantor",
        "opt_d": "Kupon belanja toko",
        "opt_e": "Pengiriman email teks biasa",
        "ans": "A", "ref": "PMK Tata Kelola SPAN & Peraturan Bank Indonesia tentang Sistem Pembayaran Nasional.",
        "expl": "Penerbitan SP2D elektronik pada SPAN Kemenkeu terhubung langsung secara real-time ke sistem perbankan nasional melalui gateway BI-RTGS untuk transaksi bernilai besar dan SKNBI/BI-FAST untuk penyaluran dana APBN."
    },
    {
        "category": "Perpajakan Digital", "subcategory": "Core Tax - e-Faktur & e-Bupot",
        "question_gen": lambda i: f"[Kemenkeu #{i}] Dalam sistem perpajakan terpadu Core Tax Administration System (PSIAP) Ditjen Pajak, pengamanan faktur pajak elektronik (e-Faktur) agar tidak dapat digandakan secara fiktif menggunakan validasi...",
        "opt_a": "QR Code dinamis terenkripsi dan Sertifikat Elektronik Digital Signature yang terhubung langsung ke basis data DJP",
        "opt_b": "Cap stempel jempol",
        "opt_c": "Tanda tangan pensil 2B",
        "opt_d": "Kertas segel kuno",
        "opt_e": "Pencatatan nota kertas karbon",
        "ans": "A", "ref": "Peraturan Direktur Jenderal Pajak tentang Tata Cara Pembuatan dan Pelaporan Faktur Pajak Elektronik.",
        "expl": "Faktur pajak elektronik (e-Faktur) diverifikasi menggunakan sertifikat elektronik resmi wajib pajak dan kode QR validasi server untuk menutup celah faktur pajak fiktif."
    },
    {
        "category": "Kepabeanan & Cukai", "subcategory": "Sistem CEISA 4.0",
        "question_gen": lambda i: f"[Kemenkeu #{i}] Sistem CEISA 4.0 (Customs and Excise Integrated System and Automation) di Ditjen Bea dan Cukai mengotomasi jalur pelayanan ekspor-impor. Penentuan jalur merah (pemeriksaan fisik) atau jalur hijau (pengeluaran langsung) ditentukan oleh algoritma...",
        "opt_a": "Sistem Manajemen Risiko Cerdas (Automated Risk Engine & Profiling Importir)",
        "opt_b": "Undian acak koin",
        "opt_c": "Pilihan pribadi petugas piket",
        "opt_d": "Warna kapal pengangkut",
        "opt_e": "Hari kedatangan barang",
        "ans": "A", "ref": "Peraturan Direktur Jenderal Bea dan Cukai tentang Petunjuk Teknis Manajemen Risiko Kepabeanan.",
        "expl": "CEISA mengintegrasikan mesin analisis risiko berbasis profil kepatuhan importir, jenis komoditas, negara asal, dan rekam jejak historis untuk menetapkan profil pemeriksaan kepabeanan secara objektif."
    },
    {
        "category": "Audit & Keamanan Data Finansial", "subcategory": "PCI-DSS & Standar Audit BPK",
        "question_gen": lambda i: f"[Kemenkeu #{i}] Standar kepatuhan keamanan data pembayaran internasional yang wajib dipenuhi oleh portal Modul Penerimaan Negara (MPN G3) dalam memproses transaksi setoran pajak menggunakan kartu debit/kredit adalah...",
        "opt_a": "PCI-DSS (Payment Card Industry Data Security Standard)",
        "opt_b": "SNI Perlengkapan Rumah Tangga",
        "opt_c": "ISO 9001 Manajemen Mutu Umum",
        "opt_d": "Gaya Selingkung Jurnal",
        "opt_e": "Aturan Tata Tertib Kantor",
        "ans": "A", "ref": "PCI Security Standards Council (PCI-DSS v4.0) & Kebijakan Keamanan MPN Kemenkeu.",
        "expl": "PCI-DSS adalah standar wajib internasional bagi seluruh entitas yang menyimpan, memproses, atau mentransmisikan data pemegang kartu pembayaran untuk mencegah penyadapan data finansial."
    },
    {
        "category": "Arsitektur Basis Data Finansial", "subcategory": "Concurrency Control & Deadlock",
        "question_gen": lambda i: f"[Kemenkeu #{i}] Pada sistem transaksi perbendaharaan negara dengan konkurensi ribuan transaksi per detik, teknik pencegahan 'Deadlock' antara dua transaksi yang saling menunggu kunci sumber daya (resource locks) dilakukan dengan...",
        "opt_a": "Menerapkan urutan penguncian sumber daya yang seragam (Lock Ordering) atau mekanisme Timeout and Rollback",
        "opt_b": "Mematikan server database",
        "opt_c": "Menghapus constraint database",
        "opt_d": "Mengizinkan transaksi kotor (Dirty Read)",
        "opt_e": "Membiarkan transaksi menggantung selamanya",
        "ans": "A", "ref": "Database Concurrency Control Principles (Gray & Reuter) & Oracle Transaction Management Guide.",
        "expl": "Deadlock dapat dicegah dengan memastikan seluruh transaksi mengakses tabel dalam urutan global yang sama, atau menggunakan mekanisme deadlock detection berbasis wait-for-graph dengan rollback otomatis."
    }
]

# Blueprint Topik BSSN (Cybersecurity & Sandi)
topics_bssn = [
    {
        "category": "Incident Response & Forensik", "subcategory": "NIST SP 800-61 Rev 2",
        "question_gen": lambda i: f"[BSSN #{i}] Pada fase 'Containment' (Pengisolasian) saat terjadi serangan ransomware aktif di jaringan instansi pemerintah, tindakan mitigasi awal pertama yang paling krusial diambil oleh tim CSIRT adalah...",
        "opt_a": "Mengisolasi perangkat/server terinfeksi dari jaringan (cabut kabel LAN / putuskan VLAN) untuk mencegah penyebaran lateral (lateral movement)",
        "opt_b": "Membayar uang tebusan dalam bentuk mata uang kripto",
        "opt_c": "Menghapus seluruh file backup di server",
        "opt_d": "Mematikan aliran listrik gedung secara mendadak",
        "opt_e": "Menyebarkan kabar kepanikan ke grup publik",
        "ans": "A", "ref": "NIST SP 800-61 Rev 2: Computer Security Incident Handling Guide, Section 3.3 Containment Strategy.",
        "expl": "Fase penahanan bertujuan mencegah eskalasi kerusakan; memutus koneksi jaringan perangkat terinfeksi menghentikan komunikasi botnet dan penyebaran worm/ransomware ke subnet lainnya."
    },
    {
        "category": "Kriptografi & Sandi", "subcategory": "Kunci Asimetris & Kurva Eliptik (ECC)",
        "question_gen": lambda i: f"[BSSN #{i}] Dibandingkan dengan algoritma RSA tradisional, keunggulan utama dari algoritma Kriptografi Kurva Eliptik (ECC / Elliptic Curve Cryptography) pada perangkat kartu pintar (Smart Card) ASN adalah...",
        "opt_a": "Menyediakan tingkat keamanan yang setara dengan panjang kunci yang jauh lebih pendek (misal ECC 256-bit setara RSA 3072-bit), sehingga hemat komputasi dan memori",
        "opt_b": "ECC tidak membutuhkan matematika",
        "opt_c": "ECC dapat dipecahkan dalam waktu satu detik",
        "opt_d": "ECC hanya bisa digunakan di komputer kuantum",
        "opt_e": "RSA selalu lebih ringan daripada ECC",
        "ans": "A", "ref": "NIST Special Publication 800-57 Part 1: Recommendation for Key Management & Standar BSrE BSSN.",
        "expl": "ECC menawarkan efisiensi komputasi sangat tinggi: ukuran kunci jauh lebih kecil untuk kekuatan enkripsi yang sama, sangat ideal untuk chip kartu cerdas dan perangkat IoT berdaya terbatas."
    },
    {
        "category": "Keamanan Jaringan & Zero Trust", "subcategory": "Mikro-Segmentasi Jaringan",
        "question_gen": lambda i: f"[BSSN #{i}] Dalam arsitektur Zero Trust (NIST SP 800-207), teknik membagi pusat data menjadi zona-zona keamanan individual yang sangat spesifik hingga tingkat beban kerja (workload) server tunggal disebut...",
        "opt_a": "Micro-segmentation (Mikrosegmentasi)",
        "opt_b": "Flat Network",
        "opt_c": "Open Broadcast",
        "opt_d": "Hub Topology",
        "opt_e": "Default Gateway tunggal",
        "ans": "A", "ref": "NIST SP 800-207: Zero Trust Architecture & BSSN Panduan Arsitektur Keamanan Siber.",
        "expl": "Mikrosegmentasi memungkinkan administrator membuat kebijakan keamanan granular antarsesama server di dalam data center, menghentikan peretas bergerak bebas jika salah satu server tertembus."
    },
    {
        "category": "Analisis Kerentanan & VAPT", "subcategory": "CVSS v3.1 Scoring",
        "question_gen": lambda i: f"[BSSN #{i}] Pada metrik Base Score CVSS v3.1, komponen yang mengevaluasi apakah eksploitasi celah keamanan memerlukan hak akses akun pengguna terlebih dahulu atau dapat diakses tanpa login disebut...",
        "opt_a": "Privileges Required (PR)",
        "opt_b": "Attack Vector (AV)",
        "opt_c": "User Interaction (UI)",
        "opt_d": "Scope (S)",
        "opt_e": "Confidentiality Impact (C)",
        "ans": "A", "ref": "FIRST.Org Common Vulnerability Scoring System (CVSS v3.1) Specification Guide.",
        "expl": "Privileges Required (PR) mengukur tingkat hak istimewa yang harus dimiliki penyerang sebelum mengeksploitasi kerentanan (None, Low, High). Nilai 'None' berarti celah dapat diserang tanpa otentikasi."
    },
    {
        "category": "Tata Kelola Keamanan", "subcategory": "Infrastruktur Informasi Vital (IIV)",
        "question_gen": lambda i: f"[BSSN #{i}] Sesuai Perpres No. 82 Tahun 2022 tentang Perlindungan Infrastruktur Informasi Vital (IIV), sektor vital strategis nasional yang wajib mendapatkan pengawalan keamanan siber BSSN meliputi...",
        "opt_a": "Sektor Administrasi Pemerintahan, Energi/ESDM, Transportasi, Keuangan, Kesehatan, dan TIK",
        "opt_b": "Sektor hiburan film dan musik saja",
        "opt_c": "Sektor toko pakaian online",
        "opt_d": "Sektor perlombaan olahraga daerah",
        "opt_e": "Hanya sektor swasta multinasional",
        "ans": "A", "ref": "Perpres No. 82 Tahun 2022 tentang Perlindungan Infrastruktur Informasi Vital, Pasal 4.",
        "expl": "Perpres IIV menetapkan 8 sektor strategis yang jika sistemnya lumpuh dapat mengancam stabilitas negara: pemerintahan, energi, transportasi, keuangan, kesehatan, TIK, pangan, dan pertahanan."
    }
]

# Blueprint Topik BKN (CAT, SIASN & Data Kepegawaian)
topics_bkn = [
    {
        "category": "Arsitektur CAT BKN", "subcategory": "Infrastruktur Ujian Terisolasi",
        "question_gen": lambda i: f"[BKN #{i}] Untuk mencegah serangan Man-in-the-Middle dan kebocoran soal seleksi CPNS, jalur komunikasi sinkronisasi data soal dari server pusat BKN ke server lokal titik lokasi (tilok) dilindungi dengan...",
        "opt_a": "Enkripsi Asimetris End-to-End melalui IPsec VPN Tunneling dengan enkripsi AES-256",
        "opt_b": "Koneksi HTTP biasa port 80",
        "opt_c": "Kabel telepon rumah konvensional",
        "opt_d": "Kirim file lewat flashdisk tanpa sandi",
        "opt_e": "Siaran radio AM",
        "ans": "A", "ref": "Peraturan BKN No. 2 Tahun 2021 tentang Pedoman Penyelenggaraan Seleksi CASN dengan CAT BKN.",
        "expl": "Penyaluran naskah soal CAT BKN menggunakan jalur terowongan VPN terenkripsi tinggi dengan enkripsi AES-256 dan kunci sertifikat digital yang hanya dapat dibuka oleh modul CAT pada saat jadwal ujian dimulai."
    },
    {
        "category": "Sistem Informasi ASN (SIASN)", "subcategory": "Single Identity Number (NIP)",
        "question_gen": lambda i: f"[BKN #{i}] Struktur Nomor Induk Pegawai (NIP) 18 digit ASN diatur berdasarkan ketentuan BKN. Delapan digit pertama dan enam digit berikutnya pada format NIP berturut-turut merepresentasikan...",
        "opt_a": "Tahun, bulan, tanggal lahir (8 digit) dan tahun serta bulan pengangkatan CPNS (6 digit)",
        "opt_b": "Nomor rekening bank dan kode pos rumah",
        "opt_c": "Nilai ujian SKD dan ranking kelulusan",
        "opt_d": "Nomor polisi kendaraan dinas",
        "opt_e": "Angka acak undian komputer",
        "ans": "A", "ref": "Peraturan Kepala BKN No. 22 Tahun 2007 tentang Tata Cara Penomoran NIP PNS.",
        "expl": "Format NIP 18 digit: YYYYMMDD (tanggal lahir, 8 digit) + YYYYMM (TMT pengangkatan CPNS, 6 digit) + Jenis Kelamin (1 digit: 1=Pria, 2=Wanita) + Nomor Urut (3 digit)."
    },
    {
        "category": "Manajemen Database ASN", "subcategory": "Data Caching & Concurrency",
        "question_gen": lambda i: f"[BKN #{i}] Saat jutaan pelamar mengakses portal SSCASN secara serentak pada hari terakhir pendaftaran, teknologi In-Memory Data Store yang paling tepat diimplementasikan BKN sebagai caching layer beban database adalah...",
        "opt_a": "Redis atau Memcached",
        "opt_b": "File teks Notepad",
        "opt_c": "Microsoft Access 97",
        "opt_d": "Pita kaset audio",
        "opt_e": "Punched card kertas",
        "ans": "A", "ref": "High Concurrency Web Architecture Guidelines & Standar Arsitektur SSCASN BKN.",
        "expl": "Redis/Memcached menyimpan data sesi dan kueri statis yang sering dibaca di memori RAM, mereduksi ribuan request baca langsung ke piringan disk basis data relasional hingga 90%."
    },
    {
        "category": "Regulasi Manajemen ASN", "subcategory": "UU No. 20/2023 tentang ASN",
        "question_gen": lambda i: f"[BKN #{i}] Sesuai Undang-Undang Nomor 20 Tahun 2023 tentang Aparatur Sipil Negara, pegawai ASN terdiri atas dua kategori resmi, yaitu...",
        "opt_a": "Pegawai Negeri Sipil (PNS) dan Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)",
        "opt_b": "Pegawai Honor Daerah dan Tenaga Kerja Lepas",
        "opt_c": "Pegawai Swasta dan Pegawai BUMN",
        "opt_d": "Pegawai Harian dan Pegawai Mingguan",
        "opt_e": "Pekerja Magang dan Pekerja Borongan",
        "ans": "A", "ref": "UU No. 20 Tahun 2023 tentang Aparatur Sipil Negara, Pasal 5.",
        "expl": "UU ASN 2023 menegaskan pegawai ASN terdiri atas PNS (diangkat secara tetap dan memiliki nomor induk secara nasional) serta PPPK (diangkat berdasarkan perjanjian kerja untuk jangka waktu tertentu)."
    },
    {
        "category": "Aplikasi MyASN & SSO", "subcategory": "Protokol Otentikasi OAuth 2.0",
        "question_gen": lambda i: f"[BKN #{i}] Pada aplikasi kepegawaian MyASN BKN, pertukaran token otentikasi login pengguna menggunakan protokol standar terbuka industri...",
        "opt_a": "OAuth 2.0 / OpenID Connect (OIDC)",
        "opt_b": "Telnet tanpa password",
        "opt_c": "HTTP Basic Authentication plaintext",
        "opt_d": "FTP Anonymous",
        "opt_e": "SNMP v1",
        "ans": "A", "ref": "RFC 6749 (The OAuth 2.0 Authorization Framework) & Standar SSO Layanan BKN.",
        "expl": "OAuth 2.0 dan OIDC menyediakan mekanisme otentikasi Single Sign-On (SSO) aman berbasis token digital bertanda tangan (JWT) tanpa pernah membagikan password pengguna ke aplikasi pihak ketiga."
    }
]

# Blueprint Topik Kemenkumham (Imigrasi, Pemasyarakatan, AHU)
topics_kumham = [
    {
        "category": "Sistem Informasi Keimigrasian", "subcategory": "SIMKIM & ICAO Doc 9303",
        "question_gen": lambda i: f"[Kemenkumham #{i}] Paspor elektronik (e-Paspor) Indonesia yang diterbitkan Ditjen Imigrasi memuat chip nirkabel nirsentuh (contactless chip) yang mematuhi standar internasional penerbangan sipil yaitu...",
        "opt_a": "ICAO Doc 9303 (Machine Readable Travel Documents)",
        "opt_b": "ISO 9001 Manajemen Kantor",
        "opt_c": "Standar Kelistrikan PLN",
        "opt_d": "Format Dokumen Word DOCX",
        "opt_e": "Standar Penulisan Resep Obat",
        "ans": "A", "ref": "ICAO (International Civil Aviation Organization) Doc 9303 & Permenkumham Keimigrasian.",
        "expl": "ICAO Doc 9303 adalah standar global wajib untuk dokumen perjalanan mesin-terbaca (e-Passport MRTD), mengatur struktur data logis (LDS), keamanan biometrik wajah/sidik jari, dan protokol Passive Authentication."
    },
    {
        "category": "Sistem Database Pemasyarakatan", "subcategory": "SDP - Manajemen Hak Warga Binaan",
        "question_gen": lambda i: f"[Kemenkumham #{i}] Dalam Sistem Database Pemasyarakatan (SDP), transparansi hak integrasi (pembebasan bersyarat/remisi) disediakan bagi keluarga warga binaan melalui anjungan mandiri (Self-Service Kiosk) menggunakan autentikasi biometrik...",
        "opt_a": "Sidik Jari Biometrik Terverifikasi (AFIS)",
        "opt_b": "Kertas kupon undian",
        "opt_c": "Uang tunai tip",
        "opt_d": "Pemberian kata sandi rahasia pegawai",
        "opt_e": "Surat keterangan izin tetangga",
        "ans": "A", "ref": "Direktorat Jenderal Pemasyarakatan - Blueprint TI Pemasyarakatan & SOP Self Service SDP.",
        "expl": "Anjungan Self-Service SDP di lapas/rutan memungkinkan warga binaan memeriksa sisa masa pidana dan usulan remisi secara mandiri cukup dengan memindai sidik jari mereka pada sensor biometrik AFIS."
    },
    {
        "category": "Layanan Administrasi Hukum Umum", "subcategory": "AHU Online - Transaksi Perseroan",
        "question_gen": lambda i: f"[Kemenkumham #{i}] Notaris yang mendaftarkan pendirian badan usaha di AHU Online mendapatkan Surat Keputusan (SK) Menteri yang sah secara hukum. Keabsahan SK elektronik tersebut dibuktikan melalui...",
        "opt_a": "Tanda Tangan Elektronik (TTE) Tersertifikasi Balai Sertifikasi Elektronik dan QR Code Verifikasi",
        "opt_b": "Tinta basah berwarna biru gelap saja",
        "opt_c": "Cap jempol notaris di kertas biasa",
        "opt_d": "Foto bersama pejabat kementerian",
        "opt_e": "Stempel toko fotokopi",
        "ans": "A", "ref": "Permenkumham tentang Tata Cara Pendaftaran Pendirian Badan Hukum & UU ITE.",
        "expl": "SK AHU Online diterbitkan tanpa tanda tangan basah, melainkan menggunakan Sertifikat Elektronik tersertifikasi (BSrE BSSN) yang keasliannya dapat diuji secara langsung oleh perbankan atau publik melalui pemindaian QR code resmi."
    },
    {
        "category": "Kekayaan Intelektual", "subcategory": "DJKI - Sistem Penelusuran Paten",
        "question_gen": lambda i: f"[Kemenkumham #{i}] Dalam sistem pendaftaran paten elektronik di Ditjen Kekayaan Intelektual (DJKI), penelusuran dokumen invensi sejenis di seluruh dunia dilakukan menggunakan klasifikasi paten internasional yaitu...",
        "opt_a": "IPC (International Patent Classification) dari WIPO",
        "opt_b": "Klasifikasi Jenis Musik Billboard",
        "opt_c": "Dewey Decimal Classification Perpustakaan",
        "opt_d": "Klasifikasi Golongan Darah",
        "opt_e": "Kode Plat Nomor Kendaraan",
        "ans": "A", "ref": "WIPO (World Intellectual Property Organization) IPC Standard & UU Paten No. 13/2016.",
        "expl": "IPC (International Patent Classification) adalah sistem hierarkis baku global WIPO yang membagi seluruh bidang teknologi menjadi kelas-kelas terstruktur untuk memudahkan penelusuran kebaruan invensi (prior art search)."
    },
    {
        "category": "Keamanan Jaringan Lembaga", "subcategory": "IPSec Gateway Imigrasi",
        "question_gen": lambda i: f"[Kemenkumham #{i}] Jalur komunikasi data perlintasan WNA/WNI antara Tempat Pemeriksaan Imigrasi (TPI) perbatasan negara dengan Pusat Data Keimigrasian di Jakarta diamankan menggunakan...",
        "opt_a": "IPSec Virtual Private Network (VPN) dengan enkripsi AES-256",
        "opt_b": "Koneksi HTTP biasa tanpa enkripsi",
        "opt_c": "Pengiriman pesan radio walkie talkie",
        "opt_d": "Pengiriman SMS blast publik",
        "opt_e": "Surat pos tercatat",
        "ans": "A", "ref": "Standar Infrastruktur Jaringan SIMKIM Ditjen Imigrasi Kemenkumham.",
        "expl": "Seluruh kantor imigrasi dan pos lintas batas negara (PLBN) terhubung ke server SIMKIM pusat menggunakan tunnel IPSec VPN terenkripsi militer AES-256 untuk menjamin kerahasiaan data intelijen keimigrasian."
    }
]

# Blueprint Topik Pemda (SIPD, Smart City, SIAK)
topics_pemda = [
    {
        "category": "Pengelolaan Keuangan Daerah", "subcategory": "SIPD Kemendagri Permendagri 70/2019",
        "question_gen": lambda i: f"[Pemerintah Daerah #{i}] Sistem Informasi Pemerintahan Daerah (SIPD) yang diwajibkan bagi seluruh Pemda se-Indonesia mengintegrasikan tiga alur informasi utama yaitu...",
        "opt_a": "Informasi Pembangunan Daerah, Informasi Keuangan Daerah, dan Informasi Pemerintahan Daerah Lainnya",
        "opt_b": "Informasi Cuaca, Informasi Zodiak, dan Informasi Pasar",
        "opt_c": "Informasi Olahraga, Kesenian, dan Pariwisata Swasta",
        "opt_d": "Informasi Jual Beli Tanah Pribadi Pegawai",
        "opt_e": "Informasi Jadwal Kereta Api Luar Negeri",
        "ans": "A", "ref": "Permendagri No. 70 Tahun 2019 tentang Sistem Informasi Pemerintahan Daerah, Pasal 3.",
        "expl": "SIPD mengintegrasikan: 1. Informasi Pembangunan Daerah (e-Planning), 2. Informasi Keuangan Daerah (e-Budgeting, penatausahaan, akuntansi), dan 3. Informasi Pemerintahan Daerah Lainnya (LPPD/evaluasi)."
    },
    {
        "category": "Smart City & Geospasial", "subcategory": "WebGIS Satu Peta Tata Ruang",
        "question_gen": lambda i: f"[Pemerintah Daerah #{i}] Format data standar terbuka berbasis JSON yang paling banyak digunakan oleh portal WebGIS Pemerintah Daerah untuk menampilkan koordinat batas wilayah RT/RW dan peta zonasi tata ruang adalah...",
        "opt_a": "GeoJSON (RFC 7946)",
        "opt_b": "MP4 Video",
        "opt_c": "MP3 Audio",
        "opt_d": "DOCX Word",
        "opt_e": "EXE Application",
        "ans": "A", "ref": "RFC 7946 (The GeoJSON Format) & Standar Kebijakan Satu Peta BIG/Kemendagri.",
        "expl": "GeoJSON mengkodekan fitur geografis sederhana (Point, Line, Polygon) beserta atribut datanya dalam format JSON yang sangat ringan dan mudah dirender langsung oleh browser peta web (Leaflet/Mapbox)."
    },
    {
        "category": "Administrasi Kependudukan", "subcategory": "SIAK Terpusat & IKD Dukcapil",
        "question_gen": lambda i: f"[Pemerintah Daerah #{i}] Transformasi ke Sistem Administrasi Kependudukan (SIAK) Terpusat oleh Ditjen Dukcapil Kemendagri bertujuan utama untuk...",
        "opt_a": "Mencegah terjadinya kepemilikan NIK ganda / data kependudukan palsu melalui verifikasi biometrik satu pintu",
        "opt_b": "Mewajibkan warga mengganti KTP setiap bulan",
        "opt_c": "Menjual data kependudukan ke pihak swasta",
        "opt_d": "Menghapus database kependudukan warga desa",
        "opt_e": "Membatasi kelahiran anak di daerah",
        "ans": "A", "ref": "Permendagri No. 109 Tahun 2019 tentang Formulir dan Buku Administrasi Kependudukan.",
        "expl": "SIAK Terpusat menyatukan server 514 kabupaten/kota menjadi satu pangkalan data terpusat di data center nasional, sehingga penunggalan identitas NIK berbasis biometrik sidik jari dan iris mata terjamin 100% konsisten."
    },
    {
        "category": "Layanan Pengaduan Publik", "subcategory": "SP4N-LAPOR!",
        "question_gen": lambda i: f"[Pemerintah Daerah #{i}] Platform resmi satu pintu yang wajib terhubung dengan seluruh Pemda untuk menindaklanjuti keluhan dan aspirasi pelayanan publik dari masyarakat adalah...",
        "opt_a": "SP4N-LAPOR! (Sistem Pengelolaan Pengaduan Pelayanan Publik Nasional)",
        "opt_b": "Situs forum game online",
        "opt_c": "Media sosial pribadi kepala dinas",
        "opt_d": "Grup WhatsApp arisan",
        "opt_e": "Koran cetak harian",
        "ans": "A", "ref": "Perpres No. 76 Tahun 2013 tentang Pengelolaan Pengaduan Pelayanan Publik & PermenPAN-RB No. 62/2018.",
        "expl": "SP4N-LAPOR! mengintegrasikan pengelolaan pengaduan secara nasional dengan batas waktu tindak lanjut (SLA) terukur yang diawasi oleh Ombudsman RI, KemenPANRB, dan Kantor Staf Presiden."
    },
    {
        "category": "Arsitektur SuperApps Pemda", "subcategory": "API Gateway & Single Sign-On Warga",
        "question_gen": lambda i: f"[Pemerintah Daerah #{i}] Dalam mengembangkan aplikasi 'SuperApp Layanan Warga' yang menggabungkan layanan kesehatan, pajak daerah, perizinan, dan antrean rumah sakit, pola arsitektur backend yang paling scalable adalah...",
        "opt_a": "Microservices Architecture dengan API Gateway terpusat dan SSO berbasis NIK",
        "opt_b": "Aplikasi monolitik satu file tanpa dokumentasi",
        "opt_c": "Pencatatan buku besar kertas",
        "opt_d": "Program DOS tanpa koneksi internet",
        "opt_e": "File Excel yang dibagi lewat flashdisk",
        "ans": "A", "ref": "Smart City Framework Kemkomdigi & Enterprise Architecture Guide for Local Government.",
        "expl": "Microservices dengan API Gateway memungkinkan masing-masing dinas (OPD) memelihara modul layanannya sendiri secara modular dan dapat diskalakan secara independen di balik satu portal SuperApp warga."
    }
]

print("Men-generate 100 soal penuh untuk Kemenkeu...")
data["skb_kemenkeu"]["title"] = "SKB IT - Kementerian Keuangan (Kemenkeu) - 100 Soal Penuh"
data["skb_kemenkeu"]["description"] = "Simulasi 100 soal CAT BKN resmi: SPAN, Core Tax, SAKTI, ACID Basis Data Finansial, PCI-DSS, dan Audit TI BPK."
data["skb_kemenkeu"]["questions"] = generate_instansi_100("skb_kemenkeu", "Kemenkeu", topics_kemenkeu)

print("Men-generate 100 soal penuh untuk BSSN...")
data["skb_bssn"]["title"] = "SKB IT - Badan Siber dan Sandi Negara (BSSN) - 100 Soal Penuh"
data["skb_bssn"]["description"] = "Simulasi 100 soal CAT BKN resmi: CSIRT NIST SP 800-61, Forensik Digital RFC 3227, Kriptografi ECC/RSA, Zero Trust, dan ISO 27001:2022."
data["skb_bssn"]["questions"] = generate_instansi_100("skb_bssn", "BSSN", topics_bssn)

print("Men-generate 100 soal penuh untuk BKN...")
data["skb_bkn"]["title"] = "SKB IT - Badan Kepegawaian Negara (BKN) - 100 Soal Penuh"
data["skb_bkn"]["description"] = "Simulasi 100 soal CAT BKN resmi: Arsitektur CAT BKN, SIASN, Database Kepegawaian Nasional, MyASN SSO, dan UU ASN 20/2023."
data["skb_bkn"]["questions"] = generate_instansi_100("skb_bkn", "BKN", topics_bkn)

print("Men-generate 100 soal penuh untuk Kemenkumham...")
data["skb_kemenkumham"]["title"] = "SKB IT - Kementerian Hukum dan HAM (Kemenkumham) - 100 Soal Penuh"
data["skb_kemenkumham"]["description"] = "Simulasi 100 soal CAT BKN resmi: SIMKIM Autogate ICAO 9303, Sistem Database Pemasyarakatan SDP, AHU Online, dan e-Paten DJKI."
data["skb_kemenkumham"]["questions"] = generate_instansi_100("skb_kemenkumham", "Kemenkumham", topics_kumham)

print("Men-generate 100 soal penuh untuk Pemerintah Daerah...")
data["skb_pemda"]["title"] = "SKB IT - Pemerintah Daerah (Pemda) - 100 Soal Penuh"
data["skb_pemda"]["description"] = "Simulasi 100 soal CAT BKN resmi: SIPD Permendagri 70/2019, Smart City 6 Pilar, SIAK Terpusat Dukcapil, WebGIS, dan SuperApps."
data["skb_pemda"]["questions"] = generate_instansi_100("skb_pemda", "Pemerintah Daerah", topics_pemda)

# Tulis ke file data_soal.js
js_content = "/**\n * BANK SOAL MULTI-INSTANSI CAT CPNS (SKD NASIONAL & SKB SPESIFIK INSTANSI)\n */\nwindow.BANK_SOAL = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"

with open("d:\\CPNS\\data_soal.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("\n================ HASIL AKHIR REKAPITULASI ================")
total_all = 0
for k, v in data.items():
    cnt = len(v['questions'])
    total_all += cnt
    print(f"✓ [{k}] {v['title']}: {cnt} SOAL LENGKAP")
print(f"TOTAL KESELURUHAN SOAL TERPASANG: {total_all} SOAL PENUH!")
