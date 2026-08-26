
  let rawDataSiswa = [];
  let isEditMode = false;

  function initPage() {
    // Populate filter kelas first
    google.script.run
      .withSuccessHandler(function(kelasData) {
        let sel = document.getElementById('siswaKelas');
        let filterSel = document.getElementById('filterKelas');
        let options = '';
        kelasData.forEach(function(k) {
          options += `<option value="${k.kode}">${k.nama}</option>`;
        });
        sel.innerHTML = options;
        filterSel.innerHTML = '<option value="">Semua Kelas</option>' + options;
      })
      .getKelasList();

    // Get Data Siswa
    google.script.run
      .withSuccessHandler(function(data) {
        rawDataSiswa = data;
        renderTable(data);
      })
      .withFailureHandler(function(err) {
         document.getElementById('tableSiswaBody').innerHTML = '<tr><td colspan="6" class="text-center py-6 text-red-500">Gagal memuat: ' + err.toString() + '</td></tr>';
      })
      .getSiswaList();
  }

  function renderTable(data) {
    var tbody = document.getElementById('tableSiswaBody');
    if (data.length === 0) {
      tbody.innerHTML = '<tr><td colspan="6" class="text-center py-6 text-slate-400 dark:text-slate-500">Tidak ada data siswa.</td></tr>';
      return;
    }
    
    var html = '';
    data.forEach(function(s) {
      let sJson = encodeURIComponent(JSON.stringify(s));
      html += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800 border-b border-slate-200 dark:border-slate-800 last:border-0 transition-colors">
        <td class="px-6 py-4 font-mono text-slate-800 dark:text-slate-100">${s.nis}<br><span class="text-xs text-slate-400 dark:text-slate-500">${s.nisn}</span></td>
        <td class="px-6 py-4">
          <button onclick="viewDetailSiswa('${sJson}')" class="font-bold text-indigo-600 dark:text-indigo-400 hover:text-indigo-800 dark:hover:text-indigo-300 text-left transition-colors">${s.nama}</button>
        </td>
        <td class="px-6 py-4 text-slate-700 dark:text-slate-300">${s.kelas}</td>
        <td class="px-6 py-4 text-slate-700 dark:text-slate-300">${s.jk}</td>
        <td class="px-6 py-4"><span class="px-2.5 py-1 rounded-full text-xs font-semibold ${s.status==='Aktif'?'bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400':'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400'}">${s.status}</span></td>
        <td class="px-6 py-4 text-right whitespace-nowrap">
          <button onclick="printKartuIndividu('${sJson}')" class="text-emerald-600 dark:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-900/30 p-2 rounded transition-colors" title="Cetak Kartu"><i class="fas fa-id-badge"></i></button>
          <button onclick="editSiswa('${sJson}')" class="text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/30 p-2 rounded transition-colors" title="Edit"><i class="fas fa-edit"></i></button>
          <button onclick="deleteSiswaRow('${s.nis}', '${s.nama}')" class="text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900/30 p-2 rounded transition-colors" title="Hapus"><i class="fas fa-trash"></i></button>
        </td>
      </tr>`;
    });
    tbody.innerHTML = html;
  }

  function filterTable() {
    var search = document.getElementById('searchSiswa').value.toLowerCase();
    var filterKelas = document.getElementById('filterKelas').value;
    
    var filtered = rawDataSiswa.filter(function(s) {
      var matchSearch = s.nama.toLowerCase().includes(search) || s.nis.includes(search) || s.nisn.includes(search);
      var matchKelas = filterKelas ? s.kelas === filterKelas : true;
      return matchSearch && matchKelas;
    });
    
    renderTable(filtered);
  }

  function generateUsername(nama) {
    if(!isEditMode) {
      let un = nama.toLowerCase().replace(/[^a-z0-9]/g, '');
      document.getElementById('siswaUsername').value = un;
    }
  }

  function showModalSiswa(siswa) {
    var modal = document.getElementById('modalSiswa');
    var content = document.getElementById('modalSiswaContent');
    
    if (siswa) {
      isEditMode = true;
      document.getElementById('modalSiswaTitle').innerText = 'Edit Data Siswa';
      document.getElementById('siswaNis').value = siswa.nis || '';
      document.getElementById('siswaNis').readOnly = true;
      document.getElementById('siswaNisn').value = siswa.nisn || '';
      document.getElementById('siswaNama').value = siswa.nama || '';
      document.getElementById('siswaTempatLahir').value = siswa.tempatLahir || '';
      document.getElementById('siswaTanggalLahir').value = siswa.tanggalLahir || '';
      document.getElementById('siswaJk').value = siswa.jk || 'L';
      document.getElementById('siswaKelas').value = siswa.kelas || '';
      document.getElementById('siswaAlamat').value = siswa.alamat || '';
      document.getElementById('siswaAyah').value = siswa.namaAyah || '';
      document.getElementById('siswaIbu').value = siswa.namaIbu || '';
      document.getElementById('siswaHp').value = siswa.noHp || '';
      document.getElementById('siswaStatus').value = siswa.status || 'Aktif';
      document.getElementById('siswaUsername').value = siswa.username || '';
      document.getElementById('siswaPassword').value = siswa.password || '123456';
    } else {
      isEditMode = false;
      document.getElementById('modalSiswaTitle').innerText = 'Tambah Siswa Baru';
      document.getElementById('formSiswa').reset();
      document.getElementById('siswaNis').readOnly = false;
      document.getElementById('siswaPassword').value = '123456';
    }
    
    modal.classList.remove('hidden');
    setTimeout(() => {
      content.classList.remove('scale-95', 'opacity-0');
      content.classList.add('scale-100', 'opacity-100');
    }, 10);
  }

  function hideModalSiswa() {
    var modal = document.getElementById('modalSiswa');
    var content = document.getElementById('modalSiswaContent');
    content.classList.remove('scale-100', 'opacity-100');
    content.classList.add('scale-95', 'opacity-0');
    setTimeout(() => { modal.classList.add('hidden'); }, 300);
  }

  function viewDetailSiswa(dataStr) {
    var s = JSON.parse(decodeURIComponent(dataStr));
    var modal = document.getElementById('modalDetail');
    var content = document.getElementById('modalDetailContent');
    
    var html = `
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div>
          <h4 class="text-sm font-bold text-indigo-600 dark:text-indigo-400 uppercase mb-4">Identitas Siswa</h4>
          <table class="w-full text-sm text-slate-700 dark:text-slate-300">
            <tbody>
              <tr><td class="py-2 text-slate-500 w-1/3">NIS / NISN</td><td class="py-2 font-medium">${s.nis} / ${s.nisn}</td></tr>
              <tr><td class="py-2 text-slate-500">Nama Lengkap</td><td class="py-2 font-medium">${s.nama}</td></tr>
              <tr><td class="py-2 text-slate-500">Tempat, Tgl Lahir</td><td class="py-2">${s.tempatLahir || '-'}, ${s.tanggalLahir || '-'}</td></tr>
              <tr><td class="py-2 text-slate-500">Jenis Kelamin</td><td class="py-2">${s.jk === 'L' ? 'Laki-laki' : 'Perempuan'}</td></tr>
              <tr><td class="py-2 text-slate-500">Kelas</td><td class="py-2 font-medium">${s.kelas}</td></tr>
              <tr><td class="py-2 text-slate-500">Alamat</td><td class="py-2">${s.alamat || '-'}</td></tr>
              <tr><td class="py-2 text-slate-500">Status</td><td class="py-2"><span class="px-2 py-0.5 rounded bg-indigo-100 text-indigo-700 text-xs">${s.status}</span></td></tr>
            </tbody>
          </table>
        </div>
        <div>
          <h4 class="text-sm font-bold text-indigo-600 dark:text-indigo-400 uppercase mb-4">Data Orang Tua & Akun</h4>
          <table class="w-full text-sm text-slate-700 dark:text-slate-300">
            <tbody>
              <tr><td class="py-2 text-slate-500 w-1/3">Nama Ayah</td><td class="py-2">${s.namaAyah || '-'}</td></tr>
              <tr><td class="py-2 text-slate-500">Nama Ibu</td><td class="py-2">${s.namaIbu || '-'}</td></tr>
              <tr><td class="py-2 text-slate-500">No. HP</td><td class="py-2">${s.noHp || '-'}</td></tr>
              <tr><td colspan="2"><hr class="my-2 border-slate-200 dark:border-slate-700"></td></tr>
              <tr><td class="py-2 text-slate-500">Username</td><td class="py-2 font-mono bg-slate-100 dark:bg-slate-800 px-2 rounded">${s.username || '-'}</td></tr>
              <tr><td class="py-2 text-slate-500">Password</td><td class="py-2 font-mono bg-slate-100 dark:bg-slate-800 px-2 rounded">${s.password || '-'}</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    `;
    
    document.getElementById('detailSiswaBody').innerHTML = html;
    
    document.getElementById('btnEditFromDetail').onclick = function() {
      hideModalDetail();
      setTimeout(() => { editSiswa(dataStr); }, 300);
    };
    
    modal.classList.remove('hidden');
    setTimeout(() => {
      content.classList.remove('scale-95', 'opacity-0');
      content.classList.add('scale-100', 'opacity-100');
    }, 10);
  }

  function hideModalDetail() {
    var modal = document.getElementById('modalDetail');
    var content = document.getElementById('modalDetailContent');
    content.classList.remove('scale-100', 'opacity-100');
    content.classList.add('scale-95', 'opacity-0');
    setTimeout(() => { modal.classList.add('hidden'); }, 300);
  }

  function editSiswa(dataStr) {
    var data = JSON.parse(decodeURIComponent(dataStr));
    showModalSiswa(data);
  }

  function handleSaveSiswa(e) {
    e.preventDefault();
    var btn = document.getElementById('btnSaveSiswa');
    var originalText = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Menyimpan...';
    btn.disabled = true;
    
    var data = {
      nis: document.getElementById('siswaNis').value,
      nisn: document.getElementById('siswaNisn').value,
      nama: document.getElementById('siswaNama').value,
      tempatLahir: document.getElementById('siswaTempatLahir').value,
      tanggalLahir: document.getElementById('siswaTanggalLahir').value,
      jk: document.getElementById('siswaJk').value,
      kelas: document.getElementById('siswaKelas').value,
      alamat: document.getElementById('siswaAlamat').value,
      namaAyah: document.getElementById('siswaAyah').value,
      namaIbu: document.getElementById('siswaIbu').value,
      noHp: document.getElementById('siswaHp').value,
      status: document.getElementById('siswaStatus').value,
      username: document.getElementById('siswaUsername').value,
      password: document.getElementById('siswaPassword').value
    };
    
    google.script.run
      .withSuccessHandler(function(res) {
        btn.innerHTML = originalText;
        btn.disabled = false;
        if (res.success) {
          Swal.fire({ icon: 'success', title: 'Berhasil!', text: res.message, timer: 1500, showConfirmButton: false });
          hideModalSiswa();
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
      .saveSiswa(data);
  }

  function deleteSiswaRow(nis, nama) {
    Swal.fire({
      title: 'Hapus Siswa?',
      text: `Anda yakin ingin menghapus data ${nama}?`,
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#ef4444',
      cancelButtonColor: '#64748b',
      confirmButtonText: 'Ya, Hapus!'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire({ title: 'Menghapus...', allowOutsideClick: false, didOpen: () => { Swal.showLoading(); }});
        google.script.run
          .withSuccessHandler(function(res) {
            if(res.success) {
              Swal.fire('Terhapus!', res.message, 'success');
              initPage();
            } else {
              Swal.fire('Gagal', res.message, 'error');
            }
          })
          .withFailureHandler(function(err){ Swal.fire('Error', err.toString(), 'error'); })
          .deleteSiswa(nis);
      }
    });
  }

  function getHtmlKartu(s) {
    return `
      <div class="kartu-container">
        <div class="kartu-header">
          <h2>KARTU PELAJAR</h2>
          <h3>SMP AL-HIKAM</h3>
        </div>
        <div class="kartu-body">
          <div class="kartu-photo">Foto<br>3x4</div>
          <div class="kartu-info">
            <table>
              <tr><td>NIS/NISN</td><td>: ${s.nis} / ${s.nisn}</td></tr>
              <tr><td>Nama</td><td>: <b>${s.nama}</b></td></tr>
              <tr><td>TTL</td><td>: ${s.tempatLahir || '-'}, ${s.tanggalLahir || '-'}</td></tr>
              <tr><td>Kelas</td><td>: ${s.kelas}</td></tr>
              <tr><td>Alamat</td><td>: ${s.alamat || '-'}</td></tr>
            </table>
          </div>
        </div>
      </div>
    `;
  }

  function printKartuIndividu(dataStr) {
    var s = JSON.parse(decodeURIComponent(dataStr));
    var html = getHtmlKartu(s);
    var printArea = document.getElementById('printArea');
    printArea.innerHTML = html;
    window.print();
    printArea.innerHTML = '';
  }

  function printAllKartu() {
    var filterKelas = document.getElementById('filterKelas').value;
    var filtered = rawDataSiswa;
    if(filterKelas) {
      filtered = rawDataSiswa.filter(s => s.kelas === filterKelas);
    }
    
    if(filtered.length === 0) {
      Swal.fire('Info', 'Tidak ada data siswa untuk dicetak', 'info');
      return;
    }

    var html = '';
    filtered.forEach((s, index) => {
      html += getHtmlKartu(s);
      // Optional page break after some cards if needed
    });
    
    var printArea = document.getElementById('printArea');
    printArea.innerHTML = html;
    window.print();
    printArea.innerHTML = '';
  }

  function exportSiswa() {
    Swal.fire({
      title: 'Export Data Siswa?',
      text: "Data akan diexport sebagai file CSV/Excel",
      icon: 'info',
      showCancelButton: true,
      confirmButtonColor: '#4f46e5',
      cancelButtonColor: '#64748b',
      confirmButtonText: 'Ya, Export!'
    }).then((result) => {
      if (result.isConfirmed) {
        google.script.run
          .withSuccessHandler(function(url) {
             window.open(url, '_blank');
          })
          .getExportUrl('Master_Siswa');
      }
    });
  }

  function showImportModal() {
     Swal.fire({
      title: 'Import Data Siswa',
      html: `
        <div class="mb-4 text-sm text-slate-600 dark:text-slate-400 text-left">
          Pastikan format file CSV sesuai urutan kolom:<br/>
          <b>NIS, NISN, Nama, Kelas, L/P, Status, Tempat Lahir, Tgl Lahir, Alamat, Nama Ayah, Nama Ibu, No HP, Username, Password</b>
        </div>
        <input type="file" id="fileImport" accept=".csv" class="w-full text-sm text-slate-500 dark:text-slate-400
          file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold
          file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100 dark:file:bg-indigo-900/30 dark:file:text-indigo-300"/>
      `,
      showCancelButton: true,
      confirmButtonColor: '#4f46e5',
      cancelButtonColor: '#64748b',
      confirmButtonText: 'Import',
      preConfirm: () => {
        const fileInput = document.getElementById('fileImport');
        if (!fileInput.files.length) Swal.showValidationMessage('Pilih file terlebih dahulu');
        return fileInput.files[0];
      }
    }).then((result) => {
      if (result.isConfirmed && result.value) {
        var file = result.value;
        var reader = new FileReader();
        reader.onload = function(e) {
          var data = e.target.result.split(',')[1];
          Swal.fire({ title: 'Memproses...', text: 'Sedang mengimport', allowOutsideClick: false, didOpen: () => { Swal.showLoading(); }});
          google.script.run
            .withSuccessHandler(function(res) {
              if (res.success) { Swal.fire('Berhasil!', res.message, 'success'); initPage(); } 
              else { Swal.fire('Gagal', res.message, 'error'); }
            })
            .withFailureHandler(function(err) { Swal.fire('Error', err.toString(), 'error'); })
            .importSiswaCsv(data, file.name);
        };
        reader.readAsDataURL(file);
      }
    });
  }

