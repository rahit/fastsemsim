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

## Package path
pkg_path = os.path.dirname(__file__)

## Package description
README = os.path.join(pkg_path, 'README')
lines = open(README).readlines()
description = ''.join(lines[:3])
long_description = ''.join(lines[:4])

## Package Version
vh = open('version','r')
lines = vh.readlines()
version = lines[0].rstrip('\n').rstrip('\r')
vh.close()

setup(
    name='fastSemSim',
    version=version,
    url='https://sourceforge.net/p/fastsemsim/home/Home/',
    description=description,
    long_description=long_description,
    keywords='semantic similarity, Ontology, Gene Ontology',
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

    package_dir={'fastSemSim':'fastSemSim'},
    package_data={'fastSemSim.data':['*']},
    packages=['fastSemSim', 'fastSemSim.data', 'fastSemSim.Ontology', 'fastSemSim.SemSim', 'fastSemSim.fastResnik'],
    # packages=['fastSemSim', 'fastSemSim.data', 'fastSemSim.GO', 'fastSemSim.SemSim', 'fastSemSim.fastResnik'],
)
