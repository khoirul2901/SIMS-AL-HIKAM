import re

with open('gas/Comp_MasterKelas.html', 'r') as f:
    content = f.read()

# Replace emerald with indigo, add dark mode styling
content = content.replace('emerald', 'indigo')
content = content.replace('bg-white', 'bg-white dark:bg-slate-900')
content = content.replace('border-slate-200', 'border-slate-200 dark:border-slate-800')
content = content.replace('text-slate-800', 'text-slate-800 dark:text-slate-100')
content = content.replace('text-slate-700', 'text-slate-700 dark:text-slate-200')
content = content.replace('text-slate-600', 'text-slate-600 dark:text-slate-300')
content = content.replace('text-slate-500', 'text-slate-500 dark:text-slate-400')
content = content.replace('text-slate-400', 'text-slate-400 dark:text-slate-500')
content = content.replace('bg-slate-50', 'bg-slate-50 dark:bg-slate-950')
content = content.replace('bg-slate-100', 'bg-slate-100 dark:bg-slate-800')
content = content.replace('text-slate-900', 'text-slate-900 dark:text-slate-100')

# Update the search bar input
content = content.replace('bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg text-sm', 'bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-200 dark:border-slate-700 rounded-lg text-sm')

# Top buttons
top_buttons = """    <div class="flex flex-wrap items-center gap-2 mt-4 sm:mt-0">
      <button onclick="showModalKelas(false)" class="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white hover:bg-indigo-700 font-medium rounded-lg transition-colors shadow-sm shadow-indigo-600/20 text-sm">
        <i class="fas fa-plus"></i> Tambah Kelas
      </button>
    </div>"""
content = re.sub(r'<button onclick="Swal.fire.*?</button>', top_buttons, content, flags=re.DOTALL)

# Modal HTML
modal_html = """
  <!-- Modal Tambah/Edit Kelas -->
  <div id="modalKelas" class="fixed inset-0 bg-slate-900/50 z-50 hidden flex items-center justify-center">
    <div class="bg-white dark:bg-slate-900 rounded-2xl shadow-xl w-full max-w-md overflow-hidden border border-slate-200 dark:border-slate-800 transform scale-95 opacity-0 transition-all duration-300" id="modalKelasContent">
      <div class="p-6 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
        <h3 class="text-lg font-bold text-slate-800 dark:text-slate-100" id="modalKelasTitle">Tambah Kelas Baru</h3>
        <button onclick="hideModalKelas()" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-300">
          <i class="fas fa-times text-xl"></i>
        </button>
      </div>
      <form id="formKelas" onsubmit="handleSaveKelas(event)" class="p-6 space-y-4">
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Kode Kelas</label>
          <input type="text" id="kelasKode" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Nama Kelas</label>
          <input type="text" id="kelasNama" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Wali Kelas</label>
          <input type="text" id="kelasWali" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Jumlah Siswa</label>
          <input type="number" id="kelasJmlSiswa" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>
        <div class="flex justify-end gap-3 pt-4">
          <button type="button" onclick="hideModalKelas()" class="px-4 py-2 text-slate-600 dark:text-slate-300 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 font-medium rounded-lg transition-colors">Batal</button>
          <button type="submit" id="btnSaveKelas" class="px-4 py-2 bg-indigo-600 text-white hover:bg-indigo-700 font-medium rounded-lg transition-colors">Simpan</button>
        </div>
      </form>
    </div>
  </div>\n"""

# Insert modal
content = content.replace('</div><script>', modal_html + '</div>\n<script>')

js_additions = """
  function showModalKelas(kelas) {
    var modal = document.getElementById('modalKelas');
    var content = document.getElementById('modalKelasContent');
    
    if (kelas && kelas.kode) {
      document.getElementById('modalKelasTitle').innerText = 'Edit Kelas';
      document.getElementById('kelasKode').value = kelas.kode;
      document.getElementById('kelasKode').readOnly = true;
      document.getElementById('kelasNama').value = kelas.nama;
      document.getElementById('kelasWali').value = kelas.waliKelas;
      document.getElementById('kelasJmlSiswa').value = kelas.jumlahSiswa;
    } else {
      document.getElementById('modalKelasTitle').innerText = 'Tambah Kelas Baru';
      document.getElementById('formKelas').reset();
      document.getElementById('kelasKode').readOnly = false;
    }
    
    modal.classList.remove('hidden');
    setTimeout(() => {
      content.classList.remove('scale-95', 'opacity-0');
      content.classList.add('scale-100', 'opacity-100');
    }, 10);
  }
  
  function hideModalKelas() {
    var modal = document.getElementById('modalKelas');
    var content = document.getElementById('modalKelasContent');
    
    content.classList.remove('scale-100', 'opacity-100');
    content.classList.add('scale-95', 'opacity-0');
    setTimeout(() => {
      modal.classList.add('hidden');
    }, 300);
  }
  
  function handleSaveKelas(e) {
    e.preventDefault();
    var btn = document.getElementById('btnSaveKelas');
    var originalText = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Menyimpan...';
    btn.disabled = true;
    
    var data = {
      kode: document.getElementById('kelasKode').value,
      nama: document.getElementById('kelasNama').value,
      waliKelas: document.getElementById('kelasWali').value,
      jumlahSiswa: document.getElementById('kelasJmlSiswa').value
    };
    
    google.script.run
      .withSuccessHandler(function(res) {
        btn.innerHTML = originalText;
        btn.disabled = false;
        
        if (res.success) {
          Swal.fire({
            icon: 'success',
            title: 'Berhasil!',
            text: res.message,
            timer: 1500,
            showConfirmButton: false
          });
          hideModalKelas();
          initPage();
        } else {
          Swal.fire('Gagal', res.message || 'Terjadi kesalahan', 'error');
        }
      })
      .withFailureHandler(function(err) {
        btn.innerHTML = originalText;
        btn.disabled = false;
        Swal.fire('Error', err.toString(), 'error');
      })
      .saveKelas(data);
  }
  
  function editKelas(btn, dataStr) {
    var data = JSON.parse(decodeURIComponent(dataStr));
    showModalKelas(data);
  }
"""

content = content.replace('function initPage() {', js_additions + '\n  function initPage() {')

# Adjust table rows
content = re.sub(r'html \+= \'<tr class="hover:bg-slate-50 dark:bg-slate-950">\';', r'html += \'<tr class="hover:bg-slate-50 dark:hover:bg-slate-800 border-b border-slate-200 dark:border-slate-800 last:border-0">\';', content)
content = re.sub(r'<td class="px-6 py-4 font-mono text-slate-800 dark:text-slate-100">\' \+ k.kode \+ \'</td>', r'<td class="px-6 py-4 font-mono text-slate-800 dark:text-slate-100">\' + k.kode + \'</td>', content)

# Modify the edit button
content = content.replace("'<td class=\"px-6 py-4 text-right\"><button class=\"text-blue-600 hover:bg-blue-50 p-2 rounded\"><i class=\"fas fa-edit\"></i></button></td>';", """'<td class="px-6 py-4 text-right"><button onclick="editKelas(this, \\'' + encodeURIComponent(JSON.stringify(k)) + '\\')" class="text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-900/30 p-2 rounded transition-colors"><i class="fas fa-edit"></i></button></td>';""")

with open('gas/Comp_MasterKelas.html', 'w') as f:
    f.write(content)

