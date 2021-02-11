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
from fastsemsim.ontology import AnnotationCorpus
from fastsemsim import data

import sys
import os
import math
import gzip

def load_ontology(i,j):
	# print "LOAD ONTOLOGY" + str(i)
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

	basic_ac_parameters = {}
# gaf-2.0 ac
	basic_ac_parameters['filter'] = {} # filter section is useful to remove undesired annotations
	basic_ac_parameters['filter']['EC'] = {} # EC filtering: select annotations depending on their EC
	basic_ac_parameters['filter']['taxonomy'] = {}
	# basic_ac_parameters['filter']['EC']['EC'] = EC_include # select which EC accept or reject
	# basic_ac_parameters['filter']['EC']['inclusive'] = True # select which EC accept or reject
	# basic_ac_parameters['filter']['EC'] = {} # EC filtering: select annotations depending on their EC
	# basic_ac_parameters['filter']['EC']['EC'] = EC_ignore # select which EC accept or reject
	# basic_ac_parameters['filter']['EC']['inclusive'] = False # select which EC accept or reject
	# basic_ac_parameters['filter']['taxonomy']['taxonomy'] = tax_include # set properly this field to load only annotations involving proteins/genes of a specific species
	# basic_ac_parameters['filter']['taxonomy']['inclusive'] = True # select which EC accept or reject
	# basic_ac_parameters['filter']['taxonomy'] = {}
	# basic_ac_parameters['filter']['taxonomy']['taxonomy'] = tax_ignore
	# basic_ac_parameters['filter']['taxonomy']['inclusive'] = False # select which EC accept or reject

# Plain ac
	basic_ac_parameters['multiple'] = True # Set to True if there are many associations per line (the object in the first field is associated to all the objects in the other fields within the same line)
	basic_ac_parameters['term first'] = False # set to True if the first field of each row is a GO term. Set to False if the first field represents a 
	basic_ac_parameters['separator'] = "\t" # select the separtor used to divide fields
	# basic_ac_parameters['simplify'] = True # after parsing and filtering, removes additional information such as taxonomy or EC. Useful if you have a huge amount of annotations and not enough memory

	ac_parameters_set = [
		{},
		basic_ac_parameters,
		]

	ac_params = {}

	print "\n#################################"
	print "\n# Testing annotation corpus parsing... #\n"
	print "#################################\n"

	acs = []
	for i in input_ac_set:
		print("\n---------------------------------------------\n")
		for k1 in ontology_parameters_set:
			ontology = load_ontology(i,k1)
			tempac = []
			for j in i[3]:
				for k in ac_parameters_set:
					print("Loading ac: " + str(i)+'\nParameters: ' + str(j))
					tempk = k
					# tempj = j.copy()
					tempac.append((i, j, k1, tempk, ontology, load_ac(ontology, j, k)))
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
			if not i[5] is None:
				print "-> " + str(len(i[5].reverse_annotations)) + " reverse_annotations, " +  str(len(i[5].annotations)) + " annotations."
			else:
				print "-> None!"
			print("--------------------")
	#

if __name__ == "__main__":
	test_AC()
#
