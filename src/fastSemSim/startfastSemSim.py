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

from fastSemSim.GO import AnnotationCorpus
from fastSemSim.GO import GeneOntology
from fastSemSim.SemSim import ObjSemSim
from fastSemSim.SemSim import TermSemSim
from fastSemSim.fastResnik import fastResnikSemSim
import sys
import os
import math
import gzip




	#-#-#-#-#-#-#-#-#-#-#-#
	# Load Gene Ontology  #
	#-#-#-#-#-#-#-#-#-#-#-#

def load_go(go_file):
	print "Loading Gene Ontology from " + str(go_file) + "..."
	fn,fe = os.path.splitext(go_file)
	if fe == '.gz':
		go_handle = gzip.open(go_file, 'rb')
	else:
		go_handle = open(go_file, 'r')
	go = GeneOntology.load_GO_XML(go_handle)
	go_handle.close()
	print "-> Ontology correctly loaded: " + str(go.node_num()) + " nodes and " +  str(go.edge_num()) + " edges."
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
		if not use_IEA:
			params['filter']['EC'] = {} # EC filtering: select annotations depending on their EC
			params['filter']['EC']['EC'] = 'IEA' # select which EC accept or reject
		
		if not tax_include == None:
			params['filter']['taxonomy'] = tax_include # set properly this field to load only annotations involving proteins/genes of a specific species
		
		params['simplify'] = True # after parsing and filtering, removes additional information such as taxonomy or EC. Useful if you have a huge amount of annotations and not enough memory
	
	#### For plain files:
	if is_plain:
		params = {}

		if multiple:
			params['multiple'] = True # Set to True if there are many associations per line (the object in the first field is associated to all the objects in the other fields within the same line)
		if GOTerm_first:
			params['term first'] = True # set to True if the first field of each row is a GO term. Set to False if the first field represents a protein/gene
		
		if not ac_separator == None:
			params['separator'] = ac_separator # select the separtor used to divide fields
	
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
	print "-> Annotation Corpus correctly loaded: " + str(len(ac.obj_set)) + " objects and " +  str(len(ac.term_set)) + " GO Terms."
	return ac
#

	# these 4 variables contain all the useful data:
	#ac.annotations # set of annotations -> it's a dictionary with genes/proteins as keys. The value for each key is a dictionary with GO Terms annotated for that protein as keys
	#ac.reverse_annotations # set of annotations -> it's  adictionary with terms as keys. The value for each key is a dictionary with genes/proteins annotated for that GO Term as keys
	#ac.obj_set # set of proteins/genes involved in annotations
	#ac.term_set # set of GO Terms involved in annotations
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
	print "Initializing Semantic Similarity class..."
	SS = ObjSemSim.ObjSemSim(ac, go, termss, mixp, params)
	print "-> Semantic Similarity class ready"
	return SS
#



#### Second step: use the ObjSemSim object to determine the semantic similarity between two proteins
	# You have to specify the GO Category to use ("MF", "BP", "CC") and the names of the two proteins. If the proteins or the category are not valid or not present in the annotation corpus, then None will be returned
#









	#-#-#-#-#-#-#-#-#
	# Pairs Sem Sim #
	#-#-#-#-#-#-#-#-#

def ss_pairs(SS, pairs, ontology, out, cut_thres = None):
	print "Evluating semantic similarity between " + str(len(pairs)) + " pairs."
	scores = []
	done = 0
	total = len(pairs)
	if verbose:
		prev_text = ""
		sys.stdout.write("Done: ")
		sys.stdout.flush()
	for i in range(0,len(pairs)):
		temp = SS.SemSim(pairs[i][0],pairs[i][1],ontology)
		#scores.append((pairs[i][0],pairs[i][1],temp))
		done+=1
		if not cut_thres == None:
			if temp == None or temp < cut_thres:
				continue
		if out == None:
			print pairs[i][0] + "\t" + pairs[i][1] + "\t" + str(temp)
		else:
			out.write(pairs[i][0] + "\t" + pairs[i][1] + "\t" + str(temp) + "\n")
			if verbose:
				sys.stdout.write("\b"*len(prev_text))
				prev_text = str(done) + ' [%.4f' % (100*done/float(total)) + " %]"
				sys.stdout.write(prev_text)
				sys.stdout.flush()
	#return scores
#







	#-#-#-#-#-#-#-#-#-#-#
	# Pairwise Sem Sim  #
	#-#-#-#-#-#-#-#-#-#-#

def ss_pairwise(SS, pairs, ontology, out, cut_thres = None):
	print "Evluating pairwise semantic similarity between " + str(len(pairs)) + " entities (" + str(len(pairs)*(len(pairs)-1)/2) + " pairs)"
	scores = {}
	done = 0
	total = len(pairs)*(len(pairs)-1)/2

	if verbose:
		prev_text = ""
		sys.stdout.write("Done: ")
		sys.stdout.flush()
	for i in range(0,len(pairs)):
		scores[pairs[i]] = {}
		for j in range(i+1,len(pairs)):
			temp = SS.SemSim(pairs[i],pairs[j],ontology)
			#scores[pairs[i]][pairs[j]] = temp
			done+=1
			if not cut_thres == None:
				if temp == None or temp < cut_thres:
					continue
			if out == None:
				print pairs[i] + "\t" + pairs[j] + "\t" + str(temp)
			else:
				out.write(pairs[i] + "\t" + pairs[j] + "\t" + str(temp) + "\n")
				if verbose:
					sys.stdout.write("\b"*len(prev_text))
					prev_text = str(done) + ' [%.4f' % (100*done/float(total)) + " %]"
					sys.stdout.write(prev_text)
					sys.stdout.flush()
	#return scores
#








	#-#-#-#-#-#-#-#-#-#-#-#-#
	# Load Query from File  #
	#-#-#-#-#-#-#-#-#-#-#-#-#

def load_query_from_file(list_file, f_type='list', separator = '\t'):
	print "Loading query from file " + str(list_file) + " [type: " + str(f_type) + "] ..."
	
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
	print "-> Query loaded from file: " + str(len(query)) + " entries."
	return query
#






	#-#-#-#-#-#-#-#-#-#-#-#-#
	# Load Query from File  #
	#-#-#-#-#-#-#-#-#-#-#-#-#

def load_query_from_ac(ac):
	query = ac.obj_set.keys()
	print "-> Query loaded from Annotation Corpus: " + str(len(query)) + " entries."
	return query
#



####----####----####----####----####----####----####----####----####----####----####----####----####----####----####----####----
	
	#-#-#-#-#-#-#-#-#-#-#
	# Enhaced version   #
	#-#-#-#-#-#-#-#-#-#-#

def init_enhanced_ss(go, ac, termss='Resnik', mixp="BMA", params = None):

	print "Initializing Semantic Similarity class..."
	SS = fastResnikSemSim.fastResnikSemSim(ac, go, termss, mixp, params)
	print "-> Semantic Similarity class ready"
	return SS
#



def ss_pairwise_enhanced(SS, pairs = None, ontology = 'BP', out = None, cut_thres = None):
	#print "Evluating pairwise semantic similarity between " + str(len(pairs)) + " entities (" + str(len(pairs)*(len(pairs)-1)/2) + " pairs)"
	out_h = out
	if out==None:
		out_h = sys.stdout
	SS.SemSim(ontology, out, cut_thres)
#



####----####----####----####----####----####----####----####----####----####----####----####----####----####----####----####----



def print_usage():
	print ""
	print "Usage:\t python FastSemSim.py [-g|--go go_file] -a|--ac ac_file [-c|--category MF|BP|CC ] [-t|--actype ac_type] [-q|--query query_file] [-u] [-s|--semsim sem_sim] [-m|--mix mixing_strategy] [-o|--output output_file] [-p|--pairs] [-l|--list] [-v] [-h]"
	print ""
	print ""
	print "Parameters:"
	print "-a,--ac:\t The Annotation Corpus to use. Can be either in GAF-2 or plain format. See documentation online for information."
	print "-c, --category:\t The Gene Ontology category to use. Can be \"MF\",\"BP\" or \"CC\". [Default: BP]"
	print "-g,--go:\t The Gene Ontology to use. Must be in obo-xml format. Can use and automatically detects the gzipped version of the GO. If not provided, the GO version included in FastSemSim will be used."
	print "-h, --help:\t Print this help page."
	print "-l, --list:\t Consider the query as a list of entries. Evaluates the pairwise semantic similarity."
	print "-m, --mixing_strategy:\t The mixing strategy to be used (if the SS measure requires it). [Default: BMA]"
	print "-o, --output:\t Output file. If not specified, results will be printed on the console."
	print "-p, --pairs:\t Consider the query as a set of pairs. If not specified, list will be assumed."
	print "-q, --query:\t Specifies the file with the query. If not specified, the behavior will be the same as if -u is specified."
	print "-s, --semsim:\t The semantic similarity measure to use. [Default: Resnik]"
	print "-t,--actype:\t Describes the format of the annotation corpus. Can be \"plain\" or \"gaf2\". [default: gaf2]"
	print "-u:\t\t Use all the entries in the annotation corpus as the query. This overrides -l and -p options."
	print "-v, --verbose:\t Print additional statistics and progress details."
	print ""
	print "Advanced Parameters:"
	print "--sep, --separator:\t Separator used in the query file (only for pairs). Use s for space, and t for tab. [Default: tab]"
	print "--tax:\t Filter the Annotation Corpus. Removes protein/genes according to the taxonomy. Used only with gaf2 files"
	print "--IEA:\t If specified, IEA annotations will be considered. Used only with gaf2 files. [that is the standard behavior]"
	print "--noIEA:\t If specified, IEA annotations will be ignored. Used only with gaf2 files."
	print "--GOTermfirst:\t If specified, plain annotation corpus files will be parsed assuming that the first column of each row contains the GO Term, and the second one contains the Entry. Used only with plain files."
	print "--entryfirst:\t If specified, plain annotation corpus files will be parsed assuming that the first column of each row contains the entry, and the second the GO Term. Used only with plain files. [this is the standard behavior]"
	print "--multiple:\t If specified, each line in plain annotation corpus files can contain more than one GO Term or Entries." 
	print "--acsep:\t Separator used for the plain annotation corpus files. Use s for space, and t for tab. [Default: tab]"
	print "--enhanced:\t Use the fast implementation of the semantic similarity measure. Currently only Resnik max is supported. Currently it forces -l and -u. Overrides -p and -q. This limitation will be removed in the future."
	print "--cut:\t Do not print/save pairs whose semantic similarity is smaller than cut threshold. This drastically reduces the size of output data for whole proteome comparison. [default: --cut 0]"
	print ""
	print "Additional Notes:"
	print "A \'None\' score is returned if at least one entry of a pair is not annotated with any term in the selected category. Using --cut removes such pairs."
#


def start():
	global go_file, ac_file, ac_type, ontology, query_file, query_type, query_from_ac, out_file, semsim_name, mix_name, query_separator, verbose, tax_include, use_IEA, GOTerm_first, multiple, ac_separator, go, ac, query, SS, use_enhanced
	
	print("-----------------------------------------------")
	print("FastSemSim 0.5 - Copyright 2011-2012 Marco Mina")
	print("-----------------------------------------------")

	program_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
	#program_dir = '.' # use this with py2exe to build a working binary
	
	go_file = program_dir + "/data/GO_2012-02-24.obo-xml.gz"
	ac_file = None
	ac_type = 'gaf2'
	ontology = "BP"
	query_file = None
	query_type = 'list'
	query_from_ac = True
	out_file = None
	semsim_name = 'Resnik'
	mix_name = 'BMA'
	query_separator = '\t'
	verbose = False
	tax_include = None
	use_IEA = True
	GOTerm_first = False
	multiple = False
	ac_separator = None
	use_enhanced = False
	cut_thres = None
	
	if len(sys.argv) < 2:
		print_usage()
		sys.exit()

	skip=False
	for i in range(1,len(sys.argv)):
		#print sys.argv[i]
		if skip:
			#print "ignore"
			skip = False
			continue
		elif sys.argv[i] == '--help' or sys.argv[i] == '-h':
			print_usage()
			sys.exit()
		elif sys.argv[i] == '-c' or sys.argv[i] == '--category':
			if sys.argv[i+1].lower() == 'bp':
				ontology = 'BP'
			elif sys.argv[i+1].lower() == 'mf':
				ontology = 'MF'
			elif sys.argv[i+1].lower() == 'cc':
				ontology = 'CC'
			else:
				print "Ontology Category not recognized."
				sys.exit()
		elif sys.argv[i] == '-g' or sys.argv[i] == '--go':
			go_file = sys.argv[i+1]
		elif sys.argv[i] == '-a' or sys.argv[i] == '--ac':
			ac_file = sys.argv[i+1]
		elif sys.argv[i] == '-t' or sys.argv[i] == '--actype':
			ac_type = sys.argv[i+1]
		elif sys.argv[i] == '-q' or sys.argv[i] == '--query':
			query_file = sys.argv[i+1]
			query_from_ac = False
		elif sys.argv[i] == '-u':
			query_from_ac = True
			continue
		elif sys.argv[i] == '-p' or sys.argv[i] == '--pairs':
			query_type = 'pairs'
			continue
		elif sys.argv[i] == '-l' or sys.argv[i] == '--list':
			query_type = 'list'
			continue
		elif sys.argv[i] == '-s' or sys.argv[i] == '--semsim':
			semsim_name = sys.argv[i+1]
		elif sys.argv[i] == '-m' or sys.argv[i] == '--mix':
			mix_name = sys.argv[i+1]
		elif sys.argv[i] == '-o' or sys.argv[i] == '--output':
			out_file = sys.argv[i+1]
		elif sys.argv[i] == '-v' or sys.argv[i] == '--verbose':
			verbose = True
			continue
		elif sys.argv[i] == '--sep' or sys.argv[i] == '--separator':
			if sys.argv[i+1] == 't':
				query_separator = "\t"
			elif sys.argv[i+1] == 's':
				query_separator = " "
			else:
				query_separator = sys.argv[i+1]
		elif sys.argv[i] == '--tax':
			tax_include = sys.argv[i+1]
		elif sys.argv[i] == '--IEA':
			use_IEA = True
			continue
		elif sys.argv[i] == '--noIEA':
			use_IEA = False
			continue
		elif sys.argv[i] == '--GOTermfirst':
			GOTerm_first = True
			continue
		elif sys.argv[i] == '--entryfirst':
			GOTerm_first = False
			continue
		elif sys.argv[i] == '--multiple':
			multiple = True
			continue
		elif sys.argv[i] == '--enhanced':
			use_enhanced = True
			continue
		elif sys.argv[i] == '--cut':
			cut_thres = float(sys.argv[i+1])
		elif sys.argv[i] == '--acsep':
			if sys.argv[i+1] == 't':
				ac_separator = "\t"
			elif sys.argv[i+1] == 's':
				ac_separator = " "
			else:
				ac_separator = sys.argv[i+1]
		else:
			print "Unknown parameter " + sys.argv[i]
			print ""
			print_usage()
			sys.exit()
		skip = True

	if ac_file == None:
		print "Please specify an annotation corpus"
		sys.exit()
	if use_enhanced:
		query_from_ac = True
		semsim_name = 'Resnik'
		mix_name = 'max'
	if not query_from_ac:
		if query_file == None:
			print "Please specify a query file or use -u"
			sys.exit()
	else:
		query_type = 'list'


	print("Gene Ontology file \t\t" + str(go_file))
	print("Annotation Corpus file \t\t" + str(ac_file))
	print("Annotation Corpus file type \t" + str(ac_type))
	if ac_type == 'gaf2':
		print("AC Consider IEA\t\t\t" + str(use_IEA))
		print("AC Filter taxonomy\t\t" + str(tax_include))
	elif ac_type == 'plain':
		if GOTerm_first:
			print("AC Row format\t\t\tGO Term -> Entry")
		else:
			print("AC Row format\t\t\tEntry -> GO Term")
		print("Many associations per line\t" + str(multiple))
	if query_from_ac:
		print("Query from \t\t\tAnnotation Corpus")
	else:
		print("Query from file \t\t" + str(query_file))
		print("Query file separator \t\t\'" + str(query_separator) + "\'")
	print("Query type \t\t\t" + str(query_type))
	if not out_file == None:
		print("Output file \t\t\t" + str(out_file))
	else:
		print("Output \t\t\t\tto console")
	print("SS measure \t\t\t" + str(semsim_name) + " " + str(mix_name))
	print("GO category \t\t\t" + ontology)
	print("Using enhanced version\t\t" + str(use_enhanced))
	print("-----------------------------------------------")

	go = load_go(go_file)
	ac = load_ac(ac_file, ac_type)
	
	if not use_enhanced:
		SS = init_ss(go, ac, semsim_name, mix_name)
	else:
		SS = init_enhanced_ss(go, ac, semsim_name, mix_name)
		
	if query_from_ac:
		query = load_query_from_ac(ac)
	else:
		query = load_query_from_file(query_file, query_type, query_separator)
	h = None
	if not out_file == None:
		h = open(out_file, 'w')
		
	if use_enhanced:
		ss_pairwise_enhanced(SS, query, ontology, h, cut_thres)
	elif query_type == 'pairs':
		ss_pairs(SS, query, ontology, h, cut_thres)
	else:
		ss_pairwise(SS, query, ontology, h, cut_thres)
	if not h == None:
		h.close()
	sys.exit()
#

if __name__ == "__main__":
	start()
#
