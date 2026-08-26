with open('gas/Comp_Pelanggaran.html', 'r') as f:
    content = f.read()

html_modal = """
    Swal.fire({
      title: 'Catat Pelanggaran',
      html: `
        <div class="space-y-4 text-left">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">NIS Siswa</label>
            <input type="text" id="nisPelanggaran" class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-blue-500 focus:border-blue-500" placeholder="Masukkan NIS">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Kategori Pelanggaran</label>
            <select id="katPelanggaran" class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
              <option value="Ringan">Ringan (5-10 poin)</option>
              <option value="Sedang">Sedang (11-20 poin)</option>
              <option value="Berat">Berat (>20 poin)</option>
            </select>
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Keterangan / Jenis Pelanggaran</label>
            <textarea id="ketPelanggaran" class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-blue-500 focus:border-blue-500" rows="3"></textarea>
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Poin Pelanggaran</label>
            <input type="number" id="poinPelanggaran" class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-blue-500 focus:border-blue-500" placeholder="0">
          </div>
        </div>
      `,
      showCancelButton: true,
      confirmButtonText: 'Simpan',
      cancelButtonText: 'Batal',
      preConfirm: () => {
        var nis = document.getElementById('nisPelanggaran').value;
        var kat = document.getElementById('katPelanggaran').value;
        var ket = document.getElementById('ketPelanggaran').value;
        var poin = document.getElementById('poinPelanggaran').value;
        if(!nis || !ket) {
          Swal.showValidationMessage('NIS dan Keterangan harus diisi');
          return false;
        }
        return {nis: nis, kategori: kat, keterangan: ket, poin: poin};
      }
    }).then((result) => {
      if(result.isConfirmed) {
        Swal.fire({title: 'Menyimpan...', allowOutsideClick: false, didOpen: () => {Swal.showLoading()}});
        google.script.run
          .withSuccessHandler(function(res) {
            Swal.fire('Berhasil', 'Pelanggaran berhasil dicatat', 'success');
            initPage(); // Refresh list
          })
          .withFailureHandler(function(err) {
            Swal.fire('Gagal', err.toString(), 'error');
          })
          .savePelanggaran(result.value);
      }
    });
"""

# Replace the button onclick inside Comp_Pelanggaran.html
content = content.replace("onclick=\"Swal.fire('Fitur Input', 'Formulir input pelanggaran sedang dikembangkan', 'info')\"", "onclick=\"bukaModalPelanggaran()\"")

script_tag = """
<script>
  function bukaModalPelanggaran() {
    %s
  }
""" % html_modal

content = content.replace("<script>", script_tag)

with open('gas/Comp_Pelanggaran.html', 'w') as f:
    f.write(content)
