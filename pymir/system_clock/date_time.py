from datetime import datetime

class date_time:
    def __init__(self, **args):
        self.dt = None
        self.parse_args(**args)

        if not self.dt:
            self.set_time(datetime.now())

    def __str__(self):
        return str(self.dt)

    def date(self):
        return str(self.dt).split(" ")[0]

    def time(self):
        return str(self.dt).split(" ")[1]

    def parse_args(self, **args):
        if 'date' in args or 'time' in args or 'datetime' in args:
            print("idk what to do")

    def set_time(self, dt):
        self.dt = dt