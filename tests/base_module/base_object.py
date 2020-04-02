import pymir

class test(pymir.obj):
    def __init__(self, *args, **kwargs):
        parent = super(test, self)
        parent.__init__(self)

    def set_initial_arguments(self):
        self.add_local_arguments({
            'test': None,
            'files': None
        })

for n in range(3):
    buffer = test()
    buffer.test = "Hello World"
    print(buffer.id)
    print(buffer.hash())