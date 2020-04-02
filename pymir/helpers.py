loaded_modules = {}
def import_common(import_only = None):
    for mod in ['os', 'pygame']:
        buffer = load_module(mod)
        
        if mod not in loaded_modules:
            loaded_modules[mod] = buffer
        
        if import_only != None and import_only == mod:
            return buffer

    return loaded_modules
    
def load_module(module_name, verbose = False):
    if verbose:
        print("Loading", module_name, end='...')

    try:
        return __import__(module_name)
    except ModuleNotFoundError as err:
        print(". [Error!]:", err)
    
    return False

def setup_environment():
    os = import_common('os')

    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"