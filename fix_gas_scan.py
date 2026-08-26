import re

def update_scan_func(filename, function_name, is_guru=False):
    with open(filename, 'r') as f:
        content = f.read()

    id_field = 'nip' if is_guru else 'nis'
    data_var = 'rawDataGuru' if is_guru else 'rawDataSiswaKelas'
    name_field = 'Nama Guru' if is_guru else 'Siswa'
    
    new_scan = f"""  function {function_name}() {{
    Swal.fire({{
      title: 'Scan QR Code Absensi',
      html: `
        <div class="flex flex-col items-center justify-center p-4">
          <div id="reader" style="width: 300px; height: 300px;" class="mb-4"></div>
          <p class="text-sm text-slate-500 mt-2">Arahkan Kamera ke QR Code {name_field}</p>
          <div class="mt-4 w-full">
            <input type="text" id="manual-id" class="w-full px-3 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500" placeholder="Atau ketik {id_field.upper()} manual di sini">
          </div>
        </div>
      `,
      showCancelButton: true,
      confirmButtonText: 'Absen Manual',
      cancelButtonText: 'Tutup',
      didOpen: () => {{
        if (!window.Html5QrcodeScanner) {{
          const script = document.createElement('script');
          script.src = "https://unpkg.com/html5-qrcode";
          script.async = true;
          script.onload = startScanner;
          document.body.appendChild(script);
        }} else {{
          startScanner();
        }}

        function startScanner() {{
          const scanner = new window.Html5QrcodeScanner(
            "reader", {{ fps: 10, qrbox: {{ width: 250, height: 250 }} }}, false
          );
          scanner.render(onScanSuccess, onScanFailure);
          
          function onScanSuccess(decodedText, decodedResult) {{
            scanner.clear();
            document.getElementById('manual-id').value = decodedText;
            Swal.clickConfirm();
          }}
          function onScanFailure(error) {{}}
          
          Swal.getPopup().scanner = scanner;
        }}
      }},
      willClose: () => {{
        const scanner = Swal.getPopup().scanner;
        if (scanner) {{
          scanner.clear().catch(e => console.log(e));
        }}
      }},
      preConfirm: () => {{
        const manualId = document.getElementById('manual-id').value;
        if (!manualId) {{
          Swal.showValidationMessage('Masukkan {id_field.upper()} terlebih dahulu');
          return false;
        }}
        return manualId;
      }}
    }}).then((result) => {{
      if (result.isConfirmed && result.value) {{
        var {id_field} = result.value;
        var s = {data_var}.find(x => x.{id_field} === {id_field});
        if(s) {{
          changeAbsen({id_field}, 'Hadir');
          var jenis = document.getElementById('jenisAbsensi').value;
          Swal.fire({{
            icon: 'success',
            title: 'Berhasil Absen!',
            text: `${{s.nama}} berhasil ditandai Hadir (${{jenis}}).`,
            timer: 2000,
            showConfirmButton: false
          }});
        }} else {{
          Swal.fire('Gagal', '{name_field} dengan {id_field.upper()} tersebut tidak ditemukan.', 'error');
        }}
      }}
    }});
  }}"""

    # For Siswa, replace simulateScanQR
    if not is_guru:
        content = re.sub(r'  function simulateScanQR\(\) \{.*?(?=\n  // Need to make sure init is called)/s', new_scan, content, flags=re.DOTALL)
    
    with open(filename, 'w') as f:
        f.write(content)

update_scan_func('gas/Comp_AbsensiSiswa.html', 'simulateScanQR', False)

