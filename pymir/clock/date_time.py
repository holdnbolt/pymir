from datetime import datetime

class date_time:
    def __init__(self, **args):
        self.dt = None
        self.parse_args(**args)

    def parse_args(self, **args):
        if 'date' in args or 'time' in args or 'datetime' in args:
            print("idk what to do")
        else:
            self.dt = datetime.now()