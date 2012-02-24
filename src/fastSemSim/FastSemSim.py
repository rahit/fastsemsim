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





	#-#-#-#-#-#-#-#-#-#-#-#
	# Load Gene Ontology  #
	#-#-#-#-#-#-#-#-#-#-#-#

def load_go(go_file):
	print "Loading Gene Ontology from " + str(go_file) + "..."
	go = GeneOntology.load_GO_XML(open(go_file))
	print "-> Ontology correctly loaded: " + str(go.node_num()) + " nodes and " +  str(go.edge_num()) + " edges."
	print ""
	return go
#






	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# load Annotation Corpus  #
	#-#-#-#-#-#-#-#-#-#-#-#-#-#

def load_ac(ac_file, ac_type):
	ac = AnnotationCorpus.AnnotationCorpus(go)
	
	is_plain = False
	if ac_type.lower() == 'plain':
		is_plain = True
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

	return ac
#






def print_stats(go, ac):
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
#









	#-#-#-#-#-#-#-#-#-#-#-#
	# Semantic Similarity #
	#-#-#-#-#-#-#-#-#-#-#-#
	
def init_ss(go, ac, termss='Resnik', mixp="BMA", params = None):

	# Semantic similarity between Genes/proteins 
	# The basic approach here is to create a "SemSim" object with some fixed parameters, and then use it to evaluate the semantic similarity between paris of proteins/genes

	#### First step: create a SemSim object
	# You must create an ObjSemSim object providing the following parameters:
	# 1) annotation corpus, 2) gene ontology, 3) pairwise or goupwise term semantic similarity name, 4)mixing strategy (only for pairwise term semantic similarity measures), 5 (optional) additional parameters
	SS = ObjSemSim.ObjSemSim(ac, go, termss, mixp, params)
	return SS
#



#### Second step: use the ObjSemSim object to determine the semantic similarity between two proteins
	# You have to specify the GO Category to use ("MF", "BP", "CC") and the names of the two proteins. If the proteins or the category are not valid or not present in the annotation corpus, then None will be returned
#









	#-#-#-#-#-#-#-#-#
	# Pairs Sem Sim #
	#-#-#-#-#-#-#-#-#

def ss_pairs(SS, pairs, ontology, out):

	scores = []
	for i in range(0,len(pairs)):
		temp = SS.SemSim(pairs[i][0],pairs[i][1],ontology)
		#scores.append((pairs[i][0],pairs[i][1],temp))
		if out == None:
			print pairs[i][0] + "\t" + pairs[i][1] + "\t" + str(temp)
		else:
			h.write(pairs[i][0] + "\t" + pairs[i][1] + "\t" + str(temp) + "\n")
	#return scores
#







	#-#-#-#-#-#-#-#-#-#-#
	# Pairwise Sem Sim  #
	#-#-#-#-#-#-#-#-#-#-#

def ss_pairwise(SS, pairs, ontology, out):
	scores = {}
	for i in range(0,len(pairs)):
		scores[pairs[i]] = {}
		for j in range(i+1,len(pairs)):
			temp = SS.SemSim(pairs[i],pairs[j],ontology)
			#scores[pairs[i]][pairs[j]] = temp
			if out == None:
				print pairs[i] + "\t" + pairs[j] + "\t" + str(temp)
			else:
				h.write(pairs[i] + "\t" + pairs[j] + "\t" + str(temp) + "\n")
	#return scores
#








	#-#-#-#-#-#-#-#-#-#-#-#-#
	# Load Query from File  #
	#-#-#-#-#-#-#-#-#-#-#-#-#

def load_query_from_file(list_file, f_type='list', separator = '\t'):
	
	list_type = {'list':None, 'pairwise':None}
	pair_type = {'pair':None, 'pairs':None}
	
	h = open(list_file,'r')
	query = []
	for line in h:
		line = line.rstrip('\n')
		line = line.rstrip('\r')
		
		if f_type.lower() in pair_type:
			line = line.rsplit(separator)
			query.append((line[0], line[1]))
			
		elif f_type.lower() in list_type:
			query.append(line)
	
	h.close()
	return query
#






	#-#-#-#-#-#-#-#-#-#-#-#-#
	# Load Query from File  #
	#-#-#-#-#-#-#-#-#-#-#-#-#

def load_query_from_ac(ac):
	query = ac.obj_set.keys()
	return query
#





def print_usage():
	print "FastSemSim - Semantic Similarity."
	print ""
	print "Simple usage: python FastSemSim.py -g|--go go_file -a|--ac ac_file -t|--actype ac_type -q|--query query -u yes|no -s|--semsim term_sem_sim -m|--mix mixing_strategy -o|--output output_file -p|--pairs yes|no"
	print ""
	print ""
	print "Parameters:"
	print "-g,--go:\tGene Ontology file to use: must be in obo-xml format. If no GO is provided, the GO version included in FastSemSim will be used."
	print "-a,--ac:\tAnnotation Corpus. Can be either in GAF-2 or plain format. See documentation online for information."
	print "-t,--actype:\tDescribes the format of the annotation corpus. Can be plain or gaf2. If not provided, .txt files will be considered as plain files, and .gaf or .goa files will be considered GAF-2 files."
	print "-q, --query:\t File with input query"
	print "-u:\t Use all the proteins in the annotation corpus as input query"
	print "-s, --semsim:\t The semantic similarity measure to use. Default: Resnik"
	print "-p, --pairs:\t Whether the query files contains pairs. Can be yes or no. If not specified, default is no."
	print "-m, --mixing_strategy:\t The mixing strategy to be used (with the SS measures that require it). Default: BMA"
	print "-o, --output:\t Output file where results should be written. If not specified, results will be printed on the console."
	print "-c, --category:\t Gene Ontology category to use. Can be MF, BP or CC."
	print "--sep:\t Separator used in query file (only for pairs)"
	print "-v, --verbose:\t Prints additional statistics and progress details."
	print "-h, --help:\t Prints usage info."
	
#



if __name__ == "__main__":

	go_file = "GO_2011-09-16.obo-xml"
	ac_file = None
	ac_type = 'gaf2'
	IEA_filtering = False
	ontology = "BP"
	query_file = None
	query_type = 'list'
	query_from_ac = True
	out_file = None
	semsim_name = 'Resnik'
	mix_name = 'BMA'
	query_separator = '\t'
	verbose = False

	if len(sys.argv) < 2 or sys.argv[1] == '--help' or sys.argv[1] == '-h':
		print_usage()
		sys.exit()

	skip=False
	for i in range(1,len(sys.argv)):
		#print sys.argv[i]
		if skip:
			#print "ignore"
			skip = False
			continue
		elif sys.argv[i] == '-g' or sys.argv[i] == '--go':
			go_file = sys.argv[i+1]
		elif sys.argv[i] == '-a' or sys.argv[i] == '--ac':
			ac_file = sys.argv[i+1]
		elif sys.argv[i] == '-t' or sys.argv[i] == '--actype':
			ac_type = sys.argv[i+1]
		elif sys.argv[i] == '-q' or sys.argv[i] == '--query':
			query_file = sys.argv[i+1]
			query_from_ac = False
		elif sys.argv[i] == '-sep' or sys.argv[i] == '--separator':
			query_separator = sys.argv[i+1]
		elif sys.argv[i] == '-u':
			if sys.argv[i+1]=='y' or sys.argv[i+1]=='yes':
				query_from_ac = True
			else:
				query_from_ac = False
		elif sys.argv[i] == '-p' or sys.argv[i] == '--pairs':
			if sys.argv[i+1]=='y' or sys.argv[i+1]=='yes':
				query_type = 'pairs'
			else:
				query_type = 'list'
		elif sys.argv[i] == '-s' or sys.argv[i] == '--semsim':
			semsim_name = sys.argv[i+1]
		elif sys.argv[i] == '-m' or sys.argv[i] == '--mix':
			mix_name = sys.argv[i+1]
		elif sys.argv[i] == '-o' or sys.argv[i] == '--output':
			out_file = sys.argv[i+1]
		elif sys.argv[i] == '-v' or sys.argv[i] == '--verbose':
			if sys.argv[i+1]=='y' or sys.argv[i+1]=='yes':
				verbose = True
			else:
				verbose = False
		elif sys.argv[i] == '-c' or sys.argv[i] == '--category':
			if sys.argv[i+1].lower() == 'bp':
				ontology = 'BP'
			elif sys.argv[i+1].lower() == 'mf':
				ontology = 'MF'
			elif sys.argv[i+1].lower() == 'cc':
				ontology = 'CC'
			else:
				print "Category not recognized."
				sys.exit()
		else:
			print_usage()
			sys.exit()
		skip = True

	if ac_file == None:
		print "Please specify an annotation corpus"
		sys.exit()
	if ac_type == None:
		print "Please specify an annotation corpus type"
		sys.exit()
	if not query_from_ac:
		if query_file == None:
			print "Please specify a query file or use all the annotation corpus"
			sys.exit()
	
	go = load_go(go_file)
	ac = load_ac(ac_file, ac_type)
	SS = init_ss(go, ac, semsim_name, mix_name)
	if query_from_ac:
		query = load_query_from_ac(ac)
	else:
		query = load_query_from_file(query_file, query_type, query_separator)
	h = None
	if not out_file == None:
		h = open(out_file, 'w')
	if query_type == 'pairs':
		ss_pairs(SS, query, ontology, h)
	else:
		ss_pairwise(SS, query, ontology, h)
	if not h == None:
		h.close()
	sys.exit()
#
