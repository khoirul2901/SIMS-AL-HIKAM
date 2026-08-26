import re
with open('src/pages/AbsensiSiswa.tsx', 'r') as f:
    content = f.read()

new_scan_qr = """  const handleScanQR = () => {
    Swal.fire({
      title: 'Scan QR Code Absensi',
      html: `
        <div class="flex flex-col items-center justify-center p-4">
          <div id="reader" style="width: 300px; height: 300px;" class="mb-4"></div>
          <p class="text-sm text-slate-500 mt-2">Arahkan Kamera ke QR Code Siswa</p>
          <div class="mt-4 w-full">
            <input type="text" id="manual-nis" class="w-full px-3 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500" placeholder="Atau ketik NIS manual di sini">
          </div>
        </div>
      `,
      showCancelButton: true,
      confirmButtonText: 'Absen Manual',
      cancelButtonText: 'Tutup',
      didOpen: () => {
        // Load html5-qrcode dynamically
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
            "reader", { fps: 10, qrbox: { width: 250, height: 250 } }, false
          );
          scanner.render(onScanSuccess, onScanFailure);
          
          function onScanSuccess(decodedText: string, decodedResult: any) {
            scanner.clear();
            (document.getElementById('manual-nis') as HTMLInputElement).value = decodedText;
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
        const manualNis = (document.getElementById('manual-nis') as HTMLInputElement).value;
        if (!manualNis) {
          Swal.showValidationMessage('Masukkan NIS terlebih dahulu');
          return false;
        }
        return manualNis;
      }
    }).then((result) => {
      if (result.isConfirmed && result.value) {
        const nis = result.value;
        const student = siswaData.find(s => s.nis === nis);
        if (student) {
          handleStatusChange(student.nis, 'Hadir');
          Swal.fire({
            icon: 'success',
            title: 'Berhasil',
            text: `Absensi untuk ${student.nama} berhasil dicatat.`,
            timer: 2000,
            showConfirmButton: false
          });
        } else {
          Swal.fire('Gagal', 'Siswa dengan NIS tersebut tidak ditemukan.', 'error');
        }
      }
    });
  };"""

# Use regex to find and replace the whole handleScanQR block
content = re.sub(r'  const handleScanQR = \(\) => \{.*?(?=\n  return \()', new_scan_qr, content, flags=re.DOTALL)

with open('src/pages/AbsensiSiswa.tsx', 'w') as f:
    f.write(content)
