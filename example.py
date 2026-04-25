import os
import sys
import siemens_tia_scripting as ts
import tempfile

portal_mode_ui = ts.Enums.PortalMode.AnyUserInterface

version = "20.0"

portal = ts.attach_portal(portal_mode = portal_mode_ui, version = version)
    
project = portal.get_project()

plcs = project.get_plcs()
for plc in plcs: 
    print(plc.get_name())
    
blocks = plcs[0].get_program_blocks() 

with tempfile.TemporaryDirectory() as temp_dir:
    blocks[3].export(target_directory_path = temp_dir, export_format = ts.Enums.ExportFormats.ExternalSource)

    exported_file = os.listdir(temp_dir)[0]

    filepath = os.path.join(temp_dir, exported_file)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

print(content)

sys.exit(0)