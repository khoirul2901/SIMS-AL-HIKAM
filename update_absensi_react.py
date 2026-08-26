with open('src/pages/AbsensiSiswa.tsx', 'r') as f:
    content = f.read()

content = content.replace("import React, { useState } from 'react';", "import React, { useState, useEffect } from 'react';\nimport { useDatabase } from '../context/DatabaseContext';")

content = content.replace("import { INITIAL_KELAS_DATA } from './MasterKelas';", "")

content = content.replace("const SISWA_DATA = [", "/* const SISWA_DATA = [")
content = content.replace("];\n\nexport const AbsensiSiswa", "]; */\n\nexport const AbsensiSiswa")

content = content.replace("export const AbsensiSiswa = () => {", "export const AbsensiSiswa = () => {\n  const { siswaData, kelasData, absensiData, setAbsensiData } = useDatabase();")

# I need to change:
# const uniqueKelas = INITIAL_KELAS_DATA.map(k => k.namaKelas).sort();
# to
# const uniqueKelas = kelasData.map(k => k.namaKelas).sort();

content = content.replace("INITIAL_KELAS_DATA", "kelasData")

# Also, I need to remove `const [data, setData] = useState(SISWA_DATA);`
# and map `siswaData` directly! But `siswaData` has `nis`, `nama`, `kelas`, `jk`, but not `status`.
# We need to compute `filteredData` dynamically with the current `absensiData`.

with open('src/pages/AbsensiSiswa.tsx', 'w') as f:
    f.write(content)
