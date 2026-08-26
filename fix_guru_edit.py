import re

with open('gas/Comp_MasterGuru.html', 'r') as f:
    content = f.read()

old_btn = '<td class="px-6 py-4 text-right"><button class="text-blue-600 hover:bg-blue-50 p-2 rounded"><i class="fas fa-edit"></i></button></td>'
new_btn = '<td class="px-6 py-4 text-right"><button onclick="editGuru(this, \\\'\' + encodeURIComponent(JSON.stringify(g)) + \'\\\')" class="text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-900/30 p-2 rounded transition-colors"><i class="fas fa-edit"></i></button></td>'

content = content.replace(old_btn, new_btn)
content = content.replace('<tr class="hover:bg-slate-50 dark:bg-slate-950">', '<tr class="hover:bg-slate-50 dark:hover:bg-slate-800 border-b border-slate-200 dark:border-slate-800 last:border-0">')
content = content.replace('<tr class="hover:bg-slate-50">', '<tr class="hover:bg-slate-50 dark:hover:bg-slate-800 border-b border-slate-200 dark:border-slate-800 last:border-0">')

with open('gas/Comp_MasterGuru.html', 'w') as f:
    f.write(content)
