with open('gas/Siswa.gs', 'r') as f:
    content = f.read()

content = content.replace("sheet.appendRow(['NIS', 'NISN', 'Nama Siswa', 'Kelas', 'L/P', 'Status']);", "sheet.appendRow(['NIS', 'NISN', 'Nama Siswa', 'Kelas', 'L/P', 'Status', 'Tempat Lahir', 'Tanggal Lahir', 'Alamat', 'Nama Ayah', 'Nama Ibu', 'No HP Ortu', 'Username', 'Password']);")

content = content.replace('''  for (var i = 1; i < data.length; i++) {
    siswaList.push({
      nis: data[i][0],
      nisn: data[i][1],
      nama: data[i][2],
      kelas: data[i][3],
      jk: data[i][4],
      status: data[i][5]
    });
  }''', '''  for (var i = 1; i < data.length; i++) {
    siswaList.push({
      nis: data[i][0] || '',
      nisn: data[i][1] || '',
      nama: data[i][2] || '',
      kelas: data[i][3] || '',
      jk: data[i][4] || '',
      status: data[i][5] || '',
      tempatLahir: data[i][6] || '',
      tanggalLahir: data[i][7] ? (data[i][7] instanceof Date ? data[i][7].toISOString().split('T')[0] : data[i][7]) : '',
      alamat: data[i][8] || '',
      namaAyah: data[i][9] || '',
      namaIbu: data[i][10] || '',
      noHp: data[i][11] || '',
      username: data[i][12] || '',
      password: data[i][13] || ''
    });
  }''')

content = content.replace('''      sheet.getRange(i+1, 2, 1, 5).setValues([[data.nisn, data.nama, data.kelas, data.jk, data.status]]);''', '''      sheet.getRange(i+1, 2, 1, 13).setValues([[data.nisn, data.nama, data.kelas, data.jk, data.status, data.tempatLahir || '', data.tanggalLahir || '', data.alamat || '', data.namaAyah || '', data.namaIbu || '', data.noHp || '', data.username || '', data.password || '']]);''')

content = content.replace('''  // Insert Baru
  sheet.appendRow([data.nis, data.nisn, data.nama, data.kelas, data.jk, data.status]);''', '''  // Insert Baru
  sheet.appendRow([data.nis, data.nisn, data.nama, data.kelas, data.jk, data.status, data.tempatLahir || '', data.tanggalLahir || '', data.alamat || '', data.namaAyah || '', data.namaIbu || '', data.noHp || '', data.username || '', data.password || '']);''')

# Let's add delete function
content += """
function deleteSiswa(nis) {
  var ss = getDb();
  var sheet = ss.getSheetByName('Master_Siswa');
  if(!sheet) return { success: false, message: 'Sheet tidak ditemukan' };
  
  var existingData = sheet.getDataRange().getValues();
  for (var i = 1; i < existingData.length; i++) {
    if (existingData[i][0] == nis) {
      sheet.deleteRow(i + 1);
      return { success: true, message: 'Data berhasil dihapus' };
    }
  }
  return { success: false, message: 'Data tidak ditemukan' };
}
"""

with open('gas/Siswa.gs', 'w') as f:
    f.write(content)
