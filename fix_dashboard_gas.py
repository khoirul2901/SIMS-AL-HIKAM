with open('gas/Comp_Dashboard.html', 'r') as f:
    content = f.read()

import re
content = re.sub(r'function initPage\(\) \{', 'window.initPage = function() {', content)

with open('gas/Comp_Dashboard.html', 'w') as f:
    f.write(content)
