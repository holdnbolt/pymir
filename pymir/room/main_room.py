class game_room:
    def __init__(self, **args):
        self.setup_args(args = args)

    def parse_args(self, args):
        if len(args) > 0:
            print(args)