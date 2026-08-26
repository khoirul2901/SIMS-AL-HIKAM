import re

with open('gas/Index.html', 'r') as f:
    content = f.read()

new_success_handler = """          .withSuccessHandler(function(html) {
            container.innerHTML = html;
            
            // Execute scripts inside the injected HTML
            var scripts = container.getElementsByTagName('script');
            for (var i = 0; i < scripts.length; i++) {
              var script = document.createElement('script');
              if (scripts[i].src) {
                script.src = scripts[i].src;
              } else {
                script.innerHTML = scripts[i].innerHTML;
              }
              document.body.appendChild(script);
            }
            
            // Jika halaman yang diload memiliki fungsi inisialisasi, panggil fungsi tersebut
            setTimeout(function() {
              if (typeof initPage === 'function') {
                initPage();
              }
            }, 100);
          })"""

content = re.sub(r'\.withSuccessHandler\(function\(html\)\s*\{\s*container\.innerHTML = html;\s*// Jika halaman yang diload memiliki fungsi inisialisasi, panggil fungsi tersebut\s*if \(typeof initPage === \'function\'\) \{\s*initPage\(\);\s*\}\s*\}\)', new_success_handler, content, flags=re.MULTILINE)

with open('gas/Index.html', 'w') as f:
    f.write(content)
