import re

with open('gas/Comp_MasterGuru.html', 'r') as f:
    content = f.read()

# Add noHp input field to the form
nohp_html = """        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">No HP</label>
          <input type="text" id="guruNoHp" required class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none">
        </div>"""

content = content.replace('        <div>\n          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Status Pegawai</label>', nohp_html + '\n        <div>\n          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Status Pegawai</label>')

# Add noHp to JS
content = content.replace("document.getElementById('guruStatus').value = guru.statusPegawai;", "document.getElementById('guruStatus').value = guru.statusPegawai;\n      document.getElementById('guruNoHp').value = guru.noHp || '';")
content = content.replace("statusPegawai: document.getElementById('guruStatus').value", "statusPegawai: document.getElementById('guruStatus').value,\n      noHp: document.getElementById('guruNoHp').value")

with open('gas/Comp_MasterGuru.html', 'w') as f:
    f.write(content)
