from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    if request.method == 'HEAD':
        if request.headers.get('User-Agent') == 'BigHe3dBrowser':
            return 'ISICTF{y4y_1_kn0w_H77P_h34d3r5}'
        else:
            return 'Sorry, only users who use BigHe3dBrowser are allowed :('
    else:
        return 'Your HEAD isn\'t big enough :P'


if __name__ == '__main__':
    app.run(debug=False)
