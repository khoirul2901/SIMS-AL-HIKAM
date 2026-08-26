with open('gas/Database.gs', 'r') as f:
    content = f.read()

content = content.replace("{ name: 'Pelanggaran', columns: ['Tanggal', 'Nama Siswa', 'Kelas', 'Kategori', 'Poin', 'Keterangan'] },", "{ name: 'Pelanggaran', columns: ['Tanggal', 'NIS', 'Nama Siswa', 'Kelas', 'Kategori', 'Pelanggaran', 'Poin', 'Pelapor'] },\n    { name: 'Kategori_Pelanggaran', columns: ['ID', 'Kategori', 'Jenis', 'Poin'] },")

with open('gas/Database.gs', 'w') as f:
    f.write(content)
