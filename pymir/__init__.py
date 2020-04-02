from . import helpers
helpers.setup_environment()
mods = helpers.import_common()
from . import base_object
from . import system_clock as clock
obj = base_object.pymir_object