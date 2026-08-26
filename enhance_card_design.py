import re

with open('gas/Comp_MasterSiswa.html', 'r') as f:
    content = f.read()

new_card_css = """  .kartu-container {
    width: 8.5cm;
    height: 5.4cm;
    border: 1px solid #cbd5e1;
    border-radius: 12px;
    padding: 0;
    box-sizing: border-box;
    display: inline-block;
    margin: 10px;
    font-family: sans-serif;
    position: relative;
    background: #ffffff;
    background-image: radial-gradient(#e2e8f0 1px, transparent 1px);
    background-size: 10px 10px;
    color: #0f172a;
    overflow: hidden;
    box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  }
  .kartu-header {
    text-align: center;
    background: linear-gradient(to right, #4f46e5, #3b82f6);
    padding: 10px 5px;
    color: #ffffff;
    border-bottom: 3px solid #f59e0b;
  }
  .kartu-header h2 { margin: 0; font-size: 14px; font-weight: bold; letter-spacing: 1px; }
  .kartu-header h3 { margin: 0; font-size: 9px; font-weight: normal; opacity: 0.9; margin-top: 2px; }
  .kartu-body { font-size: 10px; line-height: 1.4; display: flex; padding: 12px; }
  .kartu-photo { 
    width: 55px; height: 75px; 
    border: 2px solid #e2e8f0; 
    border-radius: 6px;
    margin-right: 12px; 
    text-align: center; 
    line-height: 75px; 
    font-size: 8px; 
    color: #94a3b8;
    background: #f8fafc;
  }
  .kartu-info { flex: 1; }
  .kartu-info table { width: 100%; border-collapse: collapse; }
  .kartu-info td { vertical-align: top; padding-bottom: 4px; }
  .kartu-info td:first-child { width: 55px; font-weight: bold; color: #475569; }
"""

content = re.sub(r'  \.kartu-container \{.*?\n  \}\n(?=<\/style>)' , new_card_css, content, flags=re.DOTALL)

with open('gas/Comp_MasterSiswa.html', 'w') as f:
    f.write(content)

with open('src/pages/MasterSiswa.tsx', 'r') as f:
    react_content = f.read()

react_content = re.sub(r'\.kartu-container \{.*?\.kartu-info td:first-child \{ width: 60px; font-weight: bold; \}', new_card_css.replace('}', '}\n'), react_content, flags=re.DOTALL)

with open('src/pages/MasterSiswa.tsx', 'w') as f:
    f.write(react_content)
