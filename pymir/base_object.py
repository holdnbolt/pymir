class base_object:
    def __init__(self, **args):
        self.check_arguments(args)

    def check_arguments(self, args):
        print(args)

    def initial_arguments(self, args):
        print(args)

    def setup_initial_arguments(self):
        pass