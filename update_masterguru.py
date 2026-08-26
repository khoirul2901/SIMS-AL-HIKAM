with open('src/pages/MasterGuru.tsx', 'r') as f:
    content = f.read()

content = content.replace("import React, { useState } from 'react';", "import React, { useState } from 'react';\nimport { useDatabase } from '../context/DatabaseContext';")

content = content.replace("export const MasterGuru = () => {\n  const [data, setData] = useState(INITIAL_GURU_DATA);", "export const MasterGuru = () => {\n  const { guruData: data, setGuruData: setData } = useDatabase();")

with open('src/pages/MasterGuru.tsx', 'w') as f:
    f.write(content)
