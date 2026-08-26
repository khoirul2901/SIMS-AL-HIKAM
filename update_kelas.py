with open('gas/Kelas.gs', 'r') as f:
    content = f.read()

bad_str = """  var data = sheet.getDataRange().getValues();
  var kelasList = [];
  
  // Asumsi Kolom: A(Kode Kelas), B(Nama Kelas), C(Wali Kelas), D(Jumlah Siswa)
  for (var i = 1; i < data.length; i++) {
    kelasList.push({
      kode: data[i][0],
      nama: data[i][1],
      waliKelas: data[i][2],
      jumlahSiswa: data[i][3]
    });
  }"""

good_str = """  var data = sheet.getDataRange().getValues();
  
  // Get data from Master_Siswa to calculate jumlah siswa
  var sheetSiswa = ss.getSheetByName('Master_Siswa');
  var dataSiswa = sheetSiswa ? sheetSiswa.getDataRange().getValues() : [];
  var siswaCountByKelas = {};
  
  if (dataSiswa.length > 1) {
    for (var j = 1; j < dataSiswa.length; j++) {
      var kls = dataSiswa[j][3]; // Kolom D (Kelas)
      if (kls) {
        if (!siswaCountByKelas[kls]) siswaCountByKelas[kls] = 0;
        siswaCountByKelas[kls]++;
      }
    }
  }

  var kelasList = [];
  
  // Asumsi Kolom: A(Kode Kelas), B(Nama Kelas), C(Wali Kelas)
  for (var i = 1; i < data.length; i++) {
    var namaKelas = data[i][1];
    kelasList.push({
      kode: data[i][0],
      nama: namaKelas,
      waliKelas: data[i][2],
      jumlahSiswa: siswaCountByKelas[namaKelas] || 0
    });
  }"""

content = content.replace(bad_str, good_str)

bad_save = """    sheet = ss.insertSheet('Master_Kelas');
    sheet.appendRow(['Kode Kelas', 'Nama Kelas', 'Wali Kelas', 'Jumlah Siswa']);
  }
  
  var existingData = sheet.getDataRange().getValues();
  for (var i = 1; i < existingData.length; i++) {
    if (existingData[i][0] == data.kode) {
      sheet.getRange(i+1, 2, 1, 3).setValues([[data.nama, data.waliKelas, data.jumlahSiswa]]);
      return { success: true, message: 'Data berhasil diupdate' };
    }
  }
  
  // Insert Baru
  sheet.appendRow([data.kode, data.nama, data.waliKelas, data.jumlahSiswa]);"""

good_save = """    sheet = ss.insertSheet('Master_Kelas');
    sheet.appendRow(['Kode Kelas', 'Nama Kelas', 'Wali Kelas']);
  }
  
  var existingData = sheet.getDataRange().getValues();
  for (var i = 1; i < existingData.length; i++) {
    if (existingData[i][0] == data.kode) {
      sheet.getRange(i+1, 2, 1, 2).setValues([[data.nama, data.waliKelas]]);
      return { success: true, message: 'Data berhasil diupdate' };
    }
  }
  
  // Insert Baru
  sheet.appendRow([data.kode, data.nama, data.waliKelas]);"""

content = content.replace(bad_save, good_save)

with open('gas/Kelas.gs', 'w') as f:
    f.write(content)
