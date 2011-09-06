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

import sys
from GO import GeneOntology
from GO import AnnotationCorpus
from SemSim import SemSimMeasures
from SemSim import ObjSemSim
from gui import WorkProcess
import multiprocessing

if __name__ == "__main__":
	gui2ssprocess_queue = multiprocessing.Queue()
	ssprocess2gui_queue = multiprocessing.Queue()
	in_pipe, out_pipe = multiprocessing.Pipe()
	ssprocess = WorkProcess.WorkProcess(gui2ssprocess_queue, ssprocess2gui_queue, in_pipe, out_pipe)
	ssprocess.start()
	gui2ssprocess_queue.put('reset')
	gui2ssprocess_queue.put('init')
	out_pipe.send(('../../GO/GO_2011-06-06.obo-xml','prova'))
	gui2ssprocess_queue.put('go')
	
	ssprocess.join()