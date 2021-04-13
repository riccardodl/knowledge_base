Beyond the basic stuff in python
TODO:
p.325
https://docs.python.org/3/tutorial/modules.html
https://www.youtube.com/watch?v=o9pEzgHorH0

form pathlib import Path
Path('spam') / 'bacon' / 'eggs'
Path.cwd()

python3 -c 'help(len)'

import logginglogging.basicConfig(filename='log_filename.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')logging.debug('This is a log message.'

fstring=f'Hello, {name}. Today is {day} and it is {weather}{{escapedstring}}'.

if 42 < spam < 99:

>>> print('cat', 'dog', 'moose', sep='-')cat-dog-moose
>>> kwargsForPrint = {'sep': '-'}
>>> print('cat', 'dog', 'moose', **kwargsForPrint)
cat-dog-moose

Optional static typing:
def describeNumber(number: int) -> str:
--implementation--

class Smart:
def __init__(self, characters):
    self._characters = characters
@classmethod
def fromFile(cls, filename):
    with open(filename) as fileObj:
        characters = fileObj.read()
        return cls(characters) # It also works with inheritance!

int(3).__class__.__qualname__

>>> import wizcoin
>>> purse = wizcoin.WizCoin(2, 5, 10)
>>> repr(purse) # Calls WizCoin's __repr__() behind the scenes.
'WizCoin(2, 5, 10)'
>>> str(purse) # Calls WizCoin's __str__() behind the scenes.
'2g, 5s, 10k'
>>> print(f'My purse contains {purse}.') # Calls WizCoin's __str__().
My purse contains 2g, 5s, 10k.

* use enumarate() instead of range(len()).
* use with statement isntead of open() and close().
* use is None instead of == None for null checks.
* define raw strings instead of escaping characters.
* both [:] and copy.copy() create shallow copies.
* get('key',<default>), setdefault() in dict.
* List concatenation creates a new list.
* Tuple is immutable, dict and list are mutable.
* dunder or magic methods `__init__` is for operator overload.
* A package is a collection of modules that you form by placing a file named `__init__.py` inside a folder.
* Callable operator: def hello() (is not called a "global function").
* Functions are first class objects (can be assigned, returned, etc.)
* iteratorObj1 = iter(iterableObj); next(iteratorObj1)
* Don't modify list while iterating over it, make a new one and then oldList.extend(newList) or newList.append(elementNotToDelete). List comprehension could also be good.
* Don’t copy mutable values without copy.copy() and copy.deepcopy()
* MyPy for static analysis.
* The presence of self as the first parameter is the quickest way
you can distinguish methods from functions.
* If your method’s code never needs to use the self parameter, it’s a sign that your method should probably just be a function.
* Prefer the isinstance(<Class>) method, it works with inheritance.
* Classmethods as alternative constructor are smart.
* Getter and setters are done with decorators: `@property, @someAttribute.setter, @someAttribute.deleter`.
* Python calls the getter setter methods for you when referencing the variable. This is called the backing variable or backing field.
* You make an attribute read-only by defining the getter (with the decorator) and omitting the setter (you get AttributeError).
* User normal getter/setters when you need to pass variables to the function or with long operations or when you also modify other attributes or objects.
* You can define dunder methods for the curresponding built-in functions (`__len__() or __repr__()`).
* If repr() doesn’t know how to create a repr or str string for an object, the string will be enclosed in angle brackets and contain the object’s memory address and class name.
* Numeric dunder methods: add, sub, mul, pow, truediv etc. There are reverse as well as in-place numeric dunder methods.
* In place dunder methods will return self. This is true for all the mutable objects. SHould return a new for immutables.
* There are also comparative dunder methods eq,ne,gt,lt,le,ge.
* 
* 
* 
* 
* 
* 
* 
* 
* 
