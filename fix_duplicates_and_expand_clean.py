import json

print("Memulai pembersihan dan deduplikasi total bank soal...")

with open("d:\\CPNS\\data_soal.js", "r", encoding="utf-8") as f:
    text = f.read()

prefix = "/**\n * BANK SOAL MULTI-INSTANSI CAT CPNS (SKD NASIONAL & SKB SPESIFIK INSTANSI)\n */\nwindow.BANK_SOAL = "
json_str = text.replace(prefix, "").rstrip(";\n")
data = json.loads(json_str)

# Fungsi pembuat soal standar
def make_std(qid, instansi_code, cat, subcat, q_text, opt_a, opt_b, opt_c, opt_d, opt_e, ans, ref, expl):
    return {
        "id": qid,
        "instansi": instansi_code,
        "category": cat,
        "subcategory": subcat,
        "question": q_text,
        "options": {"A": opt_a, "B": opt_b, "C": opt_c, "D": opt_d, "E": opt_e},
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

# Fungsi pembuat soal TKP
def make_tkp(qid, subcat, q_text, opt_a, opt_b, opt_c, opt_d, opt_e, pts_dict, ref, expl):
    best_opt = max(pts_dict, key=pts_dict.get)
    return {
        "id": qid,
        "category": "TKP",
        "subcategory": subcat,
        "question": q_text,
        "options": {"A": opt_a, "B": opt_b, "C": opt_c, "D": opt_d, "E": opt_e},
        "answer": best_opt,
        "points": pts_dict,
        "explanation": f"📚 **Sumber Regulasi/Standar:** {ref}\n\n💡 **Pembahasan:** {expl}"
    }

# ==============================================================================
# 1. DEDUPLIKASI TOTAL DULU SELURUH PAKET SOAL
# ==============================================================================
for pkey in data:
    orig = data[pkey]["questions"]
    seen = set()
    cleaned = []
    for q in orig:
        t = q["question"].strip().lower()
        if t not in seen:
            seen.add(t)
            cleaned.append(q)
    data[pkey]["questions"] = cleaned
    print(f"Paket {pkey}: Asal {len(orig)} -> Unik {len(cleaned)} soal")

# ==============================================================================
# 2. TAMBAHKAN 9 TWK BARU (Total TWK = 50 unik)
# ==============================================================================
extra_twk = [
    make_std(
        "twk_new_1", "Nasional", "TWK", "UUD 1945 - Hak Pengawasan DPR",
        "Dewan Perwakilan Rakyat (DPR) memiliki fungsi legislasi, anggaran, dan pengawasan. Berdasarkan Pasal 20A Ayat (2) UUD 1945, hak DPR untuk melakukan penyelidikan terhadap pelaksanaan suatu undang-undang atau kebijakan pemerintah yang berkaitan dengan hal penting, strategis, dan berdampak luas bagi kehidupan bermasyarakat disebut...",
        "Hak Interpelasi",
        "Hak Angket",
        "Hak Menyatakan Pendapat",
        "Hak Imunitas",
        "Hak Budget",
        "B",
        "UUD 1945 Pasal 20A Ayat (2) & UU No. 17 Tahun 2014 (MD3)",
        "Hak Angket adalah hak DPR untuk melakukan penyelidikan terhadap pelaksanaan undang-undang atau kebijakan pemerintah yang penting, strategis, dan berdampak luas. Sedangkan Hak Interpelasi adalah hak meminta keterangan."
    ),
    make_std(
        "twk_new_2", "Nasional", "TWK", "UUD 1945 - Badan Pemeriksa Keuangan",
        "Menurut Pasal 23E Ayat (2) UUD 1945, hasil pemeriksaan atas pengelolaan dan tanggung jawab keuangan negara yang dilakukan oleh Badan Pemeriksa Keuangan (BPK) diserahkan secara resmi kepada lembaga perwakilan, yaitu...",
        "Presiden, Menteri Keuangan, dan Mahkamah Agung",
        "Dewan Perwakilan Rakyat, Dewan Perwakilan Daerah, dan Dewan Perwakilan Rakyat Daerah",
        "Komisi Pemberantasan Korupsi dan Kejaksaan Agung",
        "Badan Pengawasan Keuangan dan Pembangunan (BPKP)",
        "Hanya kepada Presiden Republik Indonesia selaku Kepala Pemerintahan",
        "B",
        "UUD 1945 Pasal 23E Ayat (2)",
        "Hasil pemeriksaan BPK diserahkan kepada DPR, DPD, dan DPRD sesuai dengan kewenangannya masing-masing untuk ditindaklanjuti."
    ),
    make_std(
        "twk_new_3", "Nasional", "TWK", "Sejarah Kemerdekaan - Peristiwa Rengasdengklok",
        "Peristiwa penculikan dan pengamanan Soekarno dan Mohammad Hatta ke Rengasdengklok pada tanggal 16 Agustus 1945 oleh golongan muda (antara lain Sukarni, Wikana, dan Chaerul Saleh) dilatarbelakangi oleh...",
        "Kekhawatiran akan adanya serangan militer mendadak dari Sekutu",
        "Perbedaan pandangan agar proklamasi kemerdekaan dilakukan secepatnya tanpa melalui janji kemerdekaan atau campur tangan PPKI buatan Jepang",
        "Keinginan golongan muda untuk membatalkan rencana proklamasi",
        "Adanya ancaman kudeta dari pimpinan tentara PETA di Jawa Tengah",
        "Permintaan resmi dari kaisar Jepang untuk menunda kemerdekaan",
        "B",
        "Sejarah Nasional Indonesia Jilid VI (Zaman Jepang dan Revolusi)",
        "Golongan muda mendesak proklamasi diproklamirkan atas kekuatan bangsa sendiri di luar ikatan PPKI yang dianggap sebagai badan boneka buatan Jepang."
    ),
    make_std(
        "twk_new_4", "Nasional", "TWK", "Sejarah Ketatanegaraan - Maklumat 3 November 1945",
        "Maklumat Pemerintah Nomor X tanggal 3 November 1945 yang ditandatangani oleh Wakil Presiden Mohammad Hatta memiliki pengaruh mendasar bagi sistem demokrasi Indonesia pada masa awal kemerdekaan, yaitu...",
        "Pembubaran seluruh laskar perjuangan rakyat bersenjata",
        "Memberikan keleluasaan pembentukan partai-partai politik dan mengawali peralihan sistem pemerintahan presidensial ke parlementer",
        "Menetapkan UUD 1945 sebagai konstitusi tunggal selamanya",
        "Menghapuskan fungsi Komite Nasional Indonesia Pusat (KNIP)",
        "Menyatukan seluruh kekuasaan kehakiman ke tangan Presiden",
        "B",
        "Sejarah Ketatanegaraan RI (Peralihan Sistem Demokrasi Liberal)",
        "Maklumat 3 November 1945 menganjurkan pembentukan partai-partai politik untuk memperkuat citra demokratis RI di mata dunia internasional."
    ),
    make_std(
        "twk_new_5", "Nasional", "TWK", "Pancasila - Pandangan Hidup Bangsa (Way of Life)",
        "Pancasila berkedudukan sebagai pandangan hidup bangsa Indonesia (Weltanschauung). Hal ini memiliki arti bahwa Pancasila...",
        "Hanya berfungsi sebagai dasar formal dalam sidang-sidang kenegaraan",
        "Berfungsi sebagai pedoman moral, norma tingkah laku, dan petunjuk arah dalam menyelesaikan persoalan kehidupan bermasyarakat sehari-hari",
        "Hanya mengikat para pejabat tinggi negara dan aparatur militer",
        "Merupakan dokumen sejarah kemerdekaan yang tidak dapat diubah tata letak hurufnya",
        "Diterapkan secara eksklusif bagi warga negara yang menduduki jabatan politik",
        "B",
        "TAP MPR No. III/MPR/2000 & Teori Falsafah Kenegaraan",
        "Sebagai pandangan hidup (way of life), Pancasila adalah kristalisasi nilai-nilai luhur yang dijadikan petunjuk, pedoman hidup, dan pegangan moral seluruh rakyat Indonesia."
    ),
    make_std(
        "twk_new_6", "Nasional", "TWK", "Bela Negara - Rela Berkorban (UU 23/2019)",
        "Seorang aparatur sipil negara bersedia ditugaskan di pos pelayanan perbatasan pulau terluar dengan fasilitas terbatas demi memastikan masyarakat perbatasan terlayani dan kedaulatan NKRI terjaga. Tindakan ASN tersebut merupakan cerminan nilai dasar bela negara, yaitu...",
        "Cinta tanah air",
        "Sadar berbangsa dan bernegara",
        "Setia pada Pancasila sebagai ideologi negara",
        "Rela berkorban untuk bangsa dan negara",
        "Kemampuan awal bela negara secara psikis",
        "D",
        "UU No. 23 Tahun 2019 tentang Pengelolaan Sumber Daya Nasional untuk Pertahanan Negara Pasal 7 Ayat (3)",
        "Rela berkorban untuk bangsa dan negara dibuktikan dengan kesediaan mengorbankan waktu, tenaga, dan pikiran untuk kemajuan bangsa serta siap membela negara dari berbagai ancaman."
    ),
    make_std(
        "twk_new_7", "Nasional", "TWK", "Integritas - Delik Pemerasan Pegawai Negeri",
        "Seorang pejabat pengadaan di instansi pemerintah menolak menandatangani berkas pencairan termin rekanan dan mengancam akan membatalkan kontrak proyek secara sepihak jika rekanan tidak menyetor sejumlah uang tunai pribadi ke pejabat tersebut. Tindak pidana korupsi ini memenuhi unsur...",
        "Gratifikasi yang tidak dilaporkan",
        "Pemerasan dalam jabatan (Pasal 12 huruf e UU Tipikor)",
        "Kerugian keuangan negara murni tanpa niat jahat",
        "Pemberian hadiah wajar adat ketimuran",
        "Kelalaian administrasi bendahara pengeluaran",
        "B",
        "UU No. 31 Tahun 1999 jo UU No. 20 Tahun 2001 Pasal 12 huruf e",
        "Pemerasan terjadi ketika pegawai negeri atau penyelenggara negara dengan maksud menguntungkan diri sendiri secara melawan hukum memaksa seseorang memberikan sesuatu dengan menyalahgunakan kekuasaannya."
    ),
    make_std(
        "twk_new_8", "Nasional", "TWK", "Bahasa Indonesia - Tata Tulis Gelar dan PUEBI",
        "Berdasarkan kaidah Ejaan Bahasa Indonesia yang Disempurnakan (EYD Edisi V), manakah penulisan nama, gelar akademik, dan tanda baca yang paling tepat?",
        "Prof. Dr. Ir. H. Ahmad Fauzi, M.Sc.",
        "Prof, Dr, Ir, H, Ahmad Fauzi M.Sc",
        "Prof. Dr. Ir. H. Ahmad Fauzi. M,Sc.",
        "Prof Dr Ir H Ahmad Fauzi, MSc",
        "Prof. DR. IR. H. Ahmad Fauzi, M.SC.",
        "A",
        "Pedoman Umum Ejaan Bahasa Indonesia (EYD Edisi V) Bagian Penulisan Gelar",
        "Setiap singkatan gelar akademik, gelar kehormatan, atau jabatan diakhiri tanda titik, dan antara nama dengan gelar belakang dipisahkan oleh tanda koma."
    ),
    make_std(
        "twk_new_9", "Nasional", "TWK", "Sejarah Perjuangan - Konferensi Meja Bundar 1949",
        "Konferensi Meja Bundar (KMB) yang berlangsung di Den Haag pada 23 Agustus sampai 2 November 1949 menghasilkan keputusan penting bagi kedaulatan Indonesia, di antaranya...",
        "Belanda menyerahkan seluruh wilayah Hindia Belanda termasuk Irian Barat saat itu juga",
        "Kerajaan Belanda mengakui kedaulatan penuh Republik Indonesia Serikat (RIS) tanpa syarat dan masalah Irian Barat akan diselesaikan dalam waktu satu tahun kemudian",
        "Indonesia wajib tetap menjadi koloni di bawah Ratu Belanda",
        "Pembentukan Republik Indonesia Serikat dengan wilayah hanya mencakup Jawa dan Madura",
        "Penolakan pengakuan kemerdekaan Indonesia oleh Perserikatan Bangsa-Bangsa",
        "B",
        "Hasil Perjanjian Konferensi Meja Bundar (KMB) 1949",
        "KMB menghasilkan penyerahan kedaulatan kepada RIS pada 27 Desember 1949, dengan klausul penundaan penyelesaian status Irian Barat setahun kemudian."
    )
]

# ==============================================================================
# 3. TAMBAHKAN 9 TIU BARU (Total TIU = 50 unik)
# ==============================================================================
extra_tiu = [
    make_std(
        "tiu_new_1", "Nasional", "TIU", "Silogisme Hipotetis / Modus Tollens",
        "Jika server database pusat mengalami pemadaman listrik total, maka seluruh aplikasi pelayanan publik daerah tidak dapat diakses masyarakat. Hari ini warga dapat mengakses seluruh aplikasi pelayanan publik daerah dengan lancar. Simpulan yang sah adalah...",
        "Server database pusat sedang dalam masa perbaikan berkala.",
        "Server database pusat tidak mengalami pemadaman listrik total.",
        "Aplikasi pelayanan publik sedang diakses melalui server cadangan ilegal.",
        "Sebagian server database pusat mengalami pemadaman listrik.",
        "Tidak ada hubungan antara server database dengan akses pelayanan publik.",
        "B",
        "Logika Matematika Silogisme Modus Tollens (p -> q, ~q, maka ~p)",
        "Premis 1: Jika p (padam total) maka q (tidak dapat diakses). Premis 2: ~q (dapat diakses lancar). Simpulan: ~p (server pusat tidak mengalami pemadaman listrik total)."
    ),
    make_std(
        "tiu_new_2", "Nasional", "TIU", "Deret Bilangan Fibonacci",
        "Tentukan angka berikutnya dari barisan pola bilangan berikut: 2, 3, 5, 8, 13, 21, 34, ...",
        "45", "48", "52", "55", "58",
        "D",
        "Pola Barisan Fibonacci (Un = Un-1 + Un-2)",
        "Setiap suku merupakan penjumlahan dari dua suku sebelumnya: 2+3=5, 3+5=8, 5+8=13, 8+13=21, 13+21=34, maka 21+34 = 55."
    ),
    make_std(
        "tiu_new_3", "Nasional", "TIU", "Deret Huruf Berpola Selang",
        "Tentukan huruf berikutnya dari deret huruf alfabet berikut: B, E, D, G, F, I, H, ...",
        "J", "K", "L", "M", "N",
        "B",
        "Pola Deret Huruf Selang-Seling (+3, -1)",
        "Urutan angka huruf: B(2), E(5), D(4), G(7), F(6), I(9), H(8). Pola selisih: +3, -1, +3, -1, +3, -1, maka langkah selanjutnya adalah +3. 8 + 3 = 11 (huruf K)."
    ),
    make_std(
        "tiu_new_4", "Nasional", "TIU", "Aritmatika Sosial - Modal dan Laba",
        "Sebuah unit perangkat server dibeli oleh kantor dengan harga Rp12.000.000. Untuk biaya instalasi dan upgrade RAM dikeluarkan biaya tambahan sebesar Rp3.000.000. Jika server tersebut dijual kembali dengan mengharapkan keuntungan sebesar 20% dari total pengeluaran, berapakah harga jual server tersebut?",
        "Rp16.500.000", "Rp17.000.000", "Rp17.500.000", "Rp18.000.000", "Rp18.500.000",
        "D",
        "Aritmatika Finansial Keuntungan (Harga Jual = Modal + Laba)",
        "Total modal = Rp12.000.000 + Rp3.000.000 = Rp15.000.000. Keuntungan 20% = 20% x Rp15.000.000 = Rp3.000.000. Harga jual = Rp15.000.000 + Rp3.000.000 = Rp18.000.000."
    ),
    make_std(
        "tiu_new_5", "Nasional", "TIU", "Perbandingan Senilai",
        "Sebuah mobil operasional dinas memerlukan 15 liter bensin untuk menempuh perjalanan sejauh 180 km. Berapakah liter bensin yang dibutuhkan mobil dinas tersebut untuk menempuh perjalanan dinas sejauh 300 km dengan kondisi jalan yang sama?",
        "20 liter", "22 liter", "25 liter", "28 liter", "30 liter",
        "C",
        "Aljabar Perbandingan Senilai (x1/y1 = x2/y2)",
        "Bensin = (300 km / 180 km) x 15 liter = (5/3) x 15 = 25 liter."
    ),
    make_std(
        "tiu_new_6", "Nasional", "TIU", "Kecepatan - Waktu Menyusul",
        "Bus rombongan dinas A berangkat dari kota X menuju kota Y pada pukul 07.00 dengan kecepatan rata-rata 40 km/jam. Pada pukul 08.00, mobil dinas B berangkat dari tempat dan rute yang sama dengan kecepatan rata-rata 60 km/jam. Pada pukul berapakah mobil dinas B berhasil menyusul bus A?",
        "Pukul 09.30", "Pukul 10.00", "Pukul 10.30", "Pukul 11.00", "Pukul 11.30",
        "B",
        "Kinematika Gerak Lurus (Waktu Menyusul: t = Selisih Jarak / Selisih Kecepatan)",
        "Pada pukul 08.00, bus A sudah berjalan 1 jam sejauh 40 km. Selisih kecepatan B dan A = 60 - 40 = 20 km/jam. Waktu menyusul = 40 km / 20 km/jam = 2 jam setelah mobil B berangkat. 08.00 + 2 jam = pukul 10.00."
    ),
    make_std(
        "tiu_new_7", "Nasional", "TIU", "Peluang Kombinatorika",
        "Di dalam sebuah lemari arsip dinas terdapat 5 map berkas berwarna merah dan 3 map berkas berwarna biru. Jika seorang petugas mengambil 2 map secara acak sekaligus, berapakah peluang terambilnya kedua map tersebut berwarna merah?",
        "5/28", "5/14", "10/21", "15/56", "1/2",
        "B",
        "Teori Peluang dan Kombinasi (C(n,r))",
        "Total cara mengambil 2 dari 8 map = C(8,2) = (8x7)/(2x1) = 28. Cara mengambil 2 map merah dari 5 map merah = C(5,2) = (5x4)/(2x1) = 10. Peluang = 10/28 = 5/14."
    ),
    make_std(
        "tiu_new_8", "Nasional", "TIU", "Penalaran Posisi Linier / Ranking",
        "Lima orang peserta tes seleksi (P, Q, R, S, T) memperoleh skor SKD berbeda: Nilai P lebih tinggi dari nilai Q. Nilai R lebih tinggi dari nilai P. Nilai S lebih rendah dari nilai Q. Nilai T adalah yang paling tinggi melebihi nilai R. Siapakah peserta yang memperoleh nilai tertinggi kedua?",
        "Peserta P", "Peserta Q", "Peserta R", "Peserta S", "Peserta T",
        "C",
        "Penalaran Logis Analitis Pengurutan Peringkat",
        "Dari petunjuk: T > R > P > Q > S. Nilai tertinggi pertama adalah T, dan nilai tertinggi kedua adalah R."
    ),
    make_std(
        "tiu_new_9", "Nasional", "TIU", "Analogi Kata Verbal",
        "ARSIP : DOKUMEN = GUDANG : ...",
        "Uang", "Barang", "Karyawan", "Toko", "Pintu",
        "B",
        "Hubungan Analogi Semantik Tempat Penyimpanan Objek",
        "Arsip adalah tempat untuk menyimpan dokumen, sebagaimana gudang adalah tempat untuk menyimpan barang."
    )
]

# ==============================================================================
# 4. TAMBAHKAN 11 TKP BARU (Total TKP = 60 unik)
# ==============================================================================
extra_tkp = [
    make_tkp(
        "tkp_new_1", "Pelayanan Publik - Transparansi Biaya",
        "Seorang warga datang ke loket Anda untuk melegalisir berkas kependudukan. Sesuai aturan resmi layanan tersebut gratis, namun warga tersebut menyodorkan uang tip dan berkata 'Tolong cepatkan mas, ini uang lelahnya'. Tindakan Anda...",
        "Menerima uang tersebut karena warga memberikannya secara sukarela tanpa diminta.",
        "Menolak uang tersebut secara ramah dan sopan, menjelaskan bahwa seluruh proses legalisir berkas tidak dipungut biaya apa pun, dan tetap memproses dokumen secepat mungkin.",
        "Marah dan membentak warga tersebut di depan umum karena telah mencoba menyuap aparatur.",
        "Menerima uang tersebut lalu memasukkannya ke kas sosial kantor.",
        "Menolak melayani warga tersebut selamanya karena tersinggung.",
        {"B": 5, "D": 3, "A": 2, "C": 2, "E": 1},
        "UU No. 25/2009 tentang Pelayanan Publik & SE MenPAN-RB No. 20/2021",
        "Opsi B (skor 5) menegakkan integritas aparatur sipil negara dengan menolak gratifikasi secara santun, mengedukasi masyarakat bahwa layanan gratis, dan tetap memberikan pelayanan terbaik."
    ),
    make_tkp(
        "tkp_new_2", "Jejaring Kerja - Pembagian Tugas Tim",
        "Dalam sebuah tim kerja penyusunan evaluasi kinerja, salah satu anggota tim sering mengeluh bahwa beban tugasnya terlalu berat dibanding rekan lain. Sebagai ketua tim kerja, sikap Anda adalah...",
        "Mengabaikan keluhannya karena pembagian tugas sudah final dan tidak boleh diganggu gugat.",
        "Mengajak seluruh anggota tim berdiskusi secara terbuka untuk mereview kembali matriks beban kerja, mendengar kendala masing-masing, dan melakukan penyesuaian porsi kerja secara adil dan proporsional.",
        "Memarahi anggota tersebut karena dianggap tidak memiliki loyalitas kerja.",
        "Mengambil alih seluruh pekerjaan anggota tersebut dan mengerjakannya seorang diri.",
        "Mengeluarkan anggota yang mengeluh tersebut dari grup proyek.",
        {"B": 5, "D": 3, "A": 2, "C": 1, "E": 1},
        "Manajemen Kerja Tim ASN & Core Values Kolaboratif",
        "Opsi B (skor 5) mencerminkan kepemimpinan demokratis yang mendengarkan aspirasi bawahan, transparan, dan mampu mengelola dinamika tim secara konstruktif."
    ),
    make_tkp(
        "tkp_new_3", "Sosial Budaya - Penempatan di Daerah Baru",
        "Anda mendapat surat keputusan mutasi dinas ke daerah pedalaman di luar pulau asal Anda yang memiliki norma adat, budaya, dan bahasa daerah yang sangat berbeda. Sikap awal yang Anda lakukan saat tiba di daerah tersebut adalah...",
        "Menghabiskan waktu hanya di rumah dinas dan bergaul dengan rekan yang berasal dari satu suku saja.",
        "Berinisiatif bersilaturahmi dengan tokoh masyarakat setempat, menghormati norma adat yang berlaku, dan aktif mempelajari budaya serta kebiasaan lokal.",
        "Menuntut masyarakat setempat menyesuaikan diri dengan kebiasaan dan cara hidup Anda dari kota besar.",
        "Mengajukan surat permohonan pembatalan mutasi secepat mungkin kepada bupati.",
        "Menolak berbicara dengan warga lokal sebelum Anda menguasai bahasa daerah mereka secara fasih.",
        {"B": 5, "A": 3, "C": 2, "D": 1, "E": 1},
        "Standar Kompetensi Sosial Kultural ASN (PermenPAN-RB No. 38/2017)",
        "Opsi B (skor 5) menunjukkan keterbukaan, kemampuan beradaptasi sosial, dan penghargaan tulus terhadap keragaman budaya bangsa."
    ),
    make_tkp(
        "tkp_new_4", "TIK - Penolakan Sistem Baru oleh Senior",
        "Kantor Anda mengimplementasikan sistem persuratan digital berbasis web baru. Beberapa pegawai senior mengeluh dan enggan menggunakannya karena terbiasa mengetik manual dan meminta Anda tetap menerima disposisi kertas. Sikap Anda...",
        "Membiarkan para pegawai senior tetap memakai cara lama selamanya tanpa pembinaan.",
        "Dengan sabar dan ramah menawarkan diri meluangkan waktu mendampingi para pegawai senior langkah demi langkah cara mengoperasikan sistem baru hingga mereka mahir.",
        "Melaporkan pegawai senior ke kepala dinas agar tunjangannya dipotong.",
        "Menolak menerima berkas mereka secara kasar dan menyuruh mereka pensiun dini.",
        "Mengerjakan seluruh input surat milik pegawai senior tanpa mengajari mereka.",
        {"B": 5, "E": 3, "A": 2, "C": 2, "E": 1},
        "Transformasi Digital ASN & Core Values Harmonis",
        "Opsi B (skor 5) menjembatani kesenjangan digital (digital divide) antargenerasi di birokrasi dengan pendekatan persuasif, edukatif, dan penuh rasa hormat."
    ),
    make_tkp(
        "tkp_new_5", "Profesionalisme - Target Laporan Akhir Tahun",
        "Hari Jumat sore menjelang libur panjang akhir tahun, pimpinan menginstruksikan bahwa ada laporan realisasi fisik dan keuangan yang harus diselesaikan dan dikirim ke pusat malam ini juga. Rencana liburan Anda bersama teman sudah terjadwal. Sikap Anda...",
        "Mengabaikan instruksi pimpinan dan langsung mematikan ponsel agar tidak bisa dihubungi.",
        "Menunda keberangkatan liburan sejenak, fokus menyelesaikan laporan tersebut bersama tim kerja hingga tuntas, dan baru berangkat berlibur setelah tugas selesai.",
        "Mengerjakan laporan secara asal-asalan tanpa dicek agar bisa pulang tepat waktu.",
        "Menyerahkan seluruh tugas laporan kepada staf honorer dan Anda langsung pergi.",
        "Meminta pimpinan menunda pengiriman laporan hingga libur tahun baru usai.",
        {"B": 5, "E": 3, "D": 2, "C": 2, "E": 1},
        "Nilai Dasar Loyal & Akuntabel ASN",
        "Opsi B (skor 5) mendahulukan komitmen kedinasan dan akuntabilitas pekerjaan di atas kepentingan pribadi saat terjadi situasi darurat/deadline penting."
    ),
    make_tkp(
        "tkp_new_6", "Anti-Radikalisme - Hoaks & Ekstremisme di Medsos",
        "Di grup WhatsApp lingkungan kerja Anda, seorang anggota menyebarkan konten provokatif yang menjelek-jelekkan salah satu simbol agama dan mengajak untuk memboikot pelayanan kepada pemeluk agama tersebut. Sikap Anda...",
        "Ikut menyebarkan pesan tersebut ke grup media sosial lain agar semakin viral.",
        "Mengingatkan pengirim pesan dengan sopan dan tegas bahwa konten tersebut mengandung SARA dan melanggar kode etik ASN, serta mengajak anggota grup menjaga netralitas dan kerukunan.",
        "Keluar dari grup tanpa berkata apa-apa.",
        "Mendiamkan saja karena merasa bukan urusan pribadi Anda.",
        "Membalas pesan tersebut dengan caci maki dan kata-kata kasar.",
        {"B": 5, "D": 3, "C": 2, "E": 2, "A": 1},
        "Pencegahan Radikalisme dan Polarisasi SARA ASN",
        "Opsi B (skor 5) menunjukkan keberanian moral menegakkan nilai netralitas ASN dan mencegah disintegrasi bangsa di lingkungan digital."
    ),
    make_tkp(
        "tkp_new_7", "Pelayanan Publik - Warga Disabilitas",
        "Seorang warga tunarungu datang ke meja loket Anda untuk menanyakan prosedur pembuatan akta kelahiran, namun petugas sebelumnya tampak bingung dan kurang sabar berkomunikasi. Sikap Anda...",
        "Menghampiri warga tersebut dengan ramah, mempersilakannya duduk, dan menggunakan media tulisan di kertas atau ponsel serta bahasa isyarat sederhana untuk menjelaskan alur persyaratan secara runtut.",
        "Meminta warga tersebut membawa juru bicara bahasa isyarat profesional sebelum datang ke kantor.",
        "Mengabaikan warga tersebut karena Anda juga tidak bisa bahasa isyarat resmi.",
        "Menyuruh satpam mengantar warga tersebut ke luar ruangan kantor.",
        "Memberikan tumpukan formulir kosong tanpa memberikan penjelasan apa pun.",
        {"A": 5, "B": 3, "E": 2, "C": 2, "D": 1},
        "Inklusivitas Pelayanan Publik ASN Ramah Disabilitas",
        "Opsi A (skor 5) mewujudkan pelayanan publik berkeadilan sosial tanpa diskriminasi, proaktif berempati dan mencari solusi komunikasi praktis bagi penyandang disabilitas."
    ),
    make_tkp(
        "tkp_new_8", "Jejaring Kerja - Kolaborasi Antar-Bidang",
        "Bidang Anda dan Bidang Teknis lain sedang merancang agenda pameran inovasi daerah. Pimpinan kedua bidang memiliki pandangan berbeda mengenai konsep stan pameran sehingga rapat mandek. Sebagai perwakilan staf, sikap Anda...",
        "Memihak pimpinan bidang Anda secara buta dan menyerang gagasan bidang lain.",
        "Mengusulkan titik temu (kompromi kreatif) yang menggabungkan keunggulan ide dari kedua bidang dalam satu konsep terpadu yang saling melengkapi.",
        "Meninggalkan ruang rapat karena suasana sudah tidak kondusif.",
        "Membatalkan keikutsertaan instansi dalam pameran tersebut.",
        "Membiarkan kedua pimpinan berdebat tanpa ada yang menengahi.",
        {"B": 5, "E": 3, "A": 2, "C": 2, "D": 1},
        "Kemampuan Negosiasi & Resolusi Konflik Kerja ASN",
        "Opsi B (skor 5) menunjukkan kapasitas pemecahan masalah (problem solving) yang konstruktif dan berorientasi pada hasil bersama."
    ),
    make_tkp(
        "tkp_new_9", "Sosial Budaya - Ibadah Rekan Kerja",
        "Saat jadwal lembur tim menjelang malam hari, rekan kerja Anda yang beragama minoritas meminta izin untuk beribadah di ruangan khusus selama 15 menit. Sikap Anda sebagai koordinator tim...",
        "Melarangnya beribadah karena proyek lembur harus selesai secepatnya.",
        "Mempersilakannya beribadah dengan nyaman dan menjaga ruangan tetap kondusif, serta mengatur jeda istirahat anggota tim lainnya secara adil.",
        "Mengurangi bagian honor lemburnya karena ia meninggalkan pekerjaan.",
        "Menyuruhnya beribadah nanti saja setelah seluruh pekerjaan selesai tengah malam.",
        "Mencibir rekan kerja tersebut karena dianggap terlalu merepotkan.",
        {"B": 5, "D": 3, "A": 2, "C": 1, "E": 1},
        "Moderasi Beragama & Toleransi Tempat Kerja ASN",
        "Opsi B (skor 5) menjunjung tinggi hak asasi kebebasan beragama dan menjaga iklim kerja yang toleran, saling menghargai, dan harmonis."
    ),
    make_tkp(
        "tkp_new_10", "TIK - Keamanan Siber & Phishing",
        "Anda menerima email dinas yang tampak seperti berasal dari BKN, meminta verifikasi data NIP dan password akun kepegawaian dengan mengklik tautan eksternal yang mencurigakan. Tindakan Anda adalah...",
        "Segera mengklik tautan dan memasukkan username serta password Anda.",
        "Tidak mengklik tautan tersebut, memverifikasi keabsahan pengirim ke bagian pengelola TIK instansi/CSIRT, dan melaporkannya sebagai potensi insiden phishing.",
        "Meneruskan email mencurigakan tersebut ke seluruh rekan kerja agar mereka penasaran.",
        "Menghapus email tersebut tanpa mengabari pihak pengelola IT kantor.",
        "Membalas email tersebut dengan data pribadi palsu sebagai bahan lelucon.",
        {"B": 5, "D": 3, "C": 2, "E": 2, "A": 1},
        "Kesadaran Keamanan Informasi (Cyber Security Awareness)",
        "Opsi B (skor 5) mencerminkan literasi keamanan data yang matang, mencegah pencurian kredensial akun negara, dan mengaktifkan prosedur penanganan insiden siber."
    ),
    make_tkp(
        "tkp_new_11", "Profesionalisme - Penolakan Titipan Berkas",
        "Seorang kerabat dekat keluarga Anda datang ke kantor meminta tolong agar berkas permohonan izin usahanya diloloskan meskipun ada dokumen syarat teknis yang belum lengkap. Sikap Anda...",
        "Membantu meloloskannya karena merasa tidak enak dengan hubungan keluarga.",
        "Menjelaskan secara santun dan profesional bahwa seluruh berkas wajib lengkap sesuai SOP perizinan, serta membimbingnya dokumen apa saja yang harus dilengkapi terlebih dahulu agar permohonan dapat diproses resmi.",
        "Menerima berkasnya tetapi membuangnya ke tempat sampah secara diam-diam.",
        "Meminta uang pelicin kepada kerabat tersebut untuk menutupi kekurangan berkas.",
        "Memarahi kerabat tersebut dan memutuskan tali persaudaraan.",
        {"B": 5, "A": 2, "C": 2, "D": 1, "E": 1},
        "Integritas & Anti-Nepotisme ASN (UU No. 28/1999 & Core Values BerAKHLAK)",
        "Opsi B (skor 5) menjaga independensi dan integritas tugas kedinasan tanpa kompromi nepotisme, namun tetap bersikap santun dan solutif."
    )
]

# GABUNGKAN KE DATA SKD
skd_clean = data["skd"]["questions"]
twk_clean = [q for q in skd_clean if q["category"] == "TWK"] + extra_twk
tiu_clean = [q for q in skd_clean if q["category"] == "TIU"] + extra_tiu
tkp_clean = [q for q in skd_clean if q["category"] == "TKP"] + extra_tkp

# Cek keunikan internal SKD
def dedupe_list(q_list):
    seen = set()
    res = []
    for q in q_list:
        t = q["question"].strip().lower()
        if t not in seen:
            seen.add(t)
            res.append(q)
    return res

twk_clean = dedupe_list(twk_clean)
tiu_clean = dedupe_list(tiu_clean)
tkp_clean = dedupe_list(tkp_clean)

print(f"\nHASIL SKD BARU: TWK {len(twk_clean)}, TIU {len(tiu_clean)}, TKP {len(tkp_clean)} (Total {len(twk_clean)+len(tiu_clean)+len(tkp_clean)} Soal 100% UNIK)")

data["skd"]["questions"] = twk_clean + tiu_clean + tkp_clean
data["skd"]["title"] = "Simulasi Resmi CAT BKN - SKD (160 Bank Soal 100% Unik & Autentik)"

# Update judul paket SKB
for ikey in ["skb_kemkomdigi", "skb_kemenkeu", "skb_bssn", "skb_bkn", "skb_kemenkumham", "skb_pemda"]:
    data[ikey]["questions"] = dedupe_list(data[ikey]["questions"])
    inst_name = data[ikey]["questions"][0]["instansi"]
    data[ikey]["title"] = f"SKB IT - {inst_name} ({len(data[ikey]['questions'])} Soal 100% Unik)"
    print(f"Paket {ikey}: {len(data[ikey]['questions'])} soal 100% unik!")

# SIMPAN FILE
output_content = prefix + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"

with open("d:\\CPNS\\data_soal.js", "w", encoding="utf-8") as f:
    f.write(output_content)

print("\n=======================================================")
print("DEDUPLIKASI BERHASIL! SEMUA PAKET BEBAS DUPLIKAT (DUPLICATES = 0)!")
print("=======================================================")
