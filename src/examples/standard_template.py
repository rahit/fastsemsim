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
This class provides a template for using fastSemSim for evaluating protein Sem Sim.
See TermSemSimExample.py for information regarding Term Sem Sim
"""

from fastSemSim.GO import AnnotationCorpus
from fastSemSim.GO import GeneOntology
from fastSemSim.SemSim import ObjSemSim
from fastSemSim.SemSim import TermSemSim
import sys
import os
import math

if __name__ == "__main__":

	# example data
	if len(sys.argv) < 3:
		go_file = "GO_2011-09-16.obo-xml"
		ac_file = "gene_association.goa_fly"
		#ac_file = "plain_ac_example.txt"
	else:
		go_file = sys.argv[1]
		ac_file = sys.argv[2]

	is_plain = False
	IEA_filtering = False
	ontology = "BP"
	obj1 = "Q8IPD2"
	obj2 = "Q8IQQ0"
	list_file = "fly_list_example.txt"
	pairs_file = "fly_pairs_example.txt"




	#-#-#-#-#-#-#-#-#-#-#-#
	# Load Gene Ontology  #
	#-#-#-#-#-#-#-#-#-#-#-#

	# currently supported format is obo-xml. To load the GO from "go_file" simply use
	print "Loading Gene Ontology from " + str(go_file) + "..."
	go = GeneOntology.load_GO_XML(open(go_file))
	# get the number of nodes and edges in the GO
	print "-> Ontology correctly loaded: " + str(go.node_num()) + " nodes and " +  str(go.edge_num()) + " edges."
	print ""




	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# load Annotation Corpus  #
	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	
	# to load an annotation corpus you must specify:
	#1) (optional) a reference Gene Ontology to discard obsolete terms and merge alternative ids. [suggested]
	#2) the type of input file.Currently supported file formats are "gaf-2", "GOA", and "plain" files
	#3) (optional) further parameters, such as EC or taxonomy filtering options, or plain file format information
	
	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# First step: create an empty Annotation Corpus #
	ac = AnnotationCorpus.AnnotationCorpus(go) #Better if you pass a Gene Ontology as input data (see below why)

	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# Second step: set parsing parameters
	# You should fill a dictionary with the proper information. Friendly routines will be provided in future to set parsing parameters easily
	# If you specify incorrect or not pertinent parameters they'll be ignored.
	
	#### For gaf-2 / GOA files:
	if not is_plain:
		params = {}
		params['filter'] = {} # filter section is useful to remove undesired annotations
		if IEA_filtering:
			params['filter']['EC'] = {} # EC filtering: select annotations depending on their EC
			params['filter']['EC']['EC'] = 'IEA' # select which EC accept or reject

		params['filter']['taxonomy'] = '7227' # set properly this field to load only annotations involving proteins/genes of a specific species
		params['simplify'] = True # after parsing and filtering, removes additional information such as taxonomy or EC. Useful if you have a huge amount of annotations and not enough memory
	
	#### For plain files:
	if is_plain:
		params = {}
		params['multiple'] = False # Set to True if there are many associations per line (the object in the first field is associated to all the objects in the other fields within the same line)
		params['term first'] = True # set to True if the first field of each row is a GO term. Set to False if the first field represents a protein/gene
		params['separator'] = '\t' # select the separtor used to divide fields
	
	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# Third Step: parsing
	# just use parse routine. You have to specify the file to parse, the type of file and (optional) the parameters
	if is_plain:
		print "Loading annotation corpus from plain file " + str(ac_file) + "..."
		ac.parse(ac_file,'plain', params) # to parse plain files
	else:
		print "Loading annotation corpus from gaf-2 file " + str(ac_file) + "..."
		ac.parse(ac_file,'GOA', params) # to parse gaf-2 / GOA files
	
	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	#### additional useful annotation corpus routines
	ac.isConsistent() # check whether the annotations are consistent with the current gene ontology. Useful to check if everything is fine
	ac.sanitize() # removes annotations not consistent with the current gene ontology. USeful if you loaded an annotation corpus BEFORE loading a gene ontology
	print ""




	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# Accessing annotation corpus data  #
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	
	# these 4 variables contain all the useful data:
	ac.annotations # set of annotations -> it's a dictionary with genes/proteins as keys. The value for each key is a dictionary with GO Terms annotated for that protein as keys
	ac.reverse_annotations # set of annotations -> it's  adictionary with terms as keys. The value for each key is a dictionary with genes/proteins annotated for that GO Term as keys
	ac.obj_set # set of proteins/genes involved in annotations
	ac.term_set # set of GO Terms involved in annotations
	
	#Examples:
	print "-> Annotation Corpus correctly loaded. Annotated terms: " + str(len(ac.reverse_annotations)) + ". Annotated proteins: " + str(len(ac.annotations)) 
	print ""





	#-#-#-#-#-#-#-#-#-#-#-#
	# Semantic Similarity #
	#-#-#-#-#-#-#-#-#-#-#-#

	# Semantic similarity between Genes/proteins 
	# The basic approach here is to create a "SemSim" object with some fixed parameters, and then use it to evaluate the semantic similarity between paris of proteins/genes
	print "Semantic similarity example (Resnik BMA)"

	#### First step: create a SemSim object
	# You must create an ObjSemSim object providing the following parameters:
	# 1) annotation corpus, 2) gene ontology, 3) pairwise or goupwise term semantic similarity name, 4)mixing strategy (only for pairwise term semantic similarity measures), 5 (optional) additional parameters
	SS = ObjSemSim.ObjSemSim(ac, go, "Resnik", "BMA", None)
	
	#### Second step: use the ObjSemSim object to determine the semantic similarity between two proteins
	# You have to specify the GO Category to use ("MF", "BP", "CC") and the names of the two proteins. If the proteins or the category are not valid or not present in the annotation corpus, then None will be returned
	
	test = SS.SemSim(obj1,obj2,ontology) # returns the Sem Sim between obj1 and obj2. If obj1 or obj2 do not have annotations for the selected ontology, then None will be returned
	print "-> " + obj1 + " - " + obj2  + ": " + str(test)
	print ""





	#-#-#-#-#-#-#-#-#-#-#-#-#
	# More complex examples #
	#-#-#-#-#-#-#-#-#-#-#-#-#
	
	#### Calculate SS between set of pairs of proteins loaded from a file
	print "Example 1. Paris of proteins from a file"
	inf = open(pairs_file,'r')
	pairs = []
	for line in inf:
		line = line.rstrip('\n')
		line = line.rstrip('\r')
		line = line.rsplit('\t')
		pairs.append((line[0], line[1]))
	inf.close()
	scores = []
	for i in range(1,len(pairs)):
		temp = SS.SemSim(pairs[i][0],pairs[i][1],ontology)
		scores.append((pairs[i][0],pairs[i][1],temp))
		print "-> " + pairs[i][0] + " - " + pairs[i][1] + ": " + str(temp)
	print ""


	#### To calculate pairwise SS between element within a list loaded from a file

	print "Example 2. List of proteins from a file"
	inf = open(list_file,'r')
	pairs = []
	for line in inf:
		line = line.rstrip('\n')
		line = line.rstrip('\r')
		pairs.append(line)
	inf.close()
	scores = {}
	for i in range(1,len(pairs)):
		scores[pairs[i]] = {}
		for j in range(i+1,len(pairs)):
			temp = SS.SemSim(pairs[i],pairs[j],ontology)
			scores[pairs[i]][pairs[j]] = temp
			print "-> " + pairs[i] + " - " + pairs[j] + ": " + str(temp)
	print ""


	#### To calculate pairwise SS between element within a list loaded from annotation corpus
	
	print "Example 3. List of proteins from Annotation Corpus - Limited to few comparisons."
	limit = 20
	done = 0
	pairs = ac.obj_set.keys()
	scores = {}
	for i in range(1,len(pairs)):
		if done >= limit:
			break
		scores[pairs[i]] = {}
		for j in range(i+1,len(pairs)):
			done +=1
			temp = SS.SemSim(pairs[i],pairs[j],ontology)
			scores[pairs[i]][pairs[j]] = temp
			print "-> " + pairs[i] + " - " + pairs[j] + ": " + str(temp)
			if done >= limit:
				break
	print ""
