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
    
    def list_plcs(self, project_name):

        project_path = os.path.join(projects_folder, project_name)

        project = self.portal.open_project(project_path)

        plcs = project.get_plcs()

        for plc in plcs:
            plc = plc.get_name()

        return plcs
    
    