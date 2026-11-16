import json

# ==========================================
# GENERATOR BANK SOAL RESMI CAT BKN
# 110 SOAL SKD:
# - TWK : 30 Soal (No. 1 - 30)
# - TIU : 35 Soal (No. 31 - 65)
# - TKP : 45 Soal (No. 66 - 110)
# ==========================================

twk_questions = [
  # 1-6: Pancasila & Nilai-Nilai
  {
    "id": "twk_1", "category": "TWK", "subcategory": "Pilar Negara - Pancasila",
    "question": "Di tengah pesatnya perkembangan media sosial, polarisasi dan ujaran kebencian berbasis SARA kerap memicu konflik horizontal di masyarakat. Sikap seorang warga negara yang mengedepankan musyawarah mufakat serta menghormati perbedaan keyakinan merupakan wujud integrasi pengamalan Pancasila, khususnya keterkaitan antara...",
    "options": {
      "A": "Sila ke-1, Sila ke-3, dan Sila ke-4",
      "B": "Sila ke-2, Sila ke-4, dan Sila ke-5",
      "C": "Sila ke-1 dan Sila ke-2 saja",
      "D": "Sila ke-3 dan Sila ke-5 saja",
      "E": "Sila ke-2 dan Sila ke-3 saja"
    },
    "answer": "A",
    "explanation": "Menghormati keragaman keyakinan (Sila 1), merawat persatuan dan mencegah disintegrasi (Sila 3), serta mengedepankan musyawarah mufakat (Sila 4) merupakan keterkaitan utuh tiga sila tersebut."
  },
  {
    "id": "twk_2", "category": "TWK", "subcategory": "Pilar Negara - Pancasila",
    "question": "Seorang bupati menolak izin pendirian pabrik semen yang berpotensi merusak sumber mata air warga adat dan mencemari lingkungan persawahan, kendati pabrik tersebut menjanjikan pendapatan asli daerah (PAD) yang tinggi. Kebijakan bupati tersebut mencerminkan keadilan sosial bagi seluruh rakyat Indonesia yang berpijak pada nilai kemanusiaan, yaitu keterkaitan...",
    "options": {
      "A": "Sila ke-2 dan Sila ke-5",
      "B": "Sila ke-1 dan Sila ke-3",
      "C": "Sila ke-3 dan Sila ke-4",
      "D": "Sila ke-4 dan Sila ke-1",
      "E": "Sila ke-1 dan Sila ke-5"
    },
    "answer": "A",
    "explanation": "Melindungi hak hidup warga dan kelestarian lingkungan merupakan wujud memanusiakan manusia (Sila ke-2) demi mewujudkan keadilan sosial dan kesejahteraan bersama (Sila ke-5)."
  },
  {
    "id": "twk_3", "category": "TWK", "subcategory": "Pilar Negara - Pancasila",
    "question": "Pancasila sebagai ideologi terbuka memiliki dimensi fleksibilitas, realitas, dan idealisme. Makna dari dimensi realitas dalam ideologi Pancasila adalah...",
    "options": {
      "A": "Pancasila memiliki cita-cita yang abstrak dan sulit dijangkau realitas zaman",
      "B": "Nilai-nilai dasar Pancasila bersumber dan berakar langsung dari nilai-nilai riil yang hidup dalam masyarakat Indonesia",
      "C": "Pancasila dapat diubah kapan saja sesuai keinginan mayoritas penguasa politik",
      "D": "Pancasila menolak perkembangan ilmu pengetahuan modern dari dunia barat",
      "E": "Pancasila bersifat tertutup terhadap interpretasi baru dalam perkembangan peradaban"
    },
    "answer": "B",
    "explanation": "Dimensi realitas berarti nilai-nilai dasar yang terkandung dalam ideologi bersumber, berakar, dan hidup dalam masyarakat Indonesia secara nyata, bukan rekaan imajinatif belaka."
  },
  {
    "id": "twk_4", "category": "TWK", "subcategory": "Pilar Negara - Pancasila",
    "question": "Gotong royong membersihkan saluran air dan memperbaiki jembatan desa yang rusak pascabencana secara swadaya oleh warga masyarakat merupakan contoh nyata pengamalan nilai Pancasila pada tingkat...",
    "options": {
      "A": "Nilai Instrumental",
      "B": "Nilai Praktis",
      "C": "Nilai Dasar",
      "D": "Nilai Filosofis",
      "E": "Nilai Yuridis"
    },
    "answer": "B",
    "explanation": "Nilai praktis adalah realisasi nilai-nilai Pancasila dalam tindakan nyata kehidupan sehari-hari masyarakat (seperti gotong royong langsung di lapangan)."
  },
  {
    "id": "twk_5", "category": "TWK", "subcategory": "Pilar Negara - Pancasila",
    "question": "Rumusan sila pertama Pancasila dalam Piagam Jakarta mengalami perubahan pada 18 Agustus 1945 melalui kesepakatan para pendiri bangsa yang diprakarsai oleh Mohammad Hatta. Nilai keteladanan tertinggi dari peristiwa historis tersebut adalah...",
    "options": {
      "A": "Keinginan mengesampingkan hukum formal demi kekuasaan",
      "B": "Jiwa kenegarawanan, lapang dada, dan mengutamakan persatuan bangsa di atas kepentingan golongan",
      "C": "Dominasi kelompok mayoritas atas kelompok minoritas dalam perumusan dasar negara",
      "D": "Kepatuhan mutlak terhadap perintah otoritas militer Jepang",
      "E": "Kompromi politik sesaat demi memenangkan pemilihan presiden"
    },
    "answer": "B",
    "explanation": "Kesediaan para tokoh bangsa mengubah frasa tujuh kata dalam Piagam Jakarta demi keutuhan NKRI adalah bukti jiwa kenegarawanan sejati yang mendahulukan persatuan bangsa."
  },
  {
    "id": "twk_6", "category": "TWK", "subcategory": "Pilar Negara - Pancasila",
    "question": "Penetapan upah minimum yang adil dan penyediaan jaminan kesehatan nasional bagi pekerja rentan oleh pemerintah merupakan perwujudan konkret dari sila ke-...",
    "options": {
      "A": "Satu",
      "B": "Dua",
      "C": "Tiga",
      "D": "Empat",
      "E": "Lima"
    },
    "answer": "E",
    "explanation": "Jaminan sosial, keadilan upah, dan perlindungan kesejahteraan ekonomi bagi kaum pekerja adalah implementasi Sila Kelima: Keadilan Sosial bagi Seluruh Rakyat Indonesia."
  },

  # 7-12: UUD 1945 & Sistem Ketatanegaraan
  {
    "id": "twk_7", "category": "TWK", "subcategory": "Pilar Negara - UUD 1945",
    "question": "Menurut ketentuan Pasal 7B UUD NRI Tahun 1945 pasca-amandemen, lembaga negara yang berwenang memeriksa, mengadili, dan memutus pendapat DPR bahwa Presiden dan/atau Wakil Presiden telah melakukan pelanggaran hukum dalam proses pemakzulan (impeachment) adalah...",
    "options": {
      "A": "Mahkamah Konstitusi",
      "B": "Mahkamah Agung",
      "C": "Komisi Yudisial",
      "D": "Majelis Permusyawaratan Rakyat",
      "E": "Badan Pemeriksa Keuangan"
    },
    "answer": "A",
    "explanation": "Pasal 7B ayat (1) menyatakan bahwa usul pemberhentian Presiden/Wakil Presiden dapat diajukan oleh DPR kepada MPR setelah terlebih dahulu mengajukan permintaan kepada Mahkamah Konstitusi untuk memeriksa, mengadili, dan memutus pendapat DPR tersebut."
  },
  {
    "id": "twk_8", "category": "TWK", "subcategory": "Pilar Negara - UUD 1945",
    "question": "Berdasarkan Pasal 1 ayat (3) UUD 1945, Indonesia adalah negara hukum (rechtsstaat). Salah satu ciri fundamental negara hukum modern menurut prinsip konstitusionalisme adalah...",
    "options": {
      "A": "Pemusatan seluruh wewenang penegakan hukum di tangan presiden tanpa pengawasan",
      "B": "Adanya pemisahan/pembagian kekuasaan (checks and balances) dan jaminan peradilan yang bebas serta tidak memihak",
      "C": "Hukum dibuat secara tertutup oleh lembaga keamanan negara",
      "D": "Ketetapan penguasa berkedudukan lebih tinggi daripada undang-undang dasar",
      "E": "Tidak diakuinya hak asasi manusia bagi pihak oposisi pemerintah"
    },
    "answer": "B",
    "explanation": "Prinsip negara hukum menuntut adanya supremasi hukum, pemisahan kekuasaan (checks and balances), jaminan HAM, dan lembaga peradilan yang merdeka."
  },
  {
    "id": "twk_9", "category": "TWK", "subcategory": "Pilar Negara - UUD 1945",
    "question": "Pasal 27 ayat (3) UUD 1945 menyatakan bahwa 'Setiap warga negara berhak dan wajib ikut serta dalam upaya pembelaan negara'. Konsekuensi yuridis dari penggunaan kata 'berhak dan wajib' adalah...",
    "options": {
      "A": "Bela negara hanya bersifat anjuran moral sukarela tanpa landasan sanksi",
      "B": "Bela negara adalah kehormatan sekaligus kewajiban konstitusional bagi setiap warga negara tanpa kecuali",
      "C": "Hanya anggota TNI dan Polri yang memiliki kewajiban membela negara",
      "D": "Warga negara boleh menolak membela negara jika tidak berminat menjadi tentara",
      "E": "Kewajiban bela negara gugur saat seseorang telah membayar pajak penghasilan"
    },
    "answer": "B",
    "explanation": "Kata 'berhak dan wajib' menunjukkan bahwa bela negara adalah hak asasi sekaligus kewajiban hukum yang mengikat setiap warga negara Republik Indonesia."
  },
  {
    "id": "twk_10", "category": "TWK", "subcategory": "Pilar Negara - UUD 1945",
    "question": "Sesuai Pasal 23E UUD 1945, penyerahan hasil pemeriksaan atas pengelolaan dan tanggung jawab tentang keuangan negara oleh BPK dilakukan kepada...",
    "options": {
      "A": "DPR, DPD, dan DPRD sesuai dengan kewenangannya",
      "B": "Presiden dan Wakil Presiden saja",
      "C": "Menteri Keuangan Republik Indonesia",
      "D": "Mahkamah Konstitusi dan Mahkamah Agung",
      "E": "Komisi Pemberantasan Korupsi dan Kejaksaan Agung"
    },
    "answer": "A",
    "explanation": "Pasal 23E ayat (2) UUD 1945 berbunyi: 'Hasil pemeriksaan keuangan negara diserahkan kepada Dewan Perwakilan Rakyat, Dewan Perwakilan Daerah, dan Dewan Perwakilan Rakyat Daerah, sesuai dengan kewenangannya'."
  },
  {
    "id": "twk_11", "category": "TWK", "subcategory": "Pilar Negara - UUD 1945",
    "question": "Pokok pikiran keempat Pembukaan UUD 1945 berbunyi: 'Negara berdasar atas Ketuhanan Yang Maha Esa, menurut dasar kemanusiaan yang adil dan beradab'. Pokok pikiran ini mewajibkan pemerintah dan penyelenggara negara untuk...",
    "options": {
      "A": "Menjadikan salah satu ajaran agama sebagai satu-satunya hukum positif negara",
      "B": "Memelihara budi pekerti kemanusiaan yang luhur dan memegang teguh cita-cita moral rakyat yang luhur",
      "C": "Menghapus pengawasan publik terhadap kebijakan aparatur sipil negara",
      "D": "Membatasi kebebasan berpendapat demi ketertiban ekonomi sepihak",
      "E": "Menyerahkan seluruh pengelolaan sumber daya alam kepada konglomerat"
    },
    "answer": "B",
    "explanation": "Penjelasan UUD 1945 menegaskan bahwa pokok pikiran keempat mewajibkan pemerintah dan penyelenggara negara lainnya untuk memelihara budi pekerti kemanusiaan yang luhur dan memegang teguh cita-cita moral rakyat yang luhur."
  },
  {
    "id": "twk_12", "category": "TWK", "subcategory": "Pilar Negara - UUD 1945",
    "question": "Kewenangan Mahkamah Konstitusi yang diatur dalam Pasal 24C Ayat (1) UUD 1945 meliputi empat hal, KECUALI...",
    "options": {
      "A": "Menguji undang-undang terhadap UUD 1945",
      "B": "Memutus sengketa kewenangan lembaga negara yang kewenangannya diberikan oleh UUD",
      "C": "Memutus pembubaran partai politik",
      "D": "Menguji peraturan perundang-undangan di bawah undang-undang terhadap undang-undang",
      "E": "Memutus perselisihan tentang hasil pemilihan umum"
    },
    "answer": "D",
    "explanation": "Menguji peraturan perundang-undangan di bawah UU terhadap UU adalah kewenangan Mahkamah Agung (MA) berdasarkan Pasal 24A ayat (1), bukan kewenangan Mahkamah Konstitusi (MK)."
  },

  # 13-18: Integritas & Anti Korupsi
  {
    "id": "twk_13", "category": "TWK", "subcategory": "Integritas",
    "question": "Seorang petugas layanan perizinan di sebuah instansi menolak uang terima kasih dalam amplop yang diselipkan pemohon setelah sertifikat izin selesai diterbitkan sesuai SOP dan bebas biaya. Alasan etis penolakan tersebut menurut UU Pemberantasan Tindak Pidana Korupsi adalah...",
    "options": {
      "A": "Pemberian tersebut masuk kategori gratifikasi yang berpotensi menjadi bibit suap dan merusak objektivitas layanan publik",
      "B": "Jumlah uang yang diberikan dinilai terlalu sedikit bagi petugas",
      "C": "Uang tersebut tidak disertai kwitansi resmi yang dicap kelurahan",
      "D": "Petugas takut tertangkap kamera pengintai yang sedang menyala",
      "E": "Pemberian baru diperbolehkan jika pemohon izin adalah sanak keluarga sendiri"
    },
    "answer": "A",
    "explanation": "Berdasarkan Pasal 12B UU No. 20/2001, setiap gratifikasi kepada pegawai negeri atau penyelenggara negara dianggap suap apabila berhubungan dengan jabatannya dan berlawanan dengan kewajibannya."
  },
  {
    "id": "twk_14", "category": "TWK", "subcategory": "Integritas",
    "question": "KPK merumuskan 9 nilai integritas antikorupsi yang terbagi dalam 3 rumpun: Inti, Sikap, dan Etos Kerja. Yang termasuk ke dalam rumpun nilai INTI adalah...",
    "options": {
      "A": "Jujur, Tanggung Jawab, Disiplin",
      "B": "Berani, Peduli, Adil",
      "C": "Kerja Keras, Sederhana, Mandiri",
      "D": "Gotong Royong, Sabar, Tekun",
      "E": "Loyal, Tanggap, Profesional"
    },
    "answer": "A",
    "explanation": "9 Nilai Integritas KPK:\n1. Inti: Jujur, Tanggung jawab, Disiplin (Jumat Bersepeda KK).\n2. Sikap: Adil, Berani, Peduli.\n3. Etos Kerja: Kerja keras, Mandiri, Sederhana."
  },
  {
    "id": "twk_15", "category": "TWK", "subcategory": "Integritas",
    "question": "Seorang pegawai instansi memanfaatkan mobil dinas operasional kantor untuk keperluan mudik liburan hari raya bersama keluarga pribadinya. Perbuatan tersebut merupakan pelanggaran terhadap nilai integritas...",
    "options": {
      "A": "Tanggung jawab dan kesederhanaan penggunaan fasilitas negara",
      "B": "Keberanian menyampaikan pendapat di publik",
      "C": "Kemandirian dalam menjalankan tugas dinas",
      "D": "Kerja keras meningkatkan output organisasi",
      "E": "Keadilan dalam melayani sesama rekan kerja"
    },
    "answer": "A",
    "explanation": "Menggunakan fasilitas kedinasan untuk kepentingan pribadi merupakan bentuk penyalahgunaan sarana dan prasarana negara, mencerminkan hilangnya tanggung jawab dan ketidakpatuhan pada etika pemanfaatan aset publik."
  },
  {
    "id": "twk_16", "category": "TWK", "subcategory": "Integritas",
    "question": "Konflik kepentingan (conflict of interest) dalam birokrasi pemerintahan adalah kondisi di mana seorang pejabat negara...",
    "options": {
      "A": "Memiliki perbedaan pendapat intelektual dengan atasannya terkait perumusan regulasi",
      "B": "Memiliki kepentingan pribadi/bisnis/keluarga yang berpotensi mempengaruhi netralitas dan kualitas keputusannya dalam menjalankan jabatan kedinasan",
      "C": "Menghadapi beban kerja yang terlalu banyak dalam kurun waktu yang singkat",
      "D": "Melakukan rotasi mutasi pegawai secara berkala sesuai kompetensi",
      "E": "Menolak perintah atasan yang bertentangan dengan hukum"
    },
    "answer": "B",
    "explanation": "Konflik kepentingan adalah situasi di mana penyelenggara negara memiliki atau patut diduga memiliki kepentingan pribadi terhadap setiap penggunaan wewenang sehingga dapat mempengaruhi kualitas dan kinerja keputusannya."
  },
  {
    "id": "twk_17", "category": "TWK", "subcategory": "Integritas",
    "question": "Whistleblowing System (WBS) yang diterapkan di berbagai kementerian dan lembaga negara bertujuan untuk...",
    "options": {
      "A": "Memata-matai kehidupan pribadi seluruh pegawai tanpa batasan",
      "B": "Menyediakan mekanisme pelaporan tindak pidana korupsi/pelanggaran etika secara aman, terlindungi, dan independen bagi pelapor",
      "C": "Menyebarluaskan rumor internal kantor ke media massa secara anonim",
      "D": "Menjatuhkan rekan kerja yang sedang bersaing dalam promosi jabatan",
      "E": "Mengurangi hak cuti tahunan pegawai yang sering terlambat"
    },
    "answer": "B",
    "explanation": "WBS adalah sistem pelaporan pelanggaran yang menjamin kerahasiaan identitas dan perlindungan bagi pelapor demi mendeteksi kecurangan/korupsi sejak dini dalam organisasi."
  },
  {
    "id": "twk_18", "category": "TWK", "subcategory": "Integritas",
    "question": "Dalam rangka reformasi birokrasi, predikat Wilayah Bebas dari Korupsi (WBK) diberikan kepada unit kerja instansi pemerintah yang telah berhasil membangun...",
    "options": {
      "A": "Gedung perkantoran megah dengan anggaran APBN terbesar",
      "B": "Zona Integritas (ZI) melalui pencegahan korupsi, reformasi birokrasi, dan peningkatan kualitas pelayanan publik secara nyata",
      "C": "Sistem penggajian tertinggi bagi para pejabat strukturalnya",
      "D": "Aturan yang melarang masyarakat mengajukan keluhan layanan",
      "E": "Platform media sosial dengan jumlah pengikut terbanyak"
    },
    "answer": "B",
    "explanation": "WBK adalah predikat yang diberikan kepada unit kerja yang memenuhi sebagian besar manajemen perubahan, penataan tatalaksana, penataan sistem SDM, penguatan pengawasan, dan penguatan akuntabilitas kinerja."
  },

  # 19-24: Nasionalisme & Bela Negara
  {
    "id": "twk_19", "category": "TWK", "subcategory": "Nasionalisme",
    "question": "Nasionalisme Indonesia bukanlah nasionalisme chauvinistik (sempit) yang memandang bangsanya paling unggul dan merendahkan bangsa lain, melainkan berakar pada kemanusiaan yang adil dan beradab. Konsep nasionalisme yang humanis ini sejalan dengan pandangan Presiden Soekarno yang menyatakan bahwa...",
    "options": {
      "A": "Nasionalisme kita harus menutup diri sepenuhnya dari pergaulan antarbangsa",
      "B": "Nasionalisme kita hidup dan tumbuh subur dalam tamansarinya internasionalisme (peri-kemanusiaan)",
      "C": "Kedaulatan negara hanya bisa dipertahankan melalui agresi militer ke luar negeri",
      "D": "Bangsa Indonesia harus menuntut ganti rugi perang dari seluruh negara penjajah",
      "E": "Kepentingan ekonomi global berada di atas kedaulatan hukum nasional"
    },
    "answer": "B",
    "explanation": "Bung Karno menegaskan bahwa nasionalisme Indonesia bukan 'chauvinisme' (menindas bangsa lain), melainkan nasionalisme yang tumbuh subur dalam tamansarinya internasionalisme (perikemanusiaan)."
  },
  {
    "id": "twk_20", "category": "TWK", "subcategory": "Bela Negara",
    "question": "Berdasarkan UU No. 23 Tahun 2019 tentang Pengelolaan Sumber Daya Nasional untuk Pertahanan Negara, 5 nilai dasar bela negara meliputi: cinta tanah air, sadar berbangsa dan bernegara, setia pada Pancasila, rela berkorban untuk bangsa dan negara, serta...",
    "options": {
      "A": "Memiliki kemampuan awal bela negara baik fisik maupun psikis",
      "B": "Mampu mengoperasikan senjata tempur modern",
      "C": "Memiliki kekayaan materi untuk disumbangkan ke kas negara",
      "D": "Memiliki garis keturunan pejuang kemerdekaan",
      "E": "Bersedia ditempatkan di luar wilayah Republik Indonesia"
    },
    "answer": "A",
    "explanation": "5 Nilai Dasar Bela Negara:\n1. Cinta tanah air\n2. Sadar berbangsa dan bernegara\n3. Setia pada Pancasila sebagai ideologi negara\n4. Rela berkorban untuk bangsa dan negara\n5. Memiliki kemampuan awal bela negara."
  },
  {
    "id": "twk_21", "category": "TWK", "subcategory": "Nasionalisme",
    "question": "Gerakan Bangga Buatan Indonesia (BBI) yang mendorong instansi pemerintah dan masyarakat memprioritaskan belanja produk dalam negeri dan UMKM merupakan wujud nasionalisme di bidang...",
    "options": {
      "A": "Politik dan diplomasi internasional",
      "B": "Ekonomi dan kedaulatan kemandirian bangsa",
      "C": "Militer dan pertahanan teritorial",
      "D": "Agama dan keyakinan spiritual",
      "E": "Sastra dan kesenian tradisional murni"
    },
    "answer": "B",
    "explanation": "Mengutamakan produk dalam negeri dan mendukung UMKM lokal adalah manifestasi nasionalisme ekonomi demi kedaulatan dan kemandirian bangsa dari ketergantungan impor."
  },
  {
    "id": "twk_22", "category": "TWK", "subcategory": "Bela Negara",
    "question": "Dalam konteks ancaman non-militer di era Revolusi Industri 4.0, peran ASN Pranata Komputer dalam membela negara diwujudkan melalui...",
    "options": {
      "A": "Menyerang sistem web swasta tanpa dasar hukum yang jelas",
      "B": "Menjaga kedaulatan data pemerintah, memperkuat keamanan siber infrastruktur vital, dan memastikan layanan publik digital berjalan tanpa gangguan",
      "C": "Menyebarluaskan data pribadi warga negara ke forum daring asing",
      "D": "Mematikan koneksi internet publik setiap terjadi aksi unjuk rasa",
      "E": "Menggunakan perangkat bajakan demi menghemat anggaran pengadaan"
    },
    "answer": "B",
    "explanation": "Ancaman siber terhadap kedaulatan data dan layanan publik digital merupakan salah satu ancaman pertahanan non-militer. Menjaganya adalah wujud pengabdian bela negara sesuai profesi IT."
  },
  {
    "id": "twk_23", "category": "TWK", "subcategory": "Nasionalisme",
    "question": "Kongres Pemuda II pada tanggal 27-28 Oktober 1928 melahirkan ikrar Sumpah Pemuda. Dampak paling mendasar dari Sumpah Pemuda bagi perjuangan pergerakan nasional bangsa Indonesia adalah...",
    "options": {
      "A": "Berakhirnya pendudukan militer kolonial Belanda seketika itu juga",
      "B": "Transformasi paradigma perjuangan dari yang semula bersifat kedaerahan (primordial) menuju persatuan kebangsaan yang utuh",
      "C": "Dibubarkannya seluruh organisasi kepemudaan di tanah air",
      "D": "Ditetapkannya mata uang rupiah sebagai satu-satunya alat pembayaran sah saat itu",
      "E": "Diresmikannya batas wilayah daratan Republik Indonesia"
    },
    "answer": "B",
    "explanation": "Sumpah Pemuda 1928 merupakan tonggak sejarah penting yang melebur sekat-sekat kedaerahan (Jong Java, Jong Sumatranen Bond, Jong Ambon, dll.) menjadi satu identitas: tumpah darah, bangsa, dan bahasa Indonesia."
  },
  {
    "id": "twk_24", "category": "TWK", "subcategory": "Bhinneka Tunggal Ika",
    "question": "Semboyan 'Bhinneka Tunggal Ika' berasal dari kitab Kakawin Sutasoma karangan Mpu Tantular pada masa Kerajaan Majapahit. Konsep filosofis awal dari semboyan tersebut mengajarkan tentang...",
    "options": {
      "A": "Keseragaman keyakinan yang dipaksakan oleh kerajaan",
      "B": "Kerukunan dan toleransi hidup berdampingan antara penganut Siwa dan Buddha yang berbeda keyakinan namun pada hakikatnya satu kebenaran",
      "C": "Pembagian wilayah kerajaan menjadi beberapa koloni otonom",
      "D": "Penguasaan jalur perdagangan laut di Selat Malaka",
      "E": "Kewajiban seluruh rakyat memeluk keyakinan raja yang berkuasa"
    },
    "answer": "B",
    "explanation": "Frasa 'Bhinneka Tunggal Ika tan hana dharma mangrwa' dalam Sutasoma bermakna berbeda-beda (antara agama Siwa dan Buddha) tetapi tetap satu jua, tidak ada kebenaran yang mendua, menjadi landasan toleransi."
  },

  # 25-30: Bahasa Indonesia Baku & Efektif
  {
    "id": "twk_25", "category": "TWK", "subcategory": "Bahasa Indonesia",
    "question": "Pilihlah kalimat yang menggunakan ragam bahasa baku dan memenuhi kaidah penulisan Ejaan Bahasa Indonesia yang Disempurnakan (EYD V):\n",
    "options": {
      "A": "Seluruh peserta seleksi di wajibkan membawa KTP asli dan kartu ujian.",
      "B": "Pemerintah sedang mengkoordinir pendistribusian logistik ke daerah bencana.",
      "C": "Hasil analisis laboratorium menunjukkan bahwa kualitas air minum di daerah tersebut memenuhi standar baku mutu.",
      "D": "Praktek korupsi, kolusi, dan nepotisme harus di berantas hingga ke akar-akarnya.",
      "E": "Ujian CAT di selenggarakan secara transparan demi untuk menjaga akuntabilitas kelulusan."
    },
    "answer": "C",
    "explanation": "Pilihan C baku. Pada A: 'di wajibkan' salah (seharusnya serangkai 'diwajibkan'). B: 'mengkoordinir' salah (baku: 'mengoordinasikan'). D: 'Praktek' salah (baku: 'Praktik') dan 'di berantas' salah (seharusnya 'diberantas'). E: 'di selenggarakan' dan pleonasme 'demi untuk'."
  },
  {
    "id": "twk_26", "category": "TWK", "subcategory": "Bahasa Indonesia",
    "question": "Cermati kalimat majemuk berikut:\n'Meskipun menghadapi keterbatasan anggaran, tetapi pimpinan unit kerja tetap berkomitmen meningkatkan kualitas pelayanan publik.'\n\nKalimat di atas tidak efektif karena...",
    "options": {
      "A": "Tidak memiliki subjek dan predikat yang jelas",
      "B": "Menggunakan konjungsi subordinatif 'Meskipun' bersamaan dengan konjungsi koordinatif pertentangan 'tetapi' (berlebihan)",
      "C": "Kata 'kualitas' bukan kosakata baku dalam bahasa Indonesia",
      "D": "Klausa anak mendahului klausa induk",
      "E": "Menggunakan tanda koma di tengah kalimat majemuk bertingkat"
    },
    "answer": "B",
    "explanation": "Konjungsi 'meskipun/walaupun' tidak boleh dipasangkan dengan 'tetapi/namun' dalam satu kalimat karena menimbulkan kerancuan struktur anak kalimat dan induk kalimat."
  },
  {
    "id": "twk_27", "category": "TWK", "subcategory": "Bahasa Indonesia",
    "question": "Penulisan gelar akademik dan singkatan nama orang berikut yang sesuai dengan kaidah EYD adalah...",
    "options": {
      "A": "Dr. Ir. Budi Santoso, M.Kom.",
      "B": "Dr. Ir. Budi Santoso M,Kom",
      "C": "Dr, Ir, Budi Santoso. M.Kom.",
      "D": "Dr Ir Budi Santoso, M.Kom",
      "E": "Dr. Ir. Budi Santoso, M,Kom."
    },
    "answer": "A",
    "explanation": "Setiap singkatan gelar diakhiri tanda titik, dan antara nama dengan gelar dipisahkan tanda koma. 'Dr. Ir. Budi Santoso, M.Kom.' adalah bentuk penulisan yang benar."
  },
  {
    "id": "twk_28", "category": "TWK", "subcategory": "Bahasa Indonesia",
    "question": "Bacalah paragraf berikut:\n(1) Transformasi digital di sektor birokrasi pemerintahan terus digencarkan.\n(2) Salah satu indikator keberhasilannya adalah peningkatan indeks kepuasan masyarakat terhadap layanan publik daring.\n(3) Aplikasi pelayanan kependudukan kini dapat diakses masyarakat selama 24 jam.\n(4) Selain itu, efisiensi anggaran cetak dokumen manual dapat ditekan secara signifikan.\n(5) Korupsi adalah kejahatan luar biasa yang merusak sendi-sendi perekonomian negara.\n\nKalimat yang sumbang (tidak padu) dalam paragraf di atas adalah kalimat nomor...",
    "options": {
      "A": "(1)",
      "B": "(2)",
      "C": "(3)",
      "D": "(4)",
      "E": "(5)"
    },
    "answer": "E",
    "explanation": "Kalimat (1), (2), (3), dan (4) membahas transformasi digital dan dampaknya bagi layanan publik. Kalimat (5) tiba-tiba membahas korupsi sebagai kejahatan luar biasa, sehingga menyimpang dari gagasan utama."
  },
  {
    "id": "twk_29", "category": "TWK", "subcategory": "Bahasa Indonesia",
    "question": "Kata serapan yang seluruhnya dieja secara baku menurut KBBI adalah...",
    "options": {
      "A": "Apotik, diagnosa, sistim",
      "B": "Apotek, diagnosis, sistem",
      "C": "Apotek, diagnosa, sistim",
      "D": "Apotik, diagnosis, sistem",
      "E": "Apotek, diagnose, sistim"
    },
    "answer": "B",
    "explanation": "Bentuk baku: Apotek (bukan apotik), Diagnosis (bukan diagnosa), Sistem (bukan sistim)."
  },
  {
    "id": "twk_30", "category": "TWK", "subcategory": "Bahasa Indonesia",
    "question": "Ide pokok (gagasan utama) dalam sebuah paragraf induktif terletak pada...",
    "options": {
      "A": "Awal paragraf",
      "B": "Akhir paragraf",
      "C": "Awal dan akhir paragraf",
      "D": "Tengah paragraf",
      "E": "Menyebar di setiap kalimat"
    },
    "answer": "B",
    "explanation": "Paragraf deduktif memiliki ide pokok di awal, sedangkan paragraf induktif mengemukakan rincian/penjelasan khusus terlebih dahulu dan meletakkan ide pokok/kesimpulan di akhir paragraf."
  }
]

# TIU: 35 Soal (No. 31 - 65)
tiu_questions = [
  # 31-37: Silogisme Logika
  {
    "id": "tiu_31", "category": "TIU", "subcategory": "Silogisme Logika",
    "question": "Semua pegawai negeri sipil mengenakan seragam dinas pada hari Senin.\nSebagian orang yang berada di aula balai kota tidak mengenakan seragam dinas.\n\nKesimpulan yang paling tepat adalah...",
    "options": {
      "A": "Sebagian orang yang berada di aula balai kota bukan pegawai negeri sipil jika saat itu hari Senin.",
      "B": "Semua orang yang tidak mengenakan seragam dinas di aula balai kota adalah bukan pegawai.",
      "C": "Pada hari Senin, semua orang di aula balai kota adalah pegawai negeri sipil.",
      "D": "Tidak ada pegawai negeri sipil yang berada di aula balai kota pada hari Senin.",
      "E": "Orang yang berada di aula balai kota mengenakan seragam dinas selain hari Senin."
    },
    "answer": "A",
    "explanation": "Jika hari Senin dan seluruh PNS wajib berseragam, maka mereka yang tidak berseragam di aula pada hari itu dipastikan bukan PNS. Karena hanya sebagian orang yang tidak berseragam, kesimpulannya: sebagian orang di aula tersebut bukan PNS pada hari Senin."
  },
  {
    "id": "tiu_32", "category": "TIU", "subcategory": "Silogisme Logika",
    "question": "Semua dokumen rahasia negara wajib disimpan dalam brankas tahan api.\nSebagian berkas yang berada di ruang arsip tidak disimpan dalam brankas tahan api.\n\nKesimpulan yang tepat adalah...",
    "options": {
      "A": "Semua berkas di ruang arsip adalah dokumen rahasia negara.",
      "B": "Sebagian berkas yang berada di ruang arsip bukan dokumen rahasia negara.",
      "C": "Semua berkas di ruang arsip bukan dokumen rahasia negara.",
      "D": "Sebagian brankas tahan api tidak berada di ruang arsip.",
      "E": "Dokumen rahasia negara tidak boleh disimpan di ruang arsip."
    },
    "answer": "B",
    "explanation": "Karena seluruh dokumen rahasia negara wajib di brankas tahan api, maka berkas yang TIDAK disimpan di brankas tahan api tersebut pasti bukan dokumen rahasia negara."
  },
  {
    "id": "tiu_33", "category": "TIU", "subcategory": "Silogisme Logika",
    "question": "Jika seorang pelamar lulus passing grade dan masuk perangkingan 3 kali formasi, maka ia berhak mengikuti ujian SKB.\nDoni berhak mengikuti ujian SKB.\n\nKesimpulan yang paling tepat adalah...",
    "options": {
      "A": "Doni pasti lulus passing grade dan masuk perangkingan 3 kali formasi.",
      "B": "Doni belum tentu lulus passing grade.",
      "C": "Doni lulus SKB dan diangkat menjadi CPNS.",
      "D": "Doni tidak lulus passing grade.",
      "E": "Semua peserta selain Doni tidak masuk 3 kali formasi."
    },
    "answer": "A",
    "explanation": "Berdasarkan syarat mutlak keikutsertaan SKB dalam regulasi seleksi, hanya peserta yang lulus passing grade dan masuk 3x formasi yang berhak mengikuti SKB."
  },
  {
    "id": "tiu_34", "category": "TIU", "subcategory": "Silogisme Logika",
    "question": "Semua inovasi digital mempercepat proses pelayanan publik.\nBeberapa sistem informasi berbasis website adalah inovasi digital.\n\nKesimpulan yang tepat adalah...",
    "options": {
      "A": "Semua sistem informasi berbasis website mempercepat proses pelayanan publik.",
      "B": "Beberapa sistem informasi berbasis website mempercepat proses pelayanan publik.",
      "C": "Sistem informasi berbasis website tidak ada yang mempercepat pelayanan publik.",
      "D": "Inovasi digital hanya berupa sistem informasi berbasis website.",
      "E": "Pelayanan publik hanya bisa dipercepat dengan website."
    },
    "answer": "B",
    "explanation": "Premis 1: Semua A adalah B. Premis 2: Sebagian C adalah A. Kesimpulan: Sebagian C adalah B (Beberapa sistem informasi berbasis website mempercepat pelayanan publik)."
  },
  {
    "id": "tiu_35", "category": "TIU", "subcategory": "Silogisme Logika",
    "question": "Jika server pusat mengalami gangguan daya, maka basis data tidak dapat diakses.\nJika basis data tidak dapat diakses, maka loket layanan daring ditutup sementara.\nHari ini loket layanan daring tidak ditutup sementara.\n\nKesimpulan yang sah berdasarkan kaidah modus tollens adalah...",
    "options": {
      "A": "Server pusat mengalami gangguan daya.",
      "B": "Basis data tidak dapat diakses oleh petugas loket.",
      "C": "Server pusat tidak mengalami gangguan daya.",
      "D": "Loket layanan daring dipindahkan ke kantor cabang.",
      "E": "Petugas loket bekerja secara manual."
    },
    "answer": "C",
    "explanation": "P -> Q dan Q -> R, maka P -> R. Diketahui ~R (loket tidak ditutup), maka kesimpulannya adalah ~P (Server pusat tidak mengalami gangguan daya)."
  },
  {
    "id": "tiu_36", "category": "TIU", "subcategory": "Silogisme Logika",
    "question": "Tidak ada koruptor yang memiliki integritas tinggi.\nSemua teladan antikorupsi memiliki integritas tinggi.\n\nKesimpulan yang sah adalah...",
    "options": {
      "A": "Sebagian koruptor adalah teladan antikorupsi.",
      "B": "Tidak ada koruptor yang merupakan teladan antikorupsi.",
      "C": "Semua yang berintegritas tinggi adalah koruptor.",
      "D": "Sebagian teladan antikorupsi adalah koruptor.",
      "E": "Semua koruptor berintegritas rendah pada awalnya."
    },
    "answer": "B",
    "explanation": "Koruptor dan pemilik integritas tinggi adalah dua himpunan yang saling lepas. Karena semua teladan berada di dalam himpunan berintegritas tinggi, maka tidak ada koruptor yang merupakan teladan antikorupsi."
  },
  {
    "id": "tiu_37", "category": "TIU", "subcategory": "Silogisme Logika",
    "question": "Semua atlet lari memiliki stamina prima.\nSebagian mahasiswa baru adalah atlet lari.\n\nKesimpulan yang tepat adalah...",
    "options": {
      "A": "Semua mahasiswa baru memiliki stamina prima.",
      "B": "Sebagian mahasiswa baru memiliki stamina prima.",
      "C": "Hanya mahasiswa baru yang memiliki stamina prima.",
      "D": "Semua atlet lari adalah mahasiswa baru.",
      "E": "Sebagian atlet lari tidak memiliki stamina prima."
    },
    "answer": "B",
    "explanation": "Sebagian mahasiswa baru yang merupakan atlet lari pasti memiliki stamina prima. Jadi kesimpulannya: Sebagian mahasiswa baru memiliki stamina prima."
  },

  # 38-44: Analogi Kata
  {
    "id": "tiu_38", "category": "TIU", "subcategory": "Analogi Verbal",
    "question": "KOMPUTER : PROGRAMMER = ... : ...",
    "options": {
      "A": "Mobil : Sopir",
      "B": "Gedung : Arsitek",
      "C": "Buku : Pembaca",
      "D": "Pesawat : Pilot",
      "E": "Kamera : Fotografer"
    },
    "answer": "B",
    "explanation": "Hubungan pencipta/perancang: PROGRAMMER merancang KOMPUTER (perangkat lunak/sistem), sebagaimana ARSITEK merancang GEDUNG/BANGUNAN. (Sopir dan pilot hanya mengemudikan/mengoperasikan)."
  },
  {
    "id": "tiu_39", "category": "TIU", "subcategory": "Analogi Verbal",
    "question": "HAUS : AIR = ... : ...",
    "options": {
      "A": "Lapar : Makanan",
      "B": "Ngantuk : Kopi",
      "C": "Lelah : Kerja",
      "D": "Sakit : Dokter",
      "E": "Gelap : Matahari"
    },
    "answer": "A",
    "explanation": "Hubungan kebutuhan primer biologis: Seseorang yang HAUS membutuhkan AIR, sebagaimana seseorang yang LAPAR membutuhkan MAKANAN."
  },
  {
    "id": "tiu_40", "category": "TIU", "subcategory": "Analogi Verbal",
    "question": "APOTEKER : OBAT = ... : ...",
    "options": {
      "A": "Koki : Restoran",
      "B": "Petani : Cangkul",
      "C": "Pustakawan : Buku",
      "D": "Dokter : Pasien",
      "E": "Montir : Bengkel"
    },
    "answer": "C",
    "explanation": "Hubungan profesi dengan objek yang dikelolanya secara profesional: APOTEKER mengelola OBAT, sebagaimana PUSTAKAWAN mengelola BUKU."
  },
  {
    "id": "tiu_41", "category": "TIU", "subcategory": "Analogi Verbal",
    "question": "KORUPSI : PENJARA = ... : ...",
    "options": {
      "A": "Prestasi : Penghargaan",
      "B": "Belajar : Sekolah",
      "C": "Bekerja : Gaji",
      "D": "Latihan : Juara",
      "E": "Sakit : Rumah Sakit"
    },
    "answer": "A",
    "explanation": "Hubungan perbuatan dengan konsekuensi resminya: Tindakan KORUPSI diganjar hukuman PENJARA, sebagaimana tindakan PRESTASI diganjar apresiasi PENGHARGAAN."
  },
  {
    "id": "tiu_42", "category": "TIU", "subcategory": "Analogi Verbal",
    "question": "MIKROSKOP : BAKTERI = ... : ...",
    "options": {
      "A": "Teleskop : Bintang",
      "B": "Termometer : Udara",
      "C": "Stetoskop : Darah",
      "D": "Barometer : Hujan",
      "E": "Kompas : Arah"
    },
    "answer": "A",
    "explanation": "Alat optik pembesar: MIKROSKOP digunakan untuk mengamati benda mikroskopis seperti BAKTERI, sebagaimana TELESKOP digunakan untuk mengamati benda angkasa sangat jauh seperti BINTANG."
  },
  {
    "id": "tiu_43", "category": "TIU", "subcategory": "Analogi Verbal",
    "question": "KANCING : BAJU = ... : ...",
    "options": {
      "A": "Tali : Sepatu",
      "B": "Roda : Mobil",
      "C": "Pintu : Rumah",
      "D": "Kunci : Gembok",
      "E": "Topi : Kepala"
    },
    "answer": "A",
    "explanation": "KANCING adalah pengencang/penutup pada BAJU, sebagaimana TALI adalah pengencang pada SEPATU."
  },
  {
    "id": "tiu_44", "category": "TIU", "subcategory": "Analogi Verbal",
    "question": "INSOMNIA : TIDUR = ... : ...",
    "options": {
      "A": "Anemia : Darah",
      "B": "Amnesia : Ingatan",
      "C": "Apatis : Sikap",
      "D": "Disleksia : Menulis",
      "E": "Miopi : Jarak"
    },
    "answer": "B",
    "explanation": "INSOMNIA adalah gangguan/kehilangan kemampuan untuk TIDUR, sebagaimana AMNESIA adalah gangguan/kehilangan daya INGATAN."
  },

  # 45-51: Deret Angka
  {
    "id": "tiu_45", "category": "TIU", "subcategory": "Deret Angka",
    "question": "Perhatikan deret angka berikut:\n3, 7, 15, 31, 63, ... , ...\n\nDua bilangan selanjutnya yang tepat adalah...",
    "options": {
      "A": "125, 251",
      "B": "127, 255",
      "C": "126, 254",
      "D": "128, 256",
      "E": "129, 257"
    },
    "answer": "B",
    "explanation": "Pola deret: (n × 2) + 1.\n63 × 2 + 1 = 127.\n127 × 2 + 1 = 255."
  },
  {
    "id": "tiu_46", "category": "TIU", "subcategory": "Deret Angka",
    "question": "Perhatikan barisan bilangan berikut:\n4, 9, 16, 25, 36, 49, ...\n\nBilangan berikutnya pada barisan tersebut adalah...",
    "options": {
      "A": "56",
      "B": "60",
      "C": "64",
      "D": "72",
      "E": "81"
    },
    "answer": "C",
    "explanation": "Deret bilangan kuadrat berurutan: 2^2=4, 3^2=9, 4^2=16, 5^2=25, 6^2=36, 7^2=49, maka berikutnya adalah 8^2 = 64."
  },
  {
    "id": "tiu_47", "category": "TIU", "subcategory": "Deret Angka",
    "question": "Perhatikan pola bilangan larik dua tingkat berikut:\n2, 5, 4, 10, 8, 20, 16, ... , ...\n\nDua suku berikutnya adalah...",
    "options": {
      "A": "40, 32",
      "B": "32, 40",
      "C": "40, 24",
      "D": "24, 40",
      "E": "32, 64"
    },
    "answer": "A",
    "explanation": "Dua deret berselingan:\nLarik 1 (ganjil): 2, 4, 8, 16, 32 (dikali 2).\nLarik 2 (genap): 5, 10, 20, 40 (dikali 2).\nMaka dua suku berikutnya: 40 (dari larik 2) kemudian 32 (dari larik 1)."
  },
  {
    "id": "tiu_48", "category": "TIU", "subcategory": "Deret Angka",
    "question": "Perhatikan deret Fibonacci modifikasi berikut:\n1, 2, 3, 5, 8, 13, 21, ...\n\nSuku berikutnya dari deret di atas adalah...",
    "options": {
      "A": "31",
      "B": "34",
      "C": "35",
      "D": "38",
      "E": "42"
    },
    "answer": "B",
    "explanation": "Deret Fibonacci: setiap suku adalah penjumlahan 2 suku sebelumnya.\n13 + 21 = 34."
  },
  {
    "id": "tiu_49", "category": "TIU", "subcategory": "Deret Angka",
    "question": "Tentukan angka yang tepat untuk mengisi titik-titik pada deret berikut:\n100, 95, 85, 70, 50, ...\n",
    "options": {
      "A": "20",
      "B": "25",
      "C": "30",
      "D": "35",
      "E": "15"
    },
    "answer": "B",
    "explanation": "Pola pengurangan bertingkat: -5, -10, -15, -20, maka berikutnya adalah -25.\n50 - 25 = 25."
  },
  {
    "id": "tiu_50", "category": "TIU", "subcategory": "Deret Angka",
    "question": "Perhatikan pola bilangan berikut:\n1, 8, 27, 64, 125, ...\n\nSuku berikutnya adalah...",
    "options": {
      "A": "196",
      "B": "216",
      "C": "256",
      "D": "343",
      "E": "512"
    },
    "answer": "B",
    "explanation": "Pola bilangan pangkat tiga: 1^3=1, 2^3=8, 3^3=27, 4^3=64, 5^3=125, selanjutnya 6^3 = 216."
  },
  {
    "id": "tiu_51", "category": "TIU", "subcategory": "Deret Angka",
    "question": "Tentukan angka selanjutnya:\n5, 6, 10, 12, 20, 24, 40, ...\n",
    "options": {
      "A": "44",
      "B": "48",
      "C": "50",
      "D": "60",
      "E": "80"
    },
    "answer": "B",
    "explanation": "Dua deret melompat:\nDeret 1: 5, 10, 20, 40 (dikali 2)\nDeret 2: 6, 12, 24, 48 (dikali 2).\nSuku berikutnya berasal dari deret 2: 24 × 2 = 48."
  },

  # 52-58: Berhitung & Aritmatika Sosial
  {
    "id": "tiu_52", "category": "TIU", "subcategory": "Aritmatika Sosial",
    "question": "Sebuah instalasi jaringan server ditargetkan selesai dalam 30 hari oleh 12 orang teknisi. Setelah 10 hari dikerjakan, proyek terhenti selama 5 hari karena keterlambatan pengiriman material. Agar proyek selesai tepat waktu sesuai jadwal awal, berapa tambahan teknisi yang diperlukan?",
    "options": {
      "A": "2 orang",
      "B": "3 orang",
      "C": "4 orang",
      "D": "5 orang",
      "E": "6 orang"
    },
    "answer": "C",
    "explanation": "Sisa hari normal = 20 hari × 12 orang = 240 orang-hari beban sisa.\nWaktu tersisa = 20 - 5 = 15 hari.\nJumlah pekerja dibutuhkan = 240 / 15 = 16 orang.\nTambahan pekerja = 16 - 12 = 4 orang."
  },
  {
    "id": "tiu_53", "category": "TIU", "subcategory": "Aritmatika Sosial",
    "question": "Sebuah laptop kantor dibeli dengan harga resmi Rp12.000.000,00 dan mendapatkan potongan diskon bertingkat 20% kemudian didiskon lagi 10%. Berapakah harga akhir yang harus dibayarkan?",
    "options": {
      "A": "Rp8.400.000,00",
      "B": "Rp8.640.000,00",
      "C": "Rp8.800.000,00",
      "D": "Rp9.000.000,00",
      "E": "Rp9.600.000,00"
    },
    "answer": "B",
    "explanation": "Diskon bertingkat dihitung berurutan:\nHarga setelah diskon pertama = 80% × 12.000.000 = Rp9.600.000.\nHarga setelah diskon kedua = 90% × 9.600.000 = Rp8.640.000,00."
  },
  {
    "id": "tiu_54", "category": "TIU", "subcategory": "Kecepatan dan Jarak",
    "question": "Mobil A melaju dari kota P ke kota Q dengan kecepatan rata-rata 60 km/jam pada pukul 08.00. Mobil B menyusul dari kota P pada rute yang sama pada pukul 08.30 dengan kecepatan rata-rata 80 km/jam. Pada pukul berapa mobil B akan menyusul mobil A?",
    "options": {
      "A": "09.30",
      "B": "10.00",
      "C": "10.30",
      "D": "11.00",
      "E": "11.30"
    },
    "answer": "B",
    "explanation": "Selisih waktu = 30 menit (0,5 jam). Selisih jarak awal = 60 km/jam × 0,5 jam = 30 km.\nKecepatan relatif menyusul = 80 - 60 = 20 km/jam.\nWaktu menyusul = 30 km / 20 km/jam = 1,5 jam setelah mobil B berangkat.\nPukul menyusul = 08.30 + 1,5 jam = 10.00 WIB."
  },
  {
    "id": "tiu_55", "category": "TIU", "subcategory": "Aljabar & Persamaan",
    "question": "Jika x = 1/16 dan y = 16%, hubungan kuantitatif yang paling tepat antara x dan y adalah...",
    "options": {
      "A": "x > y",
      "B": "x < y",
      "C": "x = y",
      "D": "x + y = 1",
      "E": "Hubungan x dan y tidak dapat ditentukan"
    },
    "answer": "B",
    "explanation": "x = 1/16 = 0,0625 = 6,25%.\ny = 16% = 0,16.\nKarena 6,25% < 16%, maka x < y."
  },
  {
    "id": "tiu_56", "category": "TIU", "subcategory": "Statistika & Rata-rata",
    "question": "Nilai rata-rata ujian matematika dari 39 orang siswa adalah 70. Jika nilai Budi digabungkan, nilai rata-rata seluruh kelas menjadi 70,5. Berapakah nilai ujian Budi?",
    "options": {
      "A": "80",
      "B": "85",
      "C": "90",
      "D": "92",
      "E": "95"
    },
    "answer": "C",
    "explanation": "Total nilai 39 siswa = 39 × 70 = 2.730.\nTotal nilai 40 siswa (termasuk Budi) = 40 × 70,5 = 2.820.\nNilai Budi = 2.820 - 2.730 = 90."
  },
  {
    "id": "tiu_57", "category": "TIU", "subcategory": "Aljabar Cepat",
    "question": "Nilai dari (882 + 118)^2 - (882 - 118)^2 adalah...",
    "options": {
      "A": "416.304",
      "B": "420.000",
      "C": "416.000",
      "D": "415.800",
      "E": "418.000"
    },
    "answer": "A",
    "explanation": "Gunakan rumus selisih kuadrat aljabar:\n(a + b)^2 - (a - b)^2 = 4ab.\n4 × 882 × 118 = 416.304."
  },
  {
    "id": "tiu_58", "category": "TIU", "subcategory": "Perbandingan Kuantitatif",
    "question": "Sebuah bejana berbentuk silinder terisi air 1/3 bagiannya. Jika ditambahkan 10 liter air lagi, bejana tersebut menjadi terisi 1/2 bagiannya. Berapakah kapasitas total bejana tersebut?",
    "options": {
      "A": "40 liter",
      "B": "50 liter",
      "C": "60 liter",
      "D": "70 liter",
      "E": "80 liter"
    },
    "answer": "C",
    "explanation": "Misalkan kapasitas total = V.\n1/2 V - 1/3 V = 10 liter.\n(3/6 - 2/6) V = 10 liter => 1/6 V = 10 => V = 60 liter."
  },

  # 59-65: Penalaran Analitis
  {
    "id": "tiu_59", "category": "TIU", "subcategory": "Penalaran Analitis",
    "question": "Lima orang staf (A, B, C, D, E) dijadwalkan piket harian dari Senin sampai Jumat dengan ketentuan:\n1. A piket sebelum C.\n2. B piket tepat setelah D.\n3. E piket pada hari Rabu.\n4. C piket pada hari Jumat.\nSiapakah yang bertugas piket pada hari Selasa?",
    "options": {
      "A": "A",
      "B": "B",
      "C": "D",
      "D": "E",
      "E": "B atau D"
    },
    "answer": "B",
    "explanation": "Peta hari:\nSenin, Selasa, Rabu (E), Kamis, Jumat (C).\nSyarat B tepat setelah D: pasangan (D, B) hanya bisa masuk di Senin dan Selasa (D Senin, B Selasa). Sisa A di hari Kamis (sebelum C Jumat). Jadi hari Selasa adalah B."
  },
  {
    "id": "tiu_60", "category": "TIU", "subcategory": "Penalaran Analitis",
    "question": "Enam peserta (P, Q, R, S, T, U) duduk melingkar mengelilingi meja bundar:\n- P duduk berhadapan langsung dengan S.\n- Q duduk di sebelah kanan P.\n- T duduk di sebelah kiri P.\n- R duduk di sebelah kanan S.\nSiapakah yang duduk di antara T dan S?",
    "options": {
      "A": "U",
      "B": "R",
      "C": "Q",
      "D": "P",
      "E": "Tidak dapat ditentukan"
    },
    "answer": "A",
    "explanation": "Susunan melingkar 6 kursi: P di atas, S di bawah (berhadapan). Kanan P adalah Q, kiri P adalah T. Kanan S adalah R. Maka kursi tersisa di antara T dan S ditempati oleh U."
  },
  {
    "id": "tiu_61", "category": "TIU", "subcategory": "Penalaran Analitis",
    "question": "Tinggi badan lima atlet basket diukur:\n- Andi lebih tinggi dari Budi.\n- Candra lebih pendek dari Budi tetapi lebih tinggi dari Dodi.\n- Eko adalah yang paling tinggi di antara semuanya.\nUrutan atlet dari yang paling pendek ke yang paling tinggi adalah...",
    "options": {
      "A": "Dodi, Candra, Budi, Andi, Eko",
      "B": "Candra, Dodi, Budi, Andi, Eko",
      "C": "Dodi, Budi, Candra, Andi, Eko",
      "D": "Dodi, Candra, Andi, Budi, Eko",
      "E": "Eko, Andi, Budi, Candra, Dodi"
    },
    "answer": "A",
    "explanation": "Dari keterangan:\nDodi < Candra < Budi < Andi < Eko.\nUrutan dari terpendek ke tertinggi: Dodi, Candra, Budi, Andi, Eko."
  },
  {
    "id": "tiu_62", "category": "TIU", "subcategory": "Penalaran Analitis",
    "question": "Dalam perlombaan lari:\n- Fajar sampai di garis finis sebelum Gani.\n- Hadi sampai setelah Indra tetapi sebelum Fajar.\n- Jaka sampai tepat setelah Gani.\nSiapakah yang sampai di posisi pertama?",
    "options": {
      "A": "Fajar",
      "B": "Gani",
      "C": "Hadi",
      "D": "Indra",
      "E": "Jaka"
    },
    "answer": "D",
    "explanation": "Urutan finis:\nIndra -> Hadi -> Fajar -> Gani -> Jaka.\nYang finis di posisi pertama adalah Indra."
  },
  {
    "id": "tiu_63", "category": "TIU", "subcategory": "Figural / Spasial Logika",
    "question": "Sebuah kubus memiliki sisi dengan simbol yang berbeda pada tiap sisinya. Jika sisi atas adalah lingkaran dan sisi bawah adalah silang, sedangkan sisi kanan segitiga dan sisi kiri persegi, jika kubus digulingkan 90 derajat ke arah kanan, maka sisi yang kini berada di posisi atas adalah...",
    "options": {
      "A": "Persegi",
      "B": "Segitiga",
      "C": "Lingkaran",
      "D": "Silang",
      "E": "Bintang"
    },
    "answer": "A",
    "explanation": "Menggulingkan kubus 90 derajat ke kanan akan membawa sisi kiri (persegi) naik menjadi sisi atas."
  },
  {
    "id": "tiu_64", "category": "TIU", "subcategory": "Figural / Spasial Logika",
    "question": "Diberikan analogi bentuk geometri: 'Segitiga berelasi dengan 3 sisi sebagaimana Segi Enam berelasi dengan...'",
    "options": {
      "A": "4 sudut",
      "B": "5 diagonal",
      "C": "6 sisi dan 6 titik sudut",
      "D": "8 bidang simetri",
      "E": "3 garis tegak lurus"
    },
    "answer": "C",
    "explanation": "Hubungan karakteristik poligon beraturan: Segitiga memiliki 3 sisi dan 3 sudut, sedangkan Segi Enam (heksagon) memiliki 6 sisi dan 6 titik sudut."
  },
  {
    "id": "tiu_65", "category": "TIU", "subcategory": "Figural / Spasial Logika",
    "question": "Manakah di antara pilihan berikut yang secara logis tidak memiliki kesamaan kelompok dengan yang lainnya?",
    "options": {
      "A": "Kubus",
      "B": "Balok",
      "C": "Kerucut",
      "D": "Trapesium",
      "E": "Bola"
    },
    "answer": "D",
    "explanation": "Kubus, Balok, Kerucut, dan Bola adalah bangun ruang tiga dimensi (3D), sedangkan Trapesium adalah bangun datar dua dimensi (2D)."
  }
]

# TKP: 45 Soal (No. 66 - 110)
# Semua soal TKP memiliki skala bobot 1 - 5 untuk pilihan A, B, C, D, E
tkp_questions = [
  # 66-73: Pelayanan Publik
  {
    "id": "tkp_66", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Anda bertugas di loket pelayanan administrasi kependudukan. Saat antrean sangat padat, datang seorang warga lansia yang tampak kebingungan mengisi formulir permohonan akta kematian keluarganya. Sementara itu, antrean nomor berikutnya sudah menunggu. Tindakan Anda adalah...",
    "options": {
      "A": "Meminta lansia tersebut keluar dari antrean dan meminta keluarganya saja yang datang besok",
      "B": "Memanggil nomor berikutnya terlebih dahulu dan membiarkan lansia tersebut dibantu warga lain di ruang tunggu",
      "C": "Dengan sopan dan ramah meminta izin sebentar kepada antrean berikutnya, membimbing lansia tersebut mengisi poin-poin krusial di meja khusus lansia atau meminta petugas informasi mendampingi hingga selesai",
      "D": "Menegur lansia tersebut agar belajar membaca instruksi yang sudah tertera jelas di dinding pengumuman",
      "E": "Menyelesaikan formulir lansia tersebut dengan tergesa-gesa tanpa mengecek keabsahan berkas"
    },
    "points": {"A": 1, "B": 3, "C": 5, "D": 2, "E": 4},
    "answer": "C",
    "explanation": "Indikator Pelayanan Publik: Mengedepankan empati dan solusi taktis bagi kelompok rentan tanpa mengabaikan ketertiban antrean secara keseluruhan (C=5, E=4, B=3, D=2, A=1)."
  },
  {
    "id": "tkp_67", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Sistem aplikasi perizinan online kantor Anda tiba-tiba mengalami gangguan server (down) di tengah jam kerja pelayanan, sehingga banyak warga pemohon yang mulai mengeluh di ruang tunggu loket. Sikap Anda adalah...",
    "options": {
      "A": "Bersembunyi di ruangan staf belakang hingga server kembali pulih",
      "B": "Keluar menemui warga dengan santun, menyampaikan permohonan maaf atas kendala teknis, menjelaskan perkiraan estimasi perbaikan tim IT, dan menawarkan pencatatan berkas fisik sementara agar tidak menumpuk",
      "C": "Menyalahkan tim IT di depan para pemohon agar warga memahami bukan kesalahan petugas loket",
      "D": "Menyuruh seluruh warga pulang dan kembali lusa tanpa memberikan solusi alternatif",
      "E": "Tetap duduk diam di loket tanpa memberikan penjelasan apa pun"
    },
    "points": {"A": 1, "B": 5, "C": 2, "D": 3, "E": 4},
    "answer": "B",
    "explanation": "Indikator Pelayanan Publik: Komunikasi proaktif, transparansi, ketenangan meredakan keluhan masyarakat, serta memberikan alternatif solusi darurat (B=5, E=4, D=3, C=2, A=1)."
  },
  {
    "id": "tkp_68", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Seorang warga yang kecewa karena berkas permohonannya ditolak akibat syarat dokumen tidak lengkap berbicara dengan nada tinggi dan membentak Anda di loket pelayanan. Sikap Anda menghadapinya adalah...",
    "options": {
      "A": "Membalas membentak warga tersebut agar menyadari kesalahannya",
      "B": "Memanggil satpam untuk segera mengusir warga tersebut keluar dari gedung kantor",
      "C": "Tetap tenang, tidak terpancing emosi, mendengarkan keluhannya, lalu menjelaskan secara santun dan terperinci poin syarat yang kurang serta bagaimana cara melengkapinya",
      "D": "Meninggalkan loket dan menangis di toilet",
      "E": "Meloloskan saja berkasnya yang tidak lengkap agar tidak membuat keributan di loket"
    },
    "points": {"A": 1, "B": 3, "C": 5, "D": 2, "E": 4},
    "answer": "C",
    "explanation": "Pengendalian diri, profesionalitas melayani, dan penjelasan edukatif yang jelas dan santun merupakan nilai tertinggi dalam pelayanan prima (C=5, E=4, B=3, D=2, A=1)."
  },
  {
    "id": "tkp_69", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Masyarakat sering mengeluhkan lamanya waktu tunggu pembuatan kartu tanda pencari kerja di kantor dinas Anda. Sebagai staf baru, apa kontribusi inovatif yang dapat Anda usulkan kepada pimpinan?",
    "options": {
      "A": "Meminta masyarakat bersabar karena tenaga kerja di kantor memang terbatas",
      "B": "Mengusulkan integrasi formulir pendaftaran daring pra-kedatangan dan sistem antrean berbasis notifikasi WhatsApp agar waktu tunggu di lokasi berkurang drastis",
      "C": "Menyerahkan urusan keluhan tersebut kepada pimpinan lama yang lebih berpengalaman",
      "D": "Menyarankan penutupan loket offline dan hanya melayani lewat surat pos",
      "E": "Mengurangi jam operasional loket agar staf tidak kelelahan"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 1, "E": 4},
    "answer": "B",
    "explanation": "Menunjukkan inisiatif perbaikan berkesinambungan memanfaatkan teknologi untuk efisiensi dan kepuasan masyarakat (B=5, E=4, C=3, A=2, D=1)."
  },
  {
    "id": "tkp_70", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Seorang kerabat dekat Anda meminta bantuan agar proses perizinan usahanya dipercepat tanpa melalui jalur antrean resmi dan menawarkan sejumlah uang tip. Tindakan Anda adalah...",
    "options": {
      "A": "Menerima uang tersebut dan segera memproses izinnya demi hubungan kekeluargaan",
      "B": "Menolak uangnya namun tetap mempercepat proses berkasnya di belakang layar",
      "C": "Menolak dengan tegas dan santun baik uang maupun permohonan potong antrean, serta menjelaskan bahwa semua warga dilayani secara adil sesuai SOP",
      "D": "Memarahi kerabat tersebut di depan khalayak ramai hingga merasa malu",
      "E": "Mengarahkan kerabat tersebut menemui rekan kerja lain yang mau menerima tip"
    },
    "points": {"A": 1, "B": 3, "C": 5, "D": 2, "E": 4},
    "answer": "C",
    "explanation": "Menjunjung keadilan dan kesetaraan hak masyarakat dalam pelayanan publik serta menolak segala bentuk nepotisme dan suap (C=5, E=4, B=3, D=2, A=1)."
  },
  {
    "id": "tkp_71", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Menjelang jam istirahat siang, masih terdapat 3 orang warga pemohon yang belum terlayani di loket Anda, sementara rekan kerja lainnya sudah bersiap pergi makan siang. Sikap Anda adalah...",
    "options": {
      "A": "Langsung menutup loket tepat pada jamnya dan meminta mereka menunggu satu jam lagi",
      "B": "Menuntaskan pelayanan ketiga warga tersebut dengan ramah sebelum Anda mengambil istirahat makan siang",
      "C": "Melayani satu orang saja lalu menyuruh dua lainnya menunggu",
      "D": "Menyuruh satpam mengosongkan ruang pelayanan",
      "E": "Melayani dengan muka cemberut agar warga merasa bersalah mengganggu jam istirahat"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 1, "E": 4},
    "answer": "B",
    "explanation": "Dedikasi melayani dan komitmen tuntas pada kepuasan masyarakat penerima layanan (B=5, E=4, C=3, A=2, D=1)."
  },
  {
    "id": "tkp_72", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Setelah Anda menyelesaikan pelayanan dokumen perizinan, seorang pemohon lansia tampak bingung bagaimana cara menuju ke halte bus terdekat dari kantor Anda di bawah terik matahari. Sikap Anda adalah...",
    "options": {
      "A": "Menunjukkan arah jalan dengan jelas dan ramah, serta meminta bantuan petugas keamanan untuk memandu lansia tersebut menyeberang jalan",
      "B": "Membiarkannya karena tugas pelayanan Anda hanya terbatas di dalam meja loket",
      "C": "Menyuruhnya memesan taksi online sendiri tanpa bertanya",
      "D": "Mengabaikannya karena sudah ada pemohon berikutnya yang menunggu",
      "E": "Meninggalkan loket kerja berjam-jam untuk mengantar lansia tersebut pulang ke rumahnya"
    },
    "points": {"A": 5, "B": 2, "C": 3, "D": 1, "E": 4},
    "answer": "A",
    "explanation": "Kepedulian dan keramahan proporsional yang membantu menuntaskan kendala warga tanpa menelantarkan tugas pokok kantor (A=5, E=4, C=3, B=2, D=1)."
  },
  {
    "id": "tkp_73", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Berdasarkan survei kepuasan masyarakat, unit kerja Anda mendapat skor rendah pada aspek kejelasan informasi alur berkas. Langkah yang paling tepat Anda lakukan adalah...",
    "options": {
      "A": "Menyalahkan masyarakat yang dinilai malas membaca",
      "B": "Mengusulkan perancangan infografis alur pelayanan yang jelas, mencetak brosur saku, dan membuat panduan video ringkas di layar ruang tunggu",
      "C": "Meminta pimpinan membatalkan hasil survei kepuasan tersebut",
      "D": "Mengurangi jumlah persyaratan dokumen tanpa persetujuan atasan",
      "E": "Mengabaikan hasil survei karena tidak berdampak pada gaji"
    },
    "points": {"A": 2, "B": 5, "C": 1, "D": 3, "E": 4},
    "answer": "B",
    "explanation": "Responsif terhadap kritik konstruktif masyarakat melalui langkah pembenahan konkret transparansi informasi (B=5, E=4, D=3, A=2, C=1)."
  },

  # 74-81: Jejaring Kerja
  {
    "id": "tkp_74", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Anda ditugaskan dalam sebuah tim kerja lintas instansi untuk menyusun regulasi Satu Data. Setiap anggota tim memiliki ego sektoral dan mempertahankan kepentingannya masing-masing. Sikap Anda dalam memfasilitasi tim tersebut adalah...",
    "options": {
      "A": "Ikut mempertahankan ego instansi Anda sendiri agar tidak kalah saing",
      "B": "Mengajak seluruh anggota memfokuskan kembali tujuan utama pada kepentingan nasional, memetakan titik temu regulasi, dan membangun komunikasi dialogis yang setara",
      "C": "Memilih pasif dan hanya mendengarkan jalannya debat kusir",
      "D": "Mengundurkan diri dari kepanitiaan karena merasa tim tidak akan pernah kompak",
      "E": "Melaporkan kekecewaan Anda ke media massa"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 1, "E": 4},
    "answer": "B",
    "explanation": "Menjadi perekat dan jembatan kolaborasi yang mengedepankan kepentingan bersama serta sinergi jejaring kerja (B=5, E=4, C=3, A=2, D=1)."
  },
  {
    "id": "tkp_75", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Seorang rekan satu tim Anda sedang mengalami musibah keluarga sehingga progres bagian pekerjaannya dalam proyek bersama terhambat. Sikap Anda adalah...",
    "options": {
      "A": "Menegurnya di depan tim karena menurunkan kinerja kelompok",
      "B": "Bersama anggota tim lain berdiskusi untuk membagi sementara tugas rekan tersebut secara proporsional sembari memberikan dukungan moral",
      "C": "Melaporkannya langsung kepada kepala dinas agar rekan tersebut segera diganti",
      "D": "Membiarkannya saja karena setiap orang memiliki tanggung jawab masing-masing",
      "E": "Mengerjakan seluruh pekerjaannya sendirian dan menuntut bayaran lebih"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 1, "E": 4},
    "answer": "B",
    "explanation": "Kekompakan tim, empati, dan gotong royong mencari solusi bersama demi keberhasilan target organisasi (B=5, E=4, C=3, A=2, D=1)."
  },
  {
    "id": "tkp_76", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Dalam rangka memperluas kemitraan dan transfer teknologi, kantor Anda kedatangan pakar dari lembaga riset ternama. Langkah yang Anda ambil adalah...",
    "options": {
      "A": "Menghindar karena merasa minder dengan latar belakang akademis mereka",
      "B": "Menyambut dengan terbuka, aktif berdiskusi mengenai praktik terbaik, bertukar kontak, dan menjajaki potensi kerja sama yang saling menguntungkan",
      "C": "Menganggap kedatangan mereka hanya membuang-buang anggaran kantor",
      "D": "Menyerahkan seluruh urusan penerimaan tamu kepada bagian humas",
      "E": "Hanya berbicara jika ditanya langsung oleh pimpinan"
    },
    "points": {"A": 2, "B": 5, "C": 1, "D": 3, "E": 4},
    "answer": "B",
    "explanation": "Kemampuan membangun dan membina jejaring relasi strategis untuk kemajuan instansi (B=5, E=4, D=3, A=2, C=1)."
  },
  {
    "id": "tkp_77", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Saat Anda memimpin rapat evaluasi bulanan, dua orang staf senior yang memiliki pengaruh besar di kantor saling beradu argumen pribadi dan membuat suasana rapat tegang. Sikap Anda adalah...",
    "options": {
      "A": "Membiarkan mereka berkelahi agar suasana menjadi seru",
      "B": "Menengahi dengan tenang dan tegas, mengingatkan kembali agenda objektif rapat, memberikan waktu masing-masing menyampaikan inti substansi secara tertib, dan mencari solusi konsensus",
      "C": "Menutup rapat secara mendadak dan keluar dari ruangan",
      "D": "Membela salah satu pihak yang lebih Anda sukai",
      "E": "Menyalahkan keduanya dengan kata-kata kasar"
    },
    "points": {"A": 1, "B": 5, "C": 2, "D": 3, "E": 4},
    "answer": "B",
    "explanation": "Kemampuan kepemimpinan dan manajemen konflik dalam jejaring kerja tim (B=5, E=4, D=3, C=2, A=1)."
  },
  {
    "id": "tkp_78", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Rekan kerja dari bagian keuangan sering terlambat memberikan data realisasi anggaran yang Anda butuhkan untuk menyusun laporan evaluasi. Sikap Anda adalah...",
    "options": {
      "A": "Menyindir rekan tersebut di status media sosial",
      "B": "Mendatangi rekan tersebut secara santun, menanyakan kendala yang dihadapinya, serta menyepakati jadwal pengiriman data berkala yang realistis bagi kedua belah pihak",
      "C": "Membuat laporan fiktif tanpa data keuangan yang valid",
      "D": "Mendiamkan saja sampai pimpinan yang memarahi rekan tersebut",
      "E": "Memusuhi dan tidak mau lagi menyapa rekan tersebut di kantor"
    },
    "points": {"A": 1, "B": 5, "C": 2, "D": 3, "E": 4},
    "answer": "B",
    "explanation": "Komunikasi asertif antardivisi untuk menjaga kelancaran alur koordinasi kerja (B=5, E=4, D=3, C=2, A=1)."
  },
  {
    "id": "tkp_79", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Anda baru saja dimutasi ke kantor cabang daerah terpencil dengan budaya kerja dan bahasa daerah yang berbeda dari daerah asal Anda. Cara Anda beradaptasi adalah...",
    "options": {
      "A": "Menuntut rekan kerja di kantor baru mengikuti gaya hidup dan bahasa daerah asal Anda",
      "B": "Membuka diri, menghormati adat istiadat setempat, aktif berinteraksi dengan rekan kerja baru, dan mempelajari norma lokal agar cepat membaur",
      "C": "Mengurung diri di rumah dinas dan hanya keluar saat jam kerja formal",
      "D": "Mengajukan surat pengunduran diri karena merasa tidak cocok dengan lingkungannya",
      "E": "Membanding-bandingkan keunggulan kantor lama Anda di depan mereka"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 1, "E": 4},
    "answer": "B",
    "explanation": "Adaptabilitas tinggi dan kemampuan membangun jejaring di lingkungan baru yang heterogen (B=5, E=4, C=3, A=2, D=1)."
  },
  {
    "id": "tkp_80", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Organisasi profesi tempat Anda bernaung mengadakan forum diskusi nasional. Apa yang akan Anda lakukan dalam forum tersebut?",
    "options": {
      "A": "Hanya hadir saat sesi absensi untuk mendapatkan sertifikat lalu pulang",
      "B": "Aktif berpartisipasi dalam diskusi, bertukar ide pemecahan masalah dengan anggota dari instansi lain, dan memperluas relasi profesional",
      "C": "Duduk di barisan belakang sambil bermain game ponsel",
      "D": "Mencela pendapat peserta lain yang berbeda sudut pandang",
      "E": "Tidur di pojok ruangan selama sesi pemaparan berlangsung"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 1, "E": 4},
    "answer": "B",
    "explanation": "Pemanfaatan jejaring profesional untuk pengayaan wawasan dan peningkatan kompetensi (B=5, E=4, C=3, A=2, D=1)."
  },
  {
    "id": "tkp_81", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Sebuah tugas kelompok membutuhkan koordinasi cepat antara staf lapangan dan staf kantor. Platform komunikasi mana yang paling efektif Anda rekomendasikan?",
    "options": {
      "A": "Mengirim surat resmi bertanda tangan basah lewat kurir setiap ada perubahan kecil",
      "B": "Membuat grup komunikasi terpusat di aplikasi perpesanan instan dengan pembagian tugas yang jelas dan transparansi progres berkala",
      "C": "Menunggu rapat bulanan berikutnya untuk berkoordinasi",
      "D": "Menelepon staf lapangan satu per satu di luar jam kerja",
      "E": "Meminta staf lapangan bolak-balik ke kantor setiap jam"
    },
    "points": {"A": 2, "B": 5, "C": 1, "D": 4, "E": 3},
    "answer": "B",
    "explanation": "Optimalisasi media jejaring kerja modern untuk kecepatan dan efisiensi komunikasi tim (B=5, D=4, E=3, A=2, C=1)."
  },

  # 82-88: Sosial Budaya
  {
    "id": "tkp_82", "category": "TKP", "subcategory": "Sosial Budaya",
    "question": "Di kantor Anda yang memiliki latar belakang suku dan agama majemuk, salah satu rekan kerja sedang merayakan hari raya keagamaannya. Sikap Anda adalah...",
    "options": {
      "A": "Pura-pura tidak tahu agar tidak dianggap mencampuri urusan agama orang lain",
      "B": "Memberikan ucapan selamat secara tulus dan bersedia saling bertukar jadwal piket dinas agar rekan tersebut dapat beribadah dengan tenang",
      "C": "Meminta traktiran mewah kepada rekan tersebut di depan semua orang",
      "D": "Mengkritik ritual peribadatan mereka di media sosial",
      "E": "Menolak bekerja sama dengan rekan tersebut selama masa hari rayanya"
    },
    "points": {"A": 3, "B": 5, "C": 4, "D": 1, "E": 2},
    "answer": "B",
    "explanation": "Toleransi aktif, empati, dan penghargaan tulus terhadap keberagaman sosial budaya di lingkungan kerja (B=5, C=4, A=3, E=2, D=1)."
  },
  {
    "id": "tkp_83", "category": "TKP", "subcategory": "Sosial Budaya",
    "question": "Ketika Anda sedang melayani warga di kantor, datang seorang warga dari kelompok minoritas dengan pakaian adat tradisional mereka. Beberapa orang di ruang tunggu memandang dengan aneh dan berbisik-bisik. Tindakan Anda adalah...",
    "options": {
      "A": "Ikut menertawakan pakaian warga tersebut bersama pengunjung lain",
      "B": "Menyambut warga tersebut dengan penuh rasa hormat, melayani kebutuhannya secara profesional dan setara, serta menunjukkan sikap inklusif",
      "C": "Menyuruh warga tersebut mengganti pakaian modern terlebih dahulu sebelum dilayani",
      "D": "Melayaninya di sudut tersembunyi agar tidak menarik perhatian orang",
      "E": "Meminta satpam membawa warga tersebut keluar ruangan"
    },
    "points": {"A": 1, "B": 5, "C": 2, "D": 3, "E": 4},
    "answer": "B",
    "explanation": "Sikap inklusif, non-diskriminatif, dan menjunjung tinggi penghormatan terhadap keragaman budaya Nusantara (B=5, E=4, D=3, C=2, A=1)."
  },
  {
    "id": "tkp_84", "category": "TKP", "subcategory": "Sosial Budaya",
    "question": "Dalam rangka memperingati HUT instansi, panitia merencanakan pentas seni bertema budaya daerah. Apa kontribusi yang dapat Anda berikan?",
    "options": {
      "A": "Menolak hadir karena tidak menyukai musik tradisional",
      "B": "Aktif mendukung, ikut berpartisipasi menampilkan kesenian daerah atau membantu logistik kepanitiaan agar acara pelestarian budaya berjalan sukses",
      "C": "Mengusulkan mengganti seluruh acara budaya dengan pesta musik barat",
      "D": "Menghadiri acara hanya untuk mengambil jatah makan lalu pulang",
      "E": "Mengeluhkan anggaran acara di media sosial"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 4, "E": 1},
    "answer": "B",
    "explanation": "Apresiasi terhadap nilai kearifan lokal dan pelestarian budaya bangsa di lingkungan kerja (B=5, D=4, C=3, A=2, E=1)."
  },
  {
    "id": "tkp_85", "category": "TKP", "subcategory": "Sosial Budaya",
    "question": "Saat makan siang bersama di kantor, salah satu rekan kerja membawa makanan khas daerahnya yang memiliki aroma dan bentuk yang belum pernah Anda temui sebelumnya. Sikap Anda adalah...",
    "options": {
      "A": "Mengejek makanannya berbau aneh di depan rekan-rekan lain",
      "B": "Menghargai keragaman kuliner nusantara, menyapa dengan ramah, dan jika ditawari mencicipinya dengan rasa syukur dan sopan",
      "C": "Menjauh dari meja makan sambil menutup hidung secara demonstratif",
      "D": "Menyuruh rekan tersebut membuang makanannya ke tempat sampah",
      "E": "Melaporkan rekan tersebut ke bagian kepegawaian"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 1, "E": 4},
    "answer": "B",
    "explanation": "Etika menghargai perbedaan tradisi kuliner daerah dan menjunjung kesantunan pergaulan (B=5, E=4, C=3, A=2, D=1)."
  },
  {
    "id": "tkp_86", "category": "TKP", "subcategory": "Sosial Budaya",
    "question": "Bagaimana pandangan Anda mengenai stereotipe suku tertentu di masyarakat yang sering diasosiasikan dengan sifat negatif?",
    "options": {
      "A": "Mempercayai stereotipe tersebut sebagai fakta mutlak",
      "B": "Menolak stereotipe dan prasangka sempit, serta memandang setiap individu secara objektif berdasarkan kepribadian dan perilakunya masing-masing",
      "C": "Ikut menyebarluaskan lelucon bernada stereotipe di grup percakapan",
      "D": "Menghindari bergaul dengan orang yang berasal dari suku tersebut",
      "E": "Menganggap semua suku sama-sama memiliki keburukan yang tidak bisa diubah"
    },
    "points": {"A": 2, "B": 5, "C": 1, "D": 3, "E": 4},
    "answer": "B",
    "explanation": "Bebas dari prasangka rasial/etnis (prejudice) dan menjunjung prinsip objektivitas kemanusiaan (B=5, E=4, D=3, A=2, C=1)."
  },
  {
    "id": "tkp_87", "category": "TKP", "subcategory": "Sosial Budaya",
    "question": "Ketika Anda bertugas di sebuah desa adat, kepala desa meminta seluruh tamu mengenakan kain selendang tradisional sebagai bentuk penghormatan adat saat memasuki balai pertemuan. Sikap Anda adalah...",
    "options": {
      "A": "Menolak dengan arogan karena Anda adalah pejabat pemerintah dari pusat",
      "B": "Mengenakannya dengan senang hati dan rasa hormat sebagai wujud penghargaan terhadap kearifan lokal setempat",
      "C": "Mengenakannya sambil terus mengeluh dan mengejek tradisi tersebut",
      "D": "Membatalkan pertemuan penting tersebut karena tidak mau memakai kain adat",
      "E": "Membayar uang denda agar tidak perlu memakai kain selendang"
    },
    "points": {"A": 1, "B": 5, "C": 3, "D": 2, "E": 4},
    "answer": "B",
    "explanation": "Prinsip 'Di mana bumi dipijak, di situ langit dijunjung' – menghargai adat istiadat dan tata krama lokal (B=5, E=4, C=3, D=2, A=1)."
  },
  {
    "id": "tkp_88", "category": "TKP", "subcategory": "Sosial Budaya",
    "question": "Di lingkungan tempat tinggal Anda terdapat warga pendatang baru dari berbagai daerah di Indonesia. Sebagai bagian dari masyarakat, apa yang akan Anda lakukan?",
    "options": {
      "A": "Mengawasi gerak-gerik mereka dengan rasa curiga berlebihan",
      "B": "Menyapa dengan hangat, memperkenalkan diri, dan mengajak mereka berpartisipasi dalam kegiatan sosial kemasyarakatan di lingkungan RT/RW",
      "C": "Membiarkan mereka hidup terisolasi tanpa interaksi",
      "D": "Meminta pengurus RT mengusir pendatang yang berbeda keyakinan",
      "E": "Hanya menyapa jika mereka memberikan bingkisan makanan"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 1, "E": 4},
    "answer": "B",
    "explanation": "Kerukunan bertetangga dan keterbukaan sosial yang mempererat kohesi sosial masyarakat (B=5, E=4, C=3, A=2, D=1)."
  },

  # 89-95: TIK (Teknologi Informasi & Komunikasi)
  {
    "id": "tkp_89", "category": "TKP", "subcategory": "TIK",
    "question": "Instansi Anda baru saja merilis pembaruan sistem absensi berbasis kecerdasan buatan (face recognition dan geotagging). Sebagian rekan mengeluh kesulitan menggunakannya. Tindakan Anda adalah...",
    "options": {
      "A": "Ikut memprotes kebijakan pimpinan dan meminta kembali ke absensi manual",
      "B": "Cepat mempelajari fitur sistem baru tersebut, lalu membuat panduan visual ringkas serta dengan sabar membimbing rekan yang kesulitan",
      "C": "Menertawakan ketidaktahuan rekan yang belum melek teknologi",
      "D": "Menggunakan sistem tersebut hanya untuk diri sendiri tanpa memedulikan rekan lain",
      "E": "Mencari celah agar bisa memanipulasi lokasi absensi"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 4, "E": 1},
    "answer": "B",
    "explanation": "Kemampuan adaptasi teknologi dan kemauan menjadi agen perubahan yang memfasilitasi rekan kerja (B=5, D=4, C=3, A=2, E=1)."
  },
  {
    "id": "tkp_90", "category": "TKP", "subcategory": "TIK",
    "question": "Anda menerima email berkedok notifikasi resmi yang meminta verifikasi password akun portal kepegawaian Anda dengan menyertakan tautan asing mencurigakan. Tindakan Anda adalah...",
    "options": {
      "A": "Langsung mengklik tautan dan memasukkan password akun kedinasan Anda",
      "B": "Mengenali indikasi serangan phishing, tidak mengklik tautan apa pun, segera melaporkan insiden tersebut ke tim keamanan siber/CSIRT instansi, dan mengedukasi rekan sekitar",
      "C": "Meneruskan email mencurigakan tersebut ke seluruh rekan kantor",
      "D": "Membalas email tersebut dengan kata-kata makian",
      "E": "Menghapus email tanpa melaporkannya ke pihak berwenang"
    },
    "points": {"A": 1, "B": 5, "C": 2, "D": 3, "E": 4},
    "answer": "B",
    "explanation": "Kesadaran keamanan informasi (cybersecurity awareness) dan kepatuhan pada SOP penanganan insiden digital (B=5, E=4, D=3, C=2, A=1)."
  },
  {
    "id": "tkp_91", "category": "TKP", "subcategory": "TIK",
    "question": "Pekerjaan penyusunan laporan dinas Anda membutuhkan kolaborasi data secara bersamaan dengan anggota tim yang berada di lokasi berbeda. Solusi teknologi yang paling efektif adalah...",
    "options": {
      "A": "Mengetik di kertas lalu mengirimkan fotokopinya lewat pos",
      "B": "Memanfaatkan platform dokumen kolaboratif berbasis cloud yang aman dengan hak akses terkelola dan fitur riwayat revisi riil",
      "C": "Menunggu sampai seluruh anggota tim bisa berkumpul di satu ruangan fisik",
      "D": "Mengirimkan file revisi berkali-kali lewat flashdisk secara bergantian",
      "E": "Menyuruh satu orang mengetik seluruhnya tanpa masukan tim"
    },
    "points": {"A": 1, "B": 5, "C": 2, "D": 3, "E": 4},
    "answer": "B",
    "explanation": "Pemanfaatan teknologi komputasi awan (cloud) untuk efisiensi kolaborasi kerja jarak jauh (B=5, E=4, D=3, C=2, A=1)."
  },
  {
    "id": "tkp_92", "category": "TKP", "subcategory": "TIK",
    "question": "Banyak dokumen arsip fisik di kantor Anda yang rentan rusak dimakan usia dan membutuhkan waktu lama saat dicari kembali. Inisiatif teknologi yang tepat Anda lakukan adalah...",
    "options": {
      "A": "Membiarkannya lapuk karena bukan tanggung jawab Anda",
      "B": "Mengusulkan program digitalisasi arsip melalui pemindaian terstruktur, pemberian metadata pencarian, dan penyimpanan terenkripsi pada server data kantor",
      "C": "Membakar dokumen lama agar ruangan kantor menjadi lapang",
      "D": "Menjual arsip lama tersebut ke pedagang loak",
      "E": "Menyembunyikan dokumen penting di laci meja pribadi Anda"
    },
    "points": {"A": 2, "B": 5, "C": 1, "D": 1, "E": 3},
    "answer": "B",
    "explanation": "Inovasi alih media digital untuk preservasi data dan efisiensi temu kembali informasi (B=5, E=3, A=2, C=1, D=1)."
  },
  {
    "id": "tkp_93", "category": "TKP", "subcategory": "TIK",
    "question": "Bagaimana sikap Anda terhadap pemanfaatan teknologi kecerdasan buatan (Artificial Intelligence / AI) dalam membantu pekerjaan sehari-hari di kantor?",
    "options": {
      "A": "Menolak menggunakan AI karena khawatir teknologi akan menggantikan seluruh peran ASN",
      "B": "Memanfaatkan AI secara etis dan bijak sebagai alat bantu meningkatkan produktivitas analisis dan penyusunan draf, namun tetap melakukan verifikasi dan validasi kritis secara mandiri",
      "C": "Menyerahkan seluruh keputusan dinas secara membabi buta kepada output AI tanpa membaca kembali",
      "D": "Menggunakan AI untuk mengerjakan urusan pribadi saat jam kerja dinas",
      "E": "Mengunggah data rahasia instansi ke platform AI publik tanpa pertimbangan privasi"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 4, "E": 1},
    "answer": "B",
    "explanation": "Pemanfaatan teknologi mutakhir secara produktif, etis, dan tetap menjaga kendali mutu serta perlindungan data rahasia (B=5, D=4, C=3, A=2, E=1)."
  },
  {
    "id": "tkp_94", "category": "TKP", "subcategory": "TIK",
    "question": "Ketika Anda sedang mempresentasikan materi laporan dengan proyektor di hadapan pimpinan, laptop Anda tiba-tiba mengalami hang (tidak merespons). Sikap Anda adalah...",
    "options": {
      "A": "Panik, memukul proyektor, dan membatalkan presentasi",
      "B": "Tetap tenang, meminta izin sebentar untuk me-restart laptop atau berganti ke perangkat cadangan yang sudah disiapkan di flashdisk, sambil tetap menjelaskan poin pokok secara lisan",
      "C": "Menyalahkan staf yang menyediakan proyektor di depan pimpinan",
      "D": "Duduk diam sambil menunggu laptop hidup sendiri",
      "E": "Menangis di hadapan para peserta rapat"
    },
    "points": {"A": 1, "B": 5, "C": 2, "D": 3, "E": 4},
    "answer": "B",
    "explanation": "Ketenangan, manajemen krisis teknis, kesiapan rencana cadangan (contingency plan), dan profesionalisme penguasaan substansi (B=5, E=4, D=3, C=2, A=1)."
  },
  {
    "id": "tkp_95", "category": "TKP", "subcategory": "TIK",
    "question": "Pimpinan menugaskan Anda membuat dashboard visualisasi data capaian kinerja instansi yang mudah dipahami oleh publik. Langkah awal yang Anda lakukan adalah...",
    "options": {
      "A": "Membuat grafik rumit dengan warna mencolok tanpa memedulikan akurasi data",
      "B": "Mempelajari kebutuhan informasi publik, membersihkan data mentah, dan memilih grafik ringkas serta informatif yang sesuai kaidah visualisasi data",
      "C": "Menyalin tampilan dashboard kementerian lain secara sembarangan",
      "D": "Menolak tugas tersebut karena bukan latar belakang desainer grafis",
      "E": "Mengarang angka capaian agar instansi terlihat berprestasi"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 4, "E": 1},
    "answer": "B",
    "explanation": "Orientasi kualitas penyajian data, keakuratan informasi, dan literasi visual digital (B=5, D=4, C=3, A=2, E=1)."
  },

  # 96-103: Profesionalisme
  {
    "id": "tkp_96", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Anda memiliki rencana berlibur bersama keluarga yang sudah dipersiapkan sejak lama. Tiba-tiba sehari sebelum berangkat, pimpinan memanggil Anda untuk menangani penugasan mendadak penanganan bencana yang membutuhkan keahlian spesifik Anda. Sikap Anda adalah...",
    "options": {
      "A": "Menolak panggilan dinas dan mematikan ponsel agar tidak bisa dihubungi",
      "B": "Memberikan pengertian kepada keluarga dengan tulus, menunda jadwal liburan, dan segera menjalankan tugas kedinasan demi kemanusiaan dan panggilan tugas negara",
      "C": "Pergi berlibur tetapi dengan rasa bersalah sepanjang perjalanan",
      "D": "Menuntut kenaikan pangkat kilat sebagai syarat kesediaan menjalankan tugas",
      "E": "Menunjuk staf magang yang belum berpengalaman untuk menggantikan posisi Anda"
    },
    "points": {"A": 1, "B": 5, "C": 3, "D": 2, "E": 4},
    "answer": "B",
    "explanation": "Prioritas integritas kedinasan, loyalitas pada bangsa, dan kesiapan berkorban untuk kepentingan publik (B=5, E=4, C=3, D=2, A=1)."
  },
  {
    "id": "tkp_97", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Di kantor, Anda ditempatkan satu ruangan dengan rekan kerja yang sering mengeluh, bergosip, dan menyebarkan atmosfer negatif. Cara Anda menyikapinya adalah...",
    "options": {
      "A": "Ikut aktif bergosip agar diterima dalam pergaulan kantor",
      "B": "Tetap fokus dan berkinerja tinggi pada tanggung jawab tugas Anda, bersikap ramah sewajarnya, serta mengalihkan topik pembicaraan ke hal-hal positif yang membangun",
      "C": "Memusuhi dan mengajak staf lain untuk memboikot rekan tersebut",
      "D": "Mengajukan surat pindah ruangan setiap minggu",
      "E": "Membalas keluhannya dengan keluhan yang lebih berlebihan"
    },
    "points": {"A": 1, "B": 5, "C": 2, "D": 4, "E": 3},
    "answer": "B",
    "explanation": "Keteguhan menjaga etos kerja pribadi di tengah lingkungan yang kurang kondusif (B=5, D=4, E=3, C=2, A=1)."
  },
  {
    "id": "tkp_98", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Atasan memberikan kritik tajam dan evaluasi korektif terhadap laporan kerja yang baru saja Anda serahkan karena terdapat beberapa kekeliruan perhitungan. Sikap Anda adalah...",
    "options": {
      "A": "Merasa tersinggung, sakit hati, dan tidak mau lagi menyapa atasan",
      "B": "Menerima masukan dengan lapang dada dan objektif, segera meneliti kembali letak kekeliruan, memperbaikinya dengan cermat, dan menjadikannya pelajaran agar tidak terulang",
      "C": "Menyalahkan anggota tim lain atas kekeliruan tersebut",
      "D": "Membantah seluruh kritik atasan dengan nada emosional",
      "E": "Meninggalkan laporan tersebut di meja atasan tanpa diperbaiki"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 1, "E": 4},
    "answer": "B",
    "explanation": "Kedewasaan menyikapi kritik, akuntabilitas pribadi, dan komitmen perbaikan mutu kerja (B=5, E=4, C=3, A=2, D=1)."
  },
  {
    "id": "tkp_99", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Anda ditugaskan mempelajari sebuah perangkat lunak sistem analisis baru yang belum pernah Anda gunakan sebelumnya dalam waktu 3 hari. Langkah yang Anda ambil adalah...",
    "options": {
      "A": "Menyerah sebelum mencoba dan menyatakan tidak sanggup kepada pimpinan",
      "B": "Mempelajari dokumentasi resmi secara intensif, mengikuti tutorial daring, berkonsultasi dengan ahli jika menemui kendala, dan mempraktikkannya langsung hingga mahir",
      "C": "Menyuruh rekan kerja lain mengerjakannya secara diam-diam",
      "D": "Menunda belajar hingga hari ketiga dan membuat alasan sakit",
      "E": "Mengeluhkan beban kerja di media sosial"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 1, "E": 4},
    "answer": "B",
    "explanation": "Semangat belajar mandiri (growth mindset), proaktif, dan daya juang tinggi menghadapi tantangan kompetensi baru (B=5, E=4, C=3, A=2, D=1)."
  },
  {
    "id": "tkp_100", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Seorang teman akrab di kantor meminjam username dan password akun sistem Anda untuk menyelesaikan pekerjaannya karena akun miliknya sedang terblokir. Sikap Anda adalah...",
    "options": {
      "A": "Memberikannya dengan senang hati karena ia adalah sahabat dekat Anda",
      "B": "Menolak dengan santun dan menjelaskan bahwa kredensial akun bersifat rahasia dan merupakan tanggung jawab pribadi sesuai standar keamanan instansi, lalu membantunya menghubungi tim helpdesk IT",
      "C": "Memberikan password palsu agar ia kesal",
      "D": "Melaporkannya ke polisi atas tuduhan peretasan",
      "E": "Meminta imbalan uang sebagai biaya sewa akun"
    },
    "points": {"A": 2, "B": 5, "C": 3, "D": 1, "E": 4},
    "answer": "B",
    "explanation": "Kepatuhan pada kode etik kerahasiaan data dan regulasi keamanan informasi dengan tetap memberikan solusi yang sah (B=5, E=4, C=3, A=2, D=1)."
  },
  {
    "id": "tkp_101", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Ketika Anda sedang fokus menyelesaikan tugas dinas prioritas tinggi yang harus dikumpulkan 1 jam lagi, seorang rekan meminta Anda mencetakkan dokumen pribadinya. Sikap Anda adalah...",
    "options": {
      "A": "Memarahi rekan tersebut dengan kata-kata kasar",
      "B": "Menjelaskan dengan ramah bahwa Anda sedang menyelesaikan tugas prioritas instansi yang mendekati deadline, dan mempersilakannya menggunakan printer secara mandiri atau membantunya setelah tugas Anda selesai",
      "C": "Meninggalkan tugas prioritas Anda demi mencetak dokumen rekan tersebut",
      "D": "Pura-pura tidak mendengar permintaannya",
      "E": "Merusak printer agar tidak ada yang bisa menggunakannya"
    },
    "points": {"A": 2, "B": 5, "C": 1, "D": 4, "E": 3},
    "answer": "B",
    "explanation": "Skala prioritas tugas kedinasan dan ketegasan komunikasi asertif yang santun (B=5, D=4, E=3, A=2, C=1)."
  },
  {
    "id": "tkp_102", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Anda melihat celah efisiensi dalam prosedur administrasi kantor yang selama ini memakan waktu lama namun dianggap lumrah karena sudah berlangsung bertahun-tahun. Tindakan Anda adalah...",
    "options": {
      "A": "Diam saja karena merasa masih pegawai junior yang belum pantas berbicara",
      "B": "Menyusun kajian ringkas perbandingan efisiensi waktu dan biaya, lalu menyampaikannya secara santun dan konstruktif kepada pimpinan sebagai usulan perbaikan",
      "C": "Mengkritik pimpinan di media sosial atas ketidakefisienan tersebut",
      "D": "Bekerja lambat mengikuti sistem lama yang tidak efisien",
      "E": "Menyuruh bawahan Anda melanggar SOP secara diam-diam"
    },
    "points": {"A": 3, "B": 5, "C": 1, "D": 4, "E": 2},
    "answer": "B",
    "explanation": "Inisiatif perbaikan inovatif yang didasarkan pada data dan disampaikan lewat jalur resmi organisasi (B=5, D=4, A=3, E=2, C=1)."
  },
  {
    "id": "tkp_103", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Dalam sebuah proyek, target kerja yang sudah ditetapkan bersama gagal tercapai karena Anda salah mengestimasi waktu pelaksanaan. Sikap Anda menghadapi situasi ini adalah...",
    "options": {
      "A": "Mencari kambing hitam dan menyalahkan vendor eksternal",
      "B": "Mengakui kekeliruan estimasi secara jantan dan bertanggung jawab di hadapan tim, memaparkan evaluasi kegagalan, dan menyusun rencana pemulihan (recovery plan) yang realistis",
      "C": "Menghilang dari kantor dan mematikan alat komunikasi",
      "D": "Mengundurkan diri dari jabatan ASN karena malu",
      "E": "Memanipulasi data laporan hasil agar terlihat seolah-olah target sudah tercapai"
    },
    "points": {"A": 2, "B": 5, "C": 1, "D": 3, "E": 4},
    "answer": "B",
    "explanation": "Tanggung jawab moral dan akuntabilitas profesional dalam mengakui kesalahan dan berfokus pada mitigasi solusi (B=5, E=4, D=3, A=2, C=1)."
  },

  # 104-110: Anti Radikalisme
  {
    "id": "tkp_104", "category": "TKP", "subcategory": "Anti Radikalisme",
    "question": "Di media sosial beredar narasi propaganda yang mengajak aparatur sipil negara untuk memboikot upacara bendera dan menyatakan bahwa sistem pemerintahan demokrasi bertentangan dengan keyakinan agama. Sikap Anda sebagai ASN adalah...",
    "options": {
      "A": "Ikut menyebarkan konten tersebut ke grup dinas kantor",
      "B": "Tegas menolak paham tersebut, memegang teguh sumpah setia kepada Pancasila dan UUD 1945, serta mengedukasi lingkungan sekitar tentang pentingnya konsensus kebangsaan",
      "C": "Menjadi ragu-ragu dan mulai mempertimbangkan untuk tidak ikut upacara",
      "D": "Menghina pembuat konten dengan ujaran kebencian balasan",
      "E": "Mendiamkan saja karena menganggap itu urusan pribadi masing-masing"
    },
    "points": {"A": 1, "B": 5, "C": 2, "D": 3, "E": 4},
    "answer": "B",
    "explanation": "Keteguhan komitmen kebangsaan, kesetiaan pada Pancasila dan konstitusi, serta peran aktif membentengi diri dan masyarakat dari propaganda intoleran (B=5, E=4, D=3, C=2, A=1)."
  },
  {
    "id": "tkp_105", "category": "TKP", "subcategory": "Anti Radikalisme",
    "question": "Salah seorang rekan kerja yang baru saja bergabung mulai sering memperlihatkan sikap eksklusif, menolak bersalaman dengan rekan kerja yang berbeda keyakinan, dan mencap rekan lain yang tidak sepaham sebagai kelompok sesat. Tindakan Anda adalah...",
    "options": {
      "A": "Mengajaknya berdebat di depan umum hingga memicu permusuhan",
      "B": "Mengajak rekan tersebut berdialog secara personal dengan santun, mengingatkan kode etik netralitas dan kerukunan ASN, serta melaporkan ke pimpinan/bagian kepegawaian bila terindikasi radikalisme aktif",
      "C": "Ikut-ikutan bersikap intoleran agar tidak dikucilkan oleh rekan tersebut",
      "D": "Mengabaikannya dan membiarkan pahamnya menyebar ke pegawai lain",
      "E": "Menyebarkan rumor buruk tentang kehidupan pribadinya"
    },
    "points": {"A": 3, "B": 5, "C": 1, "D": 4, "E": 2},
    "answer": "B",
    "explanation": "Deteksi dini dan penanganan bijak berbasis kode etik kedinasan untuk meredam bibit eksklusivisme dan radikalisme (B=5, D=4, A=3, E=2, C=1)."
  },
  {
    "id": "tkp_106", "category": "TKP", "subcategory": "Anti Radikalisme",
    "question": "Anda diundang bergabung dalam sebuah organisasi kemasyarakatan yang secara terbuka mengusung agenda mengganti Pancasila dan merombak bentuk Negara Kesatuan Republik Indonesia melalui aksi kekerasan. Sikap Anda adalah...",
    "options": {
      "A": "Menolak dengan tegas ajakan tersebut, menjauhi organisasi terlarang itu, dan melaporkan indikasi gerakannya kepada instansi penegak hukum yang berwenang",
      "B": "Menerima undangan untuk melihat-lihat kegiatannya terlebih dahulu",
      "C": "Bergabung diam-diam tanpa sepengetahuan atasan",
      "D": "Menyumbangkan dana operasional kepada organisasi tersebut",
      "E": "Mengajak rekan kantor lain untuk ikut mendaftar"
    },
    "points": {"A": 5, "B": 2, "C": 1, "D": 1, "E": 1},
    "answer": "A",
    "explanation": "Kewaspadaan tinggi dan ketegasan mutlak menolak setiap bentuk gerakan atau organisasi terlarang yang merongrong kedaulatan NKRI (A=5, B=2, C=1, D=1, E=1)."
  },
  {
    "id": "tkp_107", "category": "TKP", "subcategory": "Anti Radikalisme",
    "question": "Di grup alumni sekolah, beberapa anggota membagikan video orasi provokatif yang mengajak pembangkangan sipil dan penyerangan terhadap simbol-simbol negara. Respon Anda yang paling tepat adalah...",
    "options": {
      "A": "Mendukung dan membagikan ulang video tersebut ke grup kantor",
      "B": "Mengingatkan dengan sopan namun tegas bahwa menyebarkan ajakan kekerasan melanggar hukum dan memecah belah bangsa, serta menyarankan agar konten tersebut dihapus",
      "C": "Menyukai postingan tersebut demi menjaga pertemanan alumni",
      "D": "Keluar dari grup tanpa memberikan peringatan apa pun",
      "E": "Menantang duel fisik seluruh anggota yang mendukung video tersebut"
    },
    "points": {"A": 1, "B": 5, "C": 2, "D": 4, "E": 3},
    "answer": "B",
    "explanation": "Peran sebagai penyejuk dan penegak literasi kebangsaan dalam ruang publik digital (B=5, D=4, E=3, C=2, A=1)."
  },
  {
    "id": "tkp_108", "category": "TKP", "subcategory": "Anti Radikalisme",
    "question": "Bagaimana pandangan Anda tentang hubungan antara nilai ajaran agama dengan ketaatan pada hukum konstitusi negara Republik Indonesia?",
    "options": {
      "A": "Keduanya bertentangan secara mutlak dan tidak akan pernah bisa disatukan",
      "B": "Keduanya selaras dan saling menguatkan; ketaatan pada hukum negara yang adil merupakan wujud nyata pengamalan nilai-nilai moral agama untuk kemaslahatan bersama",
      "C": "Hukum negara harus diabaikan jika tidak ditulis persis seperti kitab suci",
      "D": "Agama tidak boleh ada dalam kehidupan bermasyarakat",
      "E": "Hukum negara hanya berlaku bagi orang yang tidak beragama"
    },
    "points": {"A": 1, "B": 5, "C": 2, "D": 3, "E": 4},
    "answer": "B",
    "explanation": "Moderasi beragama dan kesadaran bahwa nilai keagamaan dan konstitusi negara di Indonesia saling menopang demi kedamaian dan keadilan bersama (B=5, E=4, D=3, C=2, A=1)."
  },
  {
    "id": "tkp_109", "category": "TKP", "subcategory": "Anti Radikalisme",
    "question": "Sebuah rumah ibadah di lingkungan Anda mendapatkan penolakan dari segelintir kelompok intoleran yang berpotensi memicu gesekan antargaul. Langkah bijak yang Anda dukung adalah...",
    "options": {
      "A": "Ikut serta melakukan aksi penolakan dan pembongkaran paksa",
      "B": "Mendorong penyelesaian musyawarah melalui Forum Kerukunan Umat Beragama (FKUB) dan aparat pemerintah setempat sesuai koridor peraturan perundang-undangan yang berlaku",
      "C": "Menyerang kelompok yang menolak dengan kekerasan bersenjata",
      "D": "Membiarkan konflik membesar agar menjadi perhatian dunia internasional",
      "E": "Pindah rumah ke tempat lain"
    },
    "points": {"A": 1, "B": 5, "C": 2, "D": 1, "E": 3},
    "answer": "B",
    "explanation": "Penyelesaian konflik horizontal melalui musyawarah hukum, institusi resmi (FKUB), dan perlindungan hak konstitusional warga negara (B=5, E=3, C=2, A=1, D=1)."
  },
  {
    "id": "tkp_110", "category": "TKP", "subcategory": "Anti Radikalisme",
    "question": "Sebagai calon ASN, apa komitmen utama Anda dalam menjaga persatuan dan kesatuan bangsa di tengah ancaman polarisasi ideologi?",
    "options": {
      "A": "Mementingkan keuntungan materi pribadi di atas segalanya",
      "B": "Menjadi perekat dan pemersatu bangsa, menjunjung tinggi netralitas, melayani seluruh warga tanpa diskriminasi, serta mengamalkan nilai-nilai Pancasila dalam ucapan dan tindakan",
      "C": "Hanya membela kelompok atau partai politik yang membantu kelulusan saya",
      "D": "Menjauhi pergaulan dengan masyarakat agar tidak terpengaruh politik",
      "E": "Bersikap apatis terhadap masa depan bangsa dan negara"
    },
    "points": {"A": 2, "B": 5, "C": 1, "D": 3, "E": 4},
    "answer": "B",
    "explanation": "Fungsi utama ASN sesuai Pasal 10 UU No. 5/2014 & UU No. 20/2023: Pelaksana kebijakan publik, pelayan publik, dan perekat serta pemersatu bangsa (B=5, E=4, D=3, A=2, C=1)."
  }
]

# Ambil soal SKB IT yang sudah ada
skb_it_questions = [
  {
    "id": "skb_1", "category": "Tata Kelola TI & SPBE", "subcategory": "Perpres 95/2018",
    "question": "Berdasarkan Peraturan Presiden Republik Indonesia Nomor 95 Tahun 2018 tentang Sistem Pemerintahan Berbasis Elektronik (SPBE), arsitektur SPBE terdiri atas enam domain utama. Domain yang mendefinisikan integrasi aliran data antarinstansi pemerintah untuk mewujudkan kebijakan 'Satu Data Indonesia' adalah...",
    "options": {
      "A": "Domain Layanan SPBE",
      "B": "Domain Aplikasi SPBE",
      "C": "Domain Data dan Informasi",
      "D": "Domain Infrastruktur SPBE",
      "E": "Domain Keamanan SPBE"
    },
    "answer": "C",
    "explanation": "Domain Data dan Informasi secara khusus mengatur standar data, metadata, interoperabilitas data, dan bagi pakai data pemerintah (Satu Data Indonesia)."
  },
  {
    "id": "skb_2", "category": "Tata Kelola TI & SPBE", "subcategory": "IT Governance (COBIT)",
    "question": "Dalam kerangka kerja tata kelola TI seperti COBIT 2019, terdapat pemisahan yang jelas antara tata kelola (Governance) dan manajemen (Management). Pernyataan yang paling tepat mendeskripsikan peran Governance adalah...",
    "options": {
      "A": "Merencanakan, membangun, menjalankan, dan memantau kegiatan teknis operasional harian (PBRM).",
      "B": "Mengevaluasi kebutuhan pemangku kepentingan, mengarahkan prioritas melalui pengambilan keputusan, dan memantau kinerja (EDM: Evaluate, Direct, Monitor).",
      "C": "Mengonfigurasi router, firewall, dan server aplikasi setiap hari.",
      "D": "Menulis kode program dan melakukan deployment fitur perangkat lunak ke server produksi.",
      "E": "Melayani keluhan tiket helpdesk dari para pengguna komputer instansi."
    },
    "answer": "B",
    "explanation": "Dalam COBIT, Governance berfokus pada EDM (Evaluate, Direct, Monitor) yang bertugas memastikan kebutuhan pemangku kepentingan terpenuhi secara strategis."
  },
  {
    "id": "skb_3", "category": "Rekayasa Perangkat Lunak", "subcategory": "Konsep OOP & Desain",
    "question": "Dalam paradigma Object-Oriented Programming (OOP) dan prinsip SOLID, prinsip 'Single Responsibility Principle (SRP)' menyatakan bahwa...",
    "options": {
      "A": "Sebuah kelas harus terbuka untuk ekstensi tetapi tertutup untuk modifikasi.",
      "B": "Sebuah modul perangkat lunak atau kelas hanya boleh memiliki satu alasan untuk berubah (hanya mengemban satu tanggung jawab spesifik).",
      "C": "Kelas turunan harus dapat saling menggantikan kelas induknya tanpa menimbulkan galat pada sistem.",
      "D": "Antarmuka (interface) yang besar harus dipecah menjadi banyak antarmuka yang lebih kecil dan spesifik.",
      "E": "Modul tingkat tinggi tidak boleh bergantung pada modul tingkat rendah; keduanya harus bergantung pada abstraksi."
    },
    "answer": "B",
    "explanation": "S: Single Responsibility Principle menyatakan bahwa sebuah kelas hanya boleh memiliki 1 alasan untuk berubah."
  },
  {
    "id": "skb_4", "category": "Rekayasa Perangkat Lunak", "subcategory": "Arsitektur & API",
    "question": "Saat merancang layanan pertukaran data (API) antarinstansi pemerintah berbasis RESTful, metode HTTP (HTTP Verbs) yang dirancang bersifat 'Idempotent' adalah...",
    "options": {
      "A": "POST dan PATCH",
      "B": "GET, PUT, dan DELETE",
      "C": "POST saja",
      "D": "PATCH dan POST",
      "E": "Tidak ada metode HTTP yang bersifat idempotent"
    },
    "answer": "B",
    "explanation": "GET, PUT, dan DELETE bersifat idempotent karena eksekusi berkali-kali menghasilkan efek resource akhir yang identik di server."
  },
  {
    "id": "skb_5", "category": "Rekayasa Perangkat Lunak", "subcategory": "Version Control (Git)",
    "question": "Seorang Pranata Komputer ingin menggabungkan perubahan kode dari cabang (branch) 'fitur-layanan' ke cabang utama 'main' tanpa membuat commit merge tambahan, melainkan menyusun kembali commit-commit tersebut secara linear di atas commit terakhir 'main'. Perintah Git yang tepat untuk operasi ini adalah...",
    "options": {
      "A": "git merge --no-ff fitur-layanan",
      "B": "git checkout main dilanjutkan git rebase fitur-layanan",
      "C": "git checkout fitur-layanan dilanjutkan git rebase main",
      "D": "git reset --hard HEAD~1",
      "E": "git cherry-pick main"
    },
    "answer": "C",
    "explanation": "Untuk rebase secara linear: checkout ke branch fitur lalu 'git rebase main'."
  },
  {
    "id": "skb_6", "category": "Manajemen Basis Data", "subcategory": "Normalisasi Database",
    "question": "Sebuah tabel relasional dikatakan telah memenuhi kriteria Bentuk Normal Ketiga (3rd Normal Form / 3NF) apabila...",
    "options": {
      "A": "Tabel telah memenuhi 2NF dan tidak memiliki ketergantungan transitif (transitive dependency) antar atribut non-kunci utama.",
      "B": "Seluruh kolom hanya berisi nilai atomik tunggal dan tidak ada grup perulangan.",
      "C": "Tabel telah memenuhi 1NF dan setiap atribut non-kunci bergantung secara fungsional penuh pada primary key komposit.",
      "D": "Semua penentu fungsi (determinant) adalah candidate key dari tabel tersebut (BCNF).",
      "E": "Tabel tidak memiliki foreign key yang terhubung ke tabel lain."
    },
    "answer": "A",
    "explanation": "3NF mensyaratkan 2NF dan ketiadaan transitive dependency."
  },
  {
    "id": "skb_7", "category": "Manajemen Basis Data", "subcategory": "Optimasi Query & SQL",
    "question": "Diberikan tabel 'pegawai' dengan 500.000 baris data. Query pencarian berikut mengalami penurunan performa (lambat):\nSELECT * FROM pegawai WHERE SUBSTRING(nip, 1, 4) = '1995';\n\nLangkah optimasi yang paling tepat agar indeks B-Tree pada kolom 'nip' dapat digunakan secara optimal (Sargable Query) adalah...",
    "options": {
      "A": "Mengubah query menjadi: SELECT * FROM pegawai WHERE nip LIKE '1995%';",
      "B": "Mengubah tipe data kolom 'nip' menjadi TEXT.",
      "C": "Menghapus primary key pada tabel pegawai.",
      "D": "Menambahkan klausul ORDER BY RAND() pada query tersebut.",
      "E": "Menjalankan query tersebut dua kali berturut-turut agar tersimpan di cache."
    },
    "answer": "A",
    "explanation": "Menghilangkan pembungkus fungsi SUBSTRING() menjadikan query sargable dan indeks B-Tree dapat dimanfaatkan."
  },
  {
    "id": "skb_8", "category": "Jaringan Komputer", "subcategory": "Subnetting IPv4",
    "question": "Sebuah kantor instansi pemerintah diberikan blok alamat IP 192.168.10.0/26 untuk dialokasikan ke ruangan server. Berapakah jumlah alamat IP host yang valid (usable host IP) dan subnet mask desimal dari blok tersebut?",
    "options": {
      "A": "30 host, subnet mask 255.255.255.224",
      "B": "62 host, subnet mask 255.255.255.192",
      "C": "64 host, subnet mask 255.255.255.192",
      "D": "126 host, subnet mask 255.255.255.128",
      "E": "254 host, subnet mask 255.255.255.0"
    },
    "answer": "B",
    "explanation": "Prefix /26 menyisakan 6 bit host. Usable host = 2^6 - 2 = 62 host. Subnet mask = 255.255.255.192."
  },
  {
    "id": "skb_9", "category": "Jaringan Komputer", "subcategory": "Model OSI & Protokol",
    "question": "Protokol HTTPS berjalan di atas lapisan transport yang aman dengan enkripsi TLS/SSL. Pada Model Referensi OSI 7 Layer, enkripsi dan kompresi data ditangani secara khusus pada lapisan...",
    "options": {
      "A": "Lapisan Fisik (Physical Layer)",
      "B": "Lapisan Jaringan (Network Layer)",
      "C": "Lapisan Transport (Transport Layer)",
      "D": "Lapisan Presentasi (Presentation Layer)",
      "E": "Lapisan Sesi (Session Layer)"
    },
    "answer": "D",
    "explanation": "Presentation Layer (Layer 6) menangani enkripsi, kompresi, dan translasi format sintaks data."
  },
  {
    "id": "skb_10", "category": "Keamanan Informasi & Siber", "subcategory": "OWASP Top 10 & Web Security",
    "question": "Seorang penyerang menyisipkan skrip JavaScript berbahaya ke dalam kolom komentar formulir buku tamu web pemerintah. Ketika pengguna lain atau admin membuka halaman buku tamu tersebut, skrip tersebut dieksekusi secara otomatis oleh browser korban untuk mencuri session cookie. Jenis kerentanan keamanan ini adalah...",
    "options": {
      "A": "Stored Cross-Site Scripting (Stored XSS)",
      "B": "Reflected Cross-Site Scripting (Reflected XSS)",
      "C": "SQL Injection (SQLi)",
      "D": "Distributed Denial of Service (DDoS)",
      "E": "Broken Access Control"
    },
    "answer": "A",
    "explanation": "Stored XSS tersimpan permanen di database server dan menyerang setiap pengunjung yang memuat halaman."
  }
]

# Pastikan TWK & TIU memiliki points default 5 dan 0 jika tidak ada
for q in twk_questions:
  if "points" not in q:
    ans = q["answer"]
    q["points"] = {opt: (5 if opt == ans else 0) for opt in ["A", "B", "C", "D", "E"]}

for q in tiu_questions:
  if "points" not in q:
    ans = q["answer"]
    q["points"] = {opt: (5 if opt == ans else 0) for opt in ["A", "B", "C", "D", "E"]}

for q in skb_it_questions:
  if "points" not in q:
    ans = q["answer"]
    q["points"] = {opt: (5 if opt == ans else 0) for opt in ["A", "B", "C", "D", "E"]}

# Gabungkan 110 Soal SKD (30 TWK + 35 TIU + 45 TKP)
all_skd_questions = twk_questions + tiu_questions + tkp_questions

data = {
  "skd": {
    "title": "Simulasi Resmi CAT BKN - SKD (110 Soal Full)",
    "timeMinutes": 100,
    "passingGrades": {
      "twk": 65,
      "tiu": 80,
      "tkp": 166
    },
    "questions": all_skd_questions
  },
  "skb_it": {
    "title": "Simulasi CAT BKN - SKB IT Pranata Komputer",
    "timeMinutes": 90,
    "passingGrades": {
      "total": 0
    },
    "questions": skb_it_questions
  }
}

js_content = "/**\n * BANK SOAL RESMI SIMULASI CAT BKN (110 SOAL SKD PENUH & SKB IT)\n */\nwindow.BANK_SOAL = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"

with open("d:\\CPNS\\data_soal.js", "w", encoding="utf-8") as f:
  f.write(js_content)

print(f"Sukses! Total SKD: {len(all_skd_questions)} soal (TWK: {len(twk_questions)}, TIU: {len(tiu_questions)}, TKP: {len(tkp_questions)}). Total SKB: {len(skb_it_questions)}.")
