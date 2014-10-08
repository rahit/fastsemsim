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

# LOCAL=1

PYTHON_INTERPRETER=python

# if [ ${LOCAL} = 1 ]; then
if [ -f startGui2.py ]; then
	echo "Running the local version"
	(export PYTHONPATH="."; ${PYTHON_INTERPRETER} startGui2.py)
else
# 	echo "Running the installed version"
	${PYTHON_INTERPRETER} -c "from fastSemSimGui2 import startGui; startGui.go()" "$@"
fi
