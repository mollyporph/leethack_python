import socket
def hello(person):
    hostname = socket.gethostname()
    print(f"Hello {person}, from {hostname}.")

if __name__ == "__main__":
    hello("world")
