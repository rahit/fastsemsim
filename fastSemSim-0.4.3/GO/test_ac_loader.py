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

from GO import AnnotationCorpus
from GO import GeneOntology
#from SemSim import ObjSemSim
#from SemSim import SemSimUtils
import sys
import os


if __name__ == "__main__":
	#### load ontology
	tree = GeneOntology.load_GO_XML(open(sys.argv[1]))
	print "Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())


	#### load annotations
	gp = AnnotationCorpus.AnnotationCorpus(tree)
	parameters = {'simplify':True}
	
	gp.parse(sys.argv[2], 'GOA', parameters)
	
	#gp.check_consistency()
	print "Annotated proteins: " + str(len(gp.annotations))
	print "Annotated terms: " + str(len(gp.reverse_annotations))
	
	# check if everything is ok...
	gp.check_consistency()
	gp.sanitize()
