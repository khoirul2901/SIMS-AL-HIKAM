import re
with open('src/context/DatabaseContext.tsx', 'r') as f:
    content = f.read()

bad_state = """  const [absensiData, setAbsensiData, absensiGuruData, setAbsensiGuruData, kategoriPelanggaranData, setKategoriPelanggaranData] = useState<any[]>(() => {
    const saved = localStorage.getItem('sims_absensi');
    return saved ? JSON.parse(saved) : [];
  });"""

good_state = """  const [absensiData, setAbsensiData] = useState<any[]>(() => {
    const saved = localStorage.getItem('sims_absensi');
    return saved ? JSON.parse(saved) : [];
  });
  
  const [absensiGuruData, setAbsensiGuruData] = useState<any[]>(() => {
    const saved = localStorage.getItem('sims_absensi_guru');
    return saved ? JSON.parse(saved) : [];
  });
  
  const [kategoriPelanggaranData, setKategoriPelanggaranData] = useState<any[]>(() => {
    const saved = localStorage.getItem('sims_kategori_pelanggaran');
    return saved ? JSON.parse(saved) : [
      { id: '1', kategori: 'Keterlambatan', jenis: 'Terlambat Masuk', poin: 10 },
      { id: '2', kategori: 'Kerapian', jenis: 'Rambut Panjang', poin: 5 },
      { id: '3', kategori: 'Perilaku', jenis: 'Berkelahi', poin: 50 },
    ];
  });"""

content = content.replace(bad_state, good_state)

with open('src/context/DatabaseContext.tsx', 'w') as f:
    f.write(content)
