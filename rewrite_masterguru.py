import re

with open('gas/Comp_MasterGuru.html', 'r') as f:
    content = f.read()

# Replace emerald with indigo
content = content.replace('emerald', 'indigo')

# Modify top bar buttons to include Import and Export (optional, let's just do Tambah Guru first)
top_buttons = """    <div class="flex flex-wrap items-center gap-2 mt-4 sm:mt-0">
      <button onclick="showModalGuru()" class="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white hover:bg-indigo-700 font-medium rounded-lg transition-colors shadow-sm shadow-indigo-600/20 text-sm">
        <i class="fas fa-plus"></i> Tambah Guru
      </button>
    </div>"""

content = re.sub(r'<div class="flex items-center gap-2">\s*<button.*?Tambah Guru\s*</button>\s*</div>', top_buttons, content)

# Dark mode styling
content = content.replace('bg-white', 'bg-white dark:bg-slate-900')
content = content.replace('border-slate-200', 'border-slate-200 dark:border-slate-800')
content = content.replace('text-slate-800', 'text-slate-800 dark:text-slate-100')
content = content.replace('text-slate-700', 'text-slate-700 dark:text-slate-200')
content = content.replace('text-slate-600', 'text-slate-600 dark:text-slate-300')
content = content.replace('text-slate-500', 'text-slate-500 dark:text-slate-400')
content = content.replace('text-slate-400', 'text-slate-400 dark:text-slate-500')
content = content.replace('bg-slate-50', 'bg-slate-50 dark:bg-slate-950')
content = content.replace('bg-blue-100', 'bg-blue-100 dark:bg-blue-900/30')
content = content.replace('text-blue-700', 'text-blue-700 dark:text-blue-400')
content = content.replace('text-slate-900', 'text-slate-900 dark:text-slate-100')

# Adding Modal HTML before <script>
modal_html = """
  <!-- Modal Tambah/Edit Guru -->
  <div id="modalGuru" class="fixed inset-0 bg-slate-900/50 z-50 hidden flex items-center justify-center">
    <div class="bg-white dark:bg-slate-900 rounded-2xl shadow-xl w-full max-w-lg overflow-hidden border border-slate-200 dark:border-slate-800 transform scale-95 opacity-0 transition-all duration-300" id="modalGuruContent">
      <div class="p-6 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
        <h3 class="text-lg font-bold text-slate-800 dark:text-slate-100" id="modalGuruTitle">Tambah Guru Baru</h3>
        <button onclick="hideModalGuru()" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-300">
          <i class="fas fa-times text-xl"></i>
        </button>
      </div>
      <form id="formGuru" onsubmit="handleSaveGuru(event)" class="p-6 space-y-4">
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">NIP / NUPTK</label>
          <input type="text" id="guruNip" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Nama Lengkap</label>
          <input type="text" id="guruNama" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Mata Pelajaran</label>
          <input type="text" id="guruMapel" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Status Pegawai</label>
          <select id="guruStatus" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
            <option value="GTY">Guru Tetap Yayasan (GTY)</option>
            <option value="GTT">Guru Tidak Tetap (GTT)</option>
          </select>
        </div>
        <div class="flex justify-end gap-3 pt-4">
          <button type="button" onclick="hideModalGuru()" class="px-4 py-2 text-slate-600 dark:text-slate-300 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 font-medium rounded-lg transition-colors">Batal</button>
          <button type="submit" id="btnSaveGuru" class="px-4 py-2 bg-indigo-600 text-white hover:bg-indigo-700 font-medium rounded-lg transition-colors">Simpan</button>
        </div>
      </form>
    </div>
  </div>
"""

content = content.replace('</div>\n<script>', modal_html + '</div>\n<script>')

# Replace input dark classes for search
content = content.replace('bg-white border border-slate-200 dark:border-slate-800 rounded-lg', 'bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-200 dark:border-slate-700 rounded-lg')

# JS Additions for modal
js_additions = """
  function showModalGuru(guru = null) {
    var modal = document.getElementById('modalGuru');
    var content = document.getElementById('modalGuruContent');
    
    if (guru) {
      document.getElementById('modalGuruTitle').innerText = 'Edit Guru';
      document.getElementById('guruNip').value = guru.nip;
      document.getElementById('guruNip').readOnly = true;
      document.getElementById('guruNama').value = guru.nama;
      document.getElementById('guruMapel').value = guru.mapel;
      document.getElementById('guruStatus').value = guru.statusPegawai;
    } else {
      document.getElementById('modalGuruTitle').innerText = 'Tambah Guru Baru';
      document.getElementById('formGuru').reset();
      document.getElementById('guruNip').readOnly = false;
    }
    
    modal.classList.remove('hidden');
    setTimeout(() => {
      content.classList.remove('scale-95', 'opacity-0');
      content.classList.add('scale-100', 'opacity-100');
    }, 10);
  }
  
  function hideModalGuru() {
    var modal = document.getElementById('modalGuru');
    var content = document.getElementById('modalGuruContent');
    
    content.classList.remove('scale-100', 'opacity-100');
    content.classList.add('scale-95', 'opacity-0');
    setTimeout(() => {
      modal.classList.add('hidden');
    }, 300);
  }
  
  function handleSaveGuru(e) {
    e.preventDefault();
    var btn = document.getElementById('btnSaveGuru');
    var originalText = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Menyimpan...';
    btn.disabled = true;
    
    var data = {
      nip: document.getElementById('guruNip').value,
      nama: document.getElementById('guruNama').value,
      mapel: document.getElementById('guruMapel').value,
      statusPegawai: document.getElementById('guruStatus').value
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
          hideModalGuru();
          initPage(); // Reload list
        } else {
          Swal.fire('Gagal', res.message || 'Terjadi kesalahan', 'error');
        }
      })
      .withFailureHandler(function(err) {
        btn.innerHTML = originalText;
        btn.disabled = false;
        Swal.fire('Error', err.toString(), 'error');
      })
      .saveGuru(data);
  }
  
  function editGuru(btn, dataStr) {
    var data = JSON.parse(decodeURIComponent(dataStr));
    showModalGuru(data);
  }
"""

content = content.replace('function initPage() {', js_additions + '\n  function initPage() {')

# Modify the edit button to pass data
content = content.replace("'<td class=\"px-6 py-4 text-right\"><button class=\"text-blue-600 hover:bg-blue-50 p-2 rounded\"><i class=\"fas fa-edit\"></i></button></td>';", """'<td class="px-6 py-4 text-right"><button onclick="editGuru(this, \\'' + encodeURIComponent(JSON.stringify(g)) + '\\')" class="text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-900/30 p-2 rounded transition-colors"><i class="fas fa-edit"></i></button></td>';""")

# Use raw literal for regex
content = re.sub(r'html \+= \'<tr class="hover:bg-slate-50">\';', r'html += \'<tr class="hover:bg-slate-50 dark:hover:bg-slate-800 border-b border-slate-200 dark:border-slate-800 last:border-0">\';', content)

with open('gas/Comp_MasterGuru.html', 'w') as f:
    f.write(content)
