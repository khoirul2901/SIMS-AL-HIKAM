with open('src/pages/Dashboard.tsx', 'r') as f:
    content = f.read()

# Find STAT_CARDS
import re
stat_cards_match = re.search(r'const STAT_CARDS = \[.*?\];', content, flags=re.DOTALL)
if stat_cards_match:
    stat_cards = stat_cards_match.group(0)
    content = content.replace(stat_cards, "")
    
    # insert inside Dashboard
    dashboard_def = "export const Dashboard = () => {\n  const { siswaData, guruData, kelasData, pelanggaranData } = useDatabase();\n\n  const stats = {\n    totalGuru: guruData.length,\n    totalSiswa: siswaData.length,\n    totalKelas: kelasData.length,\n    absensiHariIni: 98,\n    pelanggaranBulanIni: pelanggaranData.length,\n    jumlahArsip: 1240,\n  };\n"
    
    new_dashboard_def = dashboard_def + "\n  " + stat_cards.replace("\n", "\n  ") + "\n"
    content = content.replace(dashboard_def, new_dashboard_def)
    
    with open('src/pages/Dashboard.tsx', 'w') as f:
        f.write(content)
