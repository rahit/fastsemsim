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

from fastsemsim.Ontology import ontologies
from fastsemsim.Ontology import AnnotationCorpus
from fastsemsim import data

import sys
import os
import math
import gzip

def load_ontology(i,j):
	ontology = ontologies.load(i[0], i[1], i[2], j)
	return ontology
#

def load_ac(ontology,j,k):
	ac = AnnotationCorpus.AnnotationCorpus(ontology)
	builtin_dataset = data.dataset.Dataset()
	# print ontology.name
	# print j
	selected_source = builtin_dataset.get_default_annotation_corpus(ontology.name, j)
	if selected_source is None:
		return None
	source = selected_source['file']
	source_type = selected_source['filetype']
	# print source_type
	# print source
	ac.parse(source, source_type, k)
	ac.isConsistent()
	return ac
#

def test_AC():

	input_ac_set = [ 
		(None, None, 'DiseaseOntology', ('human',)),
		(None, None, 'GeneOntology', ('arabidopsis', 'fly', 'human', 'mouse', 'rat', 'worm', 'zebrafish')),
		]

	ontology_parameters_set = [
		# {'ignore':{}},
		# {'ignore':{'has_part':True, 'occurs_in':True, 'happens_during':True}},
		{},
		# {'ignore':{'regulates':True, 'has_part':True, 'negatively_regulates':True, 'positively_regulates':True, 'occurs_in':True, 'happens_during':True}},
		]

	ac_parameters_set = [
		# {'ignore':{}},
		# {'ignore':{'has_part':True, 'occurs_in':True, 'happens_during':True}},
		{},
		# {'ignore':{'regulates':True, 'has_part':True, 'negatively_regulates':True, 'positively_regulates':True, 'occurs_in':True, 'happens_during':True}},
		]

	print "\n#################################"
	print "\n# Testing annotation corpus parsing... #\n"
	print "#################################\n"

	acs = []
	for i in input_ac_set:
		print("\n---------------------------------------------\n")
		tempac = []
		ontology = load_ontology(i,{})
		for j in i[3]:
			for k in ac_parameters_set:
				print("Loading ac: " + str(i)+'\nParameters: ' + str(j))
				tempk = k
				# tempj = j.copy()
				tempac.append((i, j, tempk, ontology, load_ac(ontology, j, k)))
				# print j
				# print "-> Ontology loaded: " + str(ontology.node_number()) + " nodes and " +  str(ontology.edge_number()) + " edges."
				print("----------------")
		acs.append(tempac)

	print "\n#############################################################"
	print "\n# Successfully loaded " + str(len(acs)) + " ontologies"
	print "#############################################################\n"

	for j in acs:
		print("\n---------------------------------------------\n")
		for i in j:
			print str(i)
			if not i[4] is None:
				print "-> " + str(len(i[4].reverse_annotations)) + " reverse_annotations, " +  str(len(i[4].annotations)) + " annotations."
			else:
				print "-> None!"
			print("--------------------")
	#

if __name__ == "__main__":
	test_AC()
#




	
	# #-#-#-#-#-#-#-#-#-#-#-#-#-#
	# # Second step: set parsing parameters
	# # You should fill a dictionary with the proper information. Friendly routines will be provided in future to set parsing parameters easily
	# # If you specify incorrect or not pertinent parameters they'll be ignored.
	
	# #### For gaf-2 / GOA files:
	# if not is_plain:
	# 	params = {}
	
	# 	params['filter'] = {} # filter section is useful to remove undesired annotations

	# 	if not EC_include == None:
	# 		params['filter']['EC'] = {} # EC filtering: select annotations depending on their EC
	# 		params['filter']['EC']['EC'] = EC_include # select which EC accept or reject
	# 		params['filter']['EC']['inclusive'] = True # select which EC accept or reject
	# 	if not EC_ignore == None:
	# 		params['filter']['EC'] = {} # EC filtering: select annotations depending on their EC
	# 		params['filter']['EC']['EC'] = EC_ignore # select which EC accept or reject
	# 		params['filter']['EC']['inclusive'] = False # select which EC accept or reject

	# 	if not tax_include == None:
	# 		params['filter']['taxonomy'] = {}
	# 		params['filter']['taxonomy']['taxonomy'] = tax_include # set properly this field to load only annotations involving proteins/genes of a specific species
	# 		params['filter']['taxonomy']['inclusive'] = True # select which EC accept or reject
	# 	if not tax_ignore == None:
	# 		params['filter']['taxonomy'] = {}
	# 		params['filter']['taxonomy']['taxonomy'] = tax_ignore
	# 		params['filter']['taxonomy']['inclusive'] = False # select which EC accept or reject
		
	# 	params['simplify'] = True # after parsing and filtering, removes additional information such as taxonomy or EC. Useful if you have a huge amount of annotations and not enough memory
	
	# #### For plain files:
	# if is_plain:
	# 	params = {}

	# 	if ac_multiple:
	# 		params['multiple'] = True # Set to True if there are many associations per line (the object in the first field is associated to all the objects in the other fields within the same line)
	# 	if ac_term_first:
	# 		params['term first'] = True # set to True if the first field of each row is a GO term. Set to False if the first field represents a protein/gene
		
	# 	if not ac_separator == None:
	# 		params['separator'] = ac_separator # select the separtor used to divide fields
	

	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	#### additional useful annotation corpus routines
	# ac.isConsistent() # check whether the annotations are consistent with the current gene ontology. Useful to check if everything is fine
	# ac.sanitize() # removes annotations not consistent with the current gene ontology. USeful if you loaded an annotation corpus BEFORE loading a gene ontology
	# return ac
#