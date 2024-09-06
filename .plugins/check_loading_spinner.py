from IPython.core.interactiveshell import InteractiveShell
import itertools
import threading
import time
import sys

class Spinner:
    def __init__(self, message="Loading..."):
        self.spinner = itertools.cycle(['-', '/', '|', '\\'])
        self.stop_running = False
        self.message = message
        self.message_length = len(message) + 4  # Include space and spinner character

    def start(self):
        def run_spinner():
            while not self.stop_running:
                sys.stdout.write(f'\r{self.message} {next(self.spinner)} ')
                sys.stdout.flush()
                time.sleep(0.1)

        self.thread = threading.Thread(target=run_spinner)
        self.thread.start()

    def stop(self):
        self.stop_running = True
        self.thread.join()
        sys.stdout.write('\r' + ' ' * self.message_length + '\r')  # Clear the line
        sys.stdout.flush()

def custom_run_cell(self, raw_cell, **kw):
    spinner = Spinner("Loading...")
    spinner.start()
    start_time = time.time()
    
    message_displayed = [False]  # Use a list to hold a mutable boolean value
    cell_execution_done = [False]  # To indicate when the cell has finished execution

    def check_time():
        while not cell_execution_done[0]:  # Keep checking until the cell execution is done
            elapsed_time = time.time() - start_time
            if elapsed_time > 30:
                if "check()" in raw_cell and not message_displayed[0]:
                    sys.stdout.write("\rThis check will take longer to load.\n")
                    sys.stdout.flush()
                    message_displayed[0] = True
            time.sleep(1)  # Check every second

    # Start the time-checking thread
    time_checker = threading.Thread(target=check_time)
    time_checker.start()

    # Execute the cell
    result = self._orig_run_cell(raw_cell, **kw)
    
    # Indicate that the cell execution is done
    cell_execution_done[0] = True

    # Stop the spinner
    spinner.stop()

    # Clear the message if it was displayed
    if message_displayed[0]:
        sys.stdout.write('\033[F\033[K')  # Move cursor up one line and clear the line
        sys.stdout.write('\033[F\033[K')  # Move cursor up one more line and clear the line
        sys.stdout.flush()

    # Wait for the time-checking thread to finish
    time_checker.join()

    return result

def load_custom_hook():
    ipython = InteractiveShell.instance()
    if not hasattr(ipython, '_orig_run_cell'):
        ipython._orig_run_cell = ipython.run_cell
    ipython.run_cell = custom_run_cell.__get__(ipython, InteractiveShell)

# Load the custom hook
load_custom_hook()
