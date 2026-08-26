import re

with open('gas/Login.html', 'r') as f:
    content = f.read()

# Add tailwind config for dark mode
tailwind_config = """    <script>
      tailwind.config = {
        darkMode: 'class',
        theme: {
          extend: {}
        }
      }
    </script>
    <script>
      if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
      }
    </script>"""
content = content.replace('<script src="https://cdn.tailwindcss.com"></script>', '<script src="https://cdn.tailwindcss.com"></script>\n' + tailwind_config)

# Update styling
content = content.replace('bg-slate-50', 'bg-slate-50 dark:bg-slate-950')
content = content.replace('bg-white', 'bg-white dark:bg-slate-900')
content = content.replace('bg-emerald-700', 'bg-indigo-600 dark:bg-indigo-700')
content = content.replace('text-emerald-100', 'text-indigo-100')
content = content.replace('text-slate-800', 'text-slate-800 dark:text-slate-100')
content = content.replace('text-slate-700', 'text-slate-700 dark:text-slate-300')
content = content.replace('border-slate-300', 'border-slate-300 dark:border-slate-700')
content = content.replace('focus:ring-emerald-500', 'focus:ring-indigo-500 dark:focus:ring-indigo-400')
content = content.replace('focus:border-emerald-500', 'focus:border-indigo-500 dark:focus:border-indigo-400')
content = content.replace('bg-emerald-600', 'bg-indigo-600')
content = content.replace('hover:bg-emerald-700', 'hover:bg-indigo-700')
content = content.replace('class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 outline-none transition-all"', 'class="w-full px-4 py-2 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 dark:focus:ring-indigo-400 focus:border-indigo-500 dark:focus:border-indigo-400 outline-none transition-all"')


with open('gas/Login.html', 'w') as f:
    f.write(content)
