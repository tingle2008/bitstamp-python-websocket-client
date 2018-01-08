from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


class Tox(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


setup(
    name='BitstampClient-websocket',
    version='2.2.3',
    description='Bitstamp API python implementation websocket only',
    packages=['bitstamp'],
    url='https://github.com/tingle2008/bitstamp-python-websocket-client',
    license='MIT',
    author='tingle2008',
    author_email='tingle2008@gmail.com',
    install_requires=['requests'],
    tests_require=['tox'],
    cmdclass={'test': Tox},
)
