# LeetHack.py
- Install & Configure
- Introduction to Python
- LeetHacking


Two version
- Python 2
- Python 3

Never use python 2, it's dead, it was dead 20 years ago
# Let it die!


Installation

Windows: 
- download https://www.python.org/downloads/windows
- "Add python to PATH"

OSX:
- brew install python

linux
- install python or python3


Python package manager PIP

OSX: 
- Brew intalls pip for you!

Linux:
- python3-pip

Windows:
- Download https://bootstrap.pypa.io/get-pip.py
- python get-pip.py


# HelloWorld.py
```python
import socket
def hello(person):
    hostname = socket.gethostname()
    print(f"Hello {person}, from {hostname}.")

if __name__ == "__main__":
    hello("world")
```
