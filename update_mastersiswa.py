with open('src/pages/MasterSiswa.tsx', 'r') as f:
    content = f.read()

content = content.replace("import React, { useState } from 'react';", "import React, { useState } from 'react';\nimport { useDatabase } from '../context/DatabaseContext';")

content = content.replace("export const MasterSiswa = () => {\n  const [data, setData] = useState(INITIAL_SISWA_DATA);", "export const MasterSiswa = () => {\n  const { siswaData: data, setSiswaData: setData, kelasData } = useDatabase();")

# We should also replace the select options to use the kelasData dynamically
with open('src/pages/MasterSiswa.tsx', 'w') as f:
    f.write(content)
