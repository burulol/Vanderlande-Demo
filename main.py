from TIA_wrapper import TIA_wrapper

tia = TIA_wrapper()

project = tia.list_projects()[0]
plc = tia.list_plcs(project)[0]

print(tia.list_program_blocks(project, plc))