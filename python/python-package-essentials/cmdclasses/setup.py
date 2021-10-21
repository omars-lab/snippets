from setuptools import setup, find_packages

# https://dankeder.com/posts/adding-custom-commands-to-setup-py/

from setuptools import Command

class HelloWorldCommand(Command):

    description = 'Welcome someone through setup.py'
    user_options = [
            ('to-welcome=', 'w', 'name of entity to welcome.')
        ]

    def run(self):
        print(f"Hello, {self.to_welcome}")

    def initialize_options(self):
        self.to_welcome = None

    def finalize_options(self):
        pass

setup(
    name="foo",
    version="1.0",
    packages=find_packages(),
    cmdclass={
      "hello": HelloWorldCommand
    }
)
