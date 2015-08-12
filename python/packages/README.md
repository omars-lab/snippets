# General Python Packages Notes

<pre>
root/
    |— __init__.py
    |— rProg.py
    |— inner/
        |— __init__.py
        |— iProg.py
        |— leaf/
            |— __init__.py
            |— lProg.py
</pre>

What we can import:
```
from root import rProg
from root.inner import iProg
from root.inter.leaf import lProg
```

Running `from root import *` will trigger the following:
* The __all__ variable in root/__init__.py is accessed, and all modules reference within it are imported.

Notes:
* When we import, we are import modules (files). Modules have variables and functions.
* Sub modules can reference sibling modules with `.` and parent modules with `..`
* when running a python program by either passing it to the python interpretter
or by making the file an executable, __name__ is set to __main__
* When importing a module, the module's __name__ variable is set to the module name


# Packaging Tools
While referencing modules by siblings by parents and siblings is powerful, there
is a more powerful packaging mechanism. By making our project a package, we
can reference modules by their package path. In the above example, we would
be able to reference iProg by root.inner.iProg anywhere in the project, not needing
to know siblings or parents.

To do this, we can use setuptools to make our life easier.
The framework of a package involves setup.py, setup.cfg, requirements.txt, and README.md

The setup.py and setup.cfg will point to the areas of the code that need to be
packaged. They will also include package specific details. Requirements.txt provides the
package requirements of this project. A simple `pip install -r requirements.txt`
will itterate through all the project requirements and install them, but it is
not needed when installing the setup.py file directly. Its just a nice thing to know.

To install a package, go to the directory of the setup.py file
and simply run `python setup.py install` or `pip install .`

Note to self: look into what setuptools does.
Note to self: look into bdist_wheel and eggs
