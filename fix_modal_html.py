import re

with open('gas/Comp_MasterKelas.html', 'r') as f:
    kelas_content = f.read()

kelas_modal = """
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
  </div>
"""

if 'id="modalKelas"' not in kelas_content:
    kelas_content = re.sub(r'</div>\s*<script>', kelas_modal + '</div>\n<script>', kelas_content)
    with open('gas/Comp_MasterKelas.html', 'w') as f:
        f.write(kelas_content)

with open('gas/Comp_MasterMapel.html', 'r') as f:
    mapel_content = f.read()

mapel_modal = """
  <!-- Modal Tambah/Edit Mapel -->
  <div id="modalMapel" class="fixed inset-0 bg-slate-900/50 z-50 hidden flex items-center justify-center">
    <div class="bg-white dark:bg-slate-900 rounded-2xl shadow-xl w-full max-w-md overflow-hidden border border-slate-200 dark:border-slate-800 transform scale-95 opacity-0 transition-all duration-300" id="modalMapelContent">
      <div class="p-6 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
        <h3 class="text-lg font-bold text-slate-800 dark:text-slate-100" id="modalMapelTitle">Tambah Mapel Baru</h3>
        <button onclick="hideModalMapel()" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-300">
          <i class="fas fa-times text-xl"></i>
        </button>
      </div>
      <form id="formMapel" onsubmit="handleSaveMapel(event)" class="p-6 space-y-4">
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Kode Mapel</label>
          <input type="text" id="mapelKode" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Nama Mapel</label>
          <input type="text" id="mapelNama" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Kelompok</label>
          <select id="mapelKelompok" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
            <option value="Muatan Nasional">Muatan Nasional</option>
            <option value="Muatan Kewilayahan">Muatan Kewilayahan</option>
            <option value="Muatan Peminatan Kejuruan">Muatan Peminatan Kejuruan</option>
            <option value="Muatan Lokal">Muatan Lokal</option>
          </select>
        </div>
        <div class="flex justify-end gap-3 pt-4">
          <button type="button" onclick="hideModalMapel()" class="px-4 py-2 text-slate-600 dark:text-slate-300 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 font-medium rounded-lg transition-colors">Batal</button>
          <button type="submit" id="btnSaveMapel" class="px-4 py-2 bg-indigo-600 text-white hover:bg-indigo-700 font-medium rounded-lg transition-colors">Simpan</button>
        </div>
      </form>
    </div>
  </div>
"""

if 'id="modalMapel"' not in mapel_content:
    mapel_content = re.sub(r'</div>\s*<script>', mapel_modal + '</div>\n<script>', mapel_content)
    with open('gas/Comp_MasterMapel.html', 'w') as f:
        f.write(mapel_content)

