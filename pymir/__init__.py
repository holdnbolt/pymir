from . import helpers

from . import base_object
#from . import system_clock as sysclk

helpers.setup_environment()
mods = helpers.import_common()

obj = base_object.pymir_object