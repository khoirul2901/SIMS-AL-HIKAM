
  
  function showModalMapel(mapel) {
    var modal = document.getElementById('modalMapel');
    var content = document.getElementById('modalMapelContent');
    
    if (mapel && mapel.kode) {
      document.getElementById('modalMapelTitle').innerText = 'Edit Mapel';
      document.getElementById('mapelKode').value = mapel.kode;
      document.getElementById('mapelKode').readOnly = true;
      document.getElementById('mapelNama').value = mapel.nama;
      document.getElementById('mapelKelompok').value = mapel.kelompok;
    } else {
      document.getElementById('modalMapelTitle').innerText = 'Tambah Mapel Baru';
      document.getElementById('formMapel').reset();
      document.getElementById('mapelKode').readOnly = false;
    }
    
    modal.classList.remove('hidden');
    setTimeout(() => {
      content.classList.remove('scale-95', 'opacity-0');
      content.classList.add('scale-100', 'opacity-100');
    }, 10);
  }
  
  function hideModalMapel() {
    var modal = document.getElementById('modalMapel');
    var content = document.getElementById('modalMapelContent');
    
    content.classList.remove('scale-100', 'opacity-100');
    content.classList.add('scale-95', 'opacity-0');
    setTimeout(() => {
      modal.classList.add('hidden');
    }, 300);
  }
  
  function handleSaveMapel(e) {
    e.preventDefault();
    var btn = document.getElementById('btnSaveMapel');
    var originalText = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Menyimpan...';
    btn.disabled = true;
    
    var data = {
      kode: document.getElementById('mapelKode').value,
      nama: document.getElementById('mapelNama').value,
      kelompok: document.getElementById('mapelKelompok').value
    };
    
    google.script.run
      .withSuccessHandler(function(res) {
        btn.innerHTML = originalText;
        btn.disabled = false;
        
        if (res.success) {
          Swal.fire({
            icon: 'success',
            title: 'Berhasil!',
            text: res.message,
            timer: 1500,
            showConfirmButton: false
          });
          hideModalMapel();
          initPage();
        } else {
          Swal.fire('Gagal', res.message || 'Terjadi kesalahan', 'error');
        }
      })
      .withFailureHandler(function(err) {
        btn.innerHTML = originalText;
        btn.disabled = false;
        Swal.fire('Error', err.toString(), 'error');
      })
      .saveMapel(data);
  }
  
  function editMapel(btn, dataStr) {
    var data = JSON.parse(decodeURIComponent(dataStr));
    showModalMapel(data);
  }

  function initPage() {
    google.script.run
      .withSuccessHandler(function(data) {
        var tbody = document.getElementById('tableMapelBody');
        
        if (data.length === 0) {
          tbody.innerHTML = '<tr><td colspan="4" class="text-center py-6 text-slate-400 dark:text-slate-500">Tidak ada data mapel ditemukan.</td></tr>';
          return;
        }
        
        var html = '';
        data.forEach(function(m) {
          html += '<tr class="hover:bg-slate-50 dark:hover:bg-slate-800 border-b border-slate-200 dark:border-slate-800 last:border-0">';
          html += '  <td class="px-6 py-4 font-mono text-slate-800 dark:text-slate-100">' + m.kode + '</td>';
          html += '  <td class="px-6 py-4 font-medium text-slate-900 dark:text-slate-100">' + m.nama + '</td>';
          html += '  <td class="px-6 py-4"><span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-indigo-100 dark:bg-indigo-900/30 text-indigo-700 dark:text-indigo-400">' + m.kelompok + '</span></td>';
          html += '  <td class="px-6 py-4 text-right"><button onclick="editMapel(this, \'' + encodeURIComponent(JSON.stringify(m)) + '\')" class="text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-900/30 p-2 rounded transition-colors"><i class="fas fa-edit"></i></button></td>';
          html += '</tr>';
        });
        tbody.innerHTML = html;
      })
      .withFailureHandler(function(err) {
         document.getElementById('tableMapelBody').innerHTML = '<tr><td colspan="4" class="text-center py-6 text-red-500">Gagal memuat: ' + err.toString() + '</td></tr>';
      })
      .getMapelList();
  }

