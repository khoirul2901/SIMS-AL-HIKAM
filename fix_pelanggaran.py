import re

with open('src/pages/Pelanggaran.tsx', 'r') as f:
    content = f.read()

content = content.replace("import React, { useState } from 'react';", "import React, { useState } from 'react';\nimport { useDatabase } from '../context/DatabaseContext';")

content = content.replace("export const Pelanggaran = () => {\n  const [data, setData] = useState(PELANGGARAN_DATA);", "export const Pelanggaran = () => {\n  const { pelanggaranData: data, setPelanggaranData: setData, siswaData } = useDatabase();")

# Update handleAdd to use Swal HTML form
swal_form = """
  const handleAdd = () => {
    Swal.fire({
      title: 'Catat Pelanggaran',
      html: `
        <div class="space-y-4 text-left">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">NIS Siswa</label>
            <input type="text" id="nis" class="w-full px-3 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500" placeholder="Masukkan NIS">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Kategori Pelanggaran</label>
            <select id="kategori" class="w-full px-3 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500">
              <option value="Ringan">Ringan (5-10 poin)</option>
              <option value="Sedang">Sedang (11-20 poin)</option>
              <option value="Berat">Berat (>20 poin)</option>
            </select>
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Keterangan / Jenis Pelanggaran</label>
            <textarea id="pelanggaran" class="w-full px-3 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500" rows="3"></textarea>
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Poin</label>
            <input type="number" id="poin" class="w-full px-3 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500" placeholder="0">
          </div>
        </div>
      `,
      showCancelButton: true,
      confirmButtonText: 'Simpan',
      cancelButtonText: 'Batal',
      preConfirm: () => {
        const nis = (document.getElementById('nis') as HTMLInputElement).value;
        const kategori = (document.getElementById('kategori') as HTMLSelectElement).value;
        const pelanggaran = (document.getElementById('pelanggaran') as HTMLTextAreaElement).value;
        const poin = parseInt((document.getElementById('poin') as HTMLInputElement).value) || 0;
        
        if (!nis || !pelanggaran) {
          Swal.showValidationMessage('NIS dan Keterangan harus diisi');
          return false;
        }
        
        return { nis, kategori, pelanggaran, poin };
      }
    }).then((result) => {
      if (result.isConfirmed && result.value) {
        const { nis, kategori, pelanggaran, poin } = result.value;
        const siswa = siswaData.find((s: any) => s.nis === nis);
        
        if (!siswa) {
          Swal.fire('Error', 'Siswa dengan NIS tersebut tidak ditemukan!', 'error');
          return;
        }

        const newPelanggaran = {
          id: Math.random().toString(36).substr(2, 9),
          tanggal: new Date().toISOString().split('T')[0],
          nis,
          nama: siswa.nama,
          kelas: siswa.kelas,
          kategori,
          pelanggaran,
          poin,
          pelapor: 'Admin / Guru'
        };
        
        setData([...data, newPelanggaran]);
        
        Swal.fire('Tersimpan', 'Data pelanggaran berhasil dicatat', 'success');
      }
    });
  };
"""

content = re.sub(r'const handleAdd.*?icon: \'info\'\n    \}\);\n  \};', swal_form, content, flags=re.DOTALL)

with open('src/pages/Pelanggaran.tsx', 'w') as f:
    f.write(content)
