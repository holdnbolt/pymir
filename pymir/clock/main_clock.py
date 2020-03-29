from . import date_time

class main_clock:
    def __init__(self, **args):
        print(args)

    def time(self):
        dt = date_time.date_time()
        return dt.time()