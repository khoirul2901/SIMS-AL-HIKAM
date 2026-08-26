with open('src/pages/AbsensiSiswa.tsx', 'r') as f:
    content = f.read()

# Remove the state
content = content.replace("  const [data, setData] = useState(SISWA_DATA);", "")

new_filtered = """
  // Get all students for the selected class, merged with current absensi status
  const studentsInClass = siswaData.filter(s => s.kelas === selectedKelas);
  
  const filteredData = studentsInClass.map(siswa => {
    const existing = absensiData.find(a => a.nis === siswa.nis && a.tanggal === date && a.jenis === jenisAbsen);
    return {
      ...siswa,
      status: existing ? existing.status : 'Belum diabsen'
    };
  }).filter(siswa => 
    siswa.nama.toLowerCase().includes(searchTerm.toLowerCase()) || 
    siswa.nis.includes(searchTerm)
  );

  const handleStatusChange = (nis: string, status: string) => {
    const existingIdx = absensiData.findIndex(a => a.nis === nis && a.tanggal === date && a.jenis === jenisAbsen);
    if (existingIdx >= 0) {
      const newAbsensi = [...absensiData];
      newAbsensi[existingIdx].status = status;
      setAbsensiData(newAbsensi);
    } else {
      setAbsensiData([...absensiData, {
        id: Math.random().toString(36).substr(2, 9),
        tanggal: date,
        nis,
        kelas: selectedKelas,
        jenis: jenisAbsen,
        status
      }]);
    }
  };
"""

import re
content = re.sub(r'const filteredData.*?setData.*?};', new_filtered, content, flags=re.DOTALL)

# Also fix `data.find` in `handleScanQR` to `siswaData.find`
content = content.replace("const student = data.find(s => s.nis === nis);", "const student = siswaData.find(s => s.nis === nis);")
content = content.replace("handleStatusChange(student.id, 'Hadir');", "handleStatusChange(student.nis, 'Hadir');")
content = content.replace("siswa.id", "siswa.nis")

with open('src/pages/AbsensiSiswa.tsx', 'w') as f:
    f.write(content)
