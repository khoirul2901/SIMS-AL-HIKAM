with open('gas/Pelanggaran.gs', 'r') as f:
    content = f.read()

content = content.replace("sheet.appendRow(['Tanggal', 'NIS', 'Nama Siswa', 'Kelas', 'Kategori', 'Poin', 'Keterangan']);", "sheet.appendRow(['Tanggal', 'Nama Siswa', 'Kelas', 'Kategori', 'Poin', 'Keterangan']);")
content = content.replace("sheet.appendRow([tgl, data.nis, namaSiswa, kelasSiswa, data.kategori, data.poin, data.keterangan]);", "sheet.appendRow([tgl, namaSiswa, kelasSiswa, data.kategori, data.poin, data.keterangan]);")

with open('gas/Pelanggaran.gs', 'w') as f:
    f.write(content)
