with open('gas/Comp_Pelanggaran.html', 'r') as f:
    content = f.read()

new_content = """<div class="space-y-6">
  <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
    <div>
      <h1 class="text-2xl font-bold text-slate-800">Pelanggaran & Kedisiplinan</h1>
      <p class="text-sm text-slate-500 mt-1">Catat dan pantau kedisiplinan siswa</p>
    </div>
    <div class="flex gap-2">
      <button id="btnCatat" onclick="showFormCatat()" class="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white hover:bg-blue-700 font-medium rounded-lg transition-colors text-sm">
        <i class="fas fa-plus"></i> Catat Pelanggaran
      </button>
      <button id="btnKat" onclick="showFormKategori()" class="hidden items-center gap-2 px-4 py-2 bg-indigo-600 text-white hover:bg-indigo-700 font-medium rounded-lg transition-colors text-sm">
        <i class="fas fa-plus"></i> Tambah Kategori
      </button>
    </div>
  </div>

  <div class="flex border-b border-slate-200">
    <button onclick="switchTab('riwayat')" id="tab-riwayat" class="px-4 py-3 text-sm font-medium border-b-2 border-blue-600 text-blue-600 transition-colors">
      <i class="fas fa-exclamation-triangle mr-2"></i>Riwayat Pelanggaran
    </button>
    <button onclick="switchTab('kategori')" id="tab-kategori" class="px-4 py-3 text-sm font-medium border-b-2 border-transparent text-slate-500 hover:text-slate-700 transition-colors">
      <i class="fas fa-cog mr-2"></i>Pengaturan Kategori
    </button>
  </div>

  <!-- TAB RIWAYAT -->
  <div id="view-riwayat" class="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
    <div class="p-4 border-b border-slate-200 bg-slate-50">
      <div class="relative max-w-md">
        <i class="fas fa-search absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
        <input type="text" id="searchRiwayat" onkeyup="filterRiwayat()" placeholder="Cari berdasarkan nama, NIS, kelas..." class="w-full pl-9 pr-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm">
      </div>
    </div>
    
    <div class="overflow-x-auto">
      <table class="w-full text-left text-sm">
        <thead class="bg-slate-50 text-slate-600 border-b border-slate-200">
          <tr>
            <th class="px-6 py-3 font-semibold">Tanggal</th>
            <th class="px-6 py-3 font-semibold">Siswa</th>
            <th class="px-6 py-3 font-semibold">Kategori & Pelanggaran</th>
            <th class="px-6 py-3 font-semibold text-center">Poin</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-100" id="tableRiwayat">
          <tr><td colspan="4" class="px-6 py-8 text-center text-slate-500">Memuat data...</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- TAB KATEGORI -->
  <div id="view-kategori" class="hidden bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
    <div class="overflow-x-auto">
      <table class="w-full text-left text-sm">
        <thead class="bg-slate-50 text-slate-600 border-b border-slate-200">
          <tr>
            <th class="px-6 py-3 font-semibold">Tingkat / Kategori</th>
            <th class="px-6 py-3 font-semibold">Jenis Pelanggaran</th>
            <th class="px-6 py-3 font-semibold text-center">Bobot Poin</th>
            <th class="px-6 py-3 font-semibold text-right">Aksi</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-100" id="tableKategori">
        </tbody>
      </table>
    </div>
  </div>
</div>

<script>
  var currentRiwayat = [];
  var currentKategori = [];
  var currentSiswa = [];

  window.initPage = function() {
    loadPelanggaranData();
  }

  function loadPelanggaranData() {
    google.script.run
      .withSuccessHandler(function(data) {
        currentRiwayat = data.riwayat;
        currentKategori = data.kategori;
        currentSiswa = data.siswa;
        
        renderRiwayat(currentRiwayat);
        renderKategori();
      })
      .getPelanggaranData();
  }

  function switchTab(tab) {
    if(tab === 'riwayat') {
      document.getElementById('view-riwayat').classList.remove('hidden');
      document.getElementById('view-kategori').classList.add('hidden');
      
      document.getElementById('tab-riwayat').classList.add('border-blue-600', 'text-blue-600');
      document.getElementById('tab-riwayat').classList.remove('border-transparent', 'text-slate-500');
      
      document.getElementById('tab-kategori').classList.remove('border-indigo-600', 'text-indigo-600');
      document.getElementById('tab-kategori').classList.add('border-transparent', 'text-slate-500');
      
      document.getElementById('btnCatat').classList.remove('hidden');
      document.getElementById('btnKat').classList.add('hidden');
      document.getElementById('btnCatat').style.display = 'flex';
    } else {
      document.getElementById('view-riwayat').classList.add('hidden');
      document.getElementById('view-kategori').classList.remove('hidden');
      
      document.getElementById('tab-kategori').classList.add('border-indigo-600', 'text-indigo-600');
      document.getElementById('tab-kategori').classList.remove('border-transparent', 'text-slate-500');
      
      document.getElementById('tab-riwayat').classList.remove('border-blue-600', 'text-blue-600');
      document.getElementById('tab-riwayat').classList.add('border-transparent', 'text-slate-500');
      
      document.getElementById('btnCatat').classList.add('hidden');
      document.getElementById('btnKat').classList.remove('hidden');
      document.getElementById('btnCatat').style.display = 'none';
      document.getElementById('btnKat').style.display = 'flex';
    }
  }

  function getKategoriColor(kategori) {
    var k = kategori.toLowerCase();
    if(k === 'ringan') return 'bg-amber-100 text-amber-700 border-amber-200';
    if(k === 'sedang') return 'bg-orange-100 text-orange-700 border-orange-200';
    if(k === 'berat') return 'bg-red-100 text-red-700 border-red-200';
    return 'bg-slate-100 text-slate-700 border-slate-200';
  }

  function renderRiwayat(data) {
    var tbody = document.getElementById('tableRiwayat');
    if(data.length === 0) {
      tbody.innerHTML = '<tr><td colspan="4" class="px-6 py-8 text-center text-slate-500">Tidak ada riwayat pelanggaran.</td></tr>';
      return;
    }
    
    var html = '';
    data.forEach(function(item) {
      html += `
        <tr class="hover:bg-slate-50">
          <td class="px-6 py-4">${item.tanggal}</td>
          <td class="px-6 py-4">
            <p class="font-medium text-slate-800">${item.nama}</p>
            <p class="text-xs text-slate-500">Kelas ${item.kelas} • NIS: ${item.nis}</p>
          </td>
          <td class="px-6 py-4">
            <p class="font-medium text-slate-800">${item.kategori}</p>
            <p class="text-xs text-slate-500">${item.pelanggaran}</p>
          </td>
          <td class="px-6 py-4 text-center">
            <span class="px-2.5 py-1 rounded border text-xs font-bold ${getKategoriColor(item.kategori)}">
              +${item.poin} Poin
            </span>
          </td>
        </tr>
      `;
    });
    tbody.innerHTML = html;
  }

  function filterRiwayat() {
    var search = document.getElementById('searchRiwayat').value.toLowerCase();
    var filtered = currentRiwayat.filter(function(item) {
      return (item.nama && item.nama.toLowerCase().includes(search)) || 
             (item.nis && item.nis.includes(search)) ||
             (item.kelas && item.kelas.toLowerCase().includes(search)) ||
             (item.pelanggaran && item.pelanggaran.toLowerCase().includes(search));
    });
    renderRiwayat(filtered);
  }

  function renderKategori() {
    var tbody = document.getElementById('tableKategori');
    if(currentKategori.length === 0) {
      tbody.innerHTML = '<tr><td colspan="4" class="px-6 py-8 text-center text-slate-500">Tidak ada data kategori.</td></tr>';
      return;
    }
    
    var html = '';
    currentKategori.forEach(function(kat) {
      html += `
        <tr class="hover:bg-slate-50">
          <td class="px-6 py-4">
            <span class="px-2.5 py-1 rounded border text-xs font-bold ${getKategoriColor(kat.kategori)}">
              ${kat.kategori}
            </span>
          </td>
          <td class="px-6 py-4">
            <p class="font-medium text-slate-800">${kat.jenis}</p>
          </td>
          <td class="px-6 py-4 text-center">
            <span class="font-bold text-slate-700">${kat.poin}</span>
          </td>
          <td class="px-6 py-4 text-right">
            <button onclick="hapusKategori('${kat.id}')" class="text-red-500 hover:bg-red-50 p-2 rounded-lg transition-colors">
              <i class="fas fa-trash"></i>
            </button>
          </td>
        </tr>
      `;
    });
    tbody.innerHTML = html;
  }

  function showFormCatat() {
    var studentOptions = currentSiswa.map(s => `<option value="${s.nis}">${s.nama} (${s.kelas})</option>`).join('');
    var kategoriOptions = currentKategori.map(k => `<option value="${k.id}">${k.kategori} - ${k.jenis} (${k.poin} Poin)</option>`).join('');
    
    Swal.fire({
      title: 'Catat Pelanggaran',
      html: `
        <div class="space-y-4 text-left">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Cari Siswa (NIS / Nama)</label>
            <input list="students" id="inpNis" class="w-full px-3 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500" placeholder="Ketik NIS atau Nama Siswa">
            <datalist id="students">
              ${studentOptions}
            </datalist>
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Jenis Pelanggaran</label>
            <select id="inpKategoriId" class="w-full px-3 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500">
              <option value="">-- Pilih Pelanggaran --</option>
              ${kategoriOptions}
            </select>
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Catatan Tambahan (Opsional)</label>
            <textarea id="inpCatatan" class="w-full px-3 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500" rows="2"></textarea>
          </div>
        </div>
      `,
      showCancelButton: true,
      confirmButtonText: 'Simpan',
      cancelButtonText: 'Batal',
      preConfirm: () => {
        var nis = document.getElementById('inpNis').value;
        var katId = document.getElementById('inpKategoriId').value;
        if(!nis || !katId) {
          Swal.showValidationMessage('Siswa dan Jenis Pelanggaran harus diisi');
          return false;
        }
        return { nis: nis, katId: katId, catatan: document.getElementById('inpCatatan').value };
      }
    }).then((result) => {
      if(result.isConfirmed) {
        var val = result.value;
        var siswa = currentSiswa.find(s => s.nis === val.nis);
        var kat = currentKategori.find(k => k.id === val.katId);
        
        if(!siswa) {
          Swal.fire('Error', 'Siswa tidak ditemukan dalam database!', 'error');
          return;
        }
        
        var payload = {
          nis: siswa.nis,
          nama: siswa.nama,
          kelas: siswa.kelas,
          kategori: kat.kategori,
          pelanggaran: kat.jenis + (val.catatan ? ' - ' + val.catatan : ''),
          poin: kat.poin,
          pelapor: 'Admin / Guru'
        };
        
        Swal.fire({ title: 'Menyimpan...', allowOutsideClick: false });
        Swal.showLoading();
        
        google.script.run
          .withSuccessHandler(function(res) {
            Swal.fire('Tersimpan', 'Data pelanggaran berhasil dicatat', 'success');
            loadPelanggaranData(); // reload
          })
          .savePelanggaran(payload);
      }
    });
  }

  function showFormKategori() {
    Swal.fire({
      title: 'Tambah Kategori',
      html: `
        <div class="space-y-4 text-left">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Kategori (Tingkat)</label>
            <select id="inpKatLevel" class="w-full px-3 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500">
              <option value="Ringan">Ringan</option>
              <option value="Sedang">Sedang</option>
              <option value="Berat">Berat</option>
            </select>
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Jenis Pelanggaran</label>
            <input type="text" id="inpKatJenis" class="w-full px-3 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500" placeholder="Contoh: Terlambat">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Bobot Poin</label>
            <input type="number" id="inpKatPoin" class="w-full px-3 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500" placeholder="0">
          </div>
        </div>
      `,
      showCancelButton: true,
      confirmButtonText: 'Simpan',
      preConfirm: () => {
        var j = document.getElementById('inpKatJenis').value;
        if(!j) { Swal.showValidationMessage('Jenis pelanggaran harus diisi'); return false; }
        return {
          kategori: document.getElementById('inpKatLevel').value,
          jenis: j,
          poin: parseInt(document.getElementById('inpKatPoin').value) || 0
        };
      }
    }).then(result => {
      if(result.isConfirmed) {
        Swal.fire({ title: 'Menyimpan...', allowOutsideClick: false });
        Swal.showLoading();
        google.script.run
          .withSuccessHandler(function() {
            Swal.fire('Berhasil', 'Kategori ditambahkan', 'success');
            loadPelanggaranData();
          })
          .saveKategoriPelanggaran(result.value);
      }
    });
  }

  function hapusKategori(id) {
    Swal.fire({
      title: 'Hapus Kategori?',
      text: "Anda yakin ingin menghapus kategori pelanggaran ini?",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#d33',
      cancelButtonColor: '#3085d6',
      confirmButtonText: 'Ya, hapus!'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire({ title: 'Menghapus...', allowOutsideClick: false });
        Swal.showLoading();
        google.script.run
          .withSuccessHandler(function(res) {
            if(res.success) {
              Swal.fire('Terhapus!', 'Kategori telah dihapus.', 'success');
              loadPelanggaranData();
            }
          })
          .deleteKategoriPelanggaran(id);
      }
    });
  }
</script>
"""

with open('gas/Comp_Pelanggaran.html', 'w') as f:
    f.write(new_content)
