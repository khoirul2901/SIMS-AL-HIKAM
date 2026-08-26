
  
  function showModalKelas(kelas) {
    var modal = document.getElementById('modalKelas');
    var content = document.getElementById('modalKelasContent');
    
    if (kelas && kelas.kode) {
      document.getElementById('modalKelasTitle').innerText = 'Edit Kelas';
      document.getElementById('kelasKode').value = kelas.kode;
      document.getElementById('kelasKode').readOnly = true;
      document.getElementById('kelasNama').value = kelas.nama;
      document.getElementById('kelasWali').value = kelas.waliKelas;
      document.getElementById('kelasJmlSiswa').value = kelas.jumlahSiswa;
    } else {
      document.getElementById('modalKelasTitle').innerText = 'Tambah Kelas Baru';
      document.getElementById('formKelas').reset();
      document.getElementById('kelasKode').readOnly = false;
    }
    
    modal.classList.remove('hidden');
    setTimeout(() => {
      content.classList.remove('scale-95', 'opacity-0');
      content.classList.add('scale-100', 'opacity-100');
    }, 10);
  }
  
  function hideModalKelas() {
    var modal = document.getElementById('modalKelas');
    var content = document.getElementById('modalKelasContent');
    
    content.classList.remove('scale-100', 'opacity-100');
    content.classList.add('scale-95', 'opacity-0');
    setTimeout(() => {
      modal.classList.add('hidden');
    }, 300);
  }
  
  function handleSaveKelas(e) {
    e.preventDefault();
    var btn = document.getElementById('btnSaveKelas');
    var originalText = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Menyimpan...';
    btn.disabled = true;
    
    var data = {
      kode: document.getElementById('kelasKode').value,
      nama: document.getElementById('kelasNama').value,
      waliKelas: document.getElementById('kelasWali').value,
      jumlahSiswa: document.getElementById('kelasJmlSiswa').value
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
          hideModalKelas();
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
      .saveKelas(data);
  }
  
  function editKelas(btn, dataStr) {
    var data = JSON.parse(decodeURIComponent(dataStr));
    showModalKelas(data);
  }

  function initPage() {
    google.script.run
      .withSuccessHandler(function(data) {
        var tbody = document.getElementById('tableKelasBody');
        
        if (data.length === 0) {
          tbody.innerHTML = '<tr><td colspan="5" class="text-center py-6 text-slate-400 dark:text-slate-500">Tidak ada data kelas ditemukan.</td></tr>';
          return;
        }
        
        var html = '';
        data.forEach(function(k) {
          html += '<tr class="hover:bg-slate-50 dark:hover:bg-slate-800 border-b border-slate-200 dark:border-slate-800 last:border-0">';
          html += '  <td class="px-6 py-4 font-mono text-slate-800 dark:text-slate-100">' + k.kode + '</td>';
          html += '  <td class="px-6 py-4 font-medium text-slate-900 dark:text-slate-100">' + k.nama + '</td>';
          html += '  <td class="px-6 py-4">' + k.waliKelas + '</td>';
          html += '  <td class="px-6 py-4 text-center"><span class="px-2 py-1 rounded bg-slate-100 dark:bg-slate-800 font-medium">' + k.jumlahSiswa + '</span></td>';
          html += '  <td class="px-6 py-4 text-right"><button onclick="editKelas(this, \'' + encodeURIComponent(JSON.stringify(k)) + '\')" class="text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-900/30 p-2 rounded transition-colors"><i class="fas fa-edit"></i></button></td>';
          html += '</tr>';
        });
        tbody.innerHTML = html;
      })
      .withFailureHandler(function(err) {
         document.getElementById('tableKelasBody').innerHTML = '<tr><td colspan="5" class="text-center py-6 text-red-500">Gagal memuat: ' + err.toString() + '</td></tr>';
      })
      .getKelasList();
  }

