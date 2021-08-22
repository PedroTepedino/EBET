import time
import random
from flask import Flask

app = Flask(__name__)

counter = 0

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/teste')
def get_current_teste():
    global counter
    counter += 1
    return {'teste': counter}