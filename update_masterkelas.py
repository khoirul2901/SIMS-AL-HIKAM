with open('src/pages/MasterKelas.tsx', 'r') as f:
    content = f.read()

content = content.replace("import React, { useState } from 'react';", "import React, { useState } from 'react';\nimport { useDatabase } from '../context/DatabaseContext';")

content = content.replace("export const MasterKelas = () => {\n  const [data, setData] = useState(INITIAL_KELAS_DATA);", "export const MasterKelas = () => {\n  const { kelasData: data, setKelasData: setData } = useDatabase();")

with open('src/pages/MasterKelas.tsx', 'w') as f:
    f.write(content)
