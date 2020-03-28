class base_object:
    def __init__(self, **args):
        self.check_arguments(**args)

    def check_arguments(self, **args):
        for argument in args:
            if argument in self.keys:
                self.argument = args[argument]
            else:
                print("Unknown argument", argument)

    def initial_arguments(self, args):
        self.keys = list(args.keys())
        for argument in args:
            self.__dict__[argument] = args[argument]
            

    def set_initial_arguments(self):
        pass