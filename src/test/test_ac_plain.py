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
This is an example program.
It loads a Gene Ontology, and then loads an annotation corpus (in GOA GAF-2 format) filtering IEA annotations.
It provides some hints on how using the filtering features implemented in FastSemSim.
"""

from fastSemSim.GO import AnnotationCorpus
from fastSemSim.GO import GeneOntology
import sys

if __name__ == "__main__":
	#### load ontology
	tree = GeneOntology.load_GO_XML(open('../../examples/GO_2011-09-16.obo-xml'))
	print "Ontology infos: file name: " + str('../../examples/GO_2011-09-16.obo-xml') + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())

	#### load annotations
	gp = AnnotationCorpus.AnnotationCorpus(tree)
	
	params = {}
	params['multiple'] = False # Set to troue if there are many associations per line (the object in the first field is associated to all the objects in the other fields within the same line)
	params['term first'] = True # set to True if the first field of each row is a GO term. Set to False if the first field represents a protein/gene
	params['separator'] = '\t' # select the separtor used to divide fields
	gp.parse('../../examples/test_plain_ac.txt','plain', params)
	
	print "Annotated proteins: " + str(len(gp.annotations))
	print "Annotated terms: " + str(len(gp.reverse_annotations))

	print "Annotation corpus consistent with current GO: " + str(gp.isConsistent())
