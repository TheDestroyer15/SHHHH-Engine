import os, json, datetime

source_dir = f'{os.path.abspath(os.getcwd())}\\Maple Editor\\source'
project_location_container = 'projects.json'
full_project_location_container = os.path.join(source_dir, project_location_container)

class project:
    def __init__(self, name):
        self.name = name
        self.path = f'projects\\{name}'
        self.type = 'default'
        self.created_at = None
    def isValid(self):
        return True
    @staticmethod
    def create(name: str, path: str, type: str) -> None:
        if not name or not path or not type:
            raise ValueError('Name, path, and type are required to create a project.')
        path = path.strip('"')
        os.path.normpath(path)
        path = os.path.join(path, name)
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, 'project.json'), 'w') as f:
            data = {
                'name': name,
                'type': type,
                'created_at': datetime.datetime.now().isoformat()
            }
            json.dump(data, f)
        with open(full_project_location_container, 'r') as f:
            data = json.load(f)
            projects = data['projects']
            total = data['total projects']
        projects.append(path)
        total += 1
        with open(full_project_location_container, 'w') as f:
            data = {
                'projects': projects,
                'total projects': total,
            }
            json.dump(data, f)
        print(f'Created project {name} at {path}')
        return
    @staticmethod
    def load(path):
        with open(os.path.join(path, 'project.json'), 'r') as f:
            data = json.load(f)
        proj = project(data['name'])
        proj.type = data['type']
        proj.created_at = data['created_at']
        return proj
    @staticmethod
    def listAll() -> list:
        try:
            with open(full_project_location_container, 'r') as f:
                projects = json.load(f)['projects']
        except FileNotFoundError:
            with open(full_project_location_container, 'w') as f:
                data = {
                    'projects': [],
                    'total projects': 0,
                }
                json.dump(data, f)
            projects = []
    
        projects = [proj for proj in [project.load(path) for path in projects] if proj.isValid()]
        return projects
    def __repr__(self):
        return f'<Project name={self.name} path={self.path}>'
    