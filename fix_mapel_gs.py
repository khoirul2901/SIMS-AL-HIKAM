with open('gas/Mapel.gs', 'r') as f:
    content = f.read()

content = content.replace('''  sheet.appendRow([data.kode, data.nama, data.kelompok]);
  return { success: true, message: 'Data mata pelajaran berhasil ditambahkan' };''', '''  var existingData = sheet.getDataRange().getValues();
  for (var i = 1; i < existingData.length; i++) {
    if (existingData[i][0] == data.kode) {
      sheet.getRange(i+1, 2, 1, 2).setValues([[data.nama, data.kelompok]]);
      return { success: true, message: 'Data berhasil diupdate' };
    }
  }
  
  // Insert Baru
  sheet.appendRow([data.kode, data.nama, data.kelompok]);
  return { success: true, message: 'Data mata pelajaran berhasil ditambahkan' };''')

with open('gas/Mapel.gs', 'w') as f:
    f.write(content)
