import re
with open('gas/Database.gs', 'r') as f:
    content = f.read()

new_setup = """
  sheetsDef.forEach(function(def) {
    var sheet = ss.getSheetByName(def.name);
    if (!sheet) {
      sheet = ss.insertSheet(def.name);
    }
    
    // Selalu update baris pertama (header) sesuai definisi terbaru
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(def.columns);
    } else {
      // Jika sudah ada isinya, timpa baris 1
      sheet.getRange(1, 1, 1, def.columns.length).setValues([def.columns]);
    }
    
    // Format header menjadi tebal dan berwarna hijau
    sheet.getRange(1, 1, 1, def.columns.length)
         .setFontWeight('bold')
         .setBackground('#10b981')
         .setFontColor('white');
    // Freeze baris pertama agar header selalu terlihat
    sheet.setFrozenRows(1);
  });
"""

content = re.sub(r'sheetsDef\.forEach\(function\(def\) \{.*?sheet\.setFrozenRows\(1\);\n    \}\n  \}\);', new_setup, content, flags=re.DOTALL)

with open('gas/Database.gs', 'w') as f:
    f.write(content)
