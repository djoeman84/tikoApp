from threading import Lock
class Canvas:
    displayObjects = []
    canvasLock = Lock()

    @classmethod
    def get_display_objects(cls):
        with cls.canvasLock:
            return cls.displayObjects

    @classmethod
    def clear(cls):
        with cls.canvasLock:
            cls.displayObjects = []

    @classmethod
    def draw_line(cls, start, end, stroke_style=None):
        with cls.canvasLock:
            line = {
                'type': 'line',
                'description': {
                    'start': {'x': start[0], 'y': start[1]},
                    'end': {'x': end[0], 'y': end[1]}
                }
            }

            if stroke_style is not None:
                line['description']['strokeStyle'] = stroke_style

            cls.displayObjects.append(line)


    @classmethod
    def draw_rect(cls, start, end, fill_style=None, stroke_style=None):
        with cls.canvasLock:
            rect = {
                'type': 'rect',
                'description': {
                    'start': {'x': start[0], 'y': start[1]},
                    'end': {'x': end[0], 'y': end[1]}
                }
            }

            if stroke_style is not None:
                rect['description']['strokeStyle'] = stroke_style

            if fill_style is not None:
                rect['description']['fill'] = True
                rect['description']['fillStyle'] = fill_style

            cls.displayObjects.append(rect)