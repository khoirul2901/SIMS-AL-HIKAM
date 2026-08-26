
  
  function showModalGuru(guru) {
    var modal = document.getElementById('modalGuru');
    var content = document.getElementById('modalGuruContent');
    
    if (guru && guru.nip) {
      document.getElementById('modalGuruTitle').innerText = 'Edit Guru';
      document.getElementById('guruNip').value = guru.nip;
      document.getElementById('guruNip').readOnly = true;
      document.getElementById('guruNama').value = guru.nama;
      document.getElementById('guruMapel').value = guru.mapel;
      document.getElementById('guruStatus').value = guru.statusPegawai;
      document.getElementById('guruNoHp').value = guru.noHp || '';
    } else {
      document.getElementById('modalGuruTitle').innerText = 'Tambah Guru Baru';
      document.getElementById('formGuru').reset();
      document.getElementById('guruNip').readOnly = false;
    }
    
    modal.classList.remove('hidden');
    setTimeout(() => {
      content.classList.remove('scale-95', 'opacity-0');
      content.classList.add('scale-100', 'opacity-100');
    }, 10);

  }
  
  function hideModalGuru() {
    var modal = document.getElementById('modalGuru');
    var content = document.getElementById('modalGuruContent');
    
    content.classList.remove('scale-100', 'opacity-100');
    content.classList.add('scale-95', 'opacity-0');
    setTimeout(() => {
      modal.classList.add('hidden');
    }, 300);
  }
  
  function handleSaveGuru(e) {
    e.preventDefault();
    var btn = document.getElementById('btnSaveGuru');
    var originalText = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Menyimpan...';
    btn.disabled = true;
    
    var data = {
      nip: document.getElementById('guruNip').value,
      nama: document.getElementById('guruNama').value,
      mapel: document.getElementById('guruMapel').value,
      statusPegawai: document.getElementById('guruStatus').value,
      noHp: document.getElementById('guruNoHp').value
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
          hideModalGuru();
          initPage(); // Reload list
        } else {
          Swal.fire('Gagal', res.message || 'Terjadi kesalahan', 'error');
        }
      })
      .withFailureHandler(function(err) {
        btn.innerHTML = originalText;
        btn.disabled = false;
        Swal.fire('Error', err.toString(), 'error');
      })
      .saveGuru(data);
  }
  
  function editGuru(btn, dataStr) {
    var data = JSON.parse(decodeURIComponent(dataStr));
    showModalGuru(data);
  }

  function initPage() {
    google.script.run
      .withSuccessHandler(function(data) {
        var tbody = document.getElementById('tableGuruBody');
        
        if (data.length === 0) {
          tbody.innerHTML = '<tr><td colspan="5" class="text-center py-6 text-slate-400 dark:text-slate-500">Tidak ada data guru ditemukan di Database Spreadsheet.</td></tr>';
          return;
        }
        
        var html = '';
        data.forEach(function(g) {
          html += '<tr class="hover:bg-slate-50 dark:hover:bg-slate-800 border-b border-slate-200 dark:border-slate-800 last:border-0">';
          html += '  <td class="px-6 py-4 font-mono text-slate-800 dark:text-slate-100">' + (g.nip || '-') + '</td>';
          html += '  <td class="px-6 py-4 font-medium text-slate-900 dark:text-slate-100">' + g.nama + '</td>';
          html += '  <td class="px-6 py-4">' + g.mapel + '</td>';
          html += '  <td class="px-6 py-4"><span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-400">' + g.statusPegawai + '</span></td>';
          html += '  <td class="px-6 py-4 text-right"><button onclick="editGuru(this, \'' + encodeURIComponent(JSON.stringify(g)) + '\')" class="text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-900/30 p-2 rounded transition-colors"><i class="fas fa-edit"></i></button></td>';
          html += '</tr>';
        });
        tbody.innerHTML = html;
      })
      .withFailureHandler(function(err) {
         document.getElementById('tableGuruBody').innerHTML = '<tr><td colspan="5" class="text-center py-6 text-red-500">Gagal memuat: ' + err.toString() + '</td></tr>';
      })
      .getGuruList();
  }

