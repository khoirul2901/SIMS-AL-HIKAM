import re

with open('gas/Comp_Dashboard.html', 'r') as f:
    content = f.read()

insights_html = """  <!-- AI Insights -->
  <div class="bg-indigo-50 dark:bg-indigo-900/20 p-6 rounded-2xl border border-indigo-100 dark:border-indigo-800/30 shadow-sm relative overflow-hidden">
    <div class="absolute top-0 right-0 p-4 opacity-10">
      <i class="fas fa-robot text-6xl text-indigo-500"></i>
    </div>
    <div class="flex items-center gap-3 mb-6 relative z-10">
      <div class="w-10 h-10 rounded-xl bg-indigo-600 text-white flex items-center justify-center shadow-lg shadow-indigo-600/30">
        <i class="fas fa-lightbulb"></i>
      </div>
      <div>
        <h3 class="font-bold text-indigo-900 dark:text-indigo-100 text-lg">Interpretasi Cerdas</h3>
        <p class="text-xs text-indigo-600 dark:text-indigo-400">Berdasarkan data hari ini</p>
      </div>
    </div>
    
    <div class="space-y-4 relative z-10">
      <div class="p-4 bg-white dark:bg-slate-900 rounded-xl border border-indigo-100 dark:border-indigo-800/50 shadow-sm flex items-start gap-3">
        <div class="w-8 h-8 rounded-full bg-green-100 dark:bg-green-900/30 text-green-600 flex items-center justify-center shrink-0 mt-0.5">
          <i class="fas fa-check"></i>
        </div>
        <div>
          <h4 class="text-sm font-semibold text-slate-800 dark:text-slate-100">Tingkat Kehadiran Sangat Baik</h4>
          <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Kehadiran mencapai 98%. Pertahankan program motivasi pagi yang telah berjalan dengan baik.</p>
        </div>
      </div>
      
      <div class="p-4 bg-white dark:bg-slate-900 rounded-xl border border-amber-100 dark:border-amber-800/50 shadow-sm flex items-start gap-3">
        <div class="w-8 h-8 rounded-full bg-amber-100 dark:bg-amber-900/30 text-amber-600 flex items-center justify-center shrink-0 mt-0.5">
          <i class="fas fa-exclamation-triangle"></i>
        </div>
        <div>
          <h4 class="text-sm font-semibold text-slate-800 dark:text-slate-100">Perhatian: Tunggakan SPP</h4>
          <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Terdapat 15% siswa yang belum menyelesaikan administrasi bulan ini. Disarankan mengirim pesan pengingat ke orang tua.</p>
        </div>
      </div>
    </div>
  </div>
</div>
<script>"""

content = re.sub(r'</div>\s*</div>\s*<script>', '</div>\n' + insights_html, content)

with open('gas/Comp_Dashboard.html', 'w') as f:
    f.write(content)
