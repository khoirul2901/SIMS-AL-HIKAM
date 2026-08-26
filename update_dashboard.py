with open('src/pages/Dashboard.tsx', 'r') as f:
    content = f.read()

content = content.replace("import { useAuth } from '../context/AuthContext';", "import { useAuth } from '../context/AuthContext';\nimport { useDatabase } from '../context/DatabaseContext';")

content = content.replace("export const Dashboard = () => {", "export const Dashboard = () => {\n  const { siswaData, guruData, kelasData, pelanggaranData } = useDatabase();\n\n  const stats = {\n    totalGuru: guruData.length,\n    totalSiswa: siswaData.length,\n    totalKelas: kelasData.length,\n    absensiHariIni: 98,\n    pelanggaranBulanIni: pelanggaranData.length,\n    jumlahArsip: 1240,\n  };")

content = content.replace("MOCK_STATS.", "stats.")

with open('src/pages/Dashboard.tsx', 'w') as f:
    f.write(content)
