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

from fastsemsim.ontology import ontologies

import sys
import os
import math
import gzip

def load_ontology(i,j):
	ontology = ontologies.load(i[0], i[1], i[2], j)
	return ontology
#


def test_Os():

	input_ontologies_set = [ 
		(None, None, 'CellOntology'),
		(None, None, 'DiseaseOntology'),
		(None, None, 'GeneOntology'),
		('../data/Os/CellOntology_2014.10.13.obo', 'obo', 'CellOntology'),
		('../data/Os/DiseaseOntology_2014.10.13.obo', 'obo', 'DiseaseOntology'),
		('../data/Os/GeneOntology_2014.10.13.obo-xml.gz', 'obo-xml', 'GeneOntology'),
		('../data/Os/GeneOntology_2014.10.27.obo', 'obo', 'GeneOntology'),
		]

	parameters_set = [
		{'ignore':{}},
		{'ignore':{'has_part':True, 'occurs_in':True, 'happens_during':True}},
		{},
		{'ignore':{'regulates':True, 'has_part':True, 'negatively_regulates':True, 'positively_regulates':True, 'occurs_in':True, 'happens_during':True}},
		]

	print "\n#################################"
	print "\n# Testing ontologies parsing... #\n"
	print "#################################\n"

	ontology = []
	for i in input_ontologies_set:
		print("\n---------------------------------------------\n")
		tempontology = []
		for j in parameters_set:
			print("Loading ontology: " + str(i)+'\nParameters: ' + str(j))
			tempj = j.copy()
			tempontology.append((i,tempj,load_ontology(i,j)))
			# print j
			# print "-> Ontology loaded: " + str(ontology.node_number()) + " nodes and " +  str(ontology.edge_number()) + " edges."
			print("----------------")
		ontology.append(tempontology)

	print "\n#############################################################"
	print "\n# Successfully loaded " + str(len(ontology)) + " ontologies"
	print "#############################################################\n"

	for j in ontology:
		print("\n---------------------------------------------\n")
		for i in j:
			print str(i[0]) + str(i[1])
			if not i[2] is None:
				print "-> " + str(i[2].node_number()) + " nodes, " +  str(i[2].edge_number()) + " edges."
			else:
				print "-> None!"
			print("--------------------")
	#

if __name__ == "__main__":
	test_Os()
#
