from flask import render_template, redirect, url_for
from helpers import project
import os

def home():
    projects = project.listAll()
    return render_template('home.html', projects=projects)

def newProject(method, args):
    if method == 'GET':
        path = f'{os.path.abspath(os.getcwd())}\\'
        return render_template('newProject.html', path = path)
    elif method == 'POST':
        try:
            proj = project.create(args.get('name'), args.get('path'), args.get('type'))
            proj = project.load(os.path.join(args.get('path').strip('"'), args.get('name')))
        except Exception as e:
            return f'Error creating project: {str(e)}'
        return redirect(f'/project/{proj.name}')
    else:
        return 'Method Not Allowed', 405