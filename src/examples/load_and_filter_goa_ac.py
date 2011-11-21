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
from fastSemSim.SemSim import ResnikSemSim
import sys

if __name__ == "__main__":
	#### load ontology
	tree = GeneOntology.load_GO_XML(open('../../GO/GO_2011-09-16.obo-xml'))
	print "Ontology infos: file name: " + str('GO_2011-09-16.obo-xml') + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())

	#### load annotations
	gp = AnnotationCorpus.AnnotationCorpus(tree)
	
	params = {}
	params['filter'] = {}
	params['filter']['EC'] = 'IEA'
	params['filter']['taxonomy'] = 9606
	gp.parse('gene_association.goa_fly','GOA', params)
	
	print "Annotated proteins (IEA filtering): " + str(len(gp.annotations))
	print "Annotated terms (IEA filtering): " + str(len(gp.reverse_annotations))

	params = {}
	gp.parse('../../GOA/gene_association.goa_human','GOA', params)
	
	print "Annotation corpus consistent with current GO: " + str(gp.check_consistency())
	
	print "Annotated proteins (no filtering): " + str(len(gp.annotations))
	print "Annotated terms (no filtering): " + str(len(gp.reverse_annotations))
	
	# check if everything is ok...
	print "Annotation corpus consistent with current GO: " + str(gp.check_consistency())
