Basis for metaclasses



A class decloration creates a type.
    The __new__ method is invoked when creating a new class
    The type of the class is type


The type of an instance of a class is the class itself:

```
class A(object):
    pass

type(A)
>>> <type 'type'>
isinstance(A, type)
>>> True

apple = A()

type(apple)
>>> <class 'A'>
isinstance(apple, A)
>>> True
```


Type itself is a class that is used to create other types (aka classes)
Type is invoked everytime we instanstuate a new object from the class from the
__new__ method.




