from suss.dev import x
from learntools.core.richtext import *
from IPython import get_ipython
import ipynbname
import os

config_file = ".config.yml"
config_data = x.query_config(config_file)

def get_context():
    ip = get_ipython()
    
    path = None
    filename = None
    
    if '__vsc_ipynb_file__' in ip.user_ns:
        # If using VS Code Environment
        path = ip.user_ns['__vsc_ipynb_file__']
        filename = path.split("/")[-1]
    else:
        # If using Jupyter Notebook Environment
        path = str(ipynbname.path())
        filename = str(ipynbname.name())
    
    if not isinstance(path, str):
        raise TypeError(f"Expected 'CURRENT_PATH_NAME' to be a string, but got {type(path)}")
    if not isinstance(filename, str):
        raise TypeError(f"Expected 'CURRENT_FILE_NAME' to be a string, but got {type(filename)}")
    
    return {'CURRENT_PATH_NAME': path, 'CURRENT_FILE_NAME': filename}

context = get_context()

if x.check_key_in_yaml(config_file, "friendly") == True and config_data["friendly"] == True:
    from friendly.jupyter import *

if x.check_key_in_yaml(config_file, "plugins") == True and config_data["plugins"] != None:
    for plugin in config_data["plugins"]:
        try:
            x.log(f"{plugin} loaded.", colors.WARN)
            # print(os.getcwd())
            with open(f"../.plugins/{plugin}", 'r') as plugin_file:
                plugin_code = plugin_file.read()
                exec(plugin_code, context)
        except FileNotFoundError:
            print(f"Plugin file not found: {plugin}")