from flask import Flask, request, render_template, jsonify
import subprocess
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/ping", methods=['GET'])
def ping():
    url = request.args.get('url')
    if url:
        try:
            output = subprocess.run(
                f"ping {url}", shell=True, timeout=10, capture_output=True).stdout
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8')
    return 'No url provided'
