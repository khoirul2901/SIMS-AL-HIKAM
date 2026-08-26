import re

with open('src/pages/MasterKelas.tsx', 'r') as f:
    content = f.read()

# We need to add state for modal and form
imports_to_add = "import { Plus, Search, Edit2, Trash2, Users, X } from 'lucide-react';"
content = re.sub(r"import \{ .*? \} from 'lucide-react';", imports_to_add, content)

state_additions = """  const [isModalOpen, setIsModalOpen] = useState(false);
  const [formData, setFormData] = useState({ id: '', tingkat: 'VII', namaKelas: '', waliKelas: '', jumlahSiswa: 0 });
  
  const handleOpenModal = (kelas?: typeof INITIAL_DATA[0]) => {
    if (kelas) {
      setFormData(kelas);
    } else {
      setFormData({ id: '', tingkat: 'VII', namaKelas: '', waliKelas: '', jumlahSiswa: 0 });
    }
    setIsModalOpen(true);
  };

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    if (formData.id) {
      setData(data.map(item => item.id === formData.id ? formData : item));
      Swal.fire('Berhasil!', 'Data kelas berhasil diupdate.', 'success');
    } else {
      setData([...data, { ...formData, id: Date.now().toString() }]);
      Swal.fire('Berhasil!', 'Data kelas berhasil ditambahkan.', 'success');
    }
    setIsModalOpen(false);
  };
"""

content = content.replace('  const handleDelete = ', state_additions + '\n  const handleDelete = ')

content = content.replace('''  const handleAdd = () => {
    Swal.fire({
      title: 'Tambah Kelas',
      text: 'Formulir penambahan kelas akan muncul di sini.',
      icon: 'info'
    });
  };''', '')

content = content.replace('onClick={handleAdd}', 'onClick={() => handleOpenModal()}')
content = content.replace('<button className="p-1.5 text-blue-600 hover:bg-blue-50 rounded-lg transition-colors" title="Edit">', '<button onClick={() => handleOpenModal(kelas)} className="p-1.5 text-blue-600 hover:bg-blue-50 rounded-lg transition-colors" title="Edit">')

modal_ui = """
      {isModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 backdrop-blur-sm p-4">
          <div className="bg-white rounded-2xl shadow-xl w-full max-w-md overflow-hidden">
            <div className="p-6 border-b border-slate-200 flex items-center justify-between">
              <h3 className="text-lg font-bold text-slate-800">
                {formData.id ? 'Edit Kelas' : 'Tambah Kelas Baru'}
              </h3>
              <button onClick={() => setIsModalOpen(false)} className="text-slate-400 hover:text-slate-600 transition-colors">
                <X className="w-5 h-5" />
              </button>
            </div>
            <form onSubmit={handleSave} className="p-6 space-y-4">
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Tingkat</label>
                <select 
                  required 
                  value={formData.tingkat} 
                  onChange={e => setFormData({...formData, tingkat: e.target.value})}
                  className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
                >
                  <option value="VII">VII</option>
                  <option value="VIII">VIII</option>
                  <option value="IX">IX</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Nama Kelas</label>
                <input 
                  type="text" 
                  required 
                  value={formData.namaKelas} 
                  onChange={e => setFormData({...formData, namaKelas: e.target.value})}
                  className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Wali Kelas</label>
                <input 
                  type="text" 
                  required 
                  value={formData.waliKelas} 
                  onChange={e => setFormData({...formData, waliKelas: e.target.value})}
                  className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Jumlah Siswa</label>
                <input 
                  type="number" 
                  required 
                  value={formData.jumlahSiswa} 
                  onChange={e => setFormData({...formData, jumlahSiswa: parseInt(e.target.value) || 0})}
                  className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
                />
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

with open('src/pages/MasterKelas.tsx', 'w') as f:
    f.write(content)

