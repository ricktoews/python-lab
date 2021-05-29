import json
import sys
sys.path.append('mathtoys')
sys.path.append('math-scripts')

from play import get_pythag
from flask import Flask, jsonify

from phi import phi_powers

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/pythag', methods=['GET'])
def pythag():
  return json.dumps(get_pythag(), indent=4, separators=(',', ': '))

@app.route('/phi', defaults={'power': 4})
@app.route('/phi/<power>', methods=['GET'])
def phi(power):
  power = int(power)
  return json.dumps(phi_powers(power), indent=4, separators=(',', ': '))

