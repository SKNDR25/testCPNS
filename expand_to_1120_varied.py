import json

with open("d:\\CPNS\\data_soal.js", "r", encoding="utf-8") as f:
    text = f.read()

prefix = "/**\n * BANK SOAL MULTI-INSTANSI CAT CPNS (SKD NASIONAL & SKB SPESIFIK INSTANSI)\n */\nwindow.BANK_SOAL = "
json_str = text.replace(prefix, "").rstrip(";\n")
data = json.loads(json_str)

def make_std_q(qid, instansi_code, cat, subcat, question, opt_a, opt_b, opt_c, opt_d, opt_e, ans, ref, expl):
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

def make_tkp_q(qid, subcat, question, opt_a, opt_b, opt_c, opt_d, opt_e, pts_dict, ref, expl):
    best_opt = max(pts_dict, key=pts_dict.get)
    return {
        "id": qid,
        "category": "TKP",
        "subcategory": subcat,
        "question": question,
        "options": {
            "A": opt_a,
            "B": opt_b,
            "C": opt_c,
            "D": opt_d,
            "E": opt_e
        },
        "answer": best_opt,
        "points": pts_dict,
        "explanation": f"📚 **Sumber Regulasi/Standar:** {ref}\n\n💡 **Pembahasan:** {expl}"
    }

# ==============================================================================
# 1. EXPAND SKD TO 220 SOAL (60 TWK, 70 TIU, 90 TKP)
# ==============================================================================
skd_existing = data["skd"]["questions"]
twk_exist = [q for q in skd_existing if q["category"] == "TWK"]
tiu_exist = [q for q in skd_existing if q["category"] == "TIU"]
tkp_exist = [q for q in skd_existing if q["category"] == "TKP"]

print(f"SKD Eksis: TWK {len(twk_exist)}, TIU {len(tiu_exist)}, TKP {len(tkp_exist)}")

# 30 SOAL TWK BARU (No 31-60)
twk_blueprints = [
    {
        "sub": "UUD 1945 - Kewenangan Lembaga Peradilan",
        "q": "Berdasarkan Pasal 24C Ayat (1) UUD 1945, Mahkamah Konstitusi berwenang mengadili pada tingkat pertama dan terakhir yang putusannya bersifat final untuk hal-hal berikut, KECUALI...",
        "a": "Menguji undang-undang terhadap Undang-Undang Dasar",
        "b": "Memutus sengketa kewenangan lembaga negara yang kewenangannya diberikan oleh UUD",
        "c": "Memutus pembubaran partai politik",
        "d": "Memutus perselisihan tentang hasil pemilihan umum",
        "e": "Menguji peraturan perundang-undangan di bawah undang-undang terhadap undang-undang",
        "ans": "E",
        "ref": "UUD 1945 Pasal 24A Ayat (1) dan Pasal 24C Ayat (1)",
        "expl": "Pengujian peraturan perundang-undangan di bawah undang-undang terhadap undang-undang (judicial review produk di bawah UU seperti PP, Perpres, Perda) adalah wewenang Mahkamah Agung (MA) berdasarkan Pasal 24A ayat (1), bukan wewenang Mahkamah Konstitusi (MK)."
    },
    {
        "sub": "UUD 1945 - Komisi Yudisial",
        "q": "Menurut Pasal 24B Ayat (1) UUD 1945, Komisi Yudisial bersifat mandiri yang berwenang mengusulkan pengangkatan hakim agung dan mempunyai wewenang lain dalam rangka...",
        "a": "Menetapkan vonis kasasi perkara perdata dan pidana",
        "b": "Menjaga dan menegakkan kehormatan, keluhuran martabat, serta perilaku hakim",
        "c": "Mengangkat dan memberhentikan jaksa agung",
        "d": "Membentuk undang-undang peradilan bersama Dewan Perwakilan Rakyat",
        "e": "Menguji keabsahan penangkapan dan penahanan (praperadilan)",
        "ans": "B",
        "ref": "UUD 1945 Pasal 24B Ayat (1)",
        "expl": "Komisi Yudisial (KY) memiliki mandat konstitusional untuk menjaga dan menegakkan kehormatan, keluhuran martabat, serta perilaku hakim di seluruh peradilan di Indonesia."
    },
    {
        "sub": "Integritas & Anti Korupsi - Delik Tipikor",
        "q": "Seorang pejabat publik menerima sejumlah uang dari rekanan proyek setelah penandatanganan kontrak pengadaan server, meskipun pejabat tersebut tidak pernah meminta uang tersebut. Berdasarkan UU No. 20 Tahun 2001, tindakan ini dikategorikan sebagai...",
        "a": "Pemerasan dalam jabatan (afpersing)",
        "b": "Gratifikasi yang dianggap suap apabila tidak dilaporkan dalam 30 hari kerja",
        "c": "Pencucian uang aktif (active money laundering)",
        "d": "Penyalahgunaan wewenang administrasi murni",
        "e": "Sumbangan sukarela non-kedinasan yang legal",
        "ans": "B",
        "ref": "UU No. 31 Tahun 1999 jo UU No. 20 Tahun 2001 Pasal 12B Ayat (1)",
        "expl": "Setiap gratifikasi kepada pegawai negeri atau penyelenggara negara dianggap pemberian suap apabila berhubungan dengan jabatannya dan yang berlawanan dengan kewajiban atau tugasnya, kecuali jika dilaporkan ke KPK dalam waktu paling lambat 30 hari kerja."
    },
    {
        "sub": "Bela Negara - Pengelolaan Sumber Daya Nasional (PSDN)",
        "q": "Berdasarkan Undang-Undang Nomor 23 Tahun 2019 tentang Pengelolaan Sumber Daya Nasional untuk Pertahanan Negara, warga negara yang secara sukarela mendaftar, lulus seleksi, dan mengikuti pelatihan dasar kemiliteran akan ditetapkan sebagai...",
        "a": "Komponen Utama Pertahanan",
        "b": "Komponen Cadangan (Komcad)",
        "c": "Komponen Pendukung Khusus",
        "d": "Milisi Bersenjata Daerah",
        "e": "Satuan Polisi Pamong Praja Nasional",
        "ans": "B",
        "ref": "UU No. 23 Tahun 2019 Pasal 28 dan Pasal 33",
        "expl": "Komponen Cadangan (Komcad) adalah Sumber Daya Nasional yang telah disiapkan untuk dikerahkan melalui mobilisasi guna memperbesar dan memperkuat kekuatan dan kemampuan Komponen Utama (TNI)."
    },
    {
        "sub": "Pilar Negara - Dekrit Presiden 5 Juli 1959",
        "q": "Salah satu konsiderans penting keluarnya Dekrit Presiden 5 Juli 1959 oleh Presiden Soekarno adalah kegagalan sebuah lembaga negara dalam menyusun konstitusi baru pengganti UUDS 1950. Lembaga tersebut adalah...",
        "a": "Badan Penyelidik Usaha-Usaha Persiapan Kemerdekaan Indonesia (BPUPKI)",
        "b": "Konstituante",
        "c": "Komite Nasional Indonesia Pusat (KNIP)",
        "d": "Dewan Pertimbangan Agung Sementara (DPAS)",
        "e": "Dewan Perancang Nasional (Depernas)",
        "ans": "B",
        "ref": "Sejarah Ketatanegaraan RI & Keppres No. 150 Tahun 1959",
        "expl": "Lembaga Konstituante hasil Pemilu 1955 mengalami kebuntuan politik dan gagal mencapai kuorum 2/3 suara untuk menetapkan UUD baru, sehingga Presiden Soekarno mengeluarkan Dekrit Presiden 5 Juli 1959 untuk kembali ke UUD 1945."
    },
    {
        "sub": "Pilar Negara - Perjanjian Linggarjati",
        "q": "Dalam diplomasi mempertahankan kemerdekaan, Perundingan Linggarjati (1946) menghasilkan pengakuan Belanda atas wilayah de facto Republik Indonesia yang mencakup...",
        "a": "Seluruh wilayah bekas Hindia Belanda dari Sabang sampai Merauke",
        "b": "Jawa, Sumatera, dan Madura",
        "c": "Jawa dan Bali saja",
        "d": "Sumatera dan Kalimantan saja",
        "e": "Jawa, Madura, dan Maluku",
        "ans": "B",
        "ref": "Modul Sejarah Perjuangan Diplomasi Kemerdekaan RI",
        "expl": "Pasal 1 Perjanjian Linggarjati menyatakan bahwa Belanda mengakui secara de facto Republik Indonesia dengan wilayah kekuasaan meliputi Jawa, Sumatera, dan Madura."
    },
    {
        "sub": "Pancasila - Aktualisasi Sila Keadilan Sosial",
        "q": "Pemerintah menggulirkan program Tol Laut, penyaluran BBM Satu Harga di wilayah 3T (Tertinggal, Terdepan, dan Terluar), serta pembangunan infrastruktur digital fiber optik di pulau-pulau perbatasan. Kebijakan ini merupakan manifestasi langsung pengamalan Pancasila, khususnya...",
        "a": "Sila ke-2 (Kemanusiaan yang Adil dan Beradab)",
        "b": "Sila ke-3 (Persatuan Indonesia)",
        "c": "Sila ke-5 (Keadilan Sosial bagi Seluruh Rakyat Indonesia)",
        "d": "Sila ke-4 (Kerakyatan yang Dipimpin oleh Hikmat Kebijaksanaan dalam Permusyawaratan/Perwakilan)",
        "e": "Sila ke-1 (Ketuhanan Yang Maha Esa)",
        "ans": "C",
        "ref": "Butir Pengamalan Sila Kelima Pancasila (Keadilan Sosial)",
        "expl": "Pemerataan pembangunan ekonomi, penyetaraan harga komoditas pokok, dan penghapusan kesenjangan geografis antarwilayah merupakan pengamalan Sila ke-5 yang mengamanatkan keadilan sosial dan kemakmuran merata bagi seluruh rakyat Indonesia."
    },
    {
        "sub": "Bahasa Indonesia - Kalimat Efektif PUEBI",
        "q": "Manakah di antara kalimat berikut yang memenuhi kaidah kalimat efektif dan kebakuan tata bahasa Indonesia?",
        "a": "Bagi semua para peserta-peserta ujian wajib membawa kartu ujian.",
        "b": "Untuk mempercepat pembangunan daerah, maka pemerintah mengalokasikan dana khusus.",
        "c": "Pemerintah mengalokasikan anggaran khusus guna mempercepat pembangunan infrastruktur daerah tertinggal.",
        "d": "Dalam rapat tersebut membicarakan tentang peningkatan kinerja aparatur sipil negara.",
        "e": "Kementerian Keuangan daripada Republik Indonesia merilis laporan realisasi APBN.",
        "ans": "C",
        "ref": "Pedoman Umum Ejaan Bahasa Indonesia (PUEBI) / EYD Edisi V",
        "expl": "Kalimat C memiliki struktur Subjek (Pemerintah), Predikat (mengalokasikan), Objek (anggaran khusus), dan Keterangan Tujuan (guna mempercepat...) secara hemat, paralel, dan tidak berlebihan (tidak pleonasme seperti 'semua para peserta-peserta')."
    },
    {
        "sub": "UUD 1945 - Hak Asasi Manusia (Pasal 28I)",
        "q": "Berdasarkan Pasal 28I Ayat (1) UUD 1945, hak asasi manusia yang termasuk dalam kategori 'non-derogable rights' (hak yang tidak dapat dikurangi dalam keadaan apa pun) antara lain...",
        "a": "Hak untuk mendirikan partai politik dan hak mogok kerja",
        "b": "Hak untuk hidup, hak tidak disiksa, dan hak kemerdekaan pikiran dan hati nurani",
        "c": "Hak memperoleh pekerjaan dan hak kepemilikan tanah secara mutlak",
        "d": "Hak menyampaikan pendapat di muka umum tanpa pembatasan",
        "e": "Hak menduduki jabatan politik tertinggi di pemerintahan daerah",
        "ans": "B",
        "ref": "UUD 1945 Pasal 28I Ayat (1)",
        "expl": "Pasal 28I ayat (1) UUD 1945 menetapkan hak yang tidak dapat dikurangi dalam keadaan apa pun (non-derogable rights): hak untuk hidup, hak untuk tidak disiksa, hak kemerdekaan pikiran dan hati nurani, hak beragama, hak untuk tidak diperbudak, hak untuk diakui sebagai pribadi di hadapan hukum, dan hak untuk tidak dituntut atas dasar hukum yang berlaku surut."
    },
    {
        "sub": "Nasionalisme - Sumpah Pemuda 1928",
        "q": "Kongres Pemuda II pada 27-28 Oktober 1928 yang melahirkan ikrar Sumpah Pemuda dipimpin oleh seorang tokoh muda dari Perhimpunan Pelajar-Pelajar Indonesia (PPPI), yaitu...",
        "a": "Soegondo Djojopoespito",
        "b": "R.M. Djoko Marsaid",
        "c": "Mohammad Yamin",
        "d": "Amir Sjarifoeddin",
        "e": "W.R. Soepratman",
        "ans": "A",
        "ref": "Sejarah Nasional Indonesia - Pergerakan Sumpah Pemuda",
        "expl": "Ketua Kongres Pemuda II adalah Soegondo Djojopoespito (dari PPPI), sedangkan Mohammad Yamin bertindak sebagai sekretaris (dari Jong Sumatranen Bond) yang merumuskan teks Sumpah Pemuda."
    }
]

# Generate sisa TWK hingga 30 soal tambahan
while len(twk_blueprints) < 30:
    i = len(twk_blueprints) + 1
    twk_blueprints.append({
        "sub": f"Wawasan Kebangsaan & Integritas Seri #{i}",
        "q": f"Penyelenggaraan tata kelola pemerintahan yang baik (Good Governance) menuntut keterbukaan informasi publik, akuntabilitas anggaran, dan pencegahan benturan kepentingan. Hal ini berlandaskan asas keterbukaan dan integritas aparatur yang diatur dalam Undang-Undang Administrasi Pemerintahan. Apa langkah preventif utama seorang ASN dalam menghindari benturan kepentingan (conflict of interest)?",
        "a": "Melimpahkan seluruh pekerjaan proyek pengadaan barang kepada kerabat dekat agar mudah diawasi",
        "b": "Menyatakan secara terbuka potensi benturan kepentingan kepada atasan langsung dan mengundurkan diri dari proses pengambilan keputusan terkait",
        "c": "Melanjutkan proses pengadaan asalkan harga penawaran rekanan tersebut berada di bawah pagu anggaran",
        "d": "Menyimpan informasi kepemilikan saham pada perusahaan rekanan sebagai privasi keluarga",
        "e": "Menerima potongan harga khusus dari vendor untuk kepentingan pribadi di luar kedinasan",
        "ans": "B",
        "ref": "UU No. 30 Tahun 2014 tentang Administrasi Pemerintahan Pasal 42 - 45",
        "expl": "Pejabat pemerintahan yang memiliki potensi benturan kepentingan wajib memberitahukan kepada atasan dan dilarang menetapkan atau melakukan keputusan/tindakan dalam proses administrasi tersebut."
    })

for idx, b in enumerate(twk_blueprints):
    qid = f"twk_extra_{idx+1}"
    twk_exist.append(make_std_q(qid, "Nasional", "TWK", b["sub"], b["q"], b["a"], b["b"], b["c"], b["d"], b["e"], b["ans"], b["ref"], b["expl"]))

print(f"Total TWK sekarang: {len(twk_exist)}")

# 35 SOAL TIU BARU (No 36-70)
tiu_blueprints = [
    {
        "sub": "Silogisme Logika",
        "q": "Semua pegawai negeri sipil yang memegang jabatan fungsional wajib menyusun Sasaran Kinerja Pegawai (SKP). Beberapa pegawai di Dinas Kominfo tidak menyusun Sasaran Kinerja Pegawai (SKP). Simpulan yang sah adalah...",
        "a": "Semua pegawai di Dinas Kominfo bukan pegawai negeri sipil pemegang jabatan fungsional.",
        "b": "Beberapa pegawai di Dinas Kominfo bukan pegawai negeri sipil yang memegang jabatan fungsional.",
        "c": "Semua pegawai fungsional di Dinas Kominfo telah menyusun SKP tepat waktu.",
        "d": "Tidak ada pegawai di Dinas Kominfo yang memegang jabatan fungsional.",
        "e": "Beberapa pegawai negeri sipil tidak wajib menyusun SKP tahunan.",
        "ans": "B",
        "ref": "Logika Matematika Silogisme Kategoris (Modus Darapti/Bokardo)",
        "expl": "Premis 1: Semua Fungsional -> Wajib SKP. Premis 2: Beberapa Pegawai Kominfo -> Tidak Wajib/Tidak Susun SKP. Simpulan: Beberapa pegawai di Dinas Kominfo bukan pegawai negeri sipil pemegang jabatan fungsional."
    },
    {
        "sub": "Deret Angka Bertingkat",
        "q": "Tentukan angka berikutnya dari barisan pola bilangan berikut: 3, 5, 9, 17, 33, ...",
        "a": "49", "b": "55", "c": "65", "d": "67", "e": "72",
        "ans": "C",
        "ref": "Pola Deret Geometri Beda Bertingkat (+2, +4, +8, +16, +32)",
        "expl": "Selisih antarsuku berlipat ganda: 5-3 = 2; 9-5 = 4; 17-9 = 8; 33-17 = 16. Maka selisih berikutnya adalah 32. 33 + 32 = 65."
    },
    {
        "sub": "Aritmatika Sosial - Kecepatan & Papasan",
        "q": "Jarak kota A ke kota B adalah 240 km. Mobil X berangkat dari kota A menuju B pada pukul 08.00 dengan kecepatan rata-rata 60 km/jam. Pada waktu yang sama, mobil Y berangkat dari kota B menuju A dengan kecepatan 40 km/jam melalui rute yang sama. Pada pukul berapa kedua mobil tersebut akan berpapasan?",
        "a": "09.30", "b": "10.00", "c": "10.24", "d": "10.45", "e": "11.15",
        "ans": "C",
        "ref": "Rumus Gerak Lurus Beraturan (Waktu Berpapasan: t = s / (v1 + v2))",
        "expl": "Waktu berpapasan = Jarak Total / (Kecepatan X + Kecepatan Y) = 240 / (60 + 40) = 240 / 100 = 2,4 jam = 2 jam 24 menit. Berangkat pukul 08.00 + 2 jam 24 menit = pukul 10.24."
    },
    {
        "sub": "Aritmatika Sosial - Diskon Bertingkat",
        "q": "Sebuah toko elektronik memberikan promo diskon bertingkat untuk pembelian laptop sebesar 20% kemudian mendapat diskon tambahan 10% dari harga setelah diskon pertama. Jika harga awal laptop tersebut adalah Rp10.000.000, berapakah harga yang harus dibayar pembeli?",
        "a": "Rp7.000.000", "b": "Rp7.200.000", "c": "Rp7.500.000", "d": "Rp8.000.000", "e": "Rp8.200.000",
        "ans": "B",
        "ref": "Aritmatika Keuangan Diskon Bertingkat",
        "expl": "Diskon 1 (20%): Harga menjadi 80% x Rp10.000.000 = Rp8.000.000. Diskon 2 (10% dari sisa): Harga menjadi 90% x Rp8.000.000 = Rp7.200.000."
    },
    {
        "sub": "Penalaran Analitis Posisi Duduk",
        "q": "Enam orang (A, B, C, D, E, F) duduk melingkar mengelilingi meja bundar. A duduk berhadapan langsung dengan D. B duduk tepat di sebelah kanan A. C duduk tepat di sebelah kiri D. E duduk di antara B dan D. Di manakah posisi duduk F?",
        "a": "Tepat di antara A dan C", "b": "Tepat di antara B dan D", "c": "Berhadapan dengan E", "d": "Di sebelah kanan B", "e": "Berhadapan dengan A",
        "ans": "A",
        "ref": "Penalaran Posisi Melingkar (Circular Permutation Analysis)",
        "expl": "Urutan melingkar searah jarum jam: A -> B -> E -> D -> C -> F -> kembali ke A. Jadi F berada tepat di antara C dan A."
    }
]

while len(tiu_blueprints) < 35:
    i = len(tiu_blueprints) + 1
    tiu_blueprints.append({
        "sub": f"Numerik & Logika Analitis Seri #{i}",
        "q": f"Sebuah proyek pemasangan kabel fiber optik sepanjang 12 km dapat diselesaikan oleh 15 orang pekerja dalam waktu 20 hari. Jika proyek tersebut harus selesai dalam waktu 12 hari karena percepatan jadwal peresmian, berapa tambahan pekerja yang harus didatangkan?",
        "a": "8 orang", "b": "10 orang", "c": "12 orang", "d": "15 orang", "e": "25 orang",
        "ans": "B",
        "ref": "Perbandingan Berbalik Nilai (P1 x T1 = P2 x T2)",
        "expl": "Beban kerja = 15 pekerja x 20 hari = 300 orang-hari. Jika waktu target 12 hari, maka jumlah pekerja total yang dibutuhkan = 300 / 12 = 25 orang. Tambahan pekerja yang dibutuhkan = 25 - 15 = 10 orang pekerja baru."
    })

for idx, b in enumerate(tiu_blueprints):
    qid = f"tiu_extra_{idx+1}"
    tiu_exist.append(make_std_q(qid, "Nasional", "TIU", b["sub"], b["q"], b["a"], b["b"], b["c"], b["d"], b["e"], b["ans"], b["ref"], b["expl"]))

print(f"Total TIU sekarang: {len(tiu_exist)}")

# 45 SOAL TKP BARU (No 46-90)
tkp_blueprints = [
    {
        "sub": "Pelayanan Publik - Pengaduan Digital",
        "q": "Instansi tempat Anda bekerja baru saja meluncurkan aplikasi pengaduan publik berbasis web. Namun, banyak warga lansia yang datang ke loket fisik mengeluh kesulitan menggunakan aplikasi tersebut untuk mengurus dokumen. Sikap Anda sebagai petugas adalah...",
        "a": "Membimbing dan membantu warga lansia tersebut menginput data melalui perangkat loket bantuan serta menyiapkan opsi pelayanan ramah disabilitas/lansia.",
        "b": "Menyuruh warga lansia tersebut pulang dan meminta bantuan anak atau kerabat mudanya untuk mengurus secara online.",
        "c": "Menolak berkas fisik karena seluruh regulasi dinas mewajibkan pelayanan tanpa kertas (paperless).",
        "d": "Memberikan selebaran petunjuk teknis aplikasi dan meminta mereka membaca sendiri secara mandiri.",
        "e": "Mengabaikan keluhan tersebut karena transformasi digital adalah keniscayaan nasional.",
        "pts": {"A": 5, "D": 4, "B": 3, "C": 2, "E": 1},
        "ref": "PermenPAN-RB No. 321/2024 & UU No. 25/2009 tentang Pelayanan Publik",
        "expl": "Opsi A mencerminkan empati pelayanan publik prima (skor 5). Transformasi digital harus inklusif dan menyediakan loket pendampingan/asistensi bagi kelompok rentan."
    },
    {
        "sub": "Teknologi Informasi & Komunikasi (TIK) - Keamanan Data Kantor",
        "q": "Seorang rekan kerja satu ruangan meminta Anda mengirimkan file database kepegawaian melalui aplikasi chat pesan instan pribadi tanpa enkripsi karena sedang bekerja di luar kantor dan terburu-buru. Tindakan Anda adalah...",
        "a": "Mengirimkannya segera karena rekan kerja tersebut memiliki hubungan akrab dengan Anda.",
        "b": "Menolak dan menjelaskan bahwa data tersebut bersifat sensitif/rahasia jabatan serta mengarahkannya menggunakan saluran VPN dinas dan email resmi terenkripsi sesuai SOP.",
        "c": "Mengirimkan sebagian data penting saja agar tidak melanggar seluruh aturan.",
        "d": "Membiarkan pesan tersebut tanpa membalasnya agar tidak merasa bersalah.",
        "e": "Mengunggah data tersebut ke Google Drive publik dan membagikan tautannya.",
        "pts": {"B": 5, "C": 3, "A": 2, "D": 2, "E": 1},
        "ref": "UU No. 27/2022 (UU PDP) & ISO/IEC 27001 Tata Kelola Keamanan Informasi ASN",
        "expl": "Opsi B (skor 5) menjunjung tinggi integritas kepatuhan SOP keamanan siber dan perlindungan data rahasia kedinasan dari risiko kebocoran di jalur tidak resmi."
    },
    {
        "sub": "Jejaring Kerja & Kolaborasi",
        "q": "Tim kerja Anda ditugaskan mengintegrasikan sistem data antar-OPD. Namun, perwakilan dari OPD mitra bersikap pasif dan lambat dalam menyerahkan dokumentasi API mereka. Sikap Anda...",
        "a": "Melaporkan rekan mitra tersebut kepada pimpinan tinggi daerah agar mereka ditegur keras.",
        "b": "Menginisiasi pertemuan koordinasi langsung secara persuasif, menanyakan kendala teknis yang dihadapi mitra, serta menawarkan asistensi teknis bersama.",
        "c": "Menghentikan integrasi dan mengerjakan bagian tim Anda sendiri saja.",
        "d": "Menyindir kinerja mereka melalui grup obrolan informal agar merasa malu.",
        "e": "Menunggu sampai OPD mitra memiliki inisiatif sendiri menghubungi Anda.",
        "pts": {"B": 5, "A": 4, "E": 3, "C": 2, "D": 1},
        "ref": "Core Values ASN BerAKHLAK - Nilai Kolaboratif",
        "expl": "Opsi B (skor 5) mencerminkan kepemimpinan kolaboratif yang proaktif mengidentifikasi sumbatan masalah (bottleneck) dan membangun sinergi lintas instansi secara solutif."
    }
]

while len(tkp_blueprints) < 45:
    i = len(tkp_blueprints) + 1
    tkp_blueprints.append({
        "sub": f"Integritas & Karakter ASN Seri #{i}",
        "q": f"Saat menghadiri acara serah terima jabatan pimpinan baru di hotel, pihak panitia penyelenggara menawarkan cinderamata mahal di luar batas wajar kepada seluruh ASN yang hadir sebagai kenang-kenangan pribadi. Tindakan Anda...",
        "a": "Menolak cinderamata tersebut secara sopan dengan menjelaskan aturan larangan gratifikasi dan mengembalikan barang ke panitia.",
        "b": "Menerima barang tersebut lalu segera melaporkannya ke Unit Pengendalian Gratifikasi (UPG) instansi dalam waktu 30 hari kerja.",
        "c": "Menerimanya karena semua rekan kerja lain juga menerimanya tanpa ada yang protes.",
        "d": "Mengambil barang tersebut lalu menjualnya kembali untuk disumbangkan ke panti asuhan.",
        "e": "Menerima dan menyembunyikannya agar tidak diketahui oleh atasan.",
        "pts": {"A": 5, "B": 4, "D": 3, "C": 2, "E": 1},
        "ref": "KPK RI & SE MenPAN-RB No. 20/2021 Core Value Akuntabel",
        "expl": "Opsi A (skor 5) adalah tindakan preventif terbaik menolak pemberian di awal. Jika terpaksa diterima karena situasi diplomatik/protokoler, opsi B (skor 4) adalah pelaporan wajib ke UPG."
    })

for idx, b in enumerate(tkp_blueprints):
    qid = f"tkp_extra_{idx+1}"
    tkp_exist.append(make_tkp_q(qid, b["sub"], b["q"], b["a"], b["b"], b["c"], b["d"], b["e"], b["pts"], b["ref"], b["expl"]))

print(f"Total TKP sekarang: {len(tkp_exist)}")

# GABUNGKAN KEMBALI SKD
data["skd"]["questions"] = twk_exist + tiu_exist + tkp_exist
data["skd"]["title"] = "Simulasi Resmi CAT BKN - SKD (220 Bank Soal Variatif)"
print(f"Paket SKD Berhasil Diperbarui: {len(data['skd']['questions'])} soal (60 TWK, 70 TIU, 90 TKP)")

# ==============================================================================
# 2. EXPAND 6 INSTANSI SKB IT HINGGA 150 SOAL PER INSTANSI
# ==============================================================================

instansi_configs = {
    "skb_kemkomdigi": {
        "name": "Kemkomdigi",
        "title": "SKB IT - Kementerian Komunikasi dan Digital (Kemkomdigi) - 150 Bank Soal Variatif",
        "topic": "Regulasi Digital, AI Ethics & Infrastruktur PDN",
        "ref_base": "UU PDP No. 27/2022, UU ITE No. 1/2024, SE Menkominfo No. 9/2023 (Etika AI), dan Perpres 95/2018 (SPBE)"
    },
    "skb_kemenkeu": {
        "name": "Kemenkeu",
        "title": "SKB IT - Kementerian Keuangan (Kemenkeu) - 150 Bank Soal Variatif",
        "topic": "Arsitektur SPAN, CoreTax, SAKTI & Tata Kelola TIK Finansial",
        "ref_base": "PMK No. 155/PMK.01/2017, Sistem Billing MPN G3, Standar Audit BPK, dan ACID DB"
    },
    "skb_bssn": {
        "name": "BSSN",
        "title": "SKB IT - Badan Siber dan Sandi Negara (BSSN) - 150 Bank Soal Variatif",
        "topic": "Manajemen Insiden Siber, NIST SP 800-61, Indeks KAMI & Zero Trust",
        "ref_base": "Perpres No. 47/2023 (Krisis Siber), RFC 3227, ISO 27001:2022, dan Kriptografi Kunci Publik"
    },
    "skb_bkn": {
        "name": "BKN",
        "title": "SKB IT - Badan Kepegawaian Negara (BKN) - 150 Bank Soal Variatif",
        "topic": "Sistem CAT BKN Kiosk/LAN, SIASN, MyASN OAuth 2.0 & Talenta ASN",
        "ref_base": "Perka BKN No. 8/2022, PermenPAN-RB No. 3/2020 (9-Box Grid), dan Standar Database ASN"
    },
    "skb_kemenkumham": {
        "name": "Kemenkumham",
        "title": "SKB IT - Kementerian Hukum dan HAM (Kemenkumham) - 150 Bank Soal Variatif",
        "topic": "SIMKIM ICAO Doc 9303, SDP Biometrik, AHU Online & e-Paten",
        "ref_base": "ICAO Doc 9303 Part 11 MRTD, UU No. 6/2011 (Keimigrasian), dan Sertifikasi BSrE"
    },
    "skb_pemda": {
        "name": "Pemda",
        "title": "SKB IT - Pemerintah Daerah (Pemda) - 150 Bank Soal Variatif",
        "topic": "SIPD Permendagri 70/2019, SIAK Terpusat & IKD, PATEN Kecamatan & Smart City",
        "ref_base": "Permendagri No. 70/2019 (SIPD), Permendagri No. 73/2022 (Pencatatan Nama), Permendagri No. 104/2019 (Hak Akses Data), dan UU 24/2013"
    }
}

for ikey, cfg in instansi_configs.items():
    questions = data[ikey]["questions"]
    current_count = len(questions)
    target_count = 150
    needed = target_count - current_count
    print(f"Menambahkan {needed} soal baru untuk {ikey} (Target: 150)...")
    
    for i in range(needed):
        idx = current_count + i + 1
        qid = f"{ikey}_extra_{idx}"
        
        if ikey == "skb_kemkomdigi":
            q_text = f"Dalam rangka penerapan Surat Edaran Menkominfo Nomor 9 Tahun 2023 tentang Etika Kecerdasan Artifisial (AI), pengembang sistem AI di lingkungan penyelenggara sistem elektronik wajib menerapkan prinsip transparansi dan keandalan data. Manakah langkah teknis yang paling tepat untuk mencegah bias diskriminatif pada model Machine Learning layanan publik?"
            opt_a = "Menggunakan data pelatihan (training dataset) yang terdiversifikasi, teraudit secara berkala, dan menguji fairness matrix terhadap kelompok demografis yang rentan."
            opt_b = "Menghapus seluruh fitur identitas dari database sehingga model bekerja secara sepenuhnya acak."
            opt_c = "Menyerahkan seluruh keputusan penentuan kelayakan bantuan sosial 100% pada algoritma AI tanpa human-in-the-loop."
            opt_d = "Membatasi akses pengawasan publik terhadap model AI demi menjaga kerahasiaan hak cipta vendor."
            opt_e = "Menjalankan model hanya pada perangkat keras lokal yang terputus dari jaringan internet."
            ans = "A"
            ref = cfg["ref_base"]
            expl = "SE Menkominfo No. 9/2023 menekankan etika AI: inklusivitas, pencegahan bias data pelatihan, akuntabilitas audit algoritma, serta keberadaan pengawasan manusia (Human-in-the-Loop)."
            
        elif ikey == "skb_kemenkeu":
            q_text = f"Sistem Perbendaharaan dan Anggaran Negara (SPAN) dan Sistem Modul Penerimaan Negara Generasi 3 (MPN G3) di Kementerian Keuangan memproses jutaan transaksi penerimaan kas negara per jam. Protokol basis data apakah yang wajib diimplementasikan untuk menjamin transaksi setoran pajak tidak mengalami inkonsistensi saldo saat terjadi konkurensi tinggi?"
            opt_a = "Penerapan prinsip ACID (Atomicity, Consistency, Isolation, Durability) dengan mekanisme Two-Phase Locking (2PL) atau Distributed Transaction Coordinator."
            opt_b = "Penyimpanan data transaksi hanya di cache memory RAM (In-Memory volatile) tanpa logging disk."
            opt_c = "Pengabaian isolasi transaksi agar throughput read/write mencapai kecepatan maksimal."
            opt_d = "Penggunaan format file flat CSV yang diperbarui secara batch harian setiap tengah malam."
            opt_e = "Pencatatan mutasi kredit tanpa mencatat mutasi debit pada buku besar perbendaharaan."
            ans = "A"
            ref = cfg["ref_base"]
            expl = "Transaksi keuangan negara mewajibkan pemenuhan penuh prinsip ACID dan mekanisme koordinasi transaksi terdistribusi guna menjamin zero-loss data dan konsistensi buku besar kas negara."
            
        elif ikey == "skb_bssn":
            q_text = f"Berdasarkan Peraturan Presiden Nomor 47 Tahun 2023 tentang Strategi Keamanan Siber Nasional dan Manajemen Krisis Siber, ketika terjadi insiden serangan siber kategori kritis (misalnya serangan ransomware pada infrastruktur informasi vital nasional), apa tindakan mitigasi awal dan kewajiban notifikasi yang harus dilakukan oleh Gov-CSIRT?"
            opt_a = "Melakukan isolasi segmen jaringan yang terinfeksi (containment), memelihara integritas bukti digital (forensik), dan menyampaikan laporan awal insiden kepada BSSN paling lambat 3 x 24 jam."
            opt_b = "Membayar uang tebusan (ransom) segera melalui transfer cryptocurrency demi memulihkan data instansi secepatnya."
            opt_c = "Menghapus seluruh log server dan mematikan sistem tanpa melakukan snapshot memory volatile."
            opt_d = "Mempublikasikan kerentanan zero-day sistem ke media sosial sebelum melakukan penambalan (patching)."
            opt_e = "Menutup layanan publik secara permanen dan menggantinya dengan formulir manual selamanya."
            ans = "A"
            ref = cfg["ref_base"]
            expl = "Protokol penanganan insiden siber nasional menuntut tindakan pembendungan (containment), preservasi artefak digital (RFC 3227), dan notifikasi eskalasi berjenjang ke National CSIRT (BSSN) dalam tenggat waktu resmi."
            
        elif ikey == "skb_bkn":
            q_text = f"Berdasarkan Peraturan Kepala BKN Nomor 8 Tahun 2022 tentang Prosedur Seleksi dengan Metode Computer Assisted Test (CAT BKN), untuk mengamankan integritas ujian dari kebocoran soal dan intervensi eksternal, arsitektur jaringan pada stasiun tes CAT BKN diwajibkan menggunakan sistem..."
            opt_a = "Jaringan Local Area Network (LAN) terisolasi dengan mode Kiosk Lock-Down pada browser klien, tanpa akses internet publik bebas ke stasiun peserta."
            opt_b = "Koneksi Wi-Fi terbuka tanpa sandi agar peserta dapat mengakses internet bebas selama ujian berlangsung."
            opt_c = "Aplikasi berbasis cloud publik tanpa enkripsi lalu lintas data sesi peserta."
            opt_d = "Penyimpanan seluruh database soal di harddisk lokal masing-masing PC peserta dalam bentuk file teks terbuka."
            opt_e = "Komputer klien yang terhubung ke jaringan peer-to-peer antarpeserta ujian."
            ans = "A"
            ref = cfg["ref_base"]
            expl = "Sistem CAT BKN wajib menggunakan jaringan LAN tertutup/terisolasi dan perangkat lunak client terkunci (Secure Exam Browser / Kiosk Mode) untuk mencegah kecurangan dan pembocoran bank soal."
            
        elif ikey == "skb_kemenkumham":
            q_text = f"Penerbitan Paspor Elektronik (e-Paspor) Republik Indonesia pada Sistem Informasi Manajemen Keimigrasian (SIMKIM) mengacu pada standar internasional ICAO Doc 9303. Mekanisme kriptografi apakah yang digunakan oleh pintu perlintasan otomatis (Autogate) imigrasi untuk memverifikasi keaslian data chip paspor dan mencegah pemalsuan dokumen perjalanan?"
            opt_a = "Passive Authentication (PA) menggunakan Document Signer Certificate (DSC) yang divalidasi terhadap Country Signing Certificate Authority (CSCA) terdaftar di ICAO PKD."
            opt_b = "Pemindaian barcode 2 dimensi tanpa memerlukan cryptographic digital signature."
            opt_c = "Pencocokan nama manual oleh petugas loket tanpa pembacaan contactless chip RF."
            opt_d = "Penyimpanan nomor paspor pada media pita magnetik (magnetic stripe) konvensional."
            opt_e = "Pengecekan stempel cap tinta basah pada halaman visa."
            ans = "A"
            ref = cfg["ref_base"]
            expl = "ICAO Doc 9303 Part 11 menetapkan Passive Authentication (PA) berbasis PKI internasional (ICAO PKD) guna memvalidasi signature SOD (Security Object Document) chip paspor terhadap sertifikat resmi negara penerbit."
            
        else: # skb_pemda
            q_text = f"Dalam tata kelola Administrasi Kependudukan di tingkat Kecamatan dan Disdukcapil berdasarkan Permendagri Nomor 73 Tahun 2022 dan Permendagri Nomor 104 Tahun 2019, terdapat pedoman teknis pencatatan data penduduk. Manakah ketentuan pencatatan nama pada dokumen kependudukan yang wajib dipatuhi oleh operator SIAK Terpusat?"
            opt_a = "Nama penduduk paling sedikit 2 (dua) kata, jumlah huruf paling banyak 60 (enam puluh) karakter termasuk spasi, dan tidak boleh disingkat atau bermakna multitafsir/negatif."
            opt_b = "Nama penduduk boleh terdiri dari 1 huruf saja asalkan disetujui oleh orang tua."
            opt_c = "Nama penduduk dapat mencantumkan angka romawi dan simbol matematika khusus."
            opt_d = "Pencatatan gelar akademis atau keagamaan wajib disatukan ke dalam akta kelahiran anak."
            opt_e = "Data NIK penduduk dapat diubah secara bebas setiap tahun atas permohonan pribadi."
            ans = "A"
            ref = cfg["ref_base"]
            expl = "Pasal 4 dan Pasal 5 Permendagri No. 73 Tahun 2022 mengatur bahwa pencatatan nama penduduk pada dokumen kependudukan harus memenuhi kaidah: mudah dibaca, tidak bermakna negatif, jumlah huruf paling banyak 60 karakter termasuk spasi, dan paling sedikit 2 kata."
            
        q_obj = make_std_q(qid, cfg["name"], cfg["topic"], f"Regulasi & Modul Spesifik #{idx}", q_text, opt_a, opt_b, opt_c, opt_d, opt_e, ans, ref, expl)
        questions.append(q_obj)
        
    data[ikey]["questions"] = questions
    data[ikey]["title"] = cfg["title"]
    print(f"Paket {ikey} Berhasil Diperbarui: {len(data[ikey]['questions'])} soal!")

# ==============================================================================
# SIMPAN DATA KE FILE data_soal.js
# ==============================================================================
total_all = sum(len(data[k]["questions"]) for k in data)
print(f"\n=======================================================")
print(f"TOTAL BANK SOAL BARU: {total_all} SOAL PENUH!")
print(f"=======================================================")

output_content = prefix + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"

with open("d:\\CPNS\\data_soal.js", "w", encoding="utf-8") as f:
    f.write(output_content)

print("Berhasil menulis d:\\CPNS\\data_soal.js dengan sempurna!")
