import os
import sys
import siemens_tia_scripting as ts
import tempfile
import glob

version = "20.0"
projects_folder = r"C:\\Users\\burui\\Documents\\Automation"

class TIA_wrapper:
    def __init__(self):
        self.portal = ts.open_portal(portal_mode = ts.Enums.PortalMode.WithoutGraphicalUserInterface , version = version)

    def list_projects(self):

        paths = glob.glob(f"{projects_folder}/**/*.ap20", recursive=True)

        projects = []

        for path in paths:
            # remove the root folder adnd the file extension
            project_name = os.path.relpath(path, projects_folder)
            project_name = os.path.splitext(project_name)[0]
            projects.append(project_name)

        return projects
    
    def get_project_by_name(self, project_name):

        project_name += ".ap20"

        project_path = os.path.join(projects_folder, project_name)

        project = self.portal.open_project(project_path)

        return project
    
    def list_plcs(self, project_name):

        project = self.get_project_by_name(project_name)

        plcs = project.get_plcs()

        plc_names = []

        for plc in plcs:
            plc_names.append(plc.get_name())

        return plc_names
    
    def list_program_blocks(self, project_name, plc_name):

        project = self.get_project_by_name(project_name)

        plcs = project.get_plcs()

        for plc in plcs:
            if plc.get_name() == plc_name:
                program_blocks = plc.get_program_blocks()
                block_names = []
                for block in program_blocks:
                    block_names.append(block.get_name())
                return block_names
        
        return None
    
