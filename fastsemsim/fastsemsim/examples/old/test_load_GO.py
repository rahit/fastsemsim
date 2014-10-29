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
It loads a Gene Ontology.
"""

from fastSemSim.GO import GeneOntology
import sys

if __name__ == "__main__":

	ontologies = ['data/GO_filtered_2013.07.26.obo-xml.gz', 'data/GO_filtered_2013.07.26.obo.gz', 'data/GO_full_2013.07.26.obo.gz']

	#### load ontology
	for i in range(0, len(ontologies)):
		tree = GeneOntology.load_GO_XML(ontologies[i])
		print "Ontology infos: file name: " + str(ontologies[i]) + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())


	#### checking results
	total_id = 18769
	total_term = 3259
	
	error = False
	if not total_id == current_id:
		print "Count check error! Objects number should be " + str(total_id) + " instead of " + str(current_id)
		error = True
	if not total_term == current_term:
		print "Count check error! Terms number should be " + str(total_term) + " instead of " + str(current_term)
		error = True
	
	if error:
		print "Check failed!"
	else:
		print "All checks passed!"
#



def load_go(go_file):
	GO_ignore = {}
	GO_ignore['has_part'] = True
	GO_ignore['is_a'] = False
	GO_ignore['regulates'] = False
	GO_ignore['part_of'] = False
	if ignore_regulates:
		GO_ignore['regulates'] = True
	if not ignore_has_part:
		GO_ignore['has_part'] = False
	if ignore_is_a:
		GO_ignore['is_a'] = True
	if ignore_part_of:
		GO_ignore['part_of'] = True

	print "Loading Gene Ontology from " + str(go_file) + "..."
	fn,fe = os.path.splitext(go_file)
	if fe == '.gz':
		go_handle = gzip.open(go_file, 'rb')
	else:
		go_handle = open(go_file, 'r')
	go = GeneOntology.load(go_handle, {'ignore':GO_ignore})
	go_handle.close()
	print "-> Ontology correctly loaded: " + str(go.node_num()) + " nodes and " +  str(go.edge_num()) + " edges."
	return go
#
