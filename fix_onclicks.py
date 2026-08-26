import re

with open('gas/Comp_MasterSiswa.html', 'r') as f:
    content = f.read()

content = content.replace('onclick="showModalSiswa()"', 'onclick="showModalSiswa(false)"')
content = content.replace('function showModalSiswa(siswa = null)', 'function showModalSiswa(siswa)')
content = content.replace('if (siswa) {', 'if (siswa && siswa.nis) {')

with open('gas/Comp_MasterSiswa.html', 'w') as f:
    f.write(content)

with open('gas/Comp_MasterGuru.html', 'r') as f:
    content2 = f.read()

content2 = content2.replace('onclick="showModalGuru()"', 'onclick="showModalGuru(false)"')
content2 = content2.replace('function showModalGuru(guru = null)', 'function showModalGuru(guru)')
content2 = content2.replace('if (guru) {', 'if (guru && guru.nip) {')

with open('gas/Comp_MasterGuru.html', 'w') as f:
    f.write(content2)

