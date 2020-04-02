from datetime import datetime
from .. import base_object

class pymir_timestamp(base_object.pymir_object):
    def __add__(self, other):
        pass
    
    def __sub__(self, other):
        pass

    def __new__(cls, *args, **kwargs):
        parent = super(pymir_timestamp, cls)
        self = parent.__new__(cls, *args, **kwargs)
        return self

    def set_initial_arguments(self):
        self.add_local_arguments({
            'time': None,
            'string_only': False
        })