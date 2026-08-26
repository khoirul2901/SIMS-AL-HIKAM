import re

with open('gas/Index.html', 'r') as f:
    content = f.read()

# Add tailwind config for dark mode
tailwind_config = """    <script>
      tailwind.config = {
        darkMode: 'class',
        theme: {
          extend: {}
        }
      }
    </script>"""
content = content.replace('<script src="https://cdn.tailwindcss.com"></script>', '<script src="https://cdn.tailwindcss.com"></script>\n' + tailwind_config)

# Update colors for elegance (indigo/slate instead of emerald)
content = content.replace('bg-emerald-800', 'bg-slate-900')
content = content.replace('border-emerald-700/50', 'border-slate-800')
content = content.replace('text-emerald-300', 'text-slate-300')
content = content.replace('text-emerald-100', 'text-slate-400')
content = content.replace('hover:bg-emerald-700', 'hover:bg-slate-800')
content = content.replace('text-emerald-400', 'text-slate-500')
content = content.replace('text-emerald-200', 'text-slate-400')
content = content.replace('bg-emerald-900', 'bg-indigo-600')
content = content.replace('text-emerald-600', 'text-indigo-600')
content = content.replace('bg-emerald-100', 'bg-indigo-100 dark:bg-indigo-900/50')
content = content.replace('text-emerald-700', 'text-indigo-700 dark:text-indigo-300')

# Dark mode additions for body/main/header
content = content.replace('<body class="flex h-screen overflow-hidden text-slate-800">', '<body class="flex h-screen overflow-hidden text-slate-800 dark:text-slate-100 bg-slate-50 dark:bg-slate-950 transition-colors duration-300">')
content = content.replace('bg-slate-50', 'bg-slate-50 dark:bg-slate-950')
content = content.replace('bg-white', 'bg-white dark:bg-slate-900')
content = content.replace('border-slate-200', 'border-slate-200 dark:border-slate-800')
content = content.replace('text-slate-700', 'text-slate-700 dark:text-slate-200')
content = content.replace('text-slate-500', 'text-slate-500 dark:text-slate-400')

# Add dark mode toggle button in header
header_btn = """        <div class="flex items-center gap-4">
          <button onclick="toggleTheme()" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-300 transition-colors" title="Toggle Theme">
            <i id="themeIcon" class="fas fa-moon text-xl"></i>
          </button>
          <div class="w-8 h-8 rounded-full bg-indigo-100 dark:bg-indigo-900/50 text-indigo-700 dark:text-indigo-300 flex items-center justify-center font-bold" id="userInitial">"""
content = content.replace("""        <div class="flex items-center gap-4">
          <div class="w-8 h-8 rounded-full bg-indigo-100 dark:bg-indigo-900/50 text-indigo-700 dark:text-indigo-300 flex items-center justify-center font-bold" id="userInitial">""", header_btn)

# Add toggleTheme script
script_addition = """
      function toggleTheme() {
        if (document.documentElement.classList.contains('dark')) {
          document.documentElement.classList.remove('dark');
          localStorage.setItem('theme', 'light');
          document.getElementById('themeIcon').classList.replace('fa-sun', 'fa-moon');
        } else {
          document.documentElement.classList.add('dark');
          localStorage.setItem('theme', 'dark');
          document.getElementById('themeIcon').classList.replace('fa-moon', 'fa-sun');
        }
      }

      // Initialize theme
      if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
        document.addEventListener('DOMContentLoaded', () => {
          const icon = document.getElementById('themeIcon');
          if (icon) icon.classList.replace('fa-moon', 'fa-sun');
        });
      }
"""
content = content.replace('var currentPage = \'<?= page ?>\';', script_addition + '\n      var currentPage = \'<?= page ?>\';')

with open('gas/Index.html', 'w') as f:
    f.write(content)
