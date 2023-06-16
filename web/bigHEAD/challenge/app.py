from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'PUT'])
def index():
    if request.method == 'PUT':
        if request.headers.get('User-Agent') == '3p1cW3bBr0ws3r':
            if request.headers.get('Accept-Language') == 'ar-dz':
                return 'ISICTF{y4y_1_kn0w_H77P_h34d3r5}'
            return 'here in Algeria we speak arabic :('
        else:
            return 'Sorry, only users who use 3p1cW3bBr0ws3r are allowed :('
    else:
        return 'nice try :P try to PUT something else'


if __name__ == '__main__':
    app.run(debug=False)