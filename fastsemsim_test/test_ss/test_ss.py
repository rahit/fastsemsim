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
from fastsemsim import data, SemSim
from fastsemsim.SemSim import SemSimUtils
import random
import pandas as pd
import sys
import os
import math
import gzip
from fastsemsim.SemSim.SetSemSim import SetSemSim
from fastsemsim.SemSim.ObjSemSim import ObjSemSim
from fastsemsim.SemSim.ObjSetSemSim import ObjSetSemSim

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

def test_SS():

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
	# Plain ac
	basic_ac_parameters['multiple'] = True # Set to True if there are many associations per line (the object in the first field is associated to all the objects in the other fields within the same line)
	basic_ac_parameters['term first'] = False # set to True if the first field of each row is a GO term. Set to False if the first field represents a 
	basic_ac_parameters['separator'] = "\t" # select the separtor used to divide fields
	# basic_ac_parameters['simplify'] = True # after parsing and filtering, removes additional information such as taxonomy or EC. Useful if you have a huge amount of annotations and not enough memory

	ac_parameters_set = [
		{},
		# basic_ac_parameters,
		]

	ac_params = {}

	term_ss_measures = SemSim.term_SemSim_measures.keys()
	pair_ss_measures =  SemSim.mix_strategies.keys()

	print "\n#################################"
	print "\n# Testing SS measures... #\n"
	print "#################################\n"

	acs = []
	for i in input_ac_set:
		print("\n---------------------------------------------\n")
		for k1 in ontology_parameters_set:
			print('-> Loading ontology ', str(i), '...')
			ontology = load_ontology(i,k1)
			print "Ontology loaded: " + str(ontology.node_number()) + " nodes and " +  str(ontology.edge_number()) + " edges."
			for j in i[3]:
				for k in ac_parameters_set:
					print("-> Loading ac: " + str(i)+'\nParameters: ' + str(j))
					ac = load_ac(ontology, j, k)
					print "Annotation Corpus loaded: " + str(len(ac.reverse_annotations)) + " terms, " +  str(len(ac.annotations)) + " objects."
					# A = 0
					# for i in ac.reverse_annotations:
						# A += len(ac.reverse_annotations[i])
					# print A
					print('-> Setting up SemSimUtils...')
					ssutil = SemSimUtils(ontology, ac)

					print("\n---------------------------------\n")
					print('-> Testing term SemSim Measures...')
					for s in term_ss_measures:
						print("Initializing: " + str(s) + '...')
						tss_class = SemSim.select_term_SemSim(s)
						ss = tss_class(ontology, ac, ssutil, do_log=False)
						print(str(s) + " initialized. Testing with 200 random pairs [showing only a selection of 4 pairs]...")
						query = ac.reverse_annotations
						for root in ontology.roots.keys():
							print("Ontology root: " + str(root))
							offspring = ssutil.offspring[root]
							query2 = []
							for qp in offspring:
								if qp in query:
									query2.append(qp)
							limit = 200
							t1 = random.sample(query2, limit)
							t2 = random.sample(query2, limit)
							temp = []
							for conta in range(0,len(t1)):
								temp.append((t1[conta], t2[conta], ss.SemSim(t1[conta], t2[conta], root)))
							temp = pd.DataFrame(temp)
							print(temp.ix[0:4,:])
							print("----------------")

					print("\n---------------------------------\n")
					print('-> Testing ObjSetSemSim Measures...')
					for s in term_ss_measures:
						for mix in pair_ss_measures:
							print("Initializing: " + str(s) + ' + ' + str(mix) + '...')
							ss = ObjSetSemSim(ontology, ac, s, mix, ssutil, do_log = False)
							print(str(s) + ' + ' + str(mix) + " initialized. Testing with 200 random pairs [showing only a selection of 4 pairs]...")
							query2 = ac.annotations.keys()
							for root in ontology.roots.keys():
								print("Ontology root: " + str(root))
								limit = 10
								setsize = 5
								t1 = []
								for setn in range(0,limit):
									t1.append([random.sample(query2, setsize), random.sample(query2, setsize)])
								temp = []
								for conta in range(0,len(t1)):
									temp.append((t1[conta][0], t1[conta][1], ss.SemSim(t1[conta][0], t1[conta][1], root)))
								temp = pd.DataFrame(temp)
								print(temp.ix[0:4,:])
								print("----------------")

					print("\n---------------------------------\n")
					print('-> Testing ObjSemSim Measures...')
					for s in term_ss_measures:
						for mix in pair_ss_measures:
							print("Initializing: " + str(s) + ' + ' + str(mix) + '...')
							ss = ObjSemSim(ontology, ac, s, mix, ssutil, do_log = False) 
							print(str(s) + ' + ' + str(mix) + " initialized. Testing with 200 random pairs [showing only a selection of 4 pairs]...")
							query2 = ac.annotations.keys()
							for root in ontology.roots.keys():
								print("Ontology root: " + str(root))
								limit = 200
								t1 = random.sample(query2, limit)
								t2 = random.sample(query2, limit)
								temp = []
								for conta in range(0,len(t1)):
									temp.append((t1[conta], t2[conta], ss.SemSim(t1[conta], t2[conta], root)))
								temp = pd.DataFrame(temp)
								print(temp.ix[0:4,:])
								print("----------------")

					print("\n---------------------------------\n")
					print('-> Testing TermSet SemSim Measures...')
					for s in term_ss_measures:
						for mix in pair_ss_measures:
							print("Initializing: " + str(s) + ' + ' + str(mix) + '...')
							ss = SetSemSim(ontology, ac, s, mix, ssutil, do_log = False)
							print(str(s) + ' + ' + str(mix) + " initialized. Testing with 200 random pairs [showing only a selection of 4 pairs]...")
							query = ac.reverse_annotations
							for root in ontology.roots.keys():
								print("Ontology root: " + str(root))
								offspring = ssutil.offspring[root]
								query2 = []
								for qp in offspring:
									if qp in query:
										query2.append(qp)
								limit = 200
								setsize = 5
								t1 = []
								for setn in range(0,limit):
									t1.append([random.sample(query2, setsize), random.sample(query2, setsize)])
								temp = []
								for conta in range(0,len(t1)):
									temp.append((t1[conta][0], t1[conta][1], ss.SemSim(t1[conta][0], t1[conta][1], root)))
								temp = pd.DataFrame(temp)
								print(temp.ix[0:4,:])
								print("----------------")


	#

if __name__ == "__main__":
	test_SS()
#
