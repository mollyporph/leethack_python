# LeetHack.py

Slides available at
 https://github.com/mollyporph/leethack_python

- Install & Configure
- Introduction to Python
- LeetHacking


# LeetHack.py
Two version
- Python 2
- Python 3

NEVER use python 2, it's dead, it was dead 20 years ago.
Let it die!


# Install

Windows: 
- download https://www.python.org/downloads/windows
- "Add python to PATH"

OSX:
- brew install python

linux
- install python or python3


# Packages

OSX: 
- Brew intalls pip for you!

Linux:
- python3-pip

Windows:
- Download https://bootstrap.pypa.io/get-pip.py
- python get-pip.py

Always use python -m pip install x


# REPL

- Just type "python" in the console
- Type help() to get help, e.g help(print)
- exit() to exit the repl


# Types

```python
	an_int = 1

	a_float = 0.5

	another_float = a_float + an_int

	a_str = 'hello'

	also_a_string = "hello"

```


# Types

```python
	a_list = [1, 2, 3, 4, "asd", True]

	a_dict = {'a': 1, 'b': 2}

	a_set = {1, 2}

	a_tuple = 1, 2
	first, second = 1, 2

	# This is a comment
	"""
	This too

	"""
```


# bool

```python
	truthy = True
	falsy = False
	nothing = None
```


# bool

```python
	5 == 5
	6 > 5
	5 >= 5
	6 != 5

	not False
	# True
```


# bool

```python
	'a' in 'abc'
	2 in [1,2,3]

	all([True, 5 > 4, 'x' == 'x'])

	any([1 < 2, 5 == 4, True != True])

```


# bool

```python
	bool(None) == bool(0) == bool('') == bool([]) == 
	bool({}) == bool(()) == False
```


# bool

```python
	snack = 'icecream' if time > 18 else 'chocolate'

	a = None
	b = a or 'default value'
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
	a = ''
	if not a:
	   # a is empty or None

```


# Flow

```python
	myNumbers = [1,2,3]

	for number in myNumbers:
	    last = number
	# Variables survive some scopes
	while last > 1:
	    last -= 1
    

```


# Collections

List-comprehensions

```python
	a_new_list = [x for x in [1, 2, 3]]
	# [1, 2, 3]

	a_new_set = {x for x in [1, 2, 3]}
	# {1, 2, 3}

	a_new_dict = {x : 'leethack' for x in [1, 2, 3]}
	# {1: 'leethack', 2: 'leethack', 3: 'leethack'}

	a_generator = (x for x in [1,2,3])
	# Has to be iterated over or cast to list()

```


# Collections
Map, Filter, Reduce

```python
	myList = [1,2,3,4]

	# map
	doubles = [x * 2 for x in myList]

	# filter
	large_numbers = [x for x in myList if x > 2]

	# reduce
	a_sum = sum(x + 1 for x in myList if x > 2)
```


# Collections
Indexing and Slicing

```python
	myList = [1,2,3,4,5,6,7,8]

	first = mylist[0]
	last = myList[-1]
```


# Collections
Indexing and Slicing

```python
	myList = [1,2,3,4,5,6,7,8]

	# start:stop
	skip_first = myList[1:]
	last_three = myList[-3:]
	first_two = myList[:2]
	two_and_three = myList[1:3]
```


# Collections
Indexing and Slicing

```python
	myList = [1,2,3,4,5,6,7,8]

	# start:stop:step
	odd = myList[::2]
	even = myList[1::2]
	odds_in_first_four = myList[:4:2]
```


# Func

```python
	def greet():
	    print("Hello!")
```


# Func

```python
	def greet(name):
	    print(f"Hello, {name}!")
```


# Func

```python
	def greet(name, surname=None):
	    print(f"Hello {name} {surname or ''}")
```


# Func

```python
	def greet(*args):
	    print(f"Hello {','.join(args)")

	greet('Huey', 'Dewey', 'Louie')
```


# Func

```python
	def greet(**kvargs):
	    for key, val in kvargs.items():
	        print(f"Hello {key}, with color = {value}!")

	greet({'Huey': 'red', 'Dewey': 'blue', 'Louie': 'green'})
 
```


# Func

```python
	def greet(*args):
	    for name in args:
	        yield (f"Hello {name}!")

	for greeting in greet('Tom', 'Alice', 'Bob'):
	    print(greeting)
 
```


# Func

```python
	functions_are_objects = greet

	functions_are_objects()
```


# Class
```python
	class Greeter():
	      def __init__(self, name):
		  self.name = name

	      def greet(self):
		  print(f"Hello from {self.name}")
```


# Exceptions
```python
	try:
	    a_number = int("5")
	except ValueError as e:
	    print(f"Woops! {e.msg}")
	except Exception:
	    print("How did we get here?")
	finally:
	    print("Always leave with a smile :)")
```



# Exceptions

Empty raise raises original exception!
Never re-raise exception!

```python
	def add_small(x, y):
	    if x > 10 or y > 10:
               raise ValueError("Value too big!")
	    try:
               return x + y
	    except Exception:
               raise  
```


# I O

```python
	name = input("What's your name?")
	print(f"Hello, {name}")

	with open('myfile.txt', mode='r') as myfile:
	     text = myfile.read()

	with open('myfile2.txt', mode='w+') as myfile:
	     myfile.write(text)
```


# I O

```python
	import requests

	response = request.get('http://leethack.party/somepath')
	if response:
	   a_dict = response.json()
```


# I O

```python
	import requests

	myAnswer = "a b c"
	request.post('http://leethack.party/somepath', 
		      headers={'content-type': 'plain/text'},
		      data=myAnswer)

```


# HelloWorld

```python
	import socket
	def hello(person):
	    hostname = socket.gethostname()
	    print(f"Hello {person}, from {hostname}.")

	if __name__ == "__main__":
	    hello("world")
```


# Modules

```python
	-- app.py
	-- mymodule.py

	#app.py
	import mymodule

	mymodule.func()
```


# Modules
```python
	-- app.py
	-- mypackage/
	-------__init__.py
	-------mymodule.py

	#app.py
	from mypackage import mymodule

	mymodule.func()
```
