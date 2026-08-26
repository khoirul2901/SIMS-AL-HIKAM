import re

with open('src/pages/MasterMapel.tsx', 'r') as f:
    content = f.read()

imports_to_add = "import { Plus, Search, Edit2, Trash2, BookOpen, X } from 'lucide-react';"
content = re.sub(r"import \{ .*? \} from 'lucide-react';", imports_to_add, content)

state_additions = """  const [isModalOpen, setIsModalOpen] = useState(false);
  const [formData, setFormData] = useState({ id: '', kode: '', nama: '', kelompok: 'Wajib A', kkm: 75 });
  
  const handleOpenModal = (mapel?: typeof INITIAL_DATA[0]) => {
    if (mapel) {
      setFormData(mapel);
    } else {
      setFormData({ id: '', kode: '', nama: '', kelompok: 'Wajib A', kkm: 75 });
    }
    setIsModalOpen(true);
  };

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    if (formData.id) {
      setData(data.map(item => item.id === formData.id ? formData : item));
      Swal.fire('Berhasil!', 'Data mata pelajaran berhasil diupdate.', 'success');
    } else {
      setData([...data, { ...formData, id: Date.now().toString() }]);
      Swal.fire('Berhasil!', 'Data mata pelajaran berhasil ditambahkan.', 'success');
    }
    setIsModalOpen(false);
  };
"""

content = content.replace('  const handleDelete = ', state_additions + '\n  const handleDelete = ')

content = content.replace('''  const handleAdd = () => {
    Swal.fire({
      title: 'Tambah Mata Pelajaran',
      text: 'Formulir penambahan mapel akan muncul di sini.',
      icon: 'info'
    });
  };''', '')

content = content.replace('onClick={handleAdd}', 'onClick={() => handleOpenModal()}')
content = content.replace('<button className="p-1.5 text-blue-600 hover:bg-blue-50 rounded-lg transition-colors" title="Edit">', '<button onClick={() => handleOpenModal(mapel)} className="p-1.5 text-blue-600 hover:bg-blue-50 rounded-lg transition-colors" title="Edit">')

modal_ui = """
      {isModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 backdrop-blur-sm p-4">
          <div className="bg-white rounded-2xl shadow-xl w-full max-w-md overflow-hidden">
            <div className="p-6 border-b border-slate-200 flex items-center justify-between">
              <h3 className="text-lg font-bold text-slate-800">
                {formData.id ? 'Edit Mata Pelajaran' : 'Tambah Mata Pelajaran Baru'}
              </h3>
              <button onClick={() => setIsModalOpen(false)} className="text-slate-400 hover:text-slate-600 transition-colors">
                <X className="w-5 h-5" />
              </button>
            </div>
            <form onSubmit={handleSave} className="p-6 space-y-4">
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Kode Mapel</label>
                <input 
                  type="text" 
                  required 
                  value={formData.kode} 
                  onChange={e => setFormData({...formData, kode: e.target.value})}
                  className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Nama Mata Pelajaran</label>
                <input 
                  type="text" 
                  required 
                  value={formData.nama} 
                  onChange={e => setFormData({...formData, nama: e.target.value})}
                  className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Kelompok</label>
                <select 
                  required 
                  value={formData.kelompok} 
                  onChange={e => setFormData({...formData, kelompok: e.target.value})}
                  className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
                >
                  <option value="Wajib A">Wajib A</option>
                  <option value="Wajib B">Wajib B</option>
                  <option value="Peminatan">Peminatan</option>
                  <option value="Muatan Lokal">Muatan Lokal</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">KKM</label>
                <input 
                  type="number" 
                  required 
                  min="0" max="100"
                  value={formData.kkm} 
                  onChange={e => setFormData({...formData, kkm: parseInt(e.target.value) || 0})}
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

with open('src/pages/MasterMapel.tsx', 'w') as f:
    f.write(content)

