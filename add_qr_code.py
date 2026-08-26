import re

def add_qr_to_react(filepath, id_field, prefix='s'):
    with open(filepath, 'r') as f:
        content = f.read()

    # Add .kartu-qr to style
    css_patch = """            .kartu-info td:first-child { width: 55px; font-weight: bold; color: #475569; }
            .kartu-qr { margin-left: 8px; display: flex; align-items: flex-end; justify-content: flex-end; }"""
    content = content.replace('.kartu-info td:first-child { width: 55px; font-weight: bold; color: #475569; }', css_patch)

    body_old = """                  </table>
                </div>
              </div>"""
    body_new = f"""                  </table>
                </div>
                <div class="kartu-qr">
                  <img src="https://quickchart.io/qr?text=${{{prefix}.{id_field}}}&size=60&margin=1" alt="QR" style="width: 50px; height: 50px; border: 1px solid #e2e8f0; border-radius: 4px; padding: 2px; background: white;" />
                </div>
              </div>"""
    content = content.replace(body_old, body_new)
        
    with open(filepath, 'w') as f:
        f.write(content)


def add_qr_to_gas(filepath, id_field, prefix='s'):
    with open(filepath, 'r') as f:
        content = f.read()

    css_patch = """  .kartu-info td:first-child { width: 55px; font-weight: bold; color: #475569; }
  .kartu-qr { margin-left: 8px; display: flex; align-items: flex-end; justify-content: flex-end; }"""
    content = content.replace('  .kartu-info td:first-child { width: 55px; font-weight: bold; color: #475569; }', css_patch)

    body_old = """            </table>
          </div>
        </div>"""
    body_new = f"""            </table>
          </div>
          <div class="kartu-qr">
            <img src="https://quickchart.io/qr?text=${{{prefix}.{id_field}}}&size=60&margin=1" alt="QR" style="width: 50px; height: 50px; border: 1px solid #e2e8f0; border-radius: 4px; padding: 2px; background: white;" />
          </div>
        </div>"""
    content = content.replace(body_old, body_new)

    with open(filepath, 'w') as f:
        f.write(content)

# Apply to React components
add_qr_to_react('src/pages/MasterSiswa.tsx', 'nis', 's')
add_qr_to_react('src/pages/MasterGuru.tsx', 'nip', 'g')

# Apply to GAS components
add_qr_to_gas('gas/Comp_MasterSiswa.html', 'nis', 's')
add_qr_to_gas('gas/Comp_MasterGuru.html', 'nip', 'g')
