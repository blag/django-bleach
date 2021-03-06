#!/usr/bin/env python
from os import path
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as test_command


class Tox(test_command):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        test_command.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        test_command.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst')) as f:
    long_description = f.read()


setup(
    name='django-bleach',
    version="0.4.1",
    description='Easily use bleach with Django models and templates',
    long_description=long_description,
    author='Mark Walker',
    author_email='theshow@gmail.com',
    url='https://github.com/marksweb/django-bleach',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'bleach',
        'Django>=1.8',
    ],
    tests_require=[
        'bleach',
        'tox'
    ],
    cmdclass={'test': Tox},
    package_data={},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
    ],
)
