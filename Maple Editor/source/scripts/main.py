from flask import Flask
import views

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return views.home()


if __name__ == '__main__':
    port = 5000

    import socket
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f'Server started on {hostname} at {ip_address}:{port}')

    app.run(debug=True, host='0.0.0.0', port=port)

 