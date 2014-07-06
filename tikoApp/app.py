from canvas import Canvas
from time import sleep
import random

class TikoApp:
    def run(self):
        print 'RUNNING'
        r = lambda: random.randint(0, 255)
        while True:
            Canvas.clear()
            Canvas.draw_rect((0, 0), (200, 200), fill_style='#%02X%02X%02X' % (r(), r(), r()))
            sleep(random.uniform(0.03, 1))