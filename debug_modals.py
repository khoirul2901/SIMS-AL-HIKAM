import re

def add_debug(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Add error catching to handleSaveSiswa / handleSaveGuru
    content = content.replace('e.preventDefault();\n    var btn', 'e.preventDefault();\n    try {\n    var btn')
    content = content.replace('.saveSiswa(data);\n  }', '.saveSiswa(data);\n    } catch (error) {\n      Swal.fire("Debug Error", error.toString(), "error");\n    }\n  }')
    content = content.replace('.saveGuru(data);\n  }', '.saveGuru(data);\n    } catch (error) {\n      Swal.fire("Debug Error", error.toString(), "error");\n    }\n  }')
    
    # Add debug to showModalSiswa / showModalGuru
    content = content.replace('var modal = document.getElementById', 'try {\n    var modal = document.getElementById')
    content = content.replace('}, 10);\n  }', '}, 10);\n    } catch (error) {\n      alert("Debug Show Modal: " + error.toString());\n    }\n  }')

    with open(filepath, 'w') as f:
        f.write(content)

add_debug('gas/Comp_MasterSiswa.html')
add_debug('gas/Comp_MasterGuru.html')
