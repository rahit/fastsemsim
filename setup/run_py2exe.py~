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
import py2exe

Mydata_files = [('images', ['fastSemSimGui/V_30.png', 'fastSemSimGui/W_30.png', 'fastSemSimGui/advanced.png']),
								('data', ['fastSemSim/data/GO_2012-02-24.obo-xml',])]


setup(
    data_files = Mydata_files,
    options = {
        "py2exe": {
            "dll_excludes" : ["MSVCP90.dll"],
            "unbuffered": True,
            "optimize": 2
        }
    },
    windows =['startGui.py'],
    console =['startfastSemSim.py']
    )
