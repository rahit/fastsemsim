#!/bin/bash

# '''
# Copyright 2011 Marco Mina. All rights reserved.
# 
# This file is part of fastSemSim
# 
# fastSemSim is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# fastSemSim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with fastSemSim.  If not, see <http://www.gnu.org/licenses/>.
# '''

PYTHON_INTERPRETER=python

python setup.py install
cp -i -v fastSemSim.sh /usr/bin/fastSemSim
cp -i -v fastSemSimGui.sh /usr/bin/fastSemSimGui