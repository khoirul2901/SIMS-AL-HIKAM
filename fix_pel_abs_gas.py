import re

for filename in ['gas/Comp_Pelanggaran.html', 'gas/Comp_AbsensiSiswa.html']:
    with open(filename, 'r') as f:
        content = f.read()

    content = re.sub(r'function initPage\(\) \{', 'window.initPage = function() {', content)
    content = re.sub(r'function initAbsensi\(\) \{', 'window.initPage = function() {', content)
    content = content.replace("setTimeout(initAbsensi, 500);", "")

    with open(filename, 'w') as f:
        f.write(content)
