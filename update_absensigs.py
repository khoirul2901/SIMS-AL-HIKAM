with open('gas/Absensi.gs', 'w') as f:
    f.write("""// Script Absensi
function getSiswaAndAbsensi(kelas, tanggal, jenis) {
  var ss = getDb();
  var sheetSiswa = ss.getSheetByName('Master_Siswa');
  if(!sheetSiswa) return { siswa: [], absensi: [] };
  
  var dataSiswa = sheetSiswa.getDataRange().getValues();
  var resultSiswa = [];
  
  // Ambil semua siswa di kelas ini
  for(var i=1; i<dataSiswa.length; i++) {
    if(dataSiswa[i][3] == kelas) { // Kolom D: Kelas
      resultSiswa.push({
        nis: dataSiswa[i][0],
        nama: dataSiswa[i][2],
        jk: dataSiswa[i][4]
      });
    }
  }
  
  var sheetAbsen = ss.getSheetByName('Absensi_Siswa');
  var resultAbsensi = [];
  if(sheetAbsen) {
    var dataAbsen = sheetAbsen.getDataRange().getValues();
    // Cari absensi di tanggal dan jenis yang sama
    for(var j=1; j<dataAbsen.length; j++) {
      if(dataAbsen[j][0] == tanggal && dataAbsen[j][2] == jenis) { // A: tgl, C: jenis (Masuk/Pulang)
        resultAbsensi.push({
          nis: dataAbsen[j][1],
          status: dataAbsen[j][4] // E: Status
        });
      }
    }
  }
  
  return { siswa: resultSiswa, absensi: resultAbsensi };
}

function saveAbsensi(nis, kelas, tanggal, jenis, status) {
  var ss = getDb();
  var sheet = ss.getSheetByName('Absensi_Siswa');
  if(!sheet) {
    sheet = ss.insertSheet('Absensi_Siswa');
    sheet.appendRow(['Tanggal', 'NIS', 'Jenis', 'Waktu', 'Status']);
  }
  
  var existingData = sheet.getDataRange().getValues();
  
  var waktu = new Date().toLocaleTimeString();
  
  // Update jika sudah ada
  for(var i=1; i<existingData.length; i++) {
    if(existingData[i][0] == tanggal && existingData[i][1] == nis && existingData[i][2] == jenis) {
      sheet.getRange(i+1, 4, 1, 2).setValues([[waktu, status]]);
      return { success: true };
    }
  }
  
  // Insert baru
  sheet.appendRow([tanggal, nis, jenis, waktu, status]);
  return { success: true };
}
""")
