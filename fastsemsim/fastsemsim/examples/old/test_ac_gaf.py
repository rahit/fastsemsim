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
This is a test routine
It loads a Gene Ontology, and then loads an annotation corpus (in GOA GAF-2 format) filtering IEA annotations.
Data statistics are expected to comply with those manually evaluated
"""

from fastSemSim.GO import AnnotationCorpus
from fastSemSim.GO import GeneOntology
import sys

if __name__ == "__main__":

	ontology = 'GO_2011-09-16.obo-xml.gz'
	ac_file = 'gene_association.goa_fly'

	#### load ontology
	tree = GeneOntology.load_GO_XML(ontology)
	print "Ontology infos: file name: " + str(ontology) + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())

	#### load annotations - filtering
	gp = AnnotationCorpus.AnnotationCorpus(tree)
	
	params = {}
	params['filter'] = {}	
	params['filter']['EC'] = {}
	params['filter']['EC']['EC'] = 'IEA'
	params['filter']['taxonomy'] = '7227'
	params['simplify'] = True
	
	gp.parse(ac_file,'GOA', params)
	
	print "Annotated proteins (IEA filtering): " + str(len(gp.annotations))
	print "Annotated terms (IEA filtering): " + str(len(gp.reverse_annotations))
	print "Annotation corpus consistent with current GO: " + str(gp.isConsistent())
	gp.sanitize()
	
	current_id_noIEA = len(gp.annotations)
	current_term_noIEA = len(gp.reverse_annotations)

	#### load annotations - all
	
	gp.reset()
	params = {}
	gp.parse(ac_file,'GOA', params)

	print "Annotated proteins (no filtering): " + str(len(gp.annotations))
	print "Annotated terms (no filtering): " + str(len(gp.reverse_annotations))
	print "Annotation corpus consistent with current GO: " + str(gp.isConsistent())
	gp.sanitize()
		
	current_id = len(gp.annotations)
	current_term = len(gp.reverse_annotations)
	
	#### checking results
	total_id = 12370
	total_term = 5319
	total_id_noIEA = 6304
	total_term_noIEA = 4367
	
	error = False
	if not total_id == current_id:
		print "Count check error! Objects number should be " + str(total_id) + " instead of " + str(current_id)
		error = True
	if not total_id_noIEA == current_id_noIEA:
		print "Count check error! Objects number [no IEA] should be " + str(total_id_noIEA) + " instead of " + str(current_id_noIEA)
		error = True
	if not total_term == current_term:
		print "Count check error! Terms number should be " + str(total_term) + " instead of " + str(current_term)
		error = True
	if not total_term_noIEA == current_term_noIEA:
		print "Count check error! Terms number [no IEA] should be " + str(total_term_noIEA) + " instead of " + str(current_term_noIEA)
		error = True
	
	if error:
		print "Check failed!"
	else:
		print "All checks passed!"
