with open('gas/Kelas.gs', 'r') as f:
    content = f.read()

content = content.replace('''  // Insert Baru
  sheet.appendRow([data.kode, data.nama, data.waliKelas, data.jumlahSiswa]);
  return { success: true, message: 'Data kelas berhasil ditambahkan' };''', '''  var existingData = sheet.getDataRange().getValues();
  for (var i = 1; i < existingData.length; i++) {
    if (existingData[i][0] == data.kode) {
      sheet.getRange(i+1, 2, 1, 3).setValues([[data.nama, data.waliKelas, data.jumlahSiswa]]);
      return { success: true, message: 'Data berhasil diupdate' };
    }
  }
  
  // Insert Baru
  sheet.appendRow([data.kode, data.nama, data.waliKelas, data.jumlahSiswa]);
  return { success: true, message: 'Data kelas berhasil ditambahkan' };''')

with open('gas/Kelas.gs', 'w') as f:
    f.write(content)
