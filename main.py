from TIA_wrapper import TIA_wrapper

tia = TIA_wrapper()

project = tia.list_projects()[0]
plc = tia.list_plcs(project)[0]
program_block_1 = tia.list_SCL_blocks(project, plc)[0]
code1 = tia.get_code(project, plc, program_block_1)

print(f"Code for {program_block_1}:\n{code1}\n")