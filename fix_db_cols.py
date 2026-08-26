import re

with open('gas/Database.gs', 'r') as f:
    content = f.read()

# Replace Master_Siswa
old_siswa = "{ name: 'Master_Siswa', columns: ['NIS', 'NISN', 'Nama Siswa', 'Kelas', 'L/P', 'Status'] },"
new_siswa = "{ name: 'Master_Siswa', columns: ['NIS', 'NISN', 'Nama Siswa', 'Kelas', 'L/P', 'Status', 'Tempat Lahir', 'Tanggal Lahir', 'Alamat', 'Nama Ayah', 'Nama Ibu', 'No HP Ortu', 'Username', 'Password'] },"
content = content.replace(old_siswa, new_siswa)

# Replace Master_Guru
old_guru = "{ name: 'Master_Guru', columns: ['NIP', 'Nama Lengkap', 'Mata Pelajaran', 'Status Pegawai', 'No HP'] },"
new_guru = "{ name: 'Master_Guru', columns: ['NIP', 'Nama Lengkap', 'Jenis Kelamin', 'Mata Pelajaran', 'Status', 'Tempat Lahir', 'Tanggal Lahir', 'Alamat', 'Status Pegawai', 'Jabatan', 'Pendidikan', 'Jurusan', 'Tahun Lulus', 'No HP', 'Username', 'Password'] },"
content = content.replace(old_guru, new_guru)

with open('gas/Database.gs', 'w') as f:
    f.write(content)
