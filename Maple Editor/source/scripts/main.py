from flask import Flask, request
import os
import views
source_dir = f'{os.path.abspath(os.getcwd())}\\Maple Editor\\source'

app = Flask(__name__, static_folder=f'{source_dir}\\static', template_folder=f'{source_dir}\\templates')

@app.route('/')
def home():
    return views.home()

@app.route('/project/new', methods=['GET', 'POST'])
def projects():
    method = request.method
    args = request.args if method == 'GET' else request.form
    #print(f'Received {method} request with args: {args.to_dict()} \n \n')
    return views.newProject(method, args)

if __name__ == '__main__':
    port = 5000

    import socket
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f'Server started on {hostname} at {ip_address}:{port}')
    app.run(debug=True, host='0.0.0.0', port=port)

 