import re

# Fix Guru Modal
with open('gas/Comp_MasterGuru.html', 'r') as f:
    content = f.read()

if 'id="modalGuru"' not in content:
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
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">No HP</label>
          <input type="text" id="guruNoHp" class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>
        <div class="flex justify-end gap-3 pt-4">
          <button type="button" onclick="hideModalGuru()" class="px-4 py-2 text-slate-600 dark:text-slate-300 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 font-medium rounded-lg transition-colors">Batal</button>
          <button type="submit" id="btnSaveGuru" class="px-4 py-2 bg-indigo-600 text-white hover:bg-indigo-700 font-medium rounded-lg transition-colors">Simpan</button>
        </div>
      </form>
    </div>
  </div>\n"""
    content = content.replace('</div><script>', modal_html + '</div>\n<script>')
    with open('gas/Comp_MasterGuru.html', 'w') as f:
        f.write(content)


# Fix Siswa Modal
with open('gas/Comp_MasterSiswa.html', 'r') as f:
    content = f.read()

if 'id="modalSiswa"' not in content:
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
      <form id="formSiswa" onsubmit="handleSaveSiswa(event)" class="p-6 space-y-4 max-h-[70vh] overflow-y-auto custom-scrollbar">
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">NIS</label>
          <input type="text" id="siswaNis" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">NISN</label>
          <input type="text" id="siswaNisn" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Nama Lengkap</label>
          <input type="text" id="siswaNama" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Kelas</label>
            <input type="text" id="siswaKelas" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Jenis Kelamin</label>
            <select id="siswaJk" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
              <option value="L">Laki-laki (L)</option>
              <option value="P">Perempuan (P)</option>
            </select>
          </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Status</label>
          <select id="siswaStatus" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
            <option value="Aktif">Aktif</option>
            <option value="Lulus">Lulus</option>
            <option value="Pindah">Pindah</option>
            <option value="Keluar">Keluar</option>
          </select>
        </div>
        <div class="flex justify-end gap-3 pt-4">
          <button type="button" onclick="hideModalSiswa()" class="px-4 py-2 text-slate-600 dark:text-slate-300 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 font-medium rounded-lg transition-colors">Batal</button>
          <button type="submit" id="btnSaveSiswa" class="px-4 py-2 bg-indigo-600 text-white hover:bg-indigo-700 font-medium rounded-lg transition-colors">Simpan</button>
        </div>
      </form>
    </div>
  </div>\n"""
    content = content.replace('</div><script>', modal_html + '</div>\n<script>')
    with open('gas/Comp_MasterSiswa.html', 'w') as f:
        f.write(content)

