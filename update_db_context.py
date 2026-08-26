import re
with open('src/context/DatabaseContext.tsx', 'r') as f:
    content = f.read()

# Add absensiGuruData to context type
content = content.replace("absensiData: any[];\n  setAbsensiData: (data: any[]) => void;", "absensiData: any[];\n  setAbsensiData: (data: any[]) => void;\n  absensiGuruData: any[];\n  setAbsensiGuruData: (data: any[]) => void;\n  kategoriPelanggaranData: any[];\n  setKategoriPelanggaranData: (data: any[]) => void;")

# Add state
state_code = """
  const [absensiData, setAbsensiData] = useState<any[]>(() => {
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
  });
"""
content = re.sub(r'  const \[absensiData, setAbsensiData\] = useState.*?\]\);\n  \}\);', state_code, content, flags=re.DOTALL)

# Add effects
effect_code = """
  useEffect(() => { localStorage.setItem('sims_absensi', JSON.stringify(absensiData)); }, [absensiData]);
  useEffect(() => { localStorage.setItem('sims_absensi_guru', JSON.stringify(absensiGuruData)); }, [absensiGuruData]);
  useEffect(() => { localStorage.setItem('sims_kategori_pelanggaran', JSON.stringify(kategoriPelanggaranData)); }, [kategoriPelanggaranData]);
"""
content = content.replace("  useEffect(() => { localStorage.setItem('sims_absensi', JSON.stringify(absensiData)); }, [absensiData]);", effect_code)

# Add to provider values
content = content.replace("absensiData, setAbsensiData", "absensiData, setAbsensiData, absensiGuruData, setAbsensiGuruData, kategoriPelanggaranData, setKategoriPelanggaranData")

with open('src/context/DatabaseContext.tsx', 'w') as f:
    f.write(content)
