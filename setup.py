#!/usr/bin/env python3

from setuptools import setup, find_packages

from codecs import open
from os import path
import glob

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

data_files = [('', ['scribe/ui.glade', 'scribe/templates.ui'])]
# directories = glob.glob('templates/*/*/')
# for directory in directories:
#     files = glob.glob(directory + '*')
#     data_files.append((directory, files))

setup(
    name = 'scribe',
    version = '0.0.1',

    description = 'An app that will do a thing',
    long_description = long_description,

    url = 'https://github.com/espectalll/scribe',

    author = '@espectalll',
    author_email = 'espectalll@kydara.com',

    license = 'GPL',

    classifiers = [
        'Development Status :: 3 - Alpha',

        'Intended Audience :: End Users/Desktops',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords = 'scribe web cms static',

    packages = find_packages(exclude=['templates']),
    package_dir = {'scribe': 'scribe'},
    include_package_data = True,

    install_requires=['pygobject', 'pygi-composite-templates'],

    data_files = data_files,

    entry_points={
        'console_scripts': [
            'scribe=scribe:main',
        ],
    },
)
