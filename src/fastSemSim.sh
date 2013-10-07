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

# set LOCAL to 0 to run the installed version of the GUI
# LOCAL=1

PYTHON_INTERPRETER=python
DIR_CODE=`dirname $0`

if [ -f ${DIR_CODE}/startfastSemSim.py ]; then
# if [ ${LOCAL} = 1 ]; then
	# echo "Running the local version"
	(export PYTHONPATH=${PYTHONPATH}:${DIR_CODE}; ${PYTHON_INTERPRETER} ${DIR_CODE}/startfastSemSim.py "$@")
else
# 	echo "Running the installed version"
	${PYTHON_INTERPRETER} -c "from fastSemSim import startfastSemSim; startfastSemSim.start()" "$@"
fi
