import re

with open('gas/Comp_MasterSiswa.html', 'r') as f:
    content = f.read()

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

content = re.sub(r'<div class="flex items-center gap-2">\s*<button.*?>\s*<i class="fas fa-plus"></i> Tambah Siswa\s*</button>\s*</div>', top_buttons, content, flags=re.DOTALL)

with open('gas/Comp_MasterSiswa.html', 'w') as f:
    f.write(content)

with open('gas/Comp_MasterGuru.html', 'r') as f:
    content2 = f.read()

top_buttons2 = """    <div class="flex flex-wrap items-center gap-2 mt-4 sm:mt-0">
      <button onclick="showModalGuru()" class="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white hover:bg-indigo-700 font-medium rounded-lg transition-colors shadow-sm shadow-indigo-600/20 text-sm">
        <i class="fas fa-plus"></i> Tambah Guru
      </button>
    </div>"""

content2 = re.sub(r'<div class="flex items-center gap-2">\s*<button.*?>\s*<i class="fas fa-plus"></i> Tambah Guru\s*</button>\s*</div>', top_buttons2, content2, flags=re.DOTALL)

with open('gas/Comp_MasterGuru.html', 'w') as f:
    f.write(content2)

