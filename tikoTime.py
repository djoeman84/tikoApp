import sys, json, threading, random
sys.path.append('/usr/local/lib/python2.7/site-packages/')
from flask import Flask
from flask import request
from tikoApp import app
from time import sleep
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
        r = lambda: random.randint(0, 255)
        while True:
            sleep(random.uniform(0.03, 1))
            Canvas.clear()
            Canvas.draw_rect((0, 0), (200, 200), fill_style='#%02X%02X%02X' % (r(), r(), r()))


if __name__ == '__main__':
    RunApplicationThread().start()
    Popen(['open','http://127.0.0.1:5000/static/index.html','-a','Google Chrome'])
    app.run()
    app.TikoApp().run(debug=True)  # does not return

