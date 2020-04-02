from datetime import datetime
from .. import base_object

class pymir_timestamp(base_object.pymir_object):
    def __new__(cls, *args, **kwargs):
        parent = super(time, cls)
        self = parent.__new__(cls, *args, **kwargs)  
        exit(-1)
        return self

    def set_initial_arguments(self):
        self.add_local_arguments({
            'time': None,
            'string_only': False
        })