# -*- coding: iso-8859-1 -*-
'''
Copyright 2011 Marco Mina. All rights reserved.

This file is part of fastSemSim

fastSemSim is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

fastSemSim is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with fastSemSim.  If not, see <http://www.gnu.org/licenses/>.
'''

from distutils.core import setup
import os

#################################################
import py2exe
setup(
    options = {
        "py2exe": {
            "dll_excludes" : ["MSVCP90.dll"]
        }
    },
    windows =['gui\\fastSemSimGui.py'])

#################################################


## Package path
pkg_path = os.path.dirname(__file__)

## Package description
README = os.path.join(pkg_path, 'README')
lines = open(README).readlines()
description = ''.join(lines[:1])
long_description = ''.join(lines[:2])

## Package Version
version = 0.4.4

setup(
    name='fastSemSim',
    version=version,
    url='https://sourceforge.net/p/fastsemsim/home/Home/',
    description=description,
    long_description=long_description,
    keywords='semantic similarity, GO, Gene Ontology, GOA,',
    author='Marco Mina',
    author_email='marco.mina.85@gmail.com',
    license='GNU GPL version 3',
    download_url = 'https://sourceforge.net/projects/fastsemsim/files/',
    classifiers=[
        'Development Status :: 3 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
    ],

    packages=['fastSemSim'],
    #package_data={'dir': ['data.?']},
    #requires=['wx (>=2.8)']
)