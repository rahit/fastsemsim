#!/bin/bash

# set LOCAL to 0 to run the installed version of the GUI
LOCAL=1

PYTHON_INTERPRETER=python

if [ -f startfastSemSim.py ]; then
# if [ ${LOCAL} = 1 ]; then
	echo "Running the local version"
	(export PYTHONPATH="."; ${PYTHON_INTERPRETER} startfastSemSim.py "$@")
else
# 	echo "Running the installed version"
	${PYTHON_INTERPRETER} -c "from fastSemSim import startfastSemSim; startfastSemSim.start()" "$@"
fi
