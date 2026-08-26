import re

with open('gas/Comp_MasterSiswa.html', 'r') as f:
    content = f.read()

# Replace emerald with indigo
content = content.replace('emerald', 'indigo')

# Modify top bar buttons
top_buttons = """    <div class="flex flex-wrap items-center gap-2 mt-4 sm:mt-0">
      <button onclick="showImportModal()" class="flex items-center gap-2 px-4 py-2 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 font-medium rounded-lg transition-colors border border-slate-200 dark:border-slate-700 text-sm">
        <i class="fas fa-file-import"></i> Import
      </button>
      <button onclick="exportSiswa()" class="flex items-center gap-2 px-4 py-2 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 font-medium rounded-lg transition-colors border border-slate-200 dark:border-slate-700 text-sm">
        <i class="fas fa-file-export"></i> Export
      </button>
      <button onclick="showModalSiswa()" class="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white hover:bg-indigo-700 font-medium rounded-lg transition-colors shadow-sm shadow-indigo-600/20 text-sm">
        <i class="fas fa-plus"></i> Tambah Siswa
      </button>
    </div>"""

content = re.sub(r'<div class="flex items-center gap-2">\s*<button.*?Tambah Siswa\s*</button>\s*</div>', top_buttons, content)

# Dark mode styling
content = content.replace('bg-white', 'bg-white dark:bg-slate-900')
content = content.replace('border-slate-200', 'border-slate-200 dark:border-slate-800')
content = content.replace('text-slate-800', 'text-slate-800 dark:text-slate-100')
content = content.replace('text-slate-700', 'text-slate-700 dark:text-slate-200')
content = content.replace('text-slate-600', 'text-slate-600 dark:text-slate-300')
content = content.replace('text-slate-500', 'text-slate-500 dark:text-slate-400')
content = content.replace('text-slate-400', 'text-slate-400 dark:text-slate-500')
content = content.replace('bg-slate-50', 'bg-slate-50 dark:bg-slate-950')
content = content.replace('bg-indigo-100', 'bg-indigo-100 dark:bg-indigo-900/30')
content = content.replace('text-indigo-700', 'text-indigo-700 dark:text-indigo-400')
content = content.replace('hover:bg-slate-50', 'hover:bg-slate-50 dark:hover:bg-slate-800')
content = content.replace('text-slate-900', 'text-slate-900 dark:text-slate-100')

# Adding Modal HTML before <script>
modal_html = """
  <!-- Modal Tambah/Edit Siswa -->
  <div id="modalSiswa" class="fixed inset-0 bg-slate-900/50 z-50 hidden flex items-center justify-center">
    <div class="bg-white dark:bg-slate-900 rounded-2xl shadow-xl w-full max-w-lg overflow-hidden border border-slate-200 dark:border-slate-800 transform scale-95 opacity-0 transition-all duration-300" id="modalSiswaContent">
      <div class="p-6 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
        <h3 class="text-lg font-bold text-slate-800 dark:text-slate-100" id="modalSiswaTitle">Tambah Siswa Baru</h3>
        <button onclick="hideModalSiswa()" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-300">
          <i class="fas fa-times text-xl"></i>
        </button>
      </div>
      <form id="formSiswa" onsubmit="handleSaveSiswa(event)" class="p-6 space-y-4">
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">NIS</label>
            <input type="text" id="siswaNis" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">NISN</label>
            <input type="text" id="siswaNisn" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
          </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Nama Lengkap</label>
          <input type="text" id="siswaNama" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Kelas</label>
            <select id="siswaKelas" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
              <option value="7A">7A</option>
              <option value="7B">7B</option>
              <option value="8A">8A</option>
              <option value="8B">8B</option>
              <option value="9A">9A</option>
              <option value="9B">9B</option>
            </select>
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Jenis Kelamin</label>
            <select id="siswaJk" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
              <option value="L">Laki-laki</option>
              <option value="P">Perempuan</option>
            </select>
          </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Status</label>
          <select id="siswaStatus" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
            <option value="Aktif">Aktif</option>
            <option value="Pindah">Pindah</option>
            <option value="Lulus">Lulus</option>
          </select>
        </div>
        <div class="flex justify-end gap-3 pt-4">
          <button type="button" onclick="hideModalSiswa()" class="px-4 py-2 text-slate-600 dark:text-slate-300 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 font-medium rounded-lg transition-colors">Batal</button>
          <button type="submit" id="btnSaveSiswa" class="px-4 py-2 bg-indigo-600 text-white hover:bg-indigo-700 font-medium rounded-lg transition-colors">Simpan</button>
        </div>
      </form>
    </div>
  </div>
"""

content = content.replace('</div>\n<script>', modal_html + '</div>\n<script>')

# Replace input dark classes
content = content.replace('bg-white border border-slate-200 dark:border-slate-800 rounded-lg', 'bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-200 dark:border-slate-700 rounded-lg')

# JS Additions for modal
js_additions = """
  function showModalSiswa(siswa = null) {
    var modal = document.getElementById('modalSiswa');
    var content = document.getElementById('modalSiswaContent');
    
    if (siswa) {
      document.getElementById('modalSiswaTitle').innerText = 'Edit Siswa';
      document.getElementById('siswaNis').value = siswa.nis;
      document.getElementById('siswaNis').readOnly = true;
      document.getElementById('siswaNisn').value = siswa.nisn;
      document.getElementById('siswaNama').value = siswa.nama;
      document.getElementById('siswaKelas').value = siswa.kelas;
      document.getElementById('siswaJk').value = siswa.jk;
      document.getElementById('siswaStatus').value = siswa.status;
    } else {
      document.getElementById('modalSiswaTitle').innerText = 'Tambah Siswa Baru';
      document.getElementById('formSiswa').reset();
      document.getElementById('siswaNis').readOnly = false;
    }
    
    modal.classList.remove('hidden');
    setTimeout(() => {
      content.classList.remove('scale-95', 'opacity-0');
      content.classList.add('scale-100', 'opacity-100');
    }, 10);
  }
  
  function hideModalSiswa() {
    var modal = document.getElementById('modalSiswa');
    var content = document.getElementById('modalSiswaContent');
    
    content.classList.remove('scale-100', 'opacity-100');
    content.classList.add('scale-95', 'opacity-0');
    setTimeout(() => {
      modal.classList.add('hidden');
    }, 300);
  }
  
  function handleSaveSiswa(e) {
    e.preventDefault();
    var btn = document.getElementById('btnSaveSiswa');
    var originalText = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Menyimpan...';
    btn.disabled = true;
    
    var data = {
      nis: document.getElementById('siswaNis').value,
      nisn: document.getElementById('siswaNisn').value,
      nama: document.getElementById('siswaNama').value,
      kelas: document.getElementById('siswaKelas').value,
      jk: document.getElementById('siswaJk').value,
      status: document.getElementById('siswaStatus').value
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
          hideModalSiswa();
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
      .saveSiswa(data);
  }
  
  function editSiswa(btn, dataStr) {
    var data = JSON.parse(decodeURIComponent(dataStr));
    showModalSiswa(data);
  }
  
  function exportSiswa() {
    Swal.fire({
      title: 'Export Data Siswa?',
      text: "Data akan diexport sebagai file CSV/Excel",
      icon: 'info',
      showCancelButton: true,
      confirmButtonColor: '#4f46e5',
      cancelButtonColor: '#64748b',
      confirmButtonText: 'Ya, Export!'
    }).then((result) => {
      if (result.isConfirmed) {
        google.script.run
          .withSuccessHandler(function(url) {
             window.open(url, '_blank');
          })
          .getExportUrl('Master_Siswa'); // Asumsi ada fungsi getExportUrl di GAS
      }
    });
  }
  
  function showImportModal() {
     Swal.fire({
      title: 'Import Data Siswa',
      html: `
        <div class="mb-4 text-sm text-slate-600 dark:text-slate-400 text-left">
          Pastikan format file CSV/Excel sesuai dengan urutan: <br/>
          <b>NIS, NISN, Nama, Kelas, L/P, Status</b>
        </div>
        <input type="file" id="fileImport" class="w-full text-sm text-slate-500 dark:text-slate-400
          file:mr-4 file:py-2 file:px-4
          file:rounded-full file:border-0
          file:text-sm file:font-semibold
          file:bg-indigo-50 file:text-indigo-700
          hover:file:bg-indigo-100 dark:file:bg-indigo-900/30 dark:file:text-indigo-300
        "/>
      `,
      showCancelButton: true,
      confirmButtonColor: '#4f46e5',
      cancelButtonColor: '#64748b',
      confirmButtonText: 'Import',
      preConfirm: () => {
        const fileInput = document.getElementById('fileImport');
        if (!fileInput.files.length) {
          Swal.showValidationMessage('Pilih file terlebih dahulu');
        }
        return fileInput.files[0];
      }
    }).then((result) => {
      if (result.isConfirmed && result.value) {
        var file = result.value;
        var reader = new FileReader();
        reader.onload = function(e) {
          var content = e.target.result;
          // Split base64
          var data = content.split(',')[1];
          
          Swal.fire({
            title: 'Memproses...',
            text: 'Sedang mengimport data siswa',
            allowOutsideClick: false,
            didOpen: () => {
              Swal.showLoading();
            }
          });
          
          google.script.run
            .withSuccessHandler(function(res) {
              if (res.success) {
                Swal.fire('Berhasil!', res.message, 'success');
                initPage();
              } else {
                Swal.fire('Gagal', res.message, 'error');
              }
            })
            .withFailureHandler(function(err) {
              Swal.fire('Error', err.toString(), 'error');
            })
            .importSiswaCsv(data, file.name);
        };
        reader.readAsDataURL(file);
      }
    });
  }
"""

content = content.replace('function initPage() {', js_additions + '\n  function initPage() {')

# Modify the edit button to pass data
content = content.replace("'<td class=\"px-6 py-4 text-right\"><button class=\"text-blue-600 hover:bg-blue-50 p-2 rounded\"><i class=\"fas fa-edit\"></i></button></td>';", """'<td class="px-6 py-4 text-right"><button onclick="editSiswa(this, \\'' + encodeURIComponent(JSON.stringify(s)) + '\\')" class="text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-900/30 p-2 rounded transition-colors"><i class="fas fa-edit"></i></button></td>';""")

# Use raw literal for regex
content = re.sub(r'html \+= \'<tr class="hover:bg-slate-50">\';', r'html += \'<tr class="hover:bg-slate-50 dark:hover:bg-slate-800 border-b border-slate-200 dark:border-slate-800 last:border-0">\';', content)
content = content.replace('bg-indigo-100 text-indigo-700', 'bg-indigo-100 dark:bg-indigo-900/30 text-indigo-700 dark:text-indigo-400')

with open('gas/Comp_MasterSiswa.html', 'w') as f:
    f.write(content)
