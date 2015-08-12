What happends when classes are createsd:

Consdier this base class:
```
class Spam(Base):
    def __init__(self, name):
        self.name = name
    def bar(self):
        print "I am Spam.bar"
```

1. Isolate the body of the class: (Python runs the class body)
```
def __init__(self, name):
    self.name = name
def bar(self):
    print "I am Spam.bar"
```

2. Create namespace for the class (usually a dict) (from class and bases). Invoked
with:
``` clsdict = type.__prepare__('Spam', (Base,))) ```

3. Afterwards, using globals, populate the class dict with the body:
```exec(body, globals(), clsdict)```

4. Finally, create the type:
```type('Spam', Base, clsdict)```


insepct.signature(Class)
