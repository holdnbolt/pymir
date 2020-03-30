class pymir_object:
    base_dunders = ["__data__", "__datakeys__", "__name__"]
    base_keys = ["arguments", "id", "labeled_arguments"]

    def __del__(self):
        pass

    def __delattr__(self, name):
        pass

    def __getattr__(self, name):
        if name in self.base_dunders:
            return self.__dict__[name]

        if name in self.base_keys:
            return self.__dict__[name]

        if name in self.__datakeys__:
            return self.__data__[name]

        print("%s.%s does not exist" % (
            self.__name__,
            name
        ))
        return False

    def __init__(self, *args, **kwargs):
        self.set_initial_arguments()
        self.check_local_arguments(args, kwargs)

    def __new__(cls, *args, **kwargs):       
        parent_object = super(pymir_object, cls)
        self = parent_object.__new__(cls)
        self.__name__ = cls.__name__
        self.__data__ = {}
        self.__datakeys__ = []

        self.arguments = args
        self.labeled_arguments = kwargs

        parent_object.__init__(cls)
        return self

    def __setattr__(self, name, value):
        if name in self.base_dunders:
            self.__dict__[name] = value
            return True

        if name in self.base_keys:
            self.__dict__[name] = value
            return True

        if name in self.__datakeys__:
            self.__data__[name] = value
            return True

        print("%s.%s does not exist" % (self.__name__, name))
        exit(-1)

    def __str__(self):
        return self.__name__ + " [" + str(id(self)) + "]"

    def add_local_arguments(self, args):
        for key in args:
            self.__datakeys__.append(key)
            self.__data__[key] = args[key]

    def check_local_arguments(self, *args, **kwargs):
        print(self.__datakeys__)
    
    def set_initial_arguments(self):
        # To be overwrote
        pass

            
