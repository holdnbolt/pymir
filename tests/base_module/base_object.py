import pymir

class test(pymir.base_object.pymir_object):
    def __init__(self, *args, **kwargs):
        parent = super(test, self)
        parent.__init__(self)

    def set_initial_arguments(self):
        self.add_local_arguments({
            'test': None,
            'files': None
        })

buffer = test()