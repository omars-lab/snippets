try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': '',
#    'description': '',
    'version': '0.1',
    'packages': [''],
#    'install_requires': ['nose'],
    'scripts': [],
    'author': 'Omar Eid',
    'author_email': 'omar.uuid@gmail.com',
    'url': 'https://www.github.com/mr-uuid',
}

setup(**config)
