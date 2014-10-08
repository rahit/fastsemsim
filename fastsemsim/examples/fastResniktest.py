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

"""
This test file runs the fast implementation of Resnik max provided by FastSemSim
"""

from fastSemSim.GO import AnnotationCorpus
from fastSemSim.GO import GeneOntology
from fastSemSim.fastResnik import fastResnikSemSim
import sys


if __name__ == "__main__":
	if len(sys.argv) == 1:
		print "Please select the ontology category to use."
		print "Usage: python fastResnik.py [GO category]"
		print "[GO category] could be \"MF\", \"BP\" or \"CC\"."
		sys.exit()

	ontology = str(sys.argv[1])
	outfile1 = open('fastResnik_output.txt', 'w')
	
	print "Output data will be written in file fastResnik_output.txt"
	
	#### load ontology
	tree = GeneOntology.load_GO_XML(open('GO_2011-09-16.obo-xml'))
	print "Ontology infos: file name: " + str('GO_2011-09-16.obo-xml') + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())

	#### load annotations
	gp = AnnotationCorpus.AnnotationCorpus(tree)
	gp.parse('gene_association.goa_fly', 'GOA')
	#gp.parse('gene_association.goa_yeast', 'GOA')
	#gp.parse('test_plain_ac.txt', 'plain')

	print("Annotated proteins: " + str(len(gp.annotations)))
	print("Annotated terms: " + str(len(gp.reverse_annotations)))
	print("Check annotation corpus consistency... " + str(gp.check_consistency()))

	SS = fastResnikSemSim.fastResnikSemSim(gp, tree)

	
	print ontology
	
	SS.SemSim(ontology, outfile1)
	outfile1.close()

	print "Output data has been written in file fastResnik_output.txt"
	sys.exit(0)
