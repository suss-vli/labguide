import socket

def is_internet_down():
    print("Checking internet connection...")
    try:
        # Attempt to connect to a well-known internet host (Google DNS)
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        # may want to check two more DNS servers to ensure accuracy
        print("Internet is up")
        return False  # Internet is upanyway
    except OSError:
        print("Internet is down")
        return True   # Internet is down
