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


# Types

```python

an_int = 1

a_float = 0.5

another_float = a_float + an_int

a_str = 'hello'

also_a_string = "hello"

a_list = [1, 2, 3, 4, "asd", True]

a_dict = {'a': 1, 'b': 2}

a_set = {1, 2}

a_tuple = 1, 2
first, second = 1, 2

functions_are_objects = print

# This is a comment
```


# Flow
```python
for i in range(10):
    if i < 5:
       print("Low!")
    elif i > 5:
       print("High!")
    else:
       print("Just right!")
```


# Flow
```python
for i in ["a", "b", "c"]
    
```
# Exceptions
```python
try:
    a_number = int("5")
except ValueError as e:
    print(f"Woops! {e.msg})
except Exception:
    print("How did we get here?")
```


# I O
```python
name = input("What's your name?")
print(f"Hello, {name}")

with open("myfile.txt", mode='r') as myfile:
     text = myfile.read()
print(text)

```
