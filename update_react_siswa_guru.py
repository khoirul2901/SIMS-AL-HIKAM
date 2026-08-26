import re

with open('src/pages/MasterSiswa.tsx', 'r') as f:
    content = f.read()

imports_to_add = "import { Plus, Search, Filter, FileSpreadsheet, Edit2, Trash2, MoreVertical, X } from 'lucide-react';"
content = re.sub(r"import \{ .*? \} from 'lucide-react';", imports_to_add, content)

state_additions = """  const [isModalOpen, setIsModalOpen] = useState(false);
  const [formData, setFormData] = useState({ id: '', nis: '', nisn: '', nama: '', jk: 'L', kelas: 'VII-A', status: 'Aktif' });
  
  const handleOpenModal = (siswa?: typeof INITIAL_DATA[0]) => {
    if (siswa) {
      setFormData(siswa);
    } else {
      setFormData({ id: '', nis: '', nisn: '', nama: '', jk: 'L', kelas: 'VII-A', status: 'Aktif' });
    }
    setIsModalOpen(true);
  };

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    if (formData.id) {
      setData(data.map(item => item.id === formData.id ? formData : item));
      Swal.fire('Berhasil!', 'Data siswa berhasil diupdate.', 'success');
    } else {
      setData([...data, { ...formData, id: Date.now().toString() }]);
      Swal.fire('Berhasil!', 'Data siswa berhasil ditambahkan.', 'success');
    }
    setIsModalOpen(false);
  };
"""
content = content.replace('  const handleDelete = ', state_additions + '\n  const handleDelete = ')

content = content.replace('''  const handleAdd = () => {
    Swal.fire({
      title: 'Fitur Tambah Siswa',
      text: 'Formulir penambahan siswa akan muncul di sini (Modal).',
      icon: 'info'
    });
  };''', '')

content = content.replace('onClick={handleAdd}', 'onClick={() => handleOpenModal()}')
content = content.replace('<button className="p-1.5 text-blue-600 hover:bg-blue-50 rounded-lg transition-colors" title="Edit">', '<button onClick={() => handleOpenModal(siswa)} className="p-1.5 text-blue-600 hover:bg-blue-50 rounded-lg transition-colors" title="Edit">')

modal_ui = """
      {isModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 backdrop-blur-sm p-4">
          <div className="bg-white rounded-2xl shadow-xl w-full max-w-lg overflow-hidden">
            <div className="p-6 border-b border-slate-200 flex items-center justify-between">
              <h3 className="text-lg font-bold text-slate-800">
                {formData.id ? 'Edit Siswa' : 'Tambah Siswa Baru'}
              </h3>
              <button onClick={() => setIsModalOpen(false)} className="text-slate-400 hover:text-slate-600 transition-colors">
                <X className="w-5 h-5" />
              </button>
            </div>
            <form onSubmit={handleSave} className="p-6 space-y-4 max-h-[70vh] overflow-y-auto">
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">NIS</label>
                <input type="text" required value={formData.nis} onChange={e => setFormData({...formData, nis: e.target.value})} className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none" />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">NISN</label>
                <input type="text" required value={formData.nisn} onChange={e => setFormData({...formData, nisn: e.target.value})} className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none" />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Nama Lengkap</label>
                <input type="text" required value={formData.nama} onChange={e => setFormData({...formData, nama: e.target.value})} className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none" />
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Jenis Kelamin</label>
                  <select required value={formData.jk} onChange={e => setFormData({...formData, jk: e.target.value})} className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none">
                    <option value="L">Laki-laki (L)</option>
                    <option value="P">Perempuan (P)</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Kelas</label>
                  <input type="text" required value={formData.kelas} onChange={e => setFormData({...formData, kelas: e.target.value})} className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none" />
                </div>
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Status</label>
                <select required value={formData.status} onChange={e => setFormData({...formData, status: e.target.value})} className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none">
                  <option value="Aktif">Aktif</option>
                  <option value="Lulus">Lulus</option>
                  <option value="Pindah">Pindah</option>
                  <option value="Keluar">Keluar</option>
                </select>
              </div>
              <div className="flex justify-end gap-3 pt-4">
                <button type="button" onClick={() => setIsModalOpen(false)} className="px-4 py-2 text-slate-600 bg-slate-100 hover:bg-slate-200 font-medium rounded-lg transition-colors">Batal</button>
                <button type="submit" className="px-4 py-2 bg-blue-600 text-white hover:bg-blue-700 font-medium rounded-lg transition-colors">Simpan</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
"""
content = content.replace('    </div>\n  );\n};', modal_ui + '\n};')
with open('src/pages/MasterSiswa.tsx', 'w') as f:
    f.write(content)

with open('src/pages/MasterGuru.tsx', 'r') as f:
    content2 = f.read()

imports_to_add2 = "import { Plus, Search, Edit2, Trash2, Shield, X } from 'lucide-react';"
content2 = re.sub(r"import \{ .*? \} from 'lucide-react';", imports_to_add2, content2)

state_additions2 = """  const [isModalOpen, setIsModalOpen] = useState(false);
  const [formData, setFormData] = useState({ id: '', nip: '', nama: '', statusPegawai: 'GTY', jabatan: 'Guru Kelas' });
  
  const handleOpenModal = (guru?: typeof INITIAL_DATA[0]) => {
    if (guru) {
      setFormData(guru);
    } else {
      setFormData({ id: '', nip: '', nama: '', statusPegawai: 'GTY', jabatan: 'Guru Kelas' });
    }
    setIsModalOpen(true);
  };

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    if (formData.id) {
      setData(data.map(item => item.id === formData.id ? formData : item));
      Swal.fire('Berhasil!', 'Data guru berhasil diupdate.', 'success');
    } else {
      setData([...data, { ...formData, id: Date.now().toString() }]);
      Swal.fire('Berhasil!', 'Data guru berhasil ditambahkan.', 'success');
    }
    setIsModalOpen(false);
  };
"""
content2 = content2.replace('  const handleDelete = ', state_additions2 + '\n  const handleDelete = ')

content2 = content2.replace('''  const handleAdd = () => {
    Swal.fire({
      title: 'Fitur Tambah Guru',
      text: 'Formulir penambahan guru/tendik akan muncul di sini (Modal).',
      icon: 'info'
    });
  };''', '')

content2 = content2.replace('onClick={handleAdd}', 'onClick={() => handleOpenModal()}')
content2 = content2.replace('<button className="p-1.5 text-blue-600 hover:bg-blue-50 rounded-lg transition-colors" title="Edit">', '<button onClick={() => handleOpenModal(guru)} className="p-1.5 text-blue-600 hover:bg-blue-50 rounded-lg transition-colors" title="Edit">')

modal_ui2 = """
      {isModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 backdrop-blur-sm p-4">
          <div className="bg-white rounded-2xl shadow-xl w-full max-w-lg overflow-hidden">
            <div className="p-6 border-b border-slate-200 flex items-center justify-between">
              <h3 className="text-lg font-bold text-slate-800">
                {formData.id ? 'Edit Guru & Tendik' : 'Tambah Guru & Tendik Baru'}
              </h3>
              <button onClick={() => setIsModalOpen(false)} className="text-slate-400 hover:text-slate-600 transition-colors">
                <X className="w-5 h-5" />
              </button>
            </div>
            <form onSubmit={handleSave} className="p-6 space-y-4 max-h-[70vh] overflow-y-auto">
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">NIP / NUPTK</label>
                <input type="text" required value={formData.nip} onChange={e => setFormData({...formData, nip: e.target.value})} className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none" />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Nama Lengkap & Gelar</label>
                <input type="text" required value={formData.nama} onChange={e => setFormData({...formData, nama: e.target.value})} className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none" />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Status Pegawai</label>
                <select required value={formData.statusPegawai} onChange={e => setFormData({...formData, statusPegawai: e.target.value})} className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none">
                  <option value="GTY">Guru Tetap Yayasan (GTY)</option>
                  <option value="GTT">Guru Tidak Tetap (GTT)</option>
                  <option value="PTY">Pegawai Tetap Yayasan (PTY)</option>
                  <option value="PTT">Pegawai Tidak Tetap (PTT)</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Jabatan / Tugas</label>
                <input type="text" required value={formData.jabatan} onChange={e => setFormData({...formData, jabatan: e.target.value})} className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none" />
              </div>
              <div className="flex justify-end gap-3 pt-4">
                <button type="button" onClick={() => setIsModalOpen(false)} className="px-4 py-2 text-slate-600 bg-slate-100 hover:bg-slate-200 font-medium rounded-lg transition-colors">Batal</button>
                <button type="submit" className="px-4 py-2 bg-blue-600 text-white hover:bg-blue-700 font-medium rounded-lg transition-colors">Simpan</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
"""
content2 = content2.replace('    </div>\n  );\n};', modal_ui2 + '\n};')
with open('src/pages/MasterGuru.tsx', 'w') as f:
    f.write(content2)

