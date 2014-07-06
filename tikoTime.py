import sys, json, threading
sys.path.append('/usr/local/lib/python2.7/site-packages/')
from flask import Flask
from flask import request
from tikoApp.app import TikoApp
from canvas import Canvas
from subprocess import Popen

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_ui_state():
    return json.dumps({
        'displayObjects':Canvas.get_display_objects()
    })

@app.route('/', methods=['POST'])
def post_ui_state():
    pass




class RunApplicationThread(threading.Thread):
    def __init__(self):
        super(RunApplicationThread, self).__init__()

    def run(self):
        TikoApp().run()


if __name__ == '__main__':
    RunApplicationThread().start()
    Popen(['open','http://127.0.0.1:5000/static/index.html','-a','Google Chrome'])
    app.run(debug=True)

