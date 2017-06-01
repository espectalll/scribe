#!/usr/bin/env python3

from setuptools import setup, find_packages

from codecs import open
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

data_files = [('', ['scribe/ui.glade', 'scribe/templates.ui'])]
data_paths = []

for (path, directories, filenames) in os.walk('scribe/templates'):
    for filename in filenames:
        data_paths.append(os.path.join('..', path, filename))

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
    package_data={'': data_paths},
    include_package_data = True,

    install_requires=['pygobject', 'pygi-composite-templates'],

    data_files = data_files,

    entry_points={
        'console_scripts': [
            'scribe=scribe:main',
        ],
    },
)
