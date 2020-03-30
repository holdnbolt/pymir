class pymir_object:
    def __del__(self):
        pass

    def __delattr__(self, name):
        pass

    def __getattr__(self, name):
        pass

    def __init__(self, *args, **kwargs):
        print(self.arguments)

    def __new__(cls, *args, **kwargs):       
        parent_object = super(pymir_object, cls)
        self = parent_object.__new__(cls)
        
        self.arguments = args
        self.labeled_arguments = kwargs
        parent_object.__init__(cls)
        return self

    def __setattr__(self, name, value):
        print("Ha ha! no")

    def __str__(self):
        return "base_object @ [" + str(id(self)) + "]"

# class base_object:
#     def __init__(self, **args):
#         self.check_arguments(**args)

#     def check_arguments(self, **args):
#         for argument in args:
#             if argument in self.keys:
#                 self.argument = args[argument]
#             else:
#                 print("Unknown argument", argument)

#     def initial_arguments(self, args):
#         self.keys = list(args.keys())
#         for argument in args:
#             self.__dict__[argument] = args[argument]
            
#     def set_initial_arguments(self):
#         # To be overrid
#         pass