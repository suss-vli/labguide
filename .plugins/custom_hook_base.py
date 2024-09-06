from IPython.core.interactiveshell import InteractiveShell

def custom_run_cell(self, raw_cell, **kw):
    # Check if the cell contains the target code
    if "q4.a.check()" in raw_cell:
        print("hello world")
    # Execute the cell
    return self._orig_run_cell(raw_cell, **kw)

def load_custom_hook():
    ipython = InteractiveShell.instance()
    # Save the original run_cell method
    if not hasattr(ipython, '_orig_run_cell'):
        ipython._orig_run_cell = ipython.run_cell
    # Replace the run_cell method with the custom one
    ipython.run_cell = custom_run_cell.__get__(ipython, InteractiveShell)

# Load the custom hook
load_custom_hook()