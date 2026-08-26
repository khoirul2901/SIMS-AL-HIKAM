import re

with open('gas/Comp_MasterKelas.html', 'r') as f:
    content = f.read()

content = content.replace(
    'html += \'  <td class="px-6 py-4 text-right"><button class="text-blue-600 hover:bg-blue-50 p-2 rounded"><i class="fas fa-edit"></i></button></td>\';',
    """html += '  <td class="px-6 py-4 text-right"><button onclick="editKelas(this, \\'' + encodeURIComponent(JSON.stringify(k)) + '\\')" class="text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-900/30 p-2 rounded transition-colors"><i class="fas fa-edit"></i></button></td>';"""
)

with open('gas/Comp_MasterKelas.html', 'w') as f:
    f.write(content)

with open('gas/Comp_MasterMapel.html', 'r') as f:
    content2 = f.read()

content2 = content2.replace(
    'html += \'  <td class="px-6 py-4 text-right"><button class="text-blue-600 hover:bg-blue-50 p-2 rounded"><i class="fas fa-edit"></i></button></td>\';',
    """html += '  <td class="px-6 py-4 text-right"><button onclick="editMapel(this, \\'' + encodeURIComponent(JSON.stringify(m)) + '\\')" class="text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-900/30 p-2 rounded transition-colors"><i class="fas fa-edit"></i></button></td>';"""
)

with open('gas/Comp_MasterMapel.html', 'w') as f:
    f.write(content2)

