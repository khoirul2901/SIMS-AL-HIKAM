import re

with open('gas/Comp_MasterSiswa.html', 'r') as f:
    content = f.read()

# Fix hideModalSiswa syntax error
content = content.replace('''  function hideModalSiswa() {
    try {
    var modal = document.getElementById('modalSiswa');''', '''  function hideModalSiswa() {
    var modal = document.getElementById('modalSiswa');''')

# Fix showModalSiswa syntax error if any, well it has a catch so it's fine.
content = content.replace('''    } catch (error) {
      alert("Debug Show Modal: " + error.toString());
    }''', '')
content = content.replace('''  function showModalSiswa(siswa) {
    try {
    var modal = document.getElementById('modalSiswa');''', '''  function showModalSiswa(siswa) {
    var modal = document.getElementById('modalSiswa');''')

# Same for handleSaveSiswa
content = content.replace('''  function handleSaveSiswa(e) {
    e.preventDefault();
    try {
    var btn = document.getElementById('btnSaveSiswa');''', '''  function handleSaveSiswa(e) {
    e.preventDefault();
    var btn = document.getElementById('btnSaveSiswa');''')
content = content.replace('''    } catch (error) {
      Swal.fire("Debug Error", error.toString(), "error");
    }
  }''', '''  }''')

with open('gas/Comp_MasterSiswa.html', 'w') as f:
    f.write(content)

with open('gas/Comp_MasterGuru.html', 'r') as f:
    content2 = f.read()

content2 = content2.replace('''  function hideModalGuru() {
    try {
    var modal = document.getElementById('modalGuru');''', '''  function hideModalGuru() {
    var modal = document.getElementById('modalGuru');''')

content2 = content2.replace('''    } catch (error) {
      alert("Debug Show Modal: " + error.toString());
    }''', '')

content2 = content2.replace('''  function showModalGuru(guru) {
    try {
    var modal = document.getElementById('modalGuru');''', '''  function showModalGuru(guru) {
    var modal = document.getElementById('modalGuru');''')

content2 = content2.replace('''  function handleSaveGuru(e) {
    e.preventDefault();
    try {
    var btn = document.getElementById('btnSaveGuru');''', '''  function handleSaveGuru(e) {
    e.preventDefault();
    var btn = document.getElementById('btnSaveGuru');''')

content2 = content2.replace('''    } catch (error) {
      Swal.fire("Debug Error", error.toString(), "error");
    }
  }''', '''  }''')

with open('gas/Comp_MasterGuru.html', 'w') as f:
    f.write(content2)

