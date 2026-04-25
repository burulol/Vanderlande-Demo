from TIA_wrapper import TIA_wrapper

tia = TIA_wrapper()

project = tia.list_projects()[0]
plc = tia.list_plcs(project)[0]
program_block = tia.list_SCL_blocks(project, plc)[0]
code = tia.get_code(project, plc, program_block)

print(f"Project: {project}")
print(f"PLC: {plc}")
print(f"Program block: {program_block}")
print(f"Code for {program_block}:\n{code}\n")