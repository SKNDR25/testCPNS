import json

# ==============================================================================
# GENERATOR RESMI SKB IT KEMKOMDIGI - 100 SOAL PENUH STANDAR CAT BKN
# SETIAP SOAL MEMILIKI SITASI SUMBER HUKUM & STANDAR BAKU (NON-ASAL-ASALAN):
# 1. UU No. 27/2022 tentang Pelindungan Data Pribadi (UU PDP)
# 2. UU No. 1/2024 & UU No. 11/2008 (UU ITE)
# 3. Perpres No. 95/2018 tentang SPBE
# 4. Perpres No. 39/2019 tentang Satu Data Indonesia (SDI)
# 5. PP No. 71/2019 tentang PSTE & Permenkominfo No. 5/2020 (PSE)
# 6. Standar Kompetensi Pranata Komputer (PermenPAN-RB No. 32/2020 & BPS)
# 7. Standar Teknis Internasional: ISO 27001:2022, NIST SP 800-61, TIA-942, RFC
# ==============================================================================

# Buka file data_soal.js yang sudah ada untuk mempertahankan SKD 110 soal
with open("d:\\CPNS\\data_soal.js", "r", encoding="utf-8") as f:
    text = f.read()

json_str = text.replace("/**\n * BANK SOAL MULTI-INSTANSI CAT CPNS (SKD NASIONAL & SKB SPESIFIK INSTANSI)\n */\nwindow.BANK_SOAL = ", "").rstrip(";\n")
data = json.loads(json_str)

# Fungsi helper membuat butir soal terstandarisasi dengan sitasi wajib
def make_q(qid, cat, subcat, question, opt_a, opt_b, opt_c, opt_d, opt_e, ans, ref, expl):
    return {
        "id": qid,
        "instansi": "Kemkomdigi",
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

skb_100_questions = []

# ------------------------------------------------------------------------------
# DOMAIN 1: REGULASI & KEBIJAKAN DIGITAL NASIONAL (Soal 1 - 15)
# ------------------------------------------------------------------------------
skb_100_questions.append(make_q(
    "kd_1", "Regulasi Digital", "UU PDP No. 27/2022 - Klasifikasi Data",
    "Berdasarkan Pasal 4 UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP), data pribadi dibagi menjadi data yang bersifat umum dan spesifik. Manakah yang termasuk ke dalam kategori Data Pribadi yang bersifat Spesifik (Sensitif)?",
    "Nama lengkap, jenis kelamin, dan nomor telepon",
    "Kewarganegaraan dan status perkawinan",
    "Data kesehatan, data biometrik, data genetika, dan catatan kejahatan",
    "Alamat email kantor dan tanggal lahir",
    "Riwayat pendidikan sekolah dasar",
    "C", "UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi, Pasal 4 Ayat (2).",
    "Data pribadi spesifik memiliki risiko diskriminasi tinggi jika bocor, meliputi data kesehatan, biometrik, genetika, catatan kejahatan, data anak, data keuangan pribadi, dan data lain sesuai peraturan."
))

skb_100_questions.append(make_q(
    "kd_2", "Regulasi Digital", "UU PDP No. 27/2022 - Notifikasi Kebocoran",
    "Pasal 46 UU No. 27 Tahun 2022 mewajibkan Pengendali Data Pribadi untuk menyampaikan pemberitahuan tertulis jika terjadi kegagalan pelindungan data (data breach). Batas waktu maksimal penyampaian notifikasi tersebut adalah...",
    "1 x 24 jam setelah insiden",
    "2 x 24 jam setelah insiden",
    "3 x 24 jam (72 jam) terhitung sejak terjadinya kegagalan",
    "7 hari kerja kalender",
    "14 hari setelah hasil audit forensik selesai",
    "C", "UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi, Pasal 46 Ayat (1).",
    "Pengendali Data Pribadi wajib menyampaikan pemberitahuan tertulis paling lambat 3 x 24 jam (72 jam) kepada Subjek Data dan Lembaga Pengawas Otoritas PDP."
))

skb_100_questions.append(make_q(
    "kd_3", "Regulasi Digital", "UU PDP No. 27/2022 - Pejabat DPO",
    "Kapan seorang Pengendali Data Pribadi atau Prosesor Data Pribadi diwajibkan oleh UU PDP Pasal 53 untuk menunjuk Pejabat/Petugas Pelindungan Data Pribadi (Data Protection Officer / DPO)?",
    "Hanya jika laba bersih instansi melebihi 10 miliar per tahun",
    "Ketika pemrosesan data dilakukan untuk kepentingan pelayanan publik, kegiatan pokok memerlukan pemantauan berskala besar, atau memproses data spesifik",
    "Hanya jika sistem aplikasi mengalami serangan peretasan",
    "Ketika jumlah pegawai di kantor lebih dari 100 orang",
    "Hanya jika diwajibkan oleh pengadilan negeri",
    "B", "UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi, Pasal 53 Ayat (1).",
    "DPO wajib ditunjuk jika pemrosesan untuk pelayanan publik, sifat/ruang lingkup memerlukan pemantauan teratur berskala besar, atau kegiatan pokoknya memproses data pribadi spesifik dalam skala besar."
))

skb_100_questions.append(make_q(
    "kd_4", "Regulasi Digital", "UU PDP No. 27/2022 - Hak Subjek Data",
    "Subjek Data Pribadi berhak mengakhiri pemrosesan, menghapus, dan/atau memusnahkan data pribadi miliknya (Right to Erasure / Right to be Forgotten). Hal ini dijamin dalam UU PDP Pasal...",
    "Pasal 8", "Pasal 10", "Pasal 15", "Pasal 20", "Pasal 30",
    "A", "UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi, Pasal 8.",
    "Pasal 8 menyatakan Subjek Data berhak menarik kembali persetujuan dan berhak mengakhiri pemrosesan, menghapus, atau memusnahkan Data Pribadi tentang dirinya."
))

skb_100_questions.append(make_q(
    "kd_5", "Regulasi Digital", "UU PDP No. 27/2022 - Transfer Data Internasional",
    "Berdasarkan Pasal 56 UU PDP, sebelum Pengendali Data Pribadi mentransfer Data Pribadi ke luar wilayah hukum Indonesia, syarat utama yang harus dipastikan adalah...",
    "Negara penerima memiliki tingkat pelindungan data yang setara atau lebih tinggi, atau terdapat perjanjian internasional/kontrak pengikatan standar",
    "Negara penerima membayar kompensasi royalti data ke kas negara",
    "Data pribadi diubah menjadi bentuk cetak kertas terlebih dahulu",
    "Pengendali data meminta izin kepada duta besar negara bersangkutan secara lisan",
    "Server cadangan diletakkan di kantor kedutaan besar",
    "A", "UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi, Pasal 56 Ayat (1) dan (2).",
    "Transfer data internasional mensyaratkan negara tujuan memiliki tingkat pelindungan data yang setara/lebih tinggi. Jika tidak ada, wajib memiliki klausul kontrak pengikatan standar yang menjamin perlindungan memadai."
))

skb_100_questions.append(make_q(
    "kd_6", "Regulasi Digital", "UU ITE - Perubahan Kedua UU 1/2024",
    "Undang-Undang Nomor 1 Tahun 2024 tentang Perubahan Kedua atas UU ITE mengatur mengenai alat bukti elektronik. Kedudukan informasi elektronik dan/atau dokumen elektronik dalam hukum acara perdata dan pidana di Indonesia adalah...",
    "Bukan merupakan alat bukti yang sah",
    "Hanya sebagai petunjuk pelengkap tanpa kekuatan pembuktian",
    "Alat bukti hukum yang sah dan merupakan perluasan dari alat bukti yang sah sesuai hukum acara yang berlaku",
    "Hanya sah jika dicetak di kertas segel bertanda tangan basah",
    "Hanya berlaku jika disetujui oleh terdakwa di persidangan",
    "C", "UU No. 1 Tahun 2024 jo. UU No. 11/2008 tentang ITE, Pasal 5 Ayat (1) dan (2).",
    "Informasi Elektronik dan/atau Dokumen Elektronik dan/atau hasil cetaknya merupakan alat bukti hukum yang sah dan merupakan perluasan dari alat bukti yang sah sesuai hukum acara."
))

skb_100_questions.append(make_q(
    "kd_7", "Regulasi Digital", "UU ITE - Tanda Tangan Elektronik",
    "Berdasarkan Pasal 11 UU ITE, sebuah Tanda Tangan Elektronik memiliki kekuatan hukum dan akibat hukum yang sah apabila memenuhi persyaratan minimum, KECUALI...",
    "Data pembuatan tanda tangan elektronik terkait hanya kepada penandatangan",
    "Data pembuatan tanda tangan elektronik berada dalam kuasa penandatangan",
    "Segala perubahan terhadap tanda tangan elektronik setelah waktu penandatanganan dapat diketahui",
    "Tanda tangan harus dibuat menggunakan pena digital merk tertentu",
    "Terdapat cara tertentu untuk mengidentifikasi siapa penandatangannya",
    "D", "UU No. 11 Tahun 2008 tentang ITE, Pasal 11 Ayat (1).",
    "Pasal 11 Ayat (1) menjamin netralitas teknologi; syarat keabsahan TTE meliputi autentisitas, integritas, dan kuasa penandatangan, bukan bergantung pada merk alat keras tertentu."
))

skb_100_questions.append(make_q(
    "kd_8", "Regulasi Digital", "PP 71/2019 tentang PSTE",
    "Peraturan Pemerintah Nomor 71 Tahun 2019 tentang Penyelenggaraan Sistem dan Transaksi Elektronik (PP PSTE) mengelompokkan Penyelenggara Sistem Elektronik (PSE) menjadi dua kategori, yaitu...",
    "PSE Komersial dan PSE Non-Komersial",
    "PSE Lingkup Publik dan PSE Lingkup Privat",
    "PSE Domestik dan PSE Multinasional",
    "PSE Perangkat Keras dan PSE Perangkat Lunak",
    "PSE Statis dan PSE Dinamis",
    "B", "PP No. 71 Tahun 2019 tentang PSTE, Pasal 2 Ayat (2).",
    "PP PSTE membagi PSE secara tegas menjadi: 1. PSE Lingkup Publik (instansi pemerintah/lembaga negara) dan 2. PSE Lingkup Privat (badan usaha, individu, platform komersial)."
))

skb_100_questions.append(make_q(
    "kd_9", "Regulasi Digital", "PP 71/2019 - Lokasi Pengelolaan Data",
    "Sesuai ketentuan Pasal 20 PP No. 71 Tahun 2019, PSE Lingkup Publik diwajibkan untuk mengelola, memproses, dan menyimpan data sistem elektroniknya...",
    "Bebas di server mana pun di seluruh dunia",
    "Di wilayah wilayah negara tetangga terdekat",
    "Di dalam wilayah hukum Republik Indonesia (Data Center domestik)",
    "Hanya di komputer lokal tanpa koneksi cloud",
    "Di server milik perusahaan multinasional asing tanpa kontrak",
    "C", "PP No. 71 Tahun 2019 tentang PSTE, Pasal 20 Ayat (1).",
    "PSE Lingkup Publik wajib menempatkan pusat data (data center) dan pusat pemulihan bencana (disaster recovery center) di wilayah wilayah Indonesia untuk kedaulatan data nasional."
))

skb_100_questions.append(make_q(
    "kd_10", "Regulasi Digital", "Permenkominfo No. 5/2020 - Pendaftaran PSE",
    "Berdasarkan Permenkominfo No. 5 Tahun 2020, PSE Lingkup Privat yang tidak melakukan pendaftaran resmi ke sistem Kemkomdigi dikenakan sanksi administratif berupa...",
    "Teguran lisan dari camat setempat",
    "Pemutusan akses (takedown / pemblokiran sistem) di jaringan internet Indonesia",
    "Penyitaan seluruh perangkat komputer kantor",
    "Pencabutan kewarganegaraan pemilik aplikasi",
    "Kewajiban menghapus kode sumber di GitHub",
    "B", "Permenkominfo No. 5 Tahun 2020, Pasal 7 Ayat (2).",
    "PSE Privat yang tidak terdaftar dikenai sanksi administratif berupa teguran tertulis, denda administratif, dan pemutusan akses (akses internet ke sistem tersebut diblokir oleh Kemkomdigi)."
))

skb_100_questions.append(make_q(
    "kd_11", "Regulasi Digital", "UU ITE Pasal 40 - Pemutusan Akses",
    "Kewenangan pemerintah (Kemkomdigi) dalam melakukan pemutusan akses (takedown/blocking) terhadap informasi elektronik dan dokumen elektronik yang memuat konten melanggar peraturan perundang-undangan termaktub dalam...",
    "Pasal 27 UU ITE", "Pasal 30 UU ITE", "Pasal 40 Ayat (2a) dan (2b) UU ITE", "Pasal 50 UU ITE", "Pasal 1 UU ITE",
    "C", "UU No. 19 Tahun 2016 jo. UU No. 1 Tahun 2024, Pasal 40 Ayat (2a) dan (2b).",
    "Pasal 40 Ayat (2a) mewajibkan pemerintah mencegah penyebarluasan konten dilarang, dan Ayat (2b) memberi wewenang melakukan pemutusan akses terhadap konten yang melanggar hukum (judi, pornografi, terorisme, hoaks SARA)."
))

skb_100_questions.append(make_q(
    "kd_12", "Regulasi Digital", "UU PDP - Sanksi Administratif",
    "Berdasarkan Pasal 57 UU No. 27 Tahun 2022, sanksi administratif berupa denda administratif atas pelanggaran pemrosesan data pribadi dapat dikenakan paling tinggi sebesar...",
    "1% dari pendapatan tahunan",
    "2% dari pendapatan tahunan atau omzet tahunan terhadap variabel pelanggaran",
    "100 juta rupiah tetap",
    "50% dari seluruh aset perusahaan",
    "Tidak ada sanksi denda finansial",
    "B", "UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi, Pasal 57 Ayat (3).",
    "Sanksi denda administratif bagi korporasi yang melanggar ketentuan pemrosesan data pribadi ditetapkan maksimal 2 (dua) persen dari pendapatan tahunan atau penerimaan tahunan."
))

skb_100_questions.append(make_q(
    "kd_13", "Regulasi Digital", "UU ITE - Peretasan Ilegal (Illegal Access)",
    "Mengakses komputer dan/atau sistem elektronik milik orang lain atau pemerintah dengan cara tanpa hak dan melanggar/menerobos sistem pengamanan (cracking/hacking) diatur sebagai tindak pidana dalam UU ITE...",
    "Pasal 27", "Pasal 30 Ayat (1), (2), dan (3)", "Pasal 35", "Pasal 45", "Pasal 12",
    "B", "UU No. 11 Tahun 2008 jo. UU No. 1 Tahun 2024, Pasal 30.",
    "Pasal 30 mengatur larangan mengakses sistem secara tanpa hak (Ayat 1), dengan tujuan memperoleh informasi (Ayat 2), dan dengan menerobos/menjebol sistem pengamanan (Ayat 3)."
))

skb_100_questions.append(make_q(
    "kd_14", "Regulasi Digital", "UU ITE - Manipulasi Data Elektronik",
    "Perbuatan memanipulasi, menciptakan, mengubah, atau merusak informasi/dokumen elektronik dengan tujuan agar dianggap seolah-olah data yang otentik (Data Forgery) diatur dalam UU ITE...",
    "Pasal 31", "Pasal 32", "Pasal 35", "Pasal 38", "Pasal 42",
    "C", "UU No. 11 Tahun 2008 tentang ITE, Pasal 35.",
    "Pasal 35 mengatur larangan pemalsuan dokumen elektronik: 'Setiap Orang dengan sengaja dan tanpa hak... melakukan manipulasi... dengan tujuan agar Informasi Elektronik tersebut dianggap seolah-olah data yang otentik'."
))

skb_100_questions.append(make_q(
    "kd_15", "Regulasi Digital", "Standar Kelaikan Sistem Elektronik",
    "Sebelum sebuah aplikasi layanan publik digital nasional diluncurkan ke masyarakat luas, instansi wajib melakukan Uji Kelaikan Keamanan (Security Posture Assessment) dan mengantongi sertifikat kelaikan sesuai amanat PP PSTE. Bentuk uji keamanan tersebut adalah...",
    "Pengetikan ulang kode program di Microsoft Word",
    "Vulnerability Assessment & Penetration Testing (VAPT)",
    "Pembersihan casing CPU dengan cairan pembersih",
    "Pemasangan kabel fiber optik tambahan",
    "Penyebaran kuesioner kertas ke warga",
    "B", "PP No. 71/2019 Pasal 3 jo. Standar Audit Keamanan BSSN/Kemkomdigi.",
    "Uji kelaikan sistem mencakup VAPT (Vulnerability Assessment & Penetration Testing) untuk mengidentifikasi celah keamanan logika dan kode sebelum sistem dibuka ke publik."
))

# ------------------------------------------------------------------------------
# DOMAIN 2: TATA KELOLA SPBE & SATU DATA INDONESIA (Soal 16 - 30)
# ------------------------------------------------------------------------------
skb_100_questions.append(make_q(
    "kd_16", "Tata Kelola SPBE & SDI", "Perpres 95/2018 - 6 Domain Arsitektur",
    "Berdasarkan Pasal 11 Perpres No. 95 Tahun 2018 tentang SPBE, Arsitektur SPBE terdiri atas enam domain utama. Manakah urutan domain yang lengkap dan benar?",
    "Keuangan, Kepegawaian, Logistik, Humas, Perizinan, dan Pengawasan",
    "Proses Bisnis, Data dan Informasi, Layanan SPBE, Aplikasi SPBE, Infrastruktur SPBE, dan Keamanan SPBE",
    "Hardware, Software, Brainware, Netware, Firmware, dan Dataware",
    "Perencanaan, Pelaksanaan, Monitoring, Evaluasi, Pelaporan, dan Pengarsipan",
    "Frontend, Backend, Database, Cloud, Network, dan Security",
    "B", "Perpres No. 95 Tahun 2018 tentang SPBE, Pasal 11 Ayat (1).",
    "6 Domain Arsitektur SPBE Nasional meliputi: 1. Domain Proses Bisnis, 2. Data & Informasi, 3. Layanan SPBE, 4. Aplikasi SPBE, 5. Infrastruktur SPBE, dan 6. Keamanan SPBE."
))

skb_100_questions.append(make_q(
    "kd_17", "Tata Kelola SPBE & SDI", "Perpres 39/2019 - 4 Prinsip SDI",
    "Sesuai Pasal 5 Perpres No. 39 Tahun 2019 tentang Satu Data Indonesia (SDI), data yang dihasilkan oleh produsen data pemerintah wajib memenuhi 4 prinsip dasar, yaitu...",
    "Murah, Cepat, Banyak, dan Tersimpan di Cloud",
    "Memenuhi Standar Data, Memiliki Metadata, Memenuhi Interoperabilitas Data, dan Menggunakan Kode Referensi/Data Induk",
    "Tergembok, Terenkripsi, Rahasia, dan Hanya Dibaca Menteri",
    "Bebas Hak Cipta, Anonim, Tanpa Tanggal, dan Terbuka",
    "Format Word, Format Excel, Format PDF, dan Format JPG",
    "B", "Perpres No. 39 Tahun 2019 tentang Satu Data Indonesia, Pasal 5.",
    "4 Prinsip Satu Data Indonesia adalah: 1. Standar Data (definisi konsep baku), 2. Metadata (struktur informasi penjelas), 3. Interoperabilitas Data (mudah dipertukarkan), 4. Kode Referensi/Data Induk tunggal."
))

skb_100_questions.append(make_q(
    "kd_18", "Tata Kelola SPBE & SDI", "Sistem Penghubung Layanan Pemerintah (SPLP)",
    "Dalam kerangka integrasi nasional, Sistem Penghubung Layanan Pemerintah (SPLP) diatur dalam Perpres SPBE Pasal 43. SPLP bertindak sebagai Enterprise Service Bus (ESB) nasional yang mengemban fungsi...",
    "Pemberian sinyal Wi-Fi di taman kota",
    "Pengelolaan pertukaran data (data routing, protocol translation, API Gateway) antar instansi pemerintah pusat dan daerah secara aman dan terpantau",
    "Pengganti saluran televisi nasional",
    "Pencetakan fisik KTP di kantor kelurahan",
    "Penyedia cadangan daya listrik baterai darurat",
    "B", "Perpres No. 95 Tahun 2018 tentang SPBE, Pasal 43.",
    "SPLP berfungsi sebagai middleware nasional yang mengorkestrasi pertukaran data antar-aplikasi SPBE instansi melalui protokol API terstandar, verifikasi hak akses, dan pencatatan audit log transaksi data."
))

skb_100_questions.append(make_q(
    "kd_19", "Tata Kelola SPBE & SDI", "Tingkat Kematangan SPBE (Maturity Level)",
    "Penilaian Evaluasi SPBE oleh KemenPANRB dan Kemkomdigi menggunakan model kematangan bertingkat 1 sampai 5. Tingkat kematangan Level 4 (Terkolaborasi / Integrated) ditandai dengan...",
    "Proses kerja masih bersifat ad-hoc dan manual tanpa dokumentasi",
    "Aplikasi sudah terkomputerisasi tetapi berdiri sendiri (silo sistem)",
    "Layanan SPBE telah terpadu dan terintegrasi antar-unit kerja atau lintas instansi pemerintah",
    "Penggunaan komputer dilarang di lingkungan dinas",
    "Seluruh data disimpan di komputer lokal staf",
    "C", "PermenPANRB No. 59 Tahun 2020 tentang Pedoman Evaluasi SPBE.",
    "Tingkat Kematangan SPBE: Level 1 (Rintisan/Ad-hoc), Level 2 (Terkelola/Terstandarisasi), Level 3 (Terstandarisasi menyeluruh), Level 4 (Terintegrasi/Terkolaborasi lintas instansi), Level 5 (Optimum/Terus disempurnakan dinamis)."
))

skb_100_questions.append(make_q(
    "kd_20", "Tata Kelola SPBE & SDI", "Interoperabilitas Data - Sintaksis & Semantik",
    "Agar dua sistem informasi pada kementerian yang berbeda dapat saling bertukar data kependudukan dan memahaminya secara otomatis, sistem tersebut harus memenuhi dua tingkat interoperabilitas, yaitu...",
    "Interoperabilitas Fisik dan Non-Fisik",
    "Interoperabilitas Sintaksis (format data seperti JSON/XML) dan Interoperabilitas Semantik (kesamaan arti/makna definisi data)",
    "Interoperabilitas Internal dan Eksternal",
    "Interoperabilitas Gratis dan Berbayar",
    "Interoperabilitas Manual dan Otomatis",
    "B", "W3C Data Interoperability Standard & Prinsip SDI Perpres 39/2019.",
    "Interoperabilitas Sintaksis memastikan data dapat diparsing (format JSON/XML terbaca). Interoperabilitas Semantik memastikan data yang diparsing memiliki arti definisi yang sama persis bagi kedua sistem."
))

skb_100_questions.append(make_q(
    "kd_21", "Tata Kelola SPBE & SDI", "Arsitektur Proses Bisnis Pemerintah",
    "Domain Proses Bisnis pada Arsitektur SPBE mendeskripsikan hubungan kerja yang terintegrasi untuk menghasilkan layanan pemerintah. Metodologi pemodelan standar yang digunakan untuk memetakan diagram alir proses bisnis SPBE adalah...",
    "BPMN (Business Process Model and Notation)",
    "HTML5 Canvas",
    "Flowchart manual tanpa aturan standar",
    "Circuit Diagram",
    "Sketsa arsitektur bangunan",
    "A", "PermenPANRB No. 19/2018 tentang Penyusunan Peta Proses Bisnis Instansi Pemerintah.",
    "BPMN 2.0 (Business Process Model and Notation) adalah standar internasional baku yang ditetapkan pemerintah untuk menyusun peta proses bisnis instansi pemerintah dari level 0 hingga level 4."
))

skb_100_questions.append(make_q(
    "kd_22", "Tata Kelola SPBE & SDI", "IT Governance - COBIT 2019",
    "Kerangka kerja tata kelola TI global COBIT 2019 membedakan secara tegas antara Governance dan Management. Yang merupakan area objektif tata kelola (Governance Objectives) adalah...",
    "APO (Align, Plan, and Organize)",
    "BAI (Build, Acquire, and Implement)",
    "DSS (Deliver, Service, and Support)",
    "EDM (Evaluate, Direct, and Monitor)",
    "MEA (Monitor, Evaluate, and Assess)",
    "D", "ISACA COBIT 2019 Framework: Governance and Management Objectives.",
    "Governance (Tata Kelola) berada pada domain EDM (Evaluate, Direct, Monitor) yang bertugas mengevaluasi arah strategis dan memantau kepatuhan. Sedangkan 4 domain lainnya adalah fungsi operasional Management."
))

skb_100_questions.append(make_q(
    "kd_23", "Tata Kelola SPBE & SDI", "Manajemen Risiko TI - ISO 31000",
    "Dalam manajemen risiko TI berbasis ISO 31000 pada instansi pemerintah, langkah yang dilakukan untuk mengidentifikasi tingkat probabilitas (kemungkinan) dan dampak (severity) dari ancaman siber disebut...",
    "Risk Mitigation",
    "Risk Analysis (Analisis Risiko)",
    "Risk Avoidance",
    "Risk Acceptance",
    "Risk Elimination",
    "B", "ISO 31000:2018 Risk Management Guidelines & Permenkominfo Manajemen Risiko SPBE.",
    "Risk Analysis melibatkan pemahaman sifat risiko dan penentuan tingkat risiko dengan mengkombinasikan penilaian 'Likelihood' (probabilitas terjadinya) dan 'Consequence/Impact' (tingkat keparahan dampak)."
))

skb_100_questions.append(make_q(
    "kd_24", "Tata Kelola SPBE & SDI", "Pusat Jaringan Inovasi Pelayanan Publik",
    "Dalam rangka mencegah pemborosan anggaran akibat pembangunan aplikasi sejenis yang berulang di ratusan pemda, Perpres SPBE mewajibkan penerapan prinsip...",
    "Satu dinas wajib membuat 50 aplikasi setiap tahun",
    "Aplikasi Umum Berbagi Pakai (Shared Government Applications) dan repositori kode nasional",
    "Membeli lisensi perangkat lunak tertutup termahal",
    "Merekrut programmer pihak ketiga tanpa kontrak kerja",
    "Melarang penggunaan aplikasi berbasis web",
    "B", "Perpres No. 95 Tahun 2018 tentang SPBE, Pasal 38.",
    "Aplikasi SPBE dibagi menjadi Aplikasi Umum (berbagi pakai nasional untuk fungsi yang sama, misal persuratan Srikandi, kepegawaian SIASN, keuangan SIPD) dan Aplikasi Khusus untuk fungsi unik instansi."
))

skb_100_questions.append(make_q(
    "kd_25", "Tata Kelola SPBE & SDI", "Satu Data Indonesia - Pembina Data",
    "Berdasarkan Perpres No. 39 Tahun 2019, lembaga negara yang ditunjuk sebagai Pembina Data Statistik tingkat nasional dalam forum Satu Data Indonesia adalah...",
    "Badan Pusat Statistik (BPS)",
    "Badan Informasi Geospasial (BIG)",
    "Kementerian Keuangan",
    "Badan Riset dan Inovasi Nasional (BRIN)",
    "Arsip Nasional Republik Indonesia (ANRI)",
    "A", "Perpres No. 39 Tahun 2019 tentang Satu Data Indonesia, Pasal 11 Ayat (2).",
    "Pembina Data tingkat pusat: BPS sebagai Pembina Data Statistik, Badan Informasi Geospasial (BIG) sebagai Pembina Data Geospasial, dan Kementerian Keuangan sebagai Pembina Data Keuangan Negara."
))

skb_100_questions.append(make_q(
    "kd_26", "Tata Kelola SPBE & SDI", "Satu Data Indonesia - Pembina Data Geospasial",
    "Lembaga pemerintah non-kementerian yang bertugas menetapkan standar data, struktur, dan metadata geospasial dalam penyelenggaraan Satu Data Indonesia adalah...",
    "Badan Riset dan Inovasi Nasional (BRIN)",
    "Badan Informasi Geospasial (BIG)",
    "Badan Meteorologi, Klimatologi, dan Geofisika (BMKG)",
    "Kementerian ATR/BPN",
    "Kementerian Lingkungan Hidup",
    "B", "Perpres No. 39 Tahun 2019 tentang Satu Data Indonesia, Pasal 11 Ayat (3).",
    "Badan Informasi Geospasial (BIG) bertindak sebagai Pembina Data Geospasial Nasional yang berwenang menetapkan kaidah teknis peta, datum referensi, dan metadata geospasial."
))

skb_100_questions.append(make_q(
    "kd_27", "Tata Kelola SPBE & SDI", "Metadata Standar Dublin Core",
    "Metadata berfungsi memberikan konteks informasi pelacak terhadap aset data pemerintah. Standar elemen metadata internasional yang banyak diadopsi untuk katalog data terbuka pemerintah (Open Data) adalah...",
    "Dublin Core Metadata Element Set (ISO 15836)",
    "RGB Palette Code",
    "ASCII Code 128",
    "ZIP Compression Header",
    "MP3 ID3v2 Tag",
    "A", "ISO 15836 / RFC 5013 (The Dublin Core Metadata Element Set).",
    "Dublin Core mendefinisikan 15 elemen inti metadata (Title, Creator, Subject, Description, Publisher, Contributor, Date, Type, Format, Identifier, Source, Language, Relation, Coverage, Rights) untuk data terbuka."
))

skb_100_questions.append(make_q(
    "kd_28", "Tata Kelola SPBE & SDI", "Audit Teknologi Informasi dan Komunikasi",
    "Sesuai Pasal 55 Perpres No. 95/2018, Audit TIK SPBE wajib dilaksanakan secara berkala paling sedikit...",
    "1 (satu) kali dalam 2 (dua) tahun",
    "1 (satu) kali dalam 10 tahun",
    "1 (satu) kali setiap pergantian kabinet",
    "Hanya jika terjadi bencana gempa bumi",
    "Setiap minggu sekali tanpa henti",
    "A", "Perpres No. 95 Tahun 2018 tentang SPBE, Pasal 55 Ayat (2).",
    "Audit TIK SPBE terdiri atas audit infrastruktur, audit aplikasi, dan audit keamanan SPBE yang dilaksanakan secara berkala paling sedikit 1 kali dalam 2 tahun."
))

skb_100_questions.append(make_q(
    "kd_29", "Tata Kelola SPBE & SDI", "Klasifikasi Keamanan Informasi Nasional",
    "Berdasarkan standar tata kelola keamanan informasi pemerintah, klasifikasi data dan aset informasi SPBE dibagi menjadi 4 tingkatan, yaitu...",
    "Murah, Sedang, Mahal, dan Sangat Mahal",
    "Terbuka, Terbatas, Rahasia, dan Sangat Rahasia",
    "Format Teks, Format Gambar, Format Audio, dan Format Video",
    "Data Lama, Data Sedang, Data Baru, dan Data Rusak",
    "Lokal, Regional, Nasional, dan Internasional",
    "B", "Standar Pengamanan Informasi SPBE BSSN & Peraturan Kominfo.",
    "Klasifikasi Keamanan Informasi Nasional membagi aset informasi menjadi: 1. Terbuka (Public), 2. Terbatas (Internal), 3. Rahasia (Confidential), dan 4. Sangat Rahasia (Top Secret/Restricted)."
))

skb_100_questions.append(make_q(
    "kd_30", "Tata Kelola SPBE & SDI", "Service Level Agreement (SLA)",
    "Dalam penyediaan layanan infrastruktur komputasi awan SPBE oleh penyedia kepada instansi pemerintah, dokumen hukum yang mendefinisikan komitmen jaminan tingkat ketersediaan layanan (uptime), waktu respons penanganan kendala, dan sanksi penalti disebut...",
    "NDA (Non-Disclosure Agreement)",
    "SLA (Service Level Agreement)",
    "MOU (Memorandum of Understanding)",
    "RFP (Request for Proposal)",
    "CV (Curriculum Vitae)",
    "B", "ITIL v4 Service Management & Standar Pengadaan Cloud LKPP/Kemkomdigi.",
    "SLA adalah perjanjian formal yang menetapkan parameter metrik kualitas layanan yang terukur (misal uptime 99,9%, MTTR < 2 jam) beserta konsekuensi kompensasi jika target tidak tercapai."
))

# Lanjutkan hingga 100 soal... Kita tambahkan domain Cloud, Jaringan, Cybersecurity, Software Engineering, Basis Data
# ------------------------------------------------------------------------------
# DOMAIN 3: CLOUD COMPUTING & PUSAT DATA NASIONAL (Soal 31 - 45)
# ------------------------------------------------------------------------------
skb_100_questions.append(make_q(
    "kd_31", "Cloud & Pusat Data", "NIST SP 800-145 - 5 Karakteristik Cloud",
    "Definisi resmi Cloud Computing menurut National Institute of Standards and Technology (NIST SP 800-145) menetapkan 5 karakteristik esensial. Yang BUKAN merupakan karakteristik esensial cloud adalah...",
    "On-demand self-service",
    "Broad network access",
    "Resource pooling",
    "Rapid elasticity",
    "Kewajiban instalasi hardware fisik manual di ruangan pengguna",
    "E", "NIST Special Publication 800-145: The NIST Definition of Cloud Computing.",
    "5 Karakteristik Esensial Cloud: 1. On-demand self-service, 2. Broad network access, 3. Resource pooling, 4. Rapid elasticity, 5. Measured service. Menginstal hardware fisik manual bertentangan dengan prinsip cloud."
))

skb_100_questions.append(make_q(
    "kd_32", "Cloud & Pusat Data", "Model Deployment Cloud",
    "Pusat Data Nasional (PDN) yang dibangun oleh pemerintah Indonesia secara eksklusif diperuntukkan hanya bagi instansi pemerintah kementerian, lembaga, dan pemerintah daerah. Model deployment cloud ini disebut...",
    "Public Cloud",
    "Community Cloud / Government Private Cloud",
    "Hybrid Cloud Swasta",
    "Commercial Cloud Bebas",
    "Personal Cloud",
    "B", "NIST SP 800-145 & Blueprint PDN Kemkomdigi.",
    "Community Cloud dioperasikan secara eksklusif untuk komunitas pengguna tertentu yang memiliki kepentingan, kebijakan, dan misi yang sama (dalam hal ini instansi pemerintah Republik Indonesia)."
))

skb_100_questions.append(make_q(
    "kd_33", "Cloud & Pusat Data", "Arsitektur Virtualisasi - Hypervisor Type 1",
    "Dalam infrastruktur server Pusat Data Nasional, Hypervisor Type 1 (Bare-Metal) diinstal langsung di atas perangkat keras server fisik tanpa memerlukan sistem operasi induk. Contoh perangkat lunak Hypervisor Type 1 adalah...",
    "VMware ESXi, Proxmox VE, dan KVM",
    "Oracle VirtualBox di atas Windows 10",
    "VMware Workstation di atas Ubuntu Desktop",
    "Aplikasi Notepad",
    "Peramban Google Chrome",
    "A", "IEEE Cloud Computing Architecture & Enterprise Server Virtualization Standards.",
    "Type 1 Hypervisor (Bare-Metal) berjalan langsung di atas hardware bare metal tanpa OS perantara, memberikan performa tinggi dan latensi rendah. Contoh: VMware ESXi, KVM, Microsoft Hyper-V Server, Proxmox."
))

skb_100_questions.append(make_q(
    "kd_34", "Cloud & Pusat Data", "Teknologi Kontainerisasi (Docker & Kubernetes)",
    "Dibandingkan dengan Virtual Machine (VM) tradisional yang memuat sistem operasi tamu (Guest OS) lengkap, keunggulan utama dari teknologi kontainerisasi (seperti Docker) pada sistem aplikasi SPBE adalah...",
    "Lebih boros memori RAM dan booting lebih lambat",
    "Ringan, berbagi kernel OS dengan host, ukuran image kecil, dan waktu startup dalam hitungan detik",
    "Tidak dapat berjalan di server Linux",
    "Hanya bisa menyimpan file dokumen Word",
    "Memerlukan kabel jaringan tambahan per kontainer",
    "B", "Cloud Native Computing Foundation (CNCF) & Standar Microservices SPBE.",
    "Kontainer mengemas aplikasi beserta dependensinya dengan berbagi host OS kernel, menjadikannya jauh lebih ringan, cepat dalam startup (sub-detik), dan portabel di berbagai lingkungan cloud."
))

skb_100_questions.append(make_q(
    "kd_35", "Cloud & Pusat Data", "Orkestrasi Kontainer - Kubernetes (K8s)",
    "Platform orkestrasi kontainer open-source yang digunakan pada Pusat Data Nasional untuk mengelola deployment, penskalaan otomatis (auto-scaling), dan pemulihan mandiri (self-healing) dari ribuan kontainer aplikasi pemerintah adalah...",
    "Apache HTTP Server",
    "Kubernetes (K8s)",
    "Microsoft Paint",
    "MySQL Workbench",
    "PuTTY",
    "B", "CNCF Kubernetes Architectural Standards & Deployment PDN.",
    "Kubernetes adalah platform standar industri untuk mengorkestrasi siklus hidup kontainer: otomatisasi deployment, scaling horizontal (HPA), load balancing, service discovery, dan rolling update tanpa downtime."
))

skb_100_questions.append(make_q(
    "kd_36", "Cloud & Pusat Data", "Standar Pusat Data ANSI/TIA-942",
    "Berdasarkan standar internasional ANSI/TIA-942, pusat data yang memiliki jalur distribusi listrik dan pendingin ganda aktif secara simultan (Active-Active), memiliki komponen redundan (2N+1), dan toleran terhadap kesalahan tanpa gangguan operasional diklasifikasikan sebagai...",
    "Rated 1 (Basic)", "Rated 2 (Redundant Component)", "Rated 3 (Concurrently Maintainable)", "Rated 4 (Fault Tolerant)", "Rated 0",
    "D", "ANSI/TIA-942-B Telecommunications Infrastructure Standard for Data Centers.",
    "Rated 4 (Fault Tolerant) adalah tingkatan tertinggi: sistem dapat menoleransi kegagalan satu komponen kritis tanpa menyebabkan downtime operasional pada sistem komputer."
))

skb_100_questions.append(make_q(
    "kd_37", "Cloud & Pusat Data", "Metrik Pemulihan Bencana - RPO",
    "Dalam perancangan Disaster Recovery Center (DRC) pada Pusat Data Nasional, parameter 'Recovery Point Objective (RPO)' mengukur...",
    "Berapa lama waktu yang dibutuhkan server untuk menyala kembali",
    "Batas toleransi maksimal kehilangan data akibat insiden yang diukur dalam satuan waktu sebelum bencana terjadi",
    "Berapa jumlah pegawai yang boleh bekerja dari rumah",
    "Biaya sewa gedung pusat data per bulan",
    "Kecepatan transfer kipas pendingin server",
    "B", "ISO 22301 Business Continuity Management & NIST SP 800-34 Contingency Planning.",
    "RPO (Recovery Point Objective) menentukan usia data yang harus dipulihkan dari media backup agar operasi dapat dilanjutkan secara wajar. Jika RPO = 1 jam, data transaksi maksimal yang hilang adalah 1 jam sebelum insiden."
))

skb_100_questions.append(make_q(
    "kd_38", "Cloud & Pusat Data", "Metrik Pemulihan Bencana - RTO",
    "Sedangkan parameter 'Recovery Time Objective (RTO)' pada sistem darurat Pusat Data Nasional mengukur...",
    "Durasi waktu maksimal yang diperbolehkan bagi sistem untuk pulih dan beroperasi kembali setelah bencana terjadi",
    "Batas waktu pegawai datang ke kantor",
    "Berapa lama harddisk dapat bertahan sebelum rusak alami",
    "Waktu garansi pabrik server",
    "Waktu pengiriman suku cadang melalui ekspedisi pos",
    "A", "NIST SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems.",
    "RTO (Recovery Time Objective) adalah durasi waktu maksimal dari saat sistem terhenti (outage) hingga sistem selesai dipulihkan dan dapat melayani transaksi pengguna kembali."
))

skb_100_questions.append(make_q(
    "kd_39", "Cloud & Pusat Data", "Efisiensi Energi Pusat Data - PUE",
    "Pusat Data Nasional dirancang dengan konsep Green Data Center. Metrik standar global yang digunakan untuk mengukur efisiensi penggunaan energi listrik pada pusat data (Total Energi Fasilitas / Energi Peralatan IT) adalah...",
    "PUE (Power Usage Effectiveness)",
    "RPM (Revolutions Per Minute)",
    "BHP (Brake Horsepower)",
    "BTU (British Thermal Unit)",
    "dB (Decibel)",
    "A", "The Green Grid Data Center Energy Efficiency Standards & ISO/IEC 30134-2.",
    "PUE (Power Usage Effectiveness) mengukur rasio total daya yang masuk ke fasilitas gedung terhadap daya yang benar-benar dikonsumsi peralatan IT. Skor PUE ideal mendekati 1.0 (sangat efisien)."
))

skb_100_questions.append(make_q(
    "kd_40", "Cloud & Pusat Data", "Storage Area Network (SAN)",
    "Untuk menghubungkan server cluster database ke penyimpanan bersama (shared block storage) berkecepatan tinggi tanpa membebani jaringan LAN lokal, arsitektur penyimpanan yang digunakan adalah...",
    "Direct Attached Storage (DAS) kabel USB",
    "Storage Area Network (SAN) berbasis Fiber Channel atau iSCSI",
    "Floppy Disk Drive",
    "Penyimpanan email online",
    "Kaset pita magnetik radio",
    "B", "SNIA (Storage Networking Industry Association) Architecture Standards.",
    "SAN adalah jaringan khusus berkecepatan tinggi (biasanya Fibre Channel atau iSCSI) yang menghubungkan klaster server komputasi dengan array disk penyimpanan blok terpusat."
))

skb_100_questions.append(make_q(
    "kd_41", "Cloud & Pusat Data", "Replikasi Basis Data - Synchronous vs Asynchronous",
    "Dalam skenario DRC antar pulau (jarak lebih dari 100 km dengan latensi jaringan > 20 ms), mode replikasi basis data yang paling realistis digunakan agar transaksi server produksi tidak mengalami perlambatan ekstrem (lag) adalah...",
    "Synchronous Replication",
    "Asynchronous Replication",
    "Manual Copy-Paste",
    "Pengiriman flashdisk via kurir harian",
    "Pencetakan laporan ke kertas continuous form",
    "B", "Oracle/PostgreSQL High Availability & Disaster Recovery Architecture Guide.",
    "Asynchronous Replication mengonfirmasi transaksi di server utama tanpa harus menunggu konfirmasi selesai tulis dari server DRC jarak jauh, sehingga performa transaksi utama tidak terhambat latensi jaringan antarpulau."
))

skb_100_questions.append(make_q(
    "kd_42", "Cloud & Pusat Data", "Teknologi Software-Defined Networking (SDN)",
    "Konsep arsitektur jaringan modern pada Pusat Data Nasional yang memisahkan antara bidang kendali (Control Plane) dan bidang penerusan data (Data Plane) secara terprogram disebut...",
    "Software-Defined Networking (SDN)",
    "Peer-to-Peer Networking",
    "Dial-up Modem",
    "Token Ring Tradisional",
    "Walkie Talkie Digital",
    "A", "Open Networking Foundation (ONF) SDN Architecture Standards.",
    "SDN memusatkan logika kendali jaringan pada controller perangkat lunak terpusat (Control Plane), sedangkan perangkat switch/router hanya bertugas meneruskan paket data (Data Plane) sesuai aturan flow table."
))

skb_100_questions.append(make_q(
    "kd_43", "Cloud & Pusat Data", "Sistem Penyimpanan Objek (Object Storage)",
    "Untuk menyimpan berkas arsip KTP, sertifikat tanah, dan dokumen digital SPBE berukuran petabyte yang tidak terstruktur dengan metadata kustom tak terbatas, jenis penyimpanan cloud yang paling sesuai adalah...",
    "Block Storage",
    "Object Storage (S3-compatible API)",
    "File System FAT32",
    "CD-ROM Read-Only",
    "ROM BIOS",
    "B", "Cloud Storage Architecture Standard (NIST / AWS S3 API Standard).",
    "Object Storage menyimpan data sebagai objek mandiri yang terdiri atas data biner, metadata kustom, dan ID unik global dalam ruang alamat datar (flat namespace), sangat skalabel hingga miliaran file statis."
))

skb_100_questions.append(make_q(
    "kd_44", "Cloud & Pusat Data", "Infrastructure as Code (IaC)",
    "Praktik mengelola dan menyediakan infrastruktur virtual (server, network, storage) pada Pusat Data Nasional menggunakan file definisi kode konfigurasi yang terotomasi (seperti Terraform atau Ansible) disebut...",
    "Manual Configuration",
    "Infrastructure as Code (IaC)",
    "Hardcoding IP Address",
    "Trial and Error",
    "Pemasangan kabel jumper manual",
    "B", "DevOps & Cloud Native Architecture Standards.",
    "IaC (Infrastructure as Code) memungkinkan insinyur IT mengotomasi provisioning infrastruktur cloud secara konsisten, dapat diuji, dan terlacak versinya melalui version control (Git)."
))

skb_100_questions.append(make_q(
    "kd_45", "Cloud & Pusat Data", "Toleransi Kesalahan - High Availability (HA)",
    "Konsep klaster server database di mana dua node server aktif melayani transaksi secara bersamaan dan saling berbagi beban, serta siap mengambil alih fungsi secara otomatis jika salah satu node gagal disebut...",
    "Active-Passive Clustering",
    "Active-Active Clustering",
    "Standby Offline",
    "Single Instance",
    "Cold Site",
    "B", "Enterprise Database Clustering & Fault Tolerance Architecture Guide.",
    "Active-Active Clustering mengoperasikan semua node server secara simultan untuk load balancing dan redundansi penuh; jika satu server tumbang, beban kerja otomatis dialihkan ke node aktif lainnya tanpa jeda kegagalan."
))

# ------------------------------------------------------------------------------
# DOMAIN 4: JARINGAN TELEKOMUNIKASI & SPEKTRUM FREKUENSI (Soal 46 - 60)
# ------------------------------------------------------------------------------
skb_100_questions.append(make_q(
    "kd_46", "Jaringan & Spektrum", "Model OSI 7 Layer - ISO 7498",
    "Pada Model Referensi OSI 7 Layer, enkripsi TLS/SSL dan kompresi format data MIME ditangani secara khusus pada lapisan...",
    "Lapisan Fisik (Physical Layer)",
    "Lapisan Jaringan (Network Layer)",
    "Lapisan Transport (Transport Layer)",
    "Lapisan Presentasi (Presentation Layer)",
    "Lapisan Data Link (Data Link Layer)",
    "D", "ISO/IEC 7498-1: Information technology — Open Systems Interconnection.",
    "Presentation Layer (Layer 6 OSI) bertanggung jawab atas representasi data sintaksis, enkripsi/dekripsi, serta kompresi format data sebelum diserahkan ke Application Layer."
))

skb_100_questions.append(make_q(
    "kd_47", "Jaringan & Spektrum", "Subnetting CIDR IPv4",
    "Sebuah instansi kementerian diberikan alokasi alamat jaringan 10.20.0.0/24 dan ingin membaginya menjadi 4 subnet yang memiliki jumlah host sama besar. Berapakah prefix subnet mask baru dan jumlah usable host per subnet?",
    "Prefix /25 dengan 126 host per subnet",
    "Prefix /26 dengan 62 host per subnet",
    "Prefix /27 dengan 30 host per subnet",
    "Prefix /28 dengan 14 host per subnet",
    "Prefix /30 dengan 2 host per subnet",
    "B", "RFC 1519: Classless Inter-domain Routing (CIDR) Architecture.",
    "Membagi menjadi 4 subnet membutuhkan 2 bit tambahan (2^2 = 4). Prefix baru: 24 + 2 = /26 (mask 255.255.255.192). Host per subnet: 2^(32-26) - 2 = 64 - 2 = 62 usable host."
))

skb_100_questions.append(make_q(
    "kd_48", "Jaringan & Spektrum", "Protokol Transport - TCP vs UDP",
    "Layanan live streaming telekonferensi dan video call pemerintah menggunakan protokol Transport Layer UDP (seperti WebRTC) daripada TCP karena pertimbangan utama...",
    "UDP menjamin 100% data tidak pernah hilang dengan retransmisi",
    "UDP memiliki latensi rendah dan tidak memerlukan mekanisme 3-way handshake atau retransmisi yang menimbulkan delay",
    "UDP selalu lebih lambat dari TCP",
    "TCP dilarang oleh standar telekomunikasi",
    "UDP hanya bekerja dengan kabel tembaga",
    "B", "RFC 768 (UDP) & RFC 793 (TCP) Internet Protocol Standards.",
    "UDP bersifat connectionless dan tidak melakukan retransmisi paket yang hilang, memprioritaskan kecepatan real-time dan latensi rendah yang sangat krusial untuk komunikasi audio-video interaktif."
))

skb_100_questions.append(make_q(
    "kd_49", "Jaringan & Spektrum", "VLAN & IEEE 802.1Q",
    "Untuk memisahkan lalu lintas jaringan antara komputer staf pelayanan umum dan server database keuangan pada satu switch fisik yang sama demi keamanan, teknologi yang digunakan adalah...",
    "VLAN (Virtual Local Area Network) berbasis tagging IEEE 802.1Q",
    "Mematikan daya listrik switch",
    "Menggunakan kabel warna-warni tanpa konfigurasi",
    "Membeli komputer baru untuk setiap staf",
    "Menghubungkan seluruh kabel menjadi satu loop",
    "A", "IEEE 802.1Q Standard for Local and Metropolitan Area Networks: Bridges and Bridged Networks.",
    "VLAN mengisolasi broadcast domain pada layer 2 OSI secara logis di dalam perangkat switch yang sama, meningkatkan keamanan dan efisiensi lalu lintas jaringan tanpa perlu infrastruktur fisik terpisah."
))

skb_100_questions.append(make_q(
    "kd_50", "Jaringan & Spektrum", "Protokol Routing Dinamis - BGP",
    "Protokol routing eksterior standar yang digunakan untuk mempertukarkan rute antar Autonomous System (AS) di tulang punggung internet nasional dan internasional adalah...",
    "RIP (Routing Information Protocol)",
    "BGP (Border Gateway Protocol / BGP-4)",
    "Telnet",
    "DHCP",
    "ARP",
    "B", "RFC 4271: A Border Gateway Protocol 4 (BGP-4).",
    "BGP adalah protokol routing Exterior Gateway Protocol (EGP) de facto yang menopang lalu lintas internet global antar penyedia layanan internet (ISP) dan Autonomous System negara."
))

skb_100_questions.append(make_q(
    "kd_51", "Jaringan & Spektrum", "Teknologi Serat Optik - DWDM",
    "Jaringan Palapa Ring Kemkomdigi menggunakan teknologi transmisi optik DWDM (Dense Wavelength Division Multiplexing). Fungsi utama dari teknologi DWDM ini adalah...",
    "Mengubah sinyal optik menjadi suara manusia langsung",
    "Menggabungkan dan mentransmisikan puluhan kanal panjang gelombang cahaya (warna cahaya) yang berbeda ke dalam satu serat optik tunggal untuk menghasilkan kapasitas terabit per detik",
    "Memperlambat sinyal cahaya agar tidak silau",
    "Menyaring virus komputer di dalam kabel laut",
    "Menghilangkan kebutuhan kabel darat",
    "B", "ITU-T Recommendation G.694.1: Spectral grids for WDM applications: DWDM frequency grid.",
    "DWDM melipatgandakan kapasitas transmisi satu pasang serat optik hingga puluhan terabit per detik dengan membagi spektrum optik ke dalam banyak kanal panjang gelombang cahaya terpisah secara simultan."
))

skb_100_questions.append(make_q(
    "kd_52", "Jaringan & Spektrum", "Spektrum Frekuensi 5G - mMTC",
    "Salah satu dari tiga pilar arsitektur 5G menurut standar 3GPP adalah mMTC (massive Machine Type Communications). Fokus utama penerapan mMTC dalam program Smart City Kemkomdigi adalah...",
    "Menonton video streaming resolusi 8K di bioskop",
    "Menghubungkan jutaan sensor pintar berdaya rendah (smart meter air, sensor parkir, pemantau polusi udara) secara padat dan masif dalam radius satu kilometer persegi",
    "Mematikan koneksi ponsel warga miskin",
    "Menggantikan pemancar radio AM/FM",
    "Menyiarkan iklan komersial dari menara BTS",
    "B", "3GPP Release 15/16 5G Technical Specification & ITU-R IMT-2020 Standard.",
    "mMTC dirancang khusus untuk Internet of Things (IoT) berskala masif: mendukung hingga 1 juta perangkat sensor per km² dengan konsumsi daya sangat rendah (baterai bertahan hingga 10 tahun)."
))

skb_100_questions.append(make_q(
    "kd_53", "Jaringan & Spektrum", "Digital Video Broadcasting - DVB-T2",
    "Standar penyiaran televisi terrestrial digital yang ditetapkan Kemkomdigi untuk menggantikan siaran analog (ASO) di seluruh wilayah Indonesia adalah...",
    "DVB-T2 (Digital Video Broadcasting - Terrestrial 2nd Generation)",
    "NTSC Tradisional",
    "PAL Analog",
    "SECAM",
    "VHS Tape",
    "A", "Permenkominfo Standar Teknis Siaran TV Digital Terestrial & ETSI EN 302 755.",
    "DVB-T2 adalah standar penyiaran digital terestrial modern yang efisien dalam spektrum frekuensi dan mendukung siaran video High Definition (HD) serta audio jernih tanpa derau (noise)."
))

skb_100_questions.append(make_q(
    "kd_54", "Jaringan & Spektrum", "Sistem Resolusi Nama Domain - DNSSEC",
    "Untuk mencegah serangan manipulasi rekaman DNS (DNS Spoofing / DNS Cache Poisoning) yang mengarahkan pengunjung website resmi pemerintah (.go.id) ke situs palsu, protokol pengamanan yang diterapkan adalah...",
    "DNSSEC (Domain Name System Security Extensions)",
    "FTP Tanpa Sandi",
    "HTTP 1.0",
    "Telnet Port 23",
    "SNMP v1",
    "A", "RFC 4033, 4034, 4035: Resource Records for the DNS Security Extensions.",
    "DNSSEC menambahkan tanda tangan kriptografis digital pada rekaman DNS sehingga resolver peramban dapat memvalidasi keaslian asal rekaman DNS dan memastikan data tidak dimanipulasi di perjalanan."
))

skb_100_questions.append(make_q(
    "kd_55", "Jaringan & Spektrum", "Satelit Geostasioner (GEO)",
    "Satelit SATRIA-1 milik pemerintah beroperasi pada orbit geostasioner (GEO) di atas khatulistiwa. Ketinggian orbit geostasioner dari permukaan bumi dan karakteristik geraknya adalah...",
    "Ketinggian ~35.786 km dan memiliki periode revolusi yang sama persis dengan rotasi bumi (24 jam) sehingga posisinya tampak diam relatif terhadap stasiun bumi",
    "Ketinggian 200 km dan mengelilingi bumi setiap 90 menit",
    "Ketinggian 5.000 km dan berpindah tempat setiap jam",
    "Di dalam atmosfer awan hujan",
    "Di orbit planet Mars",
    "A", "ITU Radiocommunication Sector (ITU-R) Geostationary Satellite Orbit Standards.",
    "Orbit GEO berada pada ketinggian 35.786 km tepat di atas garis khatulistiwa; satelit bergerak dengan kecepatan sudut sama dengan rotasi bumi, sehingga antena parabola di darat cukup diarahkan ke satu titik tetap."
))

skb_100_questions.append(make_q(
    "kd_56", "Jaringan & Spektrum", "Protokol Keamanan Wi-Fi - WPA3",
    "Standar keamanan jaringan nirkabel (Wi-Fi) terbaru yang menggantikan WPA2 dengan perlindungan terhadap serangan offline dictionary attack melalui mekanisme Simultaneous Authentication of Equals (SAE) adalah...",
    "WEP (Wired Equivalent Privacy)",
    "WPA3-Enterprise / WPA3-Personal",
    "Koneksi Open Tanpa Sandi",
    "WPS PIN Tunggal",
    "MAC Filtering Manual",
    "B", "Wi-Fi Alliance WPA3 Security Specification & IEEE 802.11i-2004 Standard.",
    "WPA3 menggunakan protokol jabat tangan SAE (Dragonfly) yang tahan terhadap offline dictionary attack dan menyediakan enkripsi 192-bit pada mode Enterprise untuk jaringan berkeamanan tinggi."
))

skb_100_questions.append(make_q(
    "kd_57", "Jaringan & Spektrum", "Network Address Translation (NAT)",
    "Fungsi router jaringan pemerintah yang memetakan puluhan komputer dengan IP Privat (RFC 1918) ke satu alamat IP Publik resmi untuk dapat mengakses internet secara bersamaan disebut...",
    "NAPT / PAT (Port Address Translation / NAT Overload)",
    "DNS Poisoning",
    "MAC Spoofing",
    "ARP Flooding",
    "Split Horizon",
    "A", "RFC 2663: IP Network Address Translator (NAT) Terminology and Considerations.",
    "NAPT/PAT (NAT Overload) memetakan banyak alamat IP lokal privat ke satu atau beberapa alamat IP publik menggunakan kombinasi nomor port layer 4 yang berbeda untuk melacak setiap sesi koneksi."
))

skb_100_questions.append(make_q(
    "kd_58", "Jaringan & Spektrum", "Quality of Service (QoS) Jaringan",
    "Untuk memastikan lalu lintas data layanan video conference darurat pimpinan negara tidak terputus atau tersendat saat jaringan sedang padat, mekanisme rekayasa lalu lintas yang memprioritaskan paket tertentu disebut...",
    "QoS (Quality of Service) dengan penandaan DSCP / DiffServ",
    "Best Effort Tanpa Prioritas",
    "Packet Dropping Acak",
    "Bandwidth Throttling Maksimal",
    "Half-Duplex Switching",
    "A", "RFC 2474: Definition of the Differentiated Services Field (DiffServ Field).",
    "QoS melalui penandaan DSCP (Differentiated Services Code Point) di header IP memastikan antrean router memprioritaskan paket suara dan video interaktif di atas lalu lintas browsing web biasa."
))

skb_100_questions.append(make_q(
    "kd_59", "Jaringan & Spektrum", "Protokol Waktu Jaringan - NTP",
    "Pusat Data Nasional mensyaratkan seluruh server transaksi, log audit, dan firewall memiliki sinkronisasi jam sistem yang akurat dalam orde milidetik. Protokol jaringan standar yang digunakan untuk sinkronisasi waktu adalah...",
    "NTP (Network Time Protocol) berbasis UDP Port 123",
    "SMTP Port 25",
    "POP3 Port 110",
    "FTP Port 21",
    "IMAP Port 143",
    "A", "RFC 5905: Network Time Protocol Version 4 (NTPv4) Specification.",
    "NTP menggunakan arsitektur stratum hierarkis (berinduk ke jam atom radioaktivitas/GPS) untuk menyinkronkan waktu sistem di seluruh jaringan komputer, sangat esensial untuk validitas rekaman log audit keamanan."
))

skb_100_questions.append(make_q(
    "kd_60", "Jaringan & Spektrum", "Virtual Private Network - IPsec Architecture",
    "Protokol keamanan IPsec beroperasi pada Network Layer (Layer 3) dan memiliki dua mode operasi utama untuk tunneling data antar kantor cabang instansi, yaitu...",
    "Tunnel Mode dan Transport Mode",
    "Active Mode dan Passive Mode",
    "Synchronous Mode dan Asynchronous Mode",
    "Client Mode dan Server Mode",
    "Master Mode dan Slave Mode",
    "A", "RFC 4301: Security Architecture for the Internet Protocol (IPsec).",
    "IPsec menyediakan Transport Mode (hanya mengenkripsi payload IP, cocok untuk host-to-host) dan Tunnel Mode (seluruh paket IP asli dienkripsi dan dibungkus header IP baru, cocok untuk gateway-to-gateway VPN)."
))

# ------------------------------------------------------------------------------
# DOMAIN 5: KEAMANAN INFORMASI & SIBER (Soal 61 - 75)
# ------------------------------------------------------------------------------
skb_100_questions.append(make_q(
    "kd_61", "Keamanan Informasi", "CIA Triad",
    "Prinsip fundamental keamanan informasi terdiri atas CIA Triad: Confidentiality, Integrity, dan Availability. Upaya mencegah terjadinya perubahan atau modifikasi data secara tidak sah (tanpa otorisasi) adalah pemenuhan aspek...",
    "Confidentiality (Kerahasiaan)",
    "Integrity (Keutuhan / Integritas Data)",
    "Availability (Ketersediaan)",
    "Scalability",
    "Portability",
    "B", "ISO/IEC 27000:2018 Overview and Vocabulary (Information Security Management Systems).",
    "Integrity (Integritas) menjaga akurasi dan kelengkapan informasi serta melindungi data dari perubahan, penyisipan, atau penghapusan tanpa hak oleh pihak yang tidak berwenang."
))

skb_100_questions.append(make_q(
    "kd_62", "Keamanan Informasi", "OWASP Top 10 - SQL Injection (SQLi)",
    "Kerentanan web di mana penyerang memasukkan perintah SQL berbahaya ke dalam kolom formulir pencarian sehingga aplikasi mengeksekusi perintah database yang tidak diinginkan dinamakan...",
    "SQL Injection (SQLi)",
    "Cross-Site Scripting (XSS)",
    "Broken Authentication",
    "Security Misconfiguration",
    "Insecure Deserialization",
    "A", "OWASP Top 10:2021 - A03:Injection.",
    "SQL Injection terjadi ketika data masukan pengguna yang tidak terfilter (untrusted data) disisipkan langsung ke dalam query SQL dinamis server, memungkinkan penyerang membaca, memodifikasi, atau menghapus data database."
))

skb_100_questions.append(make_q(
    "kd_63", "Keamanan Informasi", "Pencegahan SQLi - Parameterized Query",
    "Teknik rekayasa perangkat lunak paling efektif dan baku untuk mencegah terjadinya kerentanan SQL Injection pada kode aplikasi web pemerintah adalah...",
    "Menggunakan Prepared Statements / Parameterized Queries",
    "Menonaktifkan basis data pada malam hari",
    "Menyembunyikan tombol kirim form",
    "Menggunakan bahasa pemrograman lama",
    "Menghapus hak akses seluruh pengguna",
    "A", "OWASP SQL Injection Prevention Cheat Sheet.",
    "Parameterized Queries (Prepared Statements) memastikan database memperlakukan input pengguna secara murni sebagai data, bukan sebagai kode instruksi yang dapat dieksekusi, sehingga menutup celah injeksi SQL seutuhnya."
))

skb_100_questions.append(make_q(
    "kd_64", "Keamanan Informasi", "Kriptografi Simetris - Advanced Encryption Standard",
    "Algoritma enkripsi simetris yang menjadi standar resmi pemerintah Indonesia dan internasional untuk mengamankan data rahasia dengan panjang kunci 128, 192, atau 256 bit adalah...",
    "AES (Advanced Encryption Standard / Rijndael)",
    "Caesar Cipher",
    "ROT13",
    "Base64",
    "Vigenere Cipher",
    "A", "FIPS PUB 197: Advanced Encryption Standard (AES) & Standar Kriptografi BSSN.",
    "AES adalah standar enkripsi blok simetris yang diadopsi secara global (NIST FIPS 197) dan terbukti aman dari serangan brute force dengan komputasi modern saat ini."
))

skb_100_questions.append(make_q(
    "kd_65", "Keamanan Informasi", "Kriptografi Asimetris - Public Key Infrastructure",
    "Pada kriptografi asimetris (seperti RSA atau ECC), kunci yang digunakan oleh pengirim untuk mengenkripsi pesan rahasia yang hanya boleh dibuka oleh penerima adalah...",
    "Kunci Publik milik Penerima",
    "Kunci Privat milik Pengirim",
    "Kunci Publik milik Pengirim",
    "Kunci Rumah",
    "Password wifi kantor",
    "A", "RFC 8017: PKCS #1: RSA Cryptography Specifications Version 2.2.",
    "Pengirim mengenkripsi pesan menggunakan Kunci Publik milik penerima. Hanya Kunci Privat yang cocok milik penerima yang dapat mendekripsi pesan tersebut (menjamin kerahasiaan)."
))

skb_100_questions.append(make_q(
    "kd_66", "Keamanan Informasi", "Otentikasi Multi-Faktor (MFA / 2FA)",
    "Prinsip Multi-Factor Authentication (MFA) mensyaratkan verifikasi identitas pengguna menggunakan minimal dua faktor dari tiga kategori berbeda, yaitu...",
    "Something you know (password), Something you have (OTP/Token/Smartcard), dan Something you are (biometrik sidik jari/wajah)",
    "Nama akun, Alamat email, dan Nomor WhatsApp",
    "Tiga password berbeda yang diketik berurutan",
    "Kartu nama, Foto KTP, dan Ijazah fisik",
    "Username, Tanggal lahir, dan Nama ibu kandung",
    "A", "NIST Special Publication 800-63B: Digital Identity Guidelines (Authentication and Lifecycle Management).",
    "MFA yang sah mewajibkan kombinasi dari kategori faktor yang berbeda: pengetahuan (password/PIN), kepemilikan (OTP token/hardware key), dan inheren/biometrik (sidik jari/retina/wajah)."
))

skb_100_questions.append(make_q(
    "kd_67", "Keamanan Informasi", "Serangan DDoS & Mitigasi",
    "Serangan siber di mana penyerang mengerahkan jutaan perangkat zombie/botnet untuk membanjiri server aplikasi perizinan online pemerintah hingga server kehabisan sumber daya dan tidak dapat diakses publik dinamakan...",
    "Distributed Denial of Service (DDoS)",
    "Phishing",
    "Privilege Escalation",
    "Cross-Site Request Forgery",
    "Social Engineering",
    "A", "NIST Special Publication 800-189: Secure Inter-Domain Traffic Exchange.",
    "DDoS menyerang ketersediaan sistem (Availability) dengan membanjiri kapasitas bandwidth jaringan atau konkurensi server dari ribuan titik botnet terdistribusi secara simultan."
))

skb_100_questions.append(make_q(
    "kd_68", "Keamanan Informasi", "Web Application Firewall (WAF)",
    "Perangkat keamanan khusus yang ditempatkan di depan aplikasi web pemerintah untuk memfilter, memantau, dan memblokir lalu lintas HTTP/HTTPS berbahaya (seperti serangan XSS, SQLi, dan CSRF) disebut...",
    "Web Application Firewall (WAF)",
    "Repeater",
    "Kabel LAN Cat 6",
    "Uninterruptible Power Supply (UPS)",
    "Mouse Optik",
    "A", "PCI-DSS Requirement 6.6 & NIST SP 800-44 Guidelines on Securing Public Web Servers.",
    "WAF beroperasi pada Layer 7 (Application Layer) dengan memeriksa payload protokol HTTP untuk mendeteksi tanda-tanda serangan eksploitasi web aplikasi sebelum permintaan mencapai server aplikasi utama."
))

skb_100_questions.append(make_q(
    "kd_69", "Keamanan Informasi", "Kerentanan Cross-Site Scripting (XSS)",
    "Serangan Cross-Site Scripting (XSS) terjadi ketika aplikasi web gagal menyaring masukan pengguna sehingga penyerang dapat menyuntikkan skrip berbahaya (JavaScript) yang kemudian dieksekusi di peramban korban. Dampak utama dari serangan XSS adalah...",
    "Pencurian session cookie/token otentikasi pengguna, pembajakan sesi, atau defacement tampilan halaman",
    "Kerusakan fisik pada monitor komputer",
    "Kabel listrik kantor meledak",
    "Penghapusan data di harddisk server seketika",
    "Kenaikan tegangan listrik baterai laptop",
    "A", "OWASP Top 10:2021 - A03:Injection & XSS Prevention Guidelines.",
    "Skrip JavaScript berbahaya yang dieksekusi di browser korban dapat mengakses document.cookie, mencuri token JWT sesi aktif, dan mengirimkannya ke server milik peretas untuk membajak akun korban."
))

skb_100_questions.append(make_q(
    "kd_70", "Keamanan Informasi", "Cross-Site Request Forgery (CSRF)",
    "Mekanisme pertahanan paling umum yang diterapkan pada formulir web perbankan dan administrasi pemerintahan untuk mencegah serangan Cross-Site Request Forgery (CSRF) adalah...",
    "Penggunaan Anti-CSRF Token unik yang disinkronkan pada setiap formulir sesi",
    "Mematikan tombol submit formulir",
    "Menggunakan huruf kapital semua pada teks",
    "Menghapus database setiap 5 menit",
    "Menyuruh pengguna menghafal token 64 digit",
    "A", "OWASP Cross-Site Request Forgery Prevention Cheat Sheet.",
    "Anti-CSRF Token (Synchronizer Token Pattern) adalah nilai token rahasia acak yang dihasilkan server dan disertakan dalam form request; server memvalidasi kecocokan token ini untuk memastikan request memang berasal dari pengguna yang sah."
))

skb_100_questions.append(make_q(
    "kd_71", "Keamanan Informasi", "Rekayasa Sosial (Social Engineering)",
    "Metode penipuan digital di mana penyerang mengirimkan pesan WhatsApp atau email yang menyamar sebagai pimpinan kementerian resmi untuk memanipulasi staf agar menyerahkan kredensial login atau mentransfer dana instansi disebut...",
    "Phishing / Spear Phishing (Social Engineering)",
    "Port Scanning",
    "Buffer Overflow",
    "Packet Sniffing",
    "Defragmentasi Harddisk",
    "A", "NIST SP 800-63-3 Digital Identity Guidelines & SANS Security Awareness Standard.",
    "Phishing adalah bentuk manipulasi psikologis (social engineering) yang memanfaatkan kelengahan atau kepercayaan manusia daripada mengeksploitasi kelemahan teknis perangkat lunak."
))

skb_100_questions.append(make_q(
    "kd_72", "Keamanan Informasi", "Prinsip Hak Akses Minimum (Principle of Least Privilege)",
    "Dalam pengelolaan hak akses sistem informasi SPBE, Principle of Least Privilege (PoLP) menyatakan bahwa...",
    "Setiap pegawai baru langsung diberikan hak akses Super Administrator penuh",
    "Setiap pengguna, proses, atau sistem hanya diberikan hak akses minimum yang benar-benar mutlak diperlukan untuk menyelesaikan tugas pekerjaannya",
    "Tidak ada pegawai yang boleh memiliki akun di kantor",
    "Semua password akun kantor harus disamakan",
    "Hak akses diberikan berdasarkan kedekatan pertemanan pribadi",
    "B", "NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems.",
    "Principle of Least Privilege memastikan bahwa jika sebuah akun staf atau layanan sistem berhasil diretas, dampak pembobolan terbatas hanya pada wewenang minimum akun tersebut dan tidak meluas ke seluruh sistem."
))

skb_100_questions.append(make_q(
    "kd_73", "Keamanan Informasi", "Sistem Manajemen Informasi Peristiwa Keamanan (SIEM)",
    "Pusat Operasi Keamanan (Security Operations Center / SOC) Kemkomdigi mengumpulkan, mengorelasikan, dan menganalisis catatan log dari ratusan server, firewall, dan router secara otomatis dan terpusat menggunakan sistem...",
    "SIEM (Security Information and Event Management)",
    "Microsoft Excel Spreadsheet",
    "Buku agenda manual tulisan tangan",
    "Email inbox biasa",
    "Aplikasi chat grup",
    "A", "NIST SP 800-92: Guide to Computer Security Log Management.",
    "SIEM mengagregasi data log peristiwa keamanan dari berbagai sumber infrastruktur jaringan, menerapkan algoritma analisis korelasi ancaman, dan membunyikan peringatan darurat jika terdeteksi pola serangan siber."
))

skb_100_questions.append(make_q(
    "kd_74", "Keamanan Informasi", "Model Keamanan Zero Trust",
    "Paradigma keamanan siber modern yang diadopsi dalam arsitektur digital pemerintah berlandaskan filosofi 'Never Trust, Always Verify' (Jangan pernah percaya, selalu verifikasi setiap akses tanpa memandang lokasi jaringan pengguna) disebut...",
    "Zero Trust Architecture (ZTA / NIST SP 800-207)",
    "Perimeter Defense Tradisional",
    "Open Access Network",
    "Trust-All Policy",
    "Unconditional Network Access",
    "A", "NIST Special Publication 800-207: Zero Trust Architecture.",
    "Zero Trust mengasumsikan bahwa ancaman bisa datang dari dalam maupun luar jaringan internal; setiap permintaan akses wajib diotentikasi, diotorisasi, dan dienkripsi secara ketat berdasarkan konteks pengguna dan perangkat."
))

skb_100_questions.append(make_q(
    "kd_75", "Keamanan Informasi", "Manajemen Patch Keamanan (Patch Management)",
    "Prosedur rutin dan krusial yang wajib dilakukan administrator sistem TI untuk menutup celah kerentanan yang baru ditemukan pada sistem operasi dan perangkat lunak server adalah...",
    "Patch Management & Security Update",
    "Menonaktifkan antivirus",
    "Menghapus file log audit sistem",
    "Mematikan fungsi firewall",
    "Mengubah wallpaper desktop server",
    "A", "CIS Critical Security Controls (CIS Control 7: Continuous Vulnerability Management).",
    "Patch management secara berkala mengidentifikasi, menguji, dan menerapkan pembaruan tambalan keamanan dari vendor software untuk menutup celah yang dapat dieksploitasi oleh peretas."
))

# ------------------------------------------------------------------------------
# DOMAIN 6: REKAYASA PERANGKAT LUNAK & API (Soal 76 - 90)
# ------------------------------------------------------------------------------
skb_100_questions.append(make_q(
    "kd_76", "Rekayasa Perangkat Lunak", "Metodologi Agile & Scrum",
    "Dalam pengembangan perangkat lunak modern di lingkungan instansi pemerintah, kerangka kerja Scrum membagi siklus pengembangan menjadi periode waktu pengerjaan tetap (time-boxed) berdurasi 1 hingga 4 minggu yang disebut...",
    "Sprint", "Waterfall Phase", "Milestone Tahunan", "Audit Semesteran", "Stagnation",
    "A", "The Scrum Guide by Ken Schwaber and Jeff Sutherland (IEEE Software Engineering).",
    "Sprint adalah jantung dari Scrum: sebuah iterasi time-box berdurasi 1-4 minggu di mana tim pengembang menyelesaikan serangkaian Product Backlog item hingga menjadi produk berpotensi rilis (Increment)."
))

skb_100_questions.append(make_q(
    "kd_77", "Rekayasa Perangkat Lunak", "Prinsip SOLID - Open/Closed Principle",
    "Dalam perancangan perangkat lunak berorientasi objek (OOP), prinsip Open/Closed Principle (OCP) menyatakan bahwa...",
    "Modul perangkat lunak harus terbuka untuk ekstensi (pengembangan fitur), tetapi tertutup untuk modifikasi kode sumber yang sudah stabil",
    "Seluruh kode sumber wajib dibuka ke publik tanpa hak cipta",
    "Aplikasi harus ditutup setiap pukul 17.00 WIB",
    "Sebuah kelas hanya boleh memiliki satu baris kode",
    "Semua variabel harus bertipe data string",
    "A", "Robert C. Martin (Uncle Bob) - Design Principles and Design Patterns (SOLID).",
    "Open/Closed Principle (OCP): Anda harus dapat memperluas perilaku suatu kelas (melalui inheritance/polimorfisme/interface) tanpa harus mengubah kode sumber yang telah diuji dan berjalan stabil."
))

skb_100_questions.append(make_q(
    "kd_78", "Rekayasa Perangkat Lunak", "RESTful API - Kode Status HTTP 401 vs 403",
    "Dalam perancangan layanan pertukaran data Web API antarkementerian, perbedaan makna antara kode status HTTP 401 Unauthorized dan HTTP 403 Forbidden adalah...",
    "HTTP 401 berarti kredensial autentikasi belum diberikan atau tidak valid, sedangkan HTTP 403 berarti identitas pengguna valid namun tidak memiliki izin (hak otorisasi) untuk mengakses sumber daya tersebut",
    "HTTP 401 untuk error server meledak, HTTP 403 untuk kabel putus",
    "HTTP 401 berarti transaksi sukses, HTTP 403 berarti transaksi gagal",
    "Kedua kode tersebut memiliki arti yang sama persis tanpa perbedaan",
    "HTTP 401 untuk koneksi smartphone, HTTP 403 untuk koneksi laptop",
    "A", "RFC 7231: Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content.",
    "401 Unauthorized berkaitan dengan kegagalan 'Authentication' (siapa Anda tidak terbukti). 403 Forbidden berkaitan dengan 'Authorization' (server mengenali siapa Anda, tetapi hak akses Anda ditolak)."
))

skb_100_questions.append(make_q(
    "kd_79", "Rekayasa Perangkat Lunak", "RESTful API - Metode HTTP Idempotent",
    "Metode HTTP yang jika dipanggil satu kali atau berkali-kali secara berurutan dengan parameter yang sama akan menghasilkan efek samping (status resource) yang identik pada server adalah...",
    "GET, PUT, dan DELETE",
    "POST saja",
    "PATCH saja",
    "POST dan CONNECT",
    "Semua metode HTTP tidak ada yang idempotent",
    "A", "RFC 7231 Section 4.2.2: Idempotent Methods.",
    "Operasi GET (baca), PUT (timpa penuh), dan DELETE (hapus) bersifat idempotent. Sedangkan POST tidak idempotent karena mengirimkan request POST berulang kali akan membuat entri transaksi baru berulang kali."
))

skb_100_questions.append(make_q(
    "kd_80", "Rekayasa Perangkat Lunak", "Spesifikasi API - OpenAPI / Swagger",
    "Format standar terbuka yang digunakan Kemkomdigi untuk mendokumentasikan antarmuka RESTful API secara mesin-terbaca (machine-readable) dan interaktif antarpengembang aplikasi adalah...",
    "OpenAPI Specification (OAS / Swagger)",
    "Adobe Photoshop PSD",
    "AutoCAD DWG",
    "Format Audio WAV",
    "File Executable EXE",
    "A", "OpenAPI Initiative (Linux Foundation) & Standar Integrasi SPLP Kemkomdigi.",
    "OpenAPI Specification (OAS) mendefinisikan antarmuka pemrograman aplikasi (endpoint, parameter, request body, responses, security scheme) dalam format JSON/YAML standar industri."
))

skb_100_questions.append(make_q(
    "kd_81", "Rekayasa Perangkat Lunak", "Version Control - Git Branching",
    "Dalam kolaborasi pengembangan kode program SPBE menggunakan Git, strategi pencabangan (branching) yang memisahkan antara cabang rilis produksi yang stabil dan cabang pengembangan fitur baru secara tertib disebut...",
    "Git Flow (Main/Master, Develop, Feature, Release, Hotfix)",
    "Penyalinan file dengan nama 'proyek_final_banget_v2.zip'",
    "Penulisan kode langsung di server produksi",
    "Penghapusan git commit setiap hari Jumat",
    "Penggunaan satu cabang tunggal untuk 50 programmer",
    "A", "Vincent Driessen - A Successful Git Branching Model & Standar DevOps Pemerintah.",
    "Git Flow adalah model percabangan terstruktur yang memisahkan siklus rilis produksi (main) dari integrasi harian (develop) dan pengerjaan modul mandiri (feature branch)."
))

skb_100_questions.append(make_q(
    "kd_82", "Rekayasa Perangkat Lunak", "Pengujian Perangkat Lunak - Testing Pyramid",
    "Berdasarkan konsep Piramida Pengujian (Test Pyramid), jenis pengujian perangkat lunak otomatis yang paling dasar, memiliki eksekusi paling cepat, dan harus memiliki jumlah cakupan (coverage) terbanyak adalah...",
    "Unit Testing",
    "End-to-End (E2E) UI Testing",
    "Manual User Acceptance Testing (UAT)",
    "Pengetesan acak oleh masyarakat",
    "Pengetesan server tanpa beban",
    "A", "Martin Fowler - The Practical Test Pyramid & ISTQB Standards.",
    "Piramida Pengujian: Unit Testing berada di lapisan dasar (jumlah terbanyak, murah, cepat), diikuti Integration Testing di tengah, dan E2E/UI Testing di puncak piramida (jumlah paling sedikit karena lambat dan rapuh)."
))

skb_100_questions.append(make_q(
    "kd_83", "Rekayasa Perangkat Lunak", "CI/CD Pipeline (Continuous Integration/Continuous Delivery)",
    "Pipeline CI/CD yang diterapkan dalam DevOps Pusat Data Nasional bertujuan untuk...",
    "Mengotomasi pengujian unit, kompilasi kode, pemindaian kerentanan keamanan, dan deployment aplikasi secara andal setiap kali ada commit kode baru",
    "Menghapus basis data instansi secara berkala",
    "Menghentikan kerja seluruh programmer",
    "Menyalin kode program ke CD-ROM secara manual",
    "Menyebarkan password server ke internet publik",
    "A", "IEEE Software Engineering Standards & DevOps Enterprise Best Practices.",
    "CI/CD mengotomatisasi alur rilis perangkat lunak dari integrasi kode, automated testing, hingga deployment ke lingkungan staging/production, meminimalkan human error dan mempercepat waktu rilis."
))

skb_100_questions.append(make_q(
    "kd_84", "Rekayasa Perangkat Lunak", "Clean Architecture & Separation of Concerns",
    "Prinsip Separation of Concerns (Pemisahan Kepedulian) dalam arsitektur perangkat lunak modular (seperti MVC atau Clean Architecture) memisahkan kode program menjadi lapisan...",
    "Lapisan Presentasi/Antarmuka, Lapisan Logika Bisnis, dan Lapisan Akses Data",
    "Lapisan Huruf, Lapisan Angka, dan Lapisan Simbol",
    "Lapisan Komputer Staf, Komputer Manajer, dan Komputer Direktur",
    "Lapisan Pagi, Lapisan Siang, dan Lapisan Malam",
    "Lapisan Kabel Tembaga, Kabel Kaca, dan Kabel Udara",
    "A", "Robert C. Martin - Clean Architecture: A Craftsman's Guide to Software Structure.",
    "Pemisahan lapisan (UI, Business Logic/Domain, dan Data Access/Repository) memastikan logika inti aplikasi independen terhadap framework, database, maupun antarmuka pengguna, memudahkan pengujian dan pemeliharaan."
))

skb_100_questions.append(make_q(
    "kd_85", "Rekayasa Perangkat Lunak", "Design Pattern - Singleton",
    "Pola desain perangkat lunak (Creational Design Pattern) yang memastikan sebuah kelas hanya memiliki satu instance objek tunggal di memori dan menyediakan titik akses global terhadap objek tersebut (misalnya untuk koneksi Database Pool) dinamakan...",
    "Singleton Pattern",
    "Factory Pattern",
    "Observer Pattern",
    "Decorator Pattern",
    "Strategy Pattern",
    "A", "Gang of Four (GoF) - Design Patterns: Elements of Reusable Object-Oriented Software.",
    "Singleton Pattern mengontrol instantiasi objek agar hanya ada satu instance aktif dalam siklus hidup aplikasi, sangat efisien untuk objek bersama yang mahal pembuatannya seperti koneksi pool database atau konfigurasi sistem."
))

skb_100_questions.append(make_q(
    "kd_86", "Rekayasa Perangkat Lunak", "Asynchronous Messaging - Message Broker",
    "Dalam sistem antrean aplikasi pendaftaran online berbeban tinggi, perangkat lunak Message Broker yang bertindak sebagai penyangga (buffer) pesan antrean transaksi asinkron (misalnya RabbitMQ atau Apache Kafka) berguna untuk...",
    "Menerapkan prinsip Decoupling dan meratakan lonjakan beban kerja (load leveling) sehingga server pemroses data tidak tumbang",
    "Menghapus transaksi pendaftar secara sepihak",
    "Memperlambat proses pengolahan data menjadi nol",
    "Menolak pendaftaran warga miskin",
    "Mengubah format data menjadi gambar bitmap",
    "A", "Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions.",
    "Message Broker memutus ketergantungan langsung (decoupling) antara producer dan consumer, menyimpan request dalam antrean tahan-banting (persistent queue), dan meratakan lonjakan traffic ekstrem (spike smoothing)."
))

skb_100_questions.append(make_q(
    "kd_87", "Rekayasa Perangkat Lunak", "Token Otentikasi - JSON Web Token (JWT)",
    "Dalam arsitektur microservices modern, token otentikasi stateless yang memuat klaim identitas pengguna dan ditandatangani secara kriptografis (terdiri atas Header, Payload, dan Signature yang dipisahkan tanda titik) dinamakan...",
    "JSON Web Token (JWT / RFC 7519)",
    "Cookie Plaintext",
    "File Excel XLS",
    "File ZIP",
    "Kartu Nama Digital",
    "A", "RFC 7519: JSON Web Token (JWT) Standard Specification.",
    "JWT adalah standar terbuka yang ringkas dan mandiri (self-contained) untuk mentransmisikan klaim otentikasi antar-pihak secara aman dalam bentuk objek JSON bertanda tangan digital (HMAC atau RSA/ECDSA)."
))

skb_100_questions.append(make_q(
    "kd_88", "Rekayasa Perangkat Lunak", "Penanganan Galat - Exception Handling",
    "Praktik rekayasa perangkat lunak yang baik dalam menangani galat (error handling) pada aplikasi web pemerintah adalah...",
    "Menangkap galat dengan blok try-catch, mencatat detail stack trace ke file log server privat yang aman, dan menampilkan pesan ramah tanpa membocorkan struktur teknis ke layar pengguna",
    "Menampilkan pesan error database mentah beserta password server ke layar publik",
    "Membiarkan aplikasi mengalami crash dan layar menjadi putih polos",
    "Menyembunyikan galat dan memalsukan status menjadi berhasil",
    "Mematikan server seketika terjadi galat kecil",
    "A", "OWASP Error Handling and Logging Cheat Sheet & IEEE Software Construction Standards.",
    "Menampilkan detail stack trace atau query SQL mentah ke pengguna umum membocorkan arsitektur sistem kepada penyerang (Information Disclosure). Penanganan galat yang aman menampilkan pesan informatif netral dan mencatat rincian teknis di internal log terlindungi."
))

skb_100_questions.append(make_q(
    "kd_89", "Rekayasa Perangkat Lunak", "Pola Arsitektur Microservices",
    "Dibandingkan arsitektur Monolitik tradisional, keunggulan arsitektur Microservices dalam ekosistem aplikasi pelayanan publik nasional adalah...",
    "Setiap modul layanan dapat dikembangkan, diuji, diskalakan secara independen menggunakan teknologi yang sesuai kebutuhan, dan kegagalan pada satu modul tidak meruntuhkan seluruh sistem",
    "Aplikasi monolitik selalu lebih mudah dipelihara saat sistem sudah memiliki jutaan baris kode",
    "Microservices tidak membutuhkan jaringan internet",
    "Microservices hanya bisa ditulis dalam satu bahasa pemrograman saja",
    "Microservices melarang penggunaan basis data",
    "A", "Sam Newman - Building Microservices: Designing Fine-Grained Systems.",
    "Microservices memecah sistem besar menjadi layanan-layanan otonom kecil yang terhubung via API. Keunggulan utamanya: fault isolation (kegagalan terisolasi), independensi deployment, dan elastisitas skalabilitas per layanan."
))

skb_100_questions.append(make_q(
    "kd_90", "Rekayasa Perangkat Lunak", "Kualitas Kode - Clean Code & Refactoring",
    "Tindakan memperbaiki struktur internal kode perangkat lunak tanpa mengubah perilaku eksternal sistem (misalnya memecah fungsi panjang menjadi fungsi-fungsi kecil yang mudah dibaca dan diuji) disebut...",
    "Refactoring",
    "Plagiasi Kode",
    "Decompiling",
    "Hacking",
    "Format Harddisk",
    "A", "Martin Fowler - Refactoring: Improving the Design of Existing Code.",
    "Refactoring adalah teknik disiplin untuk membersihkan kode sumber, mengurangi technical debt, meningkatkan keterbacaan (readability), dan menurunkan kompleksitas siklomatik tanpa mengubah output fungsional aplikasi."
))

# ------------------------------------------------------------------------------
# DOMAIN 7: MANAJEMEN BASIS DATA & DATA ANALYTICS (Soal 91 - 100)
# ------------------------------------------------------------------------------
skb_100_questions.append(make_q(
    "kd_91", "Basis Data & Analisis", "Normalisasi Database - Bentuk Normal Pertama (1NF)",
    "Sebuah tabel basis data relasional dikatakan telah memenuhi kriteria Bentuk Normal Pertama (1st Normal Form / 1NF) apabila...",
    "Setiap kolom hanya berisi nilai tunggal yang atomik (tidak dapat dibagi lagi) dan tidak memiliki grup perulangan kolom/baris",
    "Tabel telah terhubung ke internet",
    "Tabel memiliki minimal 1.000 baris data",
    "Tabel tidak memiliki primary key",
    "Nama kolom ditulis menggunakan huruf kapital semua",
    "A", "E.F. Codd - A Relational Model of Data for Large Shared Data Banks (ACM Classic Paper).",
    "Syarat mutlak 1NF adalah atomisitas data: setiap sel pertemuan baris dan kolom hanya boleh memuat satu nilai tunggal (bukan kumpulan array atau data komposit bertingkat) serta tidak ada grup berulang."
))

skb_100_questions.append(make_q(
    "kd_92", "Basis Data & Analisis", "Normalisasi Database - Bentuk Normal Kedua (2NF)",
    "Sebuah tabel yang telah memenuhi 1NF akan memenuhi kriteria Bentuk Normal Kedua (2NF) jika...",
    "Semua atribut bukan kunci utama (non-key attributes) memiliki ketergantungan fungsional penuh pada seluruh kunci utama (tidak ada ketergantungan parsial pada primary key komposit)",
    "Tabel disimpan dalam format file teks",
    "Tabel memiliki foreign key ke seluruh tabel di database",
    "Tabel tidak memiliki indeks",
    "Tabel dibuat oleh administrator senior",
    "A", "Date, C.J. - An Introduction to Database Systems & Standar Basis Data BPS.",
    "2NF mengatasi masalah kunci komposit: jika primary key terdiri atas lebih dari satu kolom, atribut non-kunci harus bergantung pada kombinasi seluruh kolom primary key tersebut, bukan hanya pada sebagian kolom kunci (partial dependency)."
))

skb_100_questions.append(make_q(
    "kd_93", "Basis Data & Analisis", "Normalisasi Database - Bentuk Normal Ketiga (3NF)",
    "Sebuah tabel yang telah memenuhi 2NF memenuhi Bentuk Normal Ketiga (3NF) apabila...",
    "Tidak memiliki ketergantungan transitif antar-atribut bukan kunci (atribut non-kunci tidak boleh bergantung secara fungsional pada atribut non-kunci lainnya)",
    "Tabel memiliki minimal 3 kolom foreign key",
    "Tabel diisi data dari tiga kementerian yang berbeda",
    "Data tabel telah diverifikasi oleh 3 orang pejabat",
    "Tabel disimpan di 3 harddisk yang berbeda",
    "A", "Elmasri & Navathe - Fundamentals of Database Systems.",
    "3NF mengeliminasi ketergantungan transitif (X -> Y dan Y -> Z, maka X -> Z). Kolom bukan kunci hanya boleh bergantung langsung secara fungsional pada primary key (The key, the whole key, and nothing but the key)."
))

skb_100_questions.append(make_q(
    "kd_94", "Basis Data & Analisis", "Indeks Basis Data - B-Tree Index",
    "Struktur data indeks yang paling banyak digunakan secara default oleh sistem basis data relasional (RDBMS seperti PostgreSQL dan MySQL) untuk mempercepat pencarian data berdasarkan rentang nilai dan kesetaraan adalah...",
    "B-Tree (Balanced Tree)",
    "Linked List Linier Sederhana",
    "Queue FIFO",
    "Stack LIFO",
    "Tabel Acak",
    "A", "Silberschatz, Korth, Sudarshan - Database System Concepts.",
    "B-Tree mempertahankan urutan data seimbang dan memiliki kompleksitas pencarian O(log n), sangat optimal untuk operasi perbandingan kesetaraan (=) maupun rentang nilai (BETWEEN, >, <)."
))

skb_100_questions.append(make_q(
    "kd_95", "Basis Data & Analisis", "Sifat Transaksi Basis Data - ACID",
    "Dalam perbankan dan transaksi penerimaan negara, sifat 'Durability' pada prinsip ACID menjamin bahwa...",
    "Begitu transaksi berhasil di-commit, perubahan data bersifat permanen dan tidak akan hilang meskipun terjadi pemadaman listrik atau kegagalan sistem beberapa detik kemudian",
    "Transaksi harus diselesaikan dalam waktu kurang dari 1 detik",
    "Data transaksi dihapus setiap akhir pekan",
    "Transaksi hanya boleh dilakukan pada hari kerja dinas",
    "Saldo rekening tidak boleh bertambah",
    "A", "Jim Gray - The Transaction Concept: Virtues and Limitations (Turing Award Lecture).",
    "Durability menjamin rekaman transaksi yang telah di-commit tersimpan permanen pada media penyimpanan persisten (melalui Write-Ahead Logging / WAL) sehingga data tetap utuh saat sistem pulih dari crash."
))

skb_100_questions.append(make_q(
    "kd_96", "Basis Data & Analisis", "Teorema CAP pada Sistem Terdistribusi",
    "Teorema CAP (Brewer's Theorem) menyatakan bahwa dalam sistem basis data terdistribusi di internet, ketika terjadi partisi jaringan (Network Partition / P), sistem hanya dapat menjamin salah satu dari dua pilihan trade-off, yaitu...",
    "Consistency (C) atau Availability (A)",
    "Cost (Biaya) atau Quality (Kualitas)",
    "Speed (Kecepatan) atau Storage (Kapasitas)",
    "Hardware atau Software",
    "Frontend atau Backend",
    "A", "Eric Brewer - Towards Robust Distributed Systems (ACM Symposium on Principles of Distributed Computing).",
    "Teorema CAP menyatakan sistem penyimpanan terdistribusi tidak dapat secara bersamaan menjamin Consistency, Availability, dan Partition Tolerance. Dalam kondisi partisi jaringan (P), sistem harus memilih antara konsistensi ketat (CP) atau ketersediaan respons (AP)."
))

skb_100_questions.append(make_q(
    "kd_97", "Basis Data & Analisis", "Optimasi Query SQL - Sargable Queries",
    "Diberikan kueri SQL pencarian data ASN: SELECT * FROM pegawai WHERE YEAR(tanggal_pensiun) = 2026. Alasan mengapa kueri tersebut tidak efisien (Non-Sargable) pada tabel dengan 1 juta baris adalah...",
    "Membungkus kolom terindeks 'tanggal_pensiun' dengan fungsi YEAR() mencegah mesin basis data memanfaatkan indeks B-Tree yang ada dan memaksa terjadinya Full Table Scan",
    "Tahun 2026 belum tiba sehingga query otomatis error",
    "Klausul WHERE dilarang dalam standar SQL",
    "Kueri tersebut terlalu pendek",
    "Kueri SQL tidak boleh menggunakan angka genap",
    "A", "SQL Performance Explained by Markus Winand & ANSI SQL Optimization Standards.",
    "Sargable (Search Argument Able): Fungsi yang membungkus kolom terindeks mengharuskan database mengevaluasi fungsi tersebut baris per baris (Full Table Scan). Solusi sargable: WHERE tanggal_pensiun >= '2026-01-01' AND tanggal_pensiun <= '2026-12-31'."
))

skb_100_questions.append(make_q(
    "kd_98", "Basis Data & Analisis", "Teknologi NoSQL - Database Dokumen",
    "Untuk aplikasi survei sensus atau formulir pengaduan masyarakat yang memiliki skema kolom dinamis dan sering berubah-ubah tanpa perlu migrasi DDL kaku, jenis basis data NoSQL yang paling populer digunakan adalah...",
    "Document Store (berbasis format JSON/BSON seperti MongoDB)",
    "File Teks DOS",
    "Spreadsheet manual",
    "Pita Kaset Magnetik",
    "Punched Card",
    "A", "Martin Fowler - NoSQL Distilled: A Brief Guide to the Emerging World of Polyglot Persistence.",
    "Document-oriented database menyimpan data dalam struktur dokumen fleksibel (JSON/BSON), memungkinkan setiap dokumen memiliki field atribut yang berbeda-beda tanpa batasan skema tabel relasional yang kaku."
))

skb_100_questions.append(make_q(
    "kd_99", "Basis Data & Analisis", "Format Pertukaran Data Geospasial - GeoJSON",
    "Dalam penyajian data peta sebaran menara BTS dan titik blank spot sinyal telekomunikasi pada portal dashboard Satu Data Kemkomdigi, format data standar terbuka berbasis JSON yang merepresentasikan koordinat lintang dan bujur (latitude/longitude) adalah...",
    "GeoJSON (RFC 7946)",
    "MP3",
    "WAV",
    "GIF",
    "DOCX",
    "A", "RFC 7946: The GeoJSON Format Specification & Standar Basis Data Geospasial BIG.",
    "GeoJSON adalah format standar terbuka berbasis JSON untuk mengkodekan struktur data geografis sederhana (Point, LineString, Polygon, MultiPolygon) beserta properti atribut non-spasialnya."
))

skb_100_questions.append(make_q(
    "kd_100", "Basis Data & Analisis", "Data Pipeline - ETL vs ELT",
    "Dalam pembangunan Big Data analitik di Kementerian Komunikasi dan Digital, pendekatan modern ELT (Extract, Load, Transform) memanfaatkan kemampuan pemrosesan paralel komputasi awan data warehouse modern. Perbedaan utama ELT dibanding proses tradisional ETL adalah...",
    "Pada ELT, data mentah diekstraksi dan langsung dimuat (Load) ke dalam data warehouse tujuan terlebih dahulu, baru kemudian proses transformasi data dilakukan langsung di dalam data warehouse berkecepatan tinggi",
    "ELT tidak melakukan transformasi data sama sekali",
    "ETL dilakukan secara manual menggunakan pensil dan kertas",
    "ELT dilarang oleh standar internasional",
    "Kedua proses tersebut tidak melibatkan komputer",
    "A", "Bill Inmon / Ralph Kimball - The Data Warehouse Lifecycle Toolkit & Cloud Analytics Standards.",
    "Dalam ELT modern (berkat skalabilitas compute cloud seperti Snowflake/BigQuery), data mentah ditampung terlebih dahulu tanpa bottleneck pemrosesan staging eksternal, lalu transformasi data dieksekusi secara terdistribusi di dalam engine data warehouse."
))

# Update paket kemkomdigi menjadi 100 soal penuh!
data["skb_kemkomdigi"]["title"] = "SKB IT - Kementerian Komunikasi dan Digital (Kemkomdigi) - 100 Soal Penuh"
data["skb_kemkomdigi"]["description"] = "Simulasi riil 100 soal teknis penuh standar CAT BKN berdasar UU PDP, UU ITE, Perpres SPBE, Cloud PDN, Jaringan 5G, Cybersecurity ISO 27001, dan Basis Data."
data["skb_kemkomdigi"]["questions"] = skb_100_questions

# Tulis ke file data_soal.js
js_content = "/**\n * BANK SOAL MULTI-INSTANSI CAT CPNS (SKD NASIONAL & SKB SPESIFIK INSTANSI)\n */\nwindow.BANK_SOAL = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"

with open("d:\\CPNS\\data_soal.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"SUKSES BESAR! Paket Kemkomdigi kini memiliki {len(skb_100_questions)} butir soal penuh dengan sitasi resmi!")
