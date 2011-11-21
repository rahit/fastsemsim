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
It loads a Gene Ontology, an annotation corpus (in GOA GAF-2 format) and evaluate Resnik Sem Sim between all the pairs of GO Terms from BP ontology present in the annotation corpus.
"""

from fastSemSim.GO import AnnotationCorpus
from fastSemSim.GO import GeneOntology
from fastSemSim.SemSim import ResnikSemSim
import sys

if __name__ == "__main__":
	#### load ontology
	tree = GeneOntology.load_GO_XML(open('GO_2011-09-16.obo-xml'))
	print "Ontology infos: file name: " + str('GO_2011-09-16.obo-xml') + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())

	#### load annotations
	gp = AnnotationCorpus.AnnotationCorpus(tree)
	gp.parse('gene_association.goa_fly','GOA')
	#gp.parse('gene_association.goa_yeast','GOA')
	
	print "Annotated proteins: " + str(len(gp.annotations))
	print "Annotated terms: " + str(len(gp.reverse_annotations))
	
	# check if everything is ok...
	gp.check_consistency()
	gp.sanitize()
	
	# create a TermSemSim object.
	TSS = ResnikSemSim.ResnikSemSim(gp, tree)
	TSS.format_and_check_data = False # if GO terms are passed as integers and are correct, this speeds up computation
	test_set = TSS.util.intersection(gp.reverse_annotations.keys(), TSS.util.offspring[tree.BP_root]).keys()

	print "query nodes: " + str(len(test_set))
	#print test_set

	# determine pairwise semantic similarity and print it on console.
	for i in range(len(test_set)):
		for j in range(i+1, len(test_set)):
			mat = TSS.SemSim(test_set[i], test_set[j])
			print str(test_set[i]) + "\t" + str(test_set[j]) + "\t" + str(mat)
	print("-----------------------------------------------------------------")
 