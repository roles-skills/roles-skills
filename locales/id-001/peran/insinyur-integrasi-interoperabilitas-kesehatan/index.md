# Insinyur integrasi (interoperabilitas kesehatan)

> Ini adalah profil acuan ilustratif untuk organisasi layanan kesehatan digital yang generik. Ini bukan uraian jabatan resmi dari pemberi kerja mana pun, dan skor penilaian jabatannya bukan penilaian formal.

> Teks ini diterjemahkan dari bahasa Inggris oleh asisten kecerdasan buatan dan belum ditinjau oleh penutur asli bahasa Indonesia. Kutipan dari Kerangka Kapabilitas Profesi Digital dan Data Pemerintah Inggris (UK GDaD PCF) dan dari ESCO tetap dalam bahasa Inggris.

**Rumpun:** [Pengembangan perangkat lunak](../../#pengembangan-perangkat-lunak)  
**Pita:** 5, 6, 7, 8a  
**Peran UK GDaD PCF:** Tidak ada (acuan ini mendefinisikan perannya)  
**Jabatan ESCO:** [integration engineer](http://data.europa.eu/esco/occupation/07e60525-1aad-4099-aaf3-2c7014c92212) (ISCO-08 2511); [database developer](http://data.europa.eu/esco/occupation/b11e1742-5e28-4270-b081-b0193d85ee7d) (ISCO-08 2521)

## Ringkasan

Insinyur integrasi menghubungkan sistem klinis dan bisnis organisasi agar informasi kesehatan dan perawatan mengalir dengan aman ke tempat yang membutuhkannya. Mereka merancang, membangun, menguji, dan mendukung antarmuka, API, dan alur pesan menggunakan standar seperti HL7 FHIR dan HL7 versi 2, memetakan data dan kode klinis antarsistem, dan menjaga integrasi tetap berjalan dalam layanan langsung.

## Di organisasi layanan kesehatan digital

- Pesan yang hilang, tertunda, ganda, atau salah cocok, seperti hasil pemeriksaan atau rujukan, dapat langsung berujung pada kerugian, sehingga pekerjaan integrasi mengikuti proses manajemen risiko klinis.
- Integrasi membawa volume besar informasi kesehatan rahasia antarorganisasi, sehingga setiap aliran memerlukan dasar hukum, transportasi yang aman, dan audit.
- Sistem kesehatan memakai banyak standar dan versi, dari pesan HL7 versi 2 hingga API HL7 FHIR dan profil IHE, sering dengan variasi lokal.
- Makna klinis harus bertahan dalam perjalanannya, sehingga para insinyur memetakan terminologi klinis seperti SNOMED CT dengan benar dan mencocokkan pasien secara andal.
- Banyak integrasi mendukung perawatan sepanjang waktu, sehingga memerlukan pemantauan, peringatan, dan jalur yang jelas untuk menyelesaikan pesan yang gagal.

## Tingkat peran

| Pita | Judul | Tingkat UK GDaD PCF | Golongan pegawai negeri Inggris | Poin penilaian jabatan |
| --- | --- | --- | --- | --- |
| 5 | [Insinyur integrasi junior](#pita-5-insinyur-integrasi-junior) | — | — | 335 |
| 6 | [Insinyur integrasi](#pita-6-insinyur-integrasi) | — | — | 418 |
| 7 | [Insinyur integrasi senior](#pita-7-insinyur-integrasi-senior) | — | — | 477 |
| 8a | [Insinyur integrasi pimpinan](#pita-8a-insinyur-integrasi-pimpinan) | — | — | 551 |

## Pita 5: Insinyur integrasi junior

Insinyur integrasi junior membangun, menguji, dan mendukung integrasi antarsistem kesehatan dan perawatan, bekerja dari spesifikasi dan dengan bimbingan dari insinyur yang lebih berpengalaman.

### Tanggung jawab

- Membangun dan mengubah pemetaan pesan, transformasi, dan panggilan API dari spesifikasi yang disepakati.
- Menguji integrasi terhadap spesifikasi dan pesan contoh, termasuk kasus kesalahan dan kasus tepi.
- Memantau alur pesan, menyelidiki pesan yang gagal atau ditolak, dan menyelesaikan atau mengeskalasikannya.
- Menangani data kesehatan dengan aman, mengikuti aturan tata kelola informasi untuk data langsung dan data uji.
- Mencatat perubahan dan hasil pengujian agar dapat dipakai sebagai bukti keselamatan klinis.

### Keterampilan

| Keterampilan | Sumber | Tingkat yang diharapkan | Arti tingkat ini |
| --- | --- | --- | --- |
| [Systems integration](../../keterampilan/#systems-integration) | UK GDaD PCF | Menerapkan | You can:<br>• build and test simple interfaces between systems<br>• work on more complex integration as part of a wider team |
| [Programming and build (software engineering)](../../keterampilan/#programming-and-build-software-engineering) | UK GDaD PCF | Menerapkan | You can:<br>• design, code, test, correct and document simple programs or scripts under the direction of others |
| [Testing](../../keterampilan/#testing) | UK GDaD PCF | Menerapkan | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Service support](../../keterampilan/#service-support) | UK GDaD PCF | Menerapkan | You can:<br>• help fix service faults following agreed procedures<br>• carry out maintenance tasks on service support infrastructure |
| [Information security](../../keterampilan/#information-security) | UK GDaD PCF | Kesadaran | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [Interoperabilitas data kesehatan](../../keterampilan/#interoperabilitas-data-kesehatan) | Acuan ini | Menerapkan | Anda dapat:<br>• membaca dan menggunakan sumber daya, profil, dan API FHIR<br>• membangun atau menguji integrasi sederhana dengan bimbingan<br>• memeriksa pesan terhadap spesifikasi |
| [Terminologi dan klasifikasi klinis](../../keterampilan/#terminologi-dan-klasifikasi-klinis) | Acuan ini | Kesadaran | Anda dapat:<br>• menjelaskan perbedaan antara terminologi klinis dan klasifikasi<br>• mengenali terminologi umum seperti SNOMED CT dan ICD |
| [Tata kelola informasi dan pelindungan data](../../keterampilan/#tata-kelola-informasi-dan-pelindungan-data) | Acuan ini | Menerapkan | Anda dapat:<br>• menerapkan prinsip pelindungan data pada pekerjaan Anda<br>• menyumbang pada penilaian dampak pelindungan data<br>• menangani permintaan informasi dan arsip dengan benar |
| [Manajemen risiko klinis](../../keterampilan/#manajemen-risiko-klinis) | Acuan ini | Kesadaran | Anda dapat:<br>• menjelaskan bagaimana sistem TI kesehatan dapat membahayakan pasien, misalnya melalui informasi yang salah, hilang, atau terlambat<br>• melaporkan kemungkinan masalah keselamatan klinis melalui jalur yang tepat |
| [Memahami layanan kesehatan dan perawatan](../../keterampilan/#memahami-layanan-kesehatan-dan-perawatan) | Acuan ini | Kesadaran | Anda dapat:<br>• menguraikan bagian utama sistem kesehatan dan perawatan serta layanan yang didukung organisasi<br>• menjelaskan mengapa keselamatan dan kerahasiaan pasien penting dalam pekerjaan Anda |

### Kualifikasi dan pengalaman yang lazim

- Gelar di bidang komputasi atau bidang terkait, magang yang telah selesai, atau pengalaman yang setara.

### Gambaran pita

- **Pengetahuan:** Pengetahuan profesional atau teknis, biasanya dari gelar sarjana atau pengalaman yang setara.
- **Otonomi:** Bekerja menuju sasaran yang luas dalam standar profesional; merencanakan pekerjaannya sendiri.
- **Cakupan:** Pekerjaan profesionalnya sendiri dalam sebuah tim atau produk.
- **Kepemimpinan:** Dapat membimbing dan memeriksa pekerjaan staf pendukung dan peserta magang.
- **Akuntabilitas:** Mutu pekerjaan profesionalnya sendiri.

### Penilaian jabatan (ilustratif)

| # | Faktor | Tingkat | Poin |
| --- | --- | --- | --- |
| 1 | Keterampilan komunikasi dan hubungan | 4 | 32 |
| 2 | Pengetahuan, pelatihan, dan pengalaman | 5 | 120 |
| 3 | Keterampilan analisis dan pertimbangan | 3 | 27 |
| 4 | Keterampilan perencanaan dan pengorganisasian | 2 | 15 |
| 5 | Keterampilan fisik | 3 | 27 |
| 6 | Tanggung jawab atas perawatan pasien dan klien | 1 | 4 |
| 7 | Tanggung jawab atas pengembangan kebijakan dan layanan | 2 | 12 |
| 8 | Tanggung jawab atas sumber daya keuangan dan fisik | 1 | 5 |
| 9 | Tanggung jawab atas orang | 1 | 5 |
| 10 | Tanggung jawab atas sumber daya informasi | 4 | 24 |
| 11 | Tanggung jawab atas penelitian dan pengembangan | 2 | 12 |
| 12 | Kebebasan bertindak | 3 | 21 |
| 13 | Upaya fisik | 2 | 7 |
| 14 | Upaya mental | 3 | 12 |
| 15 | Upaya emosional | 1 | 5 |
| 16 | Kondisi kerja | 2 | 7 |
| | **Total** | | **335** (Pita 5: 326–395) |

## Pita 6: Insinyur integrasi

Insinyur integrasi merancang, membangun, dan mendukung integrasi antarsistem kesehatan dan perawatan secara mandiri, dan membantu menentukan bagaimana sistem seharusnya bertukar data.

### Tanggung jawab

- Merancang dan membangun integrasi, API, dan alur pesan menggunakan HL7 FHIR, HL7 versi 2, dan pola pesan.
- Menganalisis sistem sumber dan sasaran serta menulis spesifikasi antarmuka dan pemetaan data, termasuk kode klinis.
- Membangun pencocokan pasien, validasi, dan penanganan kesalahan agar informasi sampai pada rekam yang benar.
- Ikut serta dalam lokakarya bahaya dan membangun pengendalian keselamatan ke dalam integrasi, seperti peringatan untuk pesan yang gagal atau tertunda.
- Bekerja dengan pemasok dan organisasi mitra untuk menguji dan meluncurkan koneksi baru.
- Menyelidiki dan memperbaiki masalah pada integrasi langsung, dan membimbing insinyur integrasi junior.

### Keterampilan

| Keterampilan | Sumber | Tingkat yang diharapkan | Arti tingkat ini |
| --- | --- | --- | --- |
| [Systems integration](../../keterampilan/#systems-integration) | UK GDaD PCF | Praktisi | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Programming and build (software engineering)](../../keterampilan/#programming-and-build-software-engineering) | UK GDaD PCF | Praktisi | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../keterampilan/#systems-design) | UK GDaD PCF | Menerapkan | You can:<br>• translate logical designs into physical designs<br>• produce detailed designs<br>• effectively document all work using required standards, methods and tools, including prototyping tools where appropriate<br>• design systems characterised by managed levels of risk, manageable business and technical complexity, and meaningful impact<br>• work with well understood technology and identify appropriate patterns |
| [Service support](../../keterampilan/#service-support) | UK GDaD PCF | Praktisi | You can:<br>• identify, locate and fix service faults |
| [Information security](../../keterampilan/#information-security) | UK GDaD PCF | Menerapkan | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [Interoperabilitas data kesehatan](../../keterampilan/#interoperabilitas-data-kesehatan) | Acuan ini | Praktisi | Anda dapat:<br>• merancang dan membangun integrasi menggunakan FHIR, HL7 versi 2, dan pola pesan<br>• menulis dan memprofilkan sumber daya FHIR dan panduan implementasi<br>• menyelesaikan masalah pemetaan dan mutu data yang kompleks antarsistem |
| [Terminologi dan klasifikasi klinis](../../keterampilan/#terminologi-dan-klasifikasi-klinis) | Acuan ini | Menerapkan | Anda dapat:<br>• menemukan dan menggunakan kode yang tepat untuk suatu butir data atau formulir<br>• menggunakan peramban terminologi dan kumpulan referensi |
| [Tata kelola informasi dan pelindungan data](../../keterampilan/#tata-kelola-informasi-dan-pelindungan-data) | Acuan ini | Menerapkan | Anda dapat:<br>• menerapkan prinsip pelindungan data pada pekerjaan Anda<br>• menyumbang pada penilaian dampak pelindungan data<br>• menangani permintaan informasi dan arsip dengan benar |
| [Manajemen risiko klinis](../../keterampilan/#manajemen-risiko-klinis) | Acuan ini | Menerapkan | Anda dapat:<br>• ikut serta dalam lokakarya bahaya dan menyumbang pada log bahaya<br>• mengikuti proses manajemen risiko klinis untuk pekerjaan Anda<br>• menyediakan bukti untuk kasus keselamatan klinis, seperti hasil pengujian |
| [Memahami layanan kesehatan dan perawatan](../../keterampilan/#memahami-layanan-kesehatan-dan-perawatan) | Acuan ini | Menerapkan | Anda dapat:<br>• menjelaskan alur kerja klinis dan perawatan yang didukung pekerjaan Anda<br>• menggunakan istilah layanan kesehatan yang umum dengan benar bersama rekan klinis dan perawatan<br>• mengenali ketika suatu perubahan dapat memengaruhi perawatan pasien dan menyampaikannya |

### Kualifikasi dan pengalaman yang lazim

- Gelar di bidang komputasi atau bidang terkait, atau pengalaman yang setara.
- Pengalaman membangun dan mendukung integrasi antarsistem produksi.

### Gambaran pita

- **Pengetahuan:** Pengetahuan spesialis di berbagai prosedur, dibangun melalui pelatihan lanjutan atau pengalaman.
- **Otonomi:** Bekerja mandiri; menafsirkan kebijakan untuk bidangnya; meminta saran untuk masalah yang kompleks.
- **Cakupan:** Sebuah produk, layanan, atau alur kerja.
- **Kepemimpinan:** Dapat memimpin tim kecil atau membimbing rekan kerja.
- **Akuntabilitas:** Hasil alur kerjanya sendiri dan mutu saran yang diberikan.

### Penilaian jabatan (ilustratif)

| # | Faktor | Tingkat | Poin |
| --- | --- | --- | --- |
| 1 | Keterampilan komunikasi dan hubungan | 4 | 32 |
| 2 | Pengetahuan, pelatihan, dan pengalaman | 6 | 156 |
| 3 | Keterampilan analisis dan pertimbangan | 4 | 42 |
| 4 | Keterampilan perencanaan dan pengorganisasian | 3 | 27 |
| 5 | Keterampilan fisik | 3 | 27 |
| 6 | Tanggung jawab atas perawatan pasien dan klien | 1 | 4 |
| 7 | Tanggung jawab atas pengembangan kebijakan dan layanan | 2 | 12 |
| 8 | Tanggung jawab atas sumber daya keuangan dan fisik | 1 | 5 |
| 9 | Tanggung jawab atas orang | 2 | 12 |
| 10 | Tanggung jawab atas sumber daya informasi | 4 | 24 |
| 11 | Tanggung jawab atas penelitian dan pengembangan | 2 | 12 |
| 12 | Kebebasan bertindak | 4 | 32 |
| 13 | Upaya fisik | 1 | 3 |
| 14 | Upaya mental | 4 | 18 |
| 15 | Upaya emosional | 1 | 5 |
| 16 | Kondisi kerja | 2 | 7 |
| | **Total** | | **418** (Pita 6: 396–465) |

## Pita 7: Insinyur integrasi senior

Insinyur integrasi senior memimpin desain dan penyampaian integrasi kompleks di banyak sistem dan organisasi, dan menetapkan standar integrasi untuk bidangnya.

### Tanggung jawab

- Memimpin desain teknis integrasi yang kompleks, seperti rekam perawatan bersama, hasil pemeriksaan, dan rujukan antarorganisasi.
- Menulis dan memelihara profil FHIR, panduan implementasi, dan standar antarmuka untuk organisasi.
- Merancang integrasi agar aman, tangguh, dan dapat diamati, dengan jalur yang jelas untuk menyelesaikan kegagalan.
- Bekerja dengan petugas keselamatan klinis untuk mengidentifikasi bahaya integrasi dan memastikan pengendalian dirancang dan diuji.
- Memastikan setiap aliran data memiliki dasar hukum dan pengaturan pembagian data yang disepakati, bekerja dengan rekan tata kelola informasi.
- Membimbing dan mengembangkan para insinyur integrasi dalam tim.

### Keterampilan

| Keterampilan | Sumber | Tingkat yang diharapkan | Arti tingkat ini |
| --- | --- | --- | --- |
| [Systems integration](../../keterampilan/#systems-integration) | UK GDaD PCF | Pakar | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Programming and build (software engineering)](../../keterampilan/#programming-and-build-software-engineering) | UK GDaD PCF | Praktisi | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../keterampilan/#systems-design) | UK GDaD PCF | Praktisi | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Information security](../../keterampilan/#information-security) | UK GDaD PCF | Praktisi | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Stakeholder relationship management](../../keterampilan/#stakeholder-relationship-management) | UK GDaD PCF | Menerapkan | You can:<br>• identify important stakeholders and communicate with them clearly and regularly<br>• tailor communication to stakeholders' needs and work with them to build relationships while meeting user needs<br>• build and reach consensus with stakeholders<br>• work to improve stakeholder relationships using evidence to explain decisions |
| [Interoperabilitas data kesehatan](../../keterampilan/#interoperabilitas-data-kesehatan) | Acuan ini | Praktisi | Anda dapat:<br>• merancang dan membangun integrasi menggunakan FHIR, HL7 versi 2, dan pola pesan<br>• menulis dan memprofilkan sumber daya FHIR dan panduan implementasi<br>• menyelesaikan masalah pemetaan dan mutu data yang kompleks antarsistem |
| [Terminologi dan klasifikasi klinis](../../keterampilan/#terminologi-dan-klasifikasi-klinis) | Acuan ini | Praktisi | Anda dapat:<br>• merancang model data dan kumpulan referensi menggunakan terminologi klinis<br>• memetakan antarterminologi dan klasifikasi, dan menjelaskan batas suatu pemetaan<br>• menasihati tim tentang penggunaan terminologi dalam produk dan analitik |
| [Tata kelola informasi dan pelindungan data](../../keterampilan/#tata-kelola-informasi-dan-pelindungan-data) | Acuan ini | Praktisi | Anda dapat:<br>• memimpin penilaian dampak pelindungan data dan perjanjian pembagian informasi<br>• menasihati tim tentang dasar hukum, persetujuan, kerahasiaan, dan retensi<br>• menyelidiki insiden dan merekomendasikan perbaikan |
| [Manajemen risiko klinis](../../keterampilan/#manajemen-risiko-klinis) | Acuan ini | Menerapkan | Anda dapat:<br>• ikut serta dalam lokakarya bahaya dan menyumbang pada log bahaya<br>• mengikuti proses manajemen risiko klinis untuk pekerjaan Anda<br>• menyediakan bukti untuk kasus keselamatan klinis, seperti hasil pengujian |
| [Manajemen identitas dan akses](../../keterampilan/#manajemen-identitas-dan-akses) | Acuan ini | Menerapkan | Anda dapat:<br>• membuat, mengubah, dan menghapus akun pengguna dan hak akses<br>• memeriksa akses terhadap aturan akses berbasis peran |

### Kualifikasi dan pengalaman yang lazim

- Pengalaman yang substansial dalam merancang dan mendukung integrasi kesehatan atau integrasi kompleks lainnya, pada tingkat yang setara dengan gelar magister.

### Gambaran pita

- **Pengetahuan:** Pengetahuan spesialis yang sangat berkembang, biasanya setingkat magister atau pengalaman yang setara.
- **Otonomi:** Bekerja menurut kebijakan organisasi; memutuskan cara mencapai hasil; menjadi pakar tempat orang lain berkonsultasi.
- **Cakupan:** Beberapa produk atau layanan, atau sebuah fungsi spesialis.
- **Kepemimpinan:** Memimpin sebuah tim atau bidang praktik profesional.
- **Akuntabilitas:** Penyampaian sebuah layanan atau fungsi spesialis, dan anggarannya jika dipegang.

### Penilaian jabatan (ilustratif)

| # | Faktor | Tingkat | Poin |
| --- | --- | --- | --- |
| 1 | Keterampilan komunikasi dan hubungan | 4 | 32 |
| 2 | Pengetahuan, pelatihan, dan pengalaman | 7 | 196 |
| 3 | Keterampilan analisis dan pertimbangan | 4 | 42 |
| 4 | Keterampilan perencanaan dan pengorganisasian | 3 | 27 |
| 5 | Keterampilan fisik | 3 | 27 |
| 6 | Tanggung jawab atas perawatan pasien dan klien | 1 | 4 |
| 7 | Tanggung jawab atas pengembangan kebijakan dan layanan | 3 | 21 |
| 8 | Tanggung jawab atas sumber daya keuangan dan fisik | 1 | 5 |
| 9 | Tanggung jawab atas orang | 2 | 12 |
| 10 | Tanggung jawab atas sumber daya informasi | 5 | 34 |
| 11 | Tanggung jawab atas penelitian dan pengembangan | 2 | 12 |
| 12 | Kebebasan bertindak | 4 | 32 |
| 13 | Upaya fisik | 1 | 3 |
| 14 | Upaya mental | 4 | 18 |
| 15 | Upaya emosional | 1 | 5 |
| 16 | Kondisi kerja | 2 | 7 |
| | **Total** | | **477** (Pita 7: 466–539) |

## Pita 8a: Insinyur integrasi pimpinan

Insinyur integrasi pimpinan memimpin rekayasa integrasi organisasi, menetapkan arah teknis dan standarnya, dan menjamin integrasi kritis di banyak sistem.

### Tanggung jawab

- Memimpin rekayasa integrasi di seluruh organisasi, menetapkan arah, pola, dan standar.
- Menjamin desain integrasi kritis, seperti yang membawa hasil pemeriksaan, obat, atau peringatan.
- Membentuk peta jalan platform integrasi bersama arsitek, manajer produk, dan pemasok.
- Mewakili organisasi dalam pekerjaan interoperabilitas dan standar lintas organisasi.
- Mengelola secara langsung atau memimpin para insinyur integrasi dan menumbuhkan komunitas praktik integrasi.

### Keterampilan

| Keterampilan | Sumber | Tingkat yang diharapkan | Arti tingkat ini |
| --- | --- | --- | --- |
| [Systems integration](../../keterampilan/#systems-integration) | UK GDaD PCF | Pakar | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Systems design](../../keterampilan/#systems-design) | UK GDaD PCF | Pakar | You can:<br>• design systems characterised by high levels of risk, impact, and business or technical complexity<br>• control system design practice within an enterprise or industry architecture<br>• influence industry-based models for the development of new technology applications<br>• develop effective implementation and procurement strategies, consistent with business needs<br>• ensure adherence to relevant technical strategies, policies, standards and practices |
| [Technical design throughout the life cycle](../../keterampilan/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Praktisi | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [Stakeholder relationship management](../../keterampilan/#stakeholder-relationship-management) | UK GDaD PCF | Praktisi | You can:<br>• work with the team to develop and maintain an understanding of stakeholders<br>• work with the team to develop and implement stakeholder communications strategies<br>• identify and resolve issues, influence stakeholders and manage relationships effectively<br>• build long-term strategic relationships and communicate clearly and regularly with stakeholders |
| [Leadership and guidance](../../keterampilan/#leadership-and-guidance) | UK GDaD PCF | Praktisi | You can:<br>• make decisions characterised by medium levels of risk and complexity and recommend decisions as risk and complexity increase<br>• build consensus between services or independent stakeholders<br>• identify problems or issues in the team dynamic and rectify them<br>• engage in varying types of feedback, choosing the right type at the appropriate time and ensuring the discussion and decision stick<br>• bring people together to form a motivated team and help create the right environment for a team to work in<br>• facilitate the best team makeup depending on the situation |
| [Interoperabilitas data kesehatan](../../keterampilan/#interoperabilitas-data-kesehatan) | Acuan ini | Pakar | Anda dapat:<br>• menetapkan standar dan strategi interoperabilitas untuk organisasi<br>• memimpin pekerjaan standar nasional atau lintas organisasi<br>• menjamin desain integrasi kritis di banyak sistem |
| [Terminologi dan klasifikasi klinis](../../keterampilan/#terminologi-dan-klasifikasi-klinis) | Acuan ini | Praktisi | Anda dapat:<br>• merancang model data dan kumpulan referensi menggunakan terminologi klinis<br>• memetakan antarterminologi dan klasifikasi, dan menjelaskan batas suatu pemetaan<br>• menasihati tim tentang penggunaan terminologi dalam produk dan analitik |
| [Tata kelola informasi dan pelindungan data](../../keterampilan/#tata-kelola-informasi-dan-pelindungan-data) | Acuan ini | Praktisi | Anda dapat:<br>• memimpin penilaian dampak pelindungan data dan perjanjian pembagian informasi<br>• menasihati tim tentang dasar hukum, persetujuan, kerahasiaan, dan retensi<br>• menyelidiki insiden dan merekomendasikan perbaikan |
| [Manajemen risiko klinis](../../keterampilan/#manajemen-risiko-klinis) | Acuan ini | Praktisi | Anda dapat:<br>• memimpin identifikasi bahaya dan penilaian risiko untuk produk atau perubahan<br>• menulis dan memelihara log bahaya dan laporan kasus keselamatan klinis<br>• menyepakati pengendalian risiko dengan tim produk dan memeriksa bahwa pengendalian itu berfungsi<br>• menasihati tim tentang penerapan standar manajemen risiko klinis |
| [Manajemen orang](../../keterampilan/#manajemen-orang) | Acuan ini | Praktisi | Anda dapat:<br>• mengelola sebuah tim secara langsung, menetapkan sasaran dan menjalankan penilaian<br>• mendukung kesejahteraan dan mengelola kehadiran, kinerja, dan perilaku<br>• merencanakan pengembangan dan suksesi tim |

### Kualifikasi dan pengalaman yang lazim

- Pengalaman luas dalam memimpin rekayasa integrasi untuk sistem kesehatan atau perawatan yang kompleks.

### Gambaran pita

- **Pengetahuan:** Pengetahuan pakar tentang suatu disiplin dan pengelolaannya.
- **Otonomi:** Menafsirkan kebijakan organisasi untuk sebuah layanan; menetapkan arah tim.
- **Cakupan:** Sebuah bidang layanan atau suatu disiplin di seluruh organisasi.
- **Kepemimpinan:** Mengelola sebuah tim, atau memimpin suatu disiplin tanpa manajemen garis.
- **Akuntabilitas:** Sebuah bidang layanan, stafnya, dan anggarannya.

### Penilaian jabatan (ilustratif)

| # | Faktor | Tingkat | Poin |
| --- | --- | --- | --- |
| 1 | Keterampilan komunikasi dan hubungan | 5 | 45 |
| 2 | Pengetahuan, pelatihan, dan pengalaman | 7 | 196 |
| 3 | Keterampilan analisis dan pertimbangan | 5 | 60 |
| 4 | Keterampilan perencanaan dan pengorganisasian | 4 | 42 |
| 5 | Keterampilan fisik | 2 | 15 |
| 6 | Tanggung jawab atas perawatan pasien dan klien | 1 | 4 |
| 7 | Tanggung jawab atas pengembangan kebijakan dan layanan | 4 | 32 |
| 8 | Tanggung jawab atas sumber daya keuangan dan fisik | 2 | 12 |
| 9 | Tanggung jawab atas orang | 3 | 21 |
| 10 | Tanggung jawab atas sumber daya informasi | 5 | 34 |
| 11 | Tanggung jawab atas penelitian dan pengembangan | 2 | 12 |
| 12 | Kebebasan bertindak | 5 | 45 |
| 13 | Upaya fisik | 1 | 3 |
| 14 | Upaya mental | 4 | 18 |
| 15 | Upaya emosional | 1 | 5 |
| 16 | Kondisi kerja | 2 | 7 |
| | **Total** | | **551** (Pita 8a: 540–584) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
