#!/bin/bash

# set LOCAL to 0 to run the installed version of the GUI
LOCAL=1

PYTHON_INTERPRETER=python

if [ ${LOCAL} = 1 ]; then
	echo "Running the local version"
	(export PYTHONPATH="."; ${PYTHON_INTERPRETER} startGui.py)
else
	echo "Running the installed version"
	echo "Not implemented"
# 	(cd examples && ${PYTHON_INTERPRETER} LoadGUI.py)
fi
