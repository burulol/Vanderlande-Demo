import os
import sys
import siemens_tia_scripting as ts
import tempfile
import glob

version = "20.0"
projects_folder = r"C:\\Users\\burui\\Documents\\Automation"


def find_projects(dir):
    return glob.glob(f"{dir}/**/*.ap20", recursive=True)

def select_project(projects):
    for i, project in enumerate(projects):
        print(f"{i}: {project}")
    index = int(input("Select a project by index: "))
    return projects[index]

def select_plc(plcs):
    for i, plc in enumerate(plcs):
        print(f"{i}: {plc.get_name()}")
    index = int(input("Select a PLC by index: "))
    return plcs[index]

def select_program_block(blocks):
    for i, block in enumerate(blocks):
        print(f"{i}: {block.get_name()}")
    index = int(input("Select a program block by index: "))
    return blocks[index]

portal = ts.open_portal(portal_mode = ts.Enums.PortalMode.WithoutGraphicalUserInterface , version = version)

project = portal.open_project(select_project(find_projects(projects_folder)))

plc = select_plc(project.get_plcs())

for program_block in plc.get_program_blocks():
    print(program_block.get_property(name = 'ProgrammingLanguage'))




sys.exit(0)