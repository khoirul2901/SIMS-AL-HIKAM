with open('src/pages/MasterGuru.tsx', 'r') as f:
    content = f.read()

bad_str = """                  </table>
                </div>
                <div class="kartu-qr">
                  <img src="https://quickchart.io/qr?text=${g.nip}&size=60&margin=1" alt="QR" style="width: 50px; height: 50px; border: 1px solid #e2e8f0; border-radius: 4px; padding: 2px; background: white;" />
                </div>
              </div>
            </div>
            <div className="p-6 border-t border-slate-200 flex justify-end gap-3 shrink-0 bg-slate-50">"""

good_str = """                  </table>
                </div>
              </div>
            </div>
            <div className="p-6 border-t border-slate-200 flex justify-end gap-3 shrink-0 bg-slate-50">"""

content = content.replace(bad_str, good_str)

with open('src/pages/MasterGuru.tsx', 'w') as f:
    f.write(content)
