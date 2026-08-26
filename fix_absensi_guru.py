with open('src/pages/AbsensiGuru.tsx', 'r') as f:
    content = f.read()

new_content = """import React, { useState } from 'react';
import { useDatabase } from '../context/DatabaseContext';
import { QrCode, Search, Save, Calendar, CheckSquare, UserCheck } from 'lucide-react';
import Swal from 'sweetalert2';

export const AbsensiGuru = () => {
  const { guruData, absensiGuruData, setAbsensiGuruData } = useDatabase();
  const [jenisAbsen, setJenisAbsen] = useState('Masuk');
  const [date, setDate] = useState(new Date().toISOString().split('T')[0]);
  const [searchTerm, setSearchTerm] = useState('');

  const filteredData = guruData.map(guru => {
    const existing = absensiGuruData.find(a => a.nip === guru.nip && a.tanggal === date && a.jenis === jenisAbsen);
    return {
      ...guru,
      status: existing ? existing.status : 'Belum diabsen',
      waktu: existing ? existing.waktu : '-'
    };
  }).filter(guru => 
    guru.nama.toLowerCase().includes(searchTerm.toLowerCase()) || 
    guru.nip.includes(searchTerm)
  );

  const handleStatusChange = (nip: string, status: string) => {
    const existingIdx = absensiGuruData.findIndex(a => a.nip === nip && a.tanggal === date && a.jenis === jenisAbsen);
    const waktu = status === 'Hadir' || status === 'Terlambat' ? new Date().toLocaleTimeString('id-ID', {hour: '2-digit', minute:'2-digit'}) : '-';
    
    if (existingIdx >= 0) {
      const newAbsensi = [...absensiGuruData];
      newAbsensi[existingIdx].status = status;
      newAbsensi[existingIdx].waktu = waktu;
      setAbsensiGuruData(newAbsensi);
    } else {
      setAbsensiGuruData([...absensiGuruData, {
        id: Math.random().toString(36).substr(2, 9),
        tanggal: date,
        nip,
        jenis: jenisAbsen,
        status,
        waktu
      }]);
    }
  };

  const handleScanQR = () => {
    Swal.fire({
      title: 'Scan QR Code Guru',
      html: `
        <div class="flex flex-col items-center justify-center p-4">
          <div id="reader-guru" style="width: 300px; height: 300px;" class="mb-4"></div>
          <p class="text-sm text-slate-500 mt-2">Arahkan Kamera ke QR Code Guru</p>
          <div class="mt-4 w-full">
            <input type="text" id="manual-nip" class="w-full px-3 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500" placeholder="Atau ketik NIP manual di sini">
          </div>
        </div>
      `,
      showCancelButton: true,
      confirmButtonText: 'Absen Manual',
      cancelButtonText: 'Tutup',
      didOpen: () => {
        if (!(window as any).Html5QrcodeScanner) {
          const script = document.createElement('script');
          script.src = "https://unpkg.com/html5-qrcode";
          script.async = true;
          script.onload = startScanner;
          document.body.appendChild(script);
        } else {
          startScanner();
        }

        function startScanner() {
          const scanner = new (window as any).Html5QrcodeScanner(
            "reader-guru", { fps: 10, qrbox: { width: 250, height: 250 } }, false
          );
          scanner.render(onScanSuccess, onScanFailure);
          
          function onScanSuccess(decodedText: string, decodedResult: any) {
            scanner.clear();
            (document.getElementById('manual-nip') as HTMLInputElement).value = decodedText;
            Swal.clickConfirm();
          }
          function onScanFailure(error: any) {}
          
          (Swal.getPopup() as any).scanner = scanner;
        }
      },
      willClose: () => {
        const scanner = (Swal.getPopup() as any).scanner;
        if (scanner) {
          scanner.clear().catch((e: any) => console.log('Failed to clear scanner', e));
        }
      },
      preConfirm: () => {
        const manualNip = (document.getElementById('manual-nip') as HTMLInputElement).value;
        if (!manualNip) {
          Swal.showValidationMessage('Masukkan NIP terlebih dahulu');
          return false;
        }
        return manualNip;
      }
    }).then((result) => {
      if (result.isConfirmed && result.value) {
        const nip = result.value;
        const guru = guruData.find(g => g.nip === nip);
        if (guru) {
          handleStatusChange(guru.nip, 'Hadir');
          Swal.fire({
            icon: 'success',
            title: 'Berhasil',
            text: `Absensi ${jenisAbsen} untuk ${guru.nama} berhasil dicatat.`,
            timer: 2000,
            showConfirmButton: false
          });
        } else {
          Swal.fire('Gagal', 'Guru dengan NIP tersebut tidak ditemukan.', 'error');
        }
      }
    });
  };

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold text-slate-800">Absensi Guru</h1>
          <p className="text-sm text-slate-500 mt-1">Input data kehadiran Tenaga Pendidik</p>
        </div>
        <div className="flex items-center gap-2">
          <button 
            onClick={handleScanQR}
            className="flex items-center gap-2 px-4 py-2 bg-slate-800 text-white hover:bg-slate-900 font-medium rounded-lg transition-colors text-sm"
          >
            <QrCode className="w-4 h-4" />
            Scan QR (Otomatis)
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Filters Panel */}
        <div className="md:col-span-1 space-y-4">
          <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
            <h3 className="font-semibold text-slate-800 mb-4 flex items-center gap-2">
              <Calendar className="w-4 h-4 text-indigo-600" />
              Filter Absensi
            </h3>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Tanggal</label>
                <input 
                  type="date" 
                  value={date}
                  onChange={(e) => setDate(e.target.value)}
                  className="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Jenis Absensi</label>
                <div className="grid grid-cols-2 gap-2">
                  <button 
                    onClick={() => setJenisAbsen('Masuk')}
                    className={`py-2 px-3 text-sm font-medium rounded-lg border transition-colors ${jenisAbsen === 'Masuk' ? 'bg-blue-50 border-blue-200 text-blue-700' : 'bg-white border-slate-200 text-slate-600 hover:bg-slate-50'}`}
                  >
                    Masuk
                  </button>
                  <button 
                    onClick={() => setJenisAbsen('Pulang')}
                    className={`py-2 px-3 text-sm font-medium rounded-lg border transition-colors ${jenisAbsen === 'Pulang' ? 'bg-blue-50 border-blue-200 text-blue-700' : 'bg-white border-slate-200 text-slate-600 hover:bg-slate-50'}`}
                  >
                    Pulang
                  </button>
                </div>
              </div>

              <div className="pt-4 border-t border-slate-100">
                <div className="bg-blue-50 rounded-lg p-3">
                  <p className="text-xs text-blue-800 font-medium mb-1">Ringkasan {jenisAbsen} Guru</p>
                  <div className="grid grid-cols-2 gap-2 text-sm mt-2">
                    <div className="flex justify-between"><span className="text-slate-500">Hadir:</span> <span className="font-semibold text-emerald-600">{filteredData.filter(g => g.status === 'Hadir').length}</span></div>
                    <div className="flex justify-between"><span className="text-slate-500">Izin:</span> <span className="font-semibold text-blue-600">{filteredData.filter(g => g.status === 'Izin').length}</span></div>
                    <div className="flex justify-between"><span className="text-slate-500">Sakit:</span> <span className="font-semibold text-amber-600">{filteredData.filter(g => g.status === 'Sakit').length}</span></div>
                    <div className="flex justify-between"><span className="text-slate-500">Alpa:</span> <span className="font-semibold text-red-600">{filteredData.filter(g => g.status === 'Alpa').length}</span></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* List Panel */}
        <div className="md:col-span-2">
          <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden flex flex-col h-[calc(100vh-12rem)] min-h-[500px]">
            <div className="p-4 border-b border-slate-200 flex flex-col sm:flex-row justify-between gap-4 bg-slate-50 shrink-0">
              <div className="relative flex-1">
                <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
                <input 
                  type="text" 
                  placeholder="Cari nama atau NIP guru..." 
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="w-full pl-9 pr-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm"
                />
              </div>
            </div>

            <div className="overflow-auto flex-1">
              <table className="w-full text-left text-sm">
                <thead className="bg-slate-50 text-slate-600 sticky top-0 z-10 shadow-sm">
                  <tr>
                    <th className="px-4 py-3 font-semibold border-b">Guru</th>
                    <th className="px-4 py-3 font-semibold border-b w-32">Waktu</th>
                    <th className="px-4 py-3 font-semibold border-b w-64 text-center">Status Kehadiran</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {filteredData.length > 0 ? filteredData.map((guru) => (
                    <tr key={guru.nip} className="hover:bg-slate-50 transition-colors">
                      <td className="px-4 py-3">
                        <div className="flex items-center gap-3">
                          <div className="w-10 h-10 rounded-full bg-indigo-100 text-indigo-600 flex items-center justify-center shrink-0">
                            <span className="font-bold text-sm">{guru.nama.charAt(0)}</span>
                          </div>
                          <div>
                            <p className="font-medium text-slate-800 line-clamp-1">{guru.nama}</p>
                            <p className="text-xs text-slate-500">{guru.nip} • {guru.mapel}</p>
                          </div>
                        </div>
                      </td>
                      <td className="px-4 py-3 text-slate-600 font-medium">{guru.waktu}</td>
                      <td className="px-4 py-3">
                        <div className="flex items-center justify-center gap-1">
                          <button 
                            onClick={() => handleStatusChange(guru.nip, 'Hadir')}
                            className={`w-8 h-8 rounded flex items-center justify-center transition-colors ${guru.status === 'Hadir' ? 'bg-emerald-500 text-white' : 'bg-slate-100 text-slate-400 hover:bg-slate-200'}`}
                            title="Hadir"
                          >
                            H
                          </button>
                          <button 
                            onClick={() => handleStatusChange(guru.nip, 'Izin')}
                            className={`w-8 h-8 rounded flex items-center justify-center transition-colors ${guru.status === 'Izin' ? 'bg-blue-500 text-white' : 'bg-slate-100 text-slate-400 hover:bg-slate-200'}`}
                            title="Izin"
                          >
                            I
                          </button>
                          <button 
                            onClick={() => handleStatusChange(guru.nip, 'Sakit')}
                            className={`w-8 h-8 rounded flex items-center justify-center transition-colors ${guru.status === 'Sakit' ? 'bg-amber-500 text-white' : 'bg-slate-100 text-slate-400 hover:bg-slate-200'}`}
                            title="Sakit"
                          >
                            S
                          </button>
                          <button 
                            onClick={() => handleStatusChange(guru.nip, 'Alpa')}
                            className={`w-8 h-8 rounded flex items-center justify-center transition-colors ${guru.status === 'Alpa' ? 'bg-red-500 text-white' : 'bg-slate-100 text-slate-400 hover:bg-slate-200'}`}
                            title="Alpa"
                          >
                            A
                          </button>
                        </div>
                      </td>
                    </tr>
                  )) : (
                    <tr>
                      <td colSpan={3} className="px-4 py-8 text-center text-slate-500">
                        <div className="flex flex-col items-center justify-center">
                          <UserCheck className="w-12 h-12 text-slate-300 mb-2" />
                          <p>Tidak ada data guru yang ditemukan.</p>
                        </div>
                      </td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
"""

with open('src/pages/AbsensiGuru.tsx', 'w') as f:
    f.write(new_content)
