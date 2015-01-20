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

from fastSemSim.Ontology import ontologies
from fastSemSim.Ontology import AnnotationCorpus
from fastSemSim.SemSim import SemSimMeasures

import sys
import os
import math
import gzip

import argparse

	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# Cmd line parameter parsing  #
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def prbool(string):
	if string == 'True' or string == 'true' or string == True or string == 'yes' or string == 'Yes' or string == '1':
		return True
	if string == 'False' or string == 'false' or string == False or string == 'No' or string == 'no' or string == '0':
		return False
	msg = 'Cannot interpret %r as a boolean. Allowed arguments: True, False, 0, 1, Yes, No' % string
	raise argparse.ArgumentTypeError(msg)
	return None
#

def parse_args():
	parser = argparse.ArgumentParser(
		description='FastSemSim commad line tool',
		prog='FastSemSim', usage=None, epilog=None, 
		fromfile_prefix_chars='@', add_help=True)

	param_go = parser.add_argument_group(title='Gene Ontology (GO)', description='Parameters relative to the Gene Ontology')
	param_ac = parser.add_argument_group(title='Annotation Corpus (AC)', description='Parameters relative to Annotation Corpus')
	param_query = parser.add_argument_group(title='Query (Q)', description='Parameters relative to Query')

	param_go.add_argument('-o','--ontology', '--ontology_file', action='store', nargs=1, default=None, help=None, metavar='ontology_file', dest='ontology_file')
	param_go.add_argument('--ontology_file_format','--o_file_format', action='store', nargs=1, default=None, help=None, metavar='ontology_file_format', dest='ontology_file_format')
	param_go.add_argument('--ontology_type', '--o_type', action='store', nargs=1, default=None, help=None, metavar='ontology_type', dest='ontology_type')
	param_go.add_argument('--ignore_has_part', action='store', nargs='?', default=True, type=prbool, help=None, metavar='ignore_has_part', dest='ignore_has_part')
	param_go.add_argument('--ignore_is_a', action='store', nargs='?', default=False, type=prbool, help=None, metavar='ignore_is_a', dest='ignore_is_a')
	param_go.add_argument('--ignore_part_of', action='store', nargs='?', default=False, type=prbool, help=None, metavar='ignore_part_of', dest='ignore_part_of')
	param_go.add_argument('--ignore_regulates', action='store', nargs='?', default=False, type=prbool, help=None, metavar='ignore_regulates', dest='ignore_regulates')
	param_go.add_argument('--verbose', '-v', action='count', default=None, help=None, dest='verbose')

	param_ac.add_argument('-a','--ac', '--ac_file', action='store', nargs=1, default=None, help=None, metavar='ac_file', dest='ac_file')
	param_ac.add_argument('--ac_type', action='store', nargs=1, default=['gaf2'], help=None, metavar='ac_type', dest='ac_type', choices=['gaf2','plain'])
	param_ac.add_argument('--ac_sep', action='store', nargs=1, default=['\t'], help=None, metavar='ac_sep', dest='ac_sep')
	param_ac.add_argument('--ac_termfirst', action='store_const', const=True, default=False, help=None, metavar='ac_termfirst', dest='ac_termfirst')
	param_ac.add_argument('--ac_multiple', action='store_const', const=True, default=False, help=None, metavar='ac_multiple', dest='ac_multiple')
	param_ac.add_argument('--include_tax', action='append', nargs='+', default=None, type=int, help=None, metavar='tax', dest='include_tax')
	param_ac.add_argument('--ignore_tax', action='append', nargs='+', default=None, type=int, help=None, metavar='tax', dest='ignore_tax')
	param_ac.add_argument('--include_EC', action='append', nargs='+', default=None, help=None, metavar='Evidence Code', dest='include_EC')
	param_ac.add_argument('--ignore_EC', action='append', nargs='+', default=None, help=None, metavar='Evidence Code', dest='ignore_EC')

	param_query.add_argument('--query_type', action='store', nargs=1, default=['SS'], choices=['SS', 'stats'], help=None, metavar='query_type', dest='query_type')
	param_query.add_argument('--query_ss_type', action='store', nargs=1, default=['obj'], choices=['obj', 'term', 'termset', 'objset'], help=None, metavar='query_ss_type', dest='query_ss_type')
	param_query.add_argument('--query_mode', action='store', nargs=1, default=['list'], choices=['list', 'pairs'], help=None, metavar='query_mode', dest='query_mode')
	param_query.add_argument('--query_input', action='store', nargs=1, default=['ac'], choices=['ac', 'ontology', 'file', 'terminal'], help=None, metavar='query_input', dest='query_input')
	param_query.add_argument('--query_file', action='store', nargs=1, default=None, help=None, metavar='query_file', dest='query_file')
	param_query.add_argument('--query_file_sep', action='store', nargs=1, default=['\t'], help=None, metavar='query_file_sep', dest='query_file_sep')

	# param_query.add_argument('--query_GOterm', action='store_const', const=['term'], help=params_help['query_GO'], metavar='query_GO', dest='query_type')


	args = parser.parse_args()
	# print(args)
	return args


def parse_parameters(args):
	global ontology_file, ontology_type, ignore_is_a, ignore_part_of, ignore_has_part, ignore_regulates, ontology_file_format
	global EC_include, EC_ignore, tax_include, tax_ignore, ac_file, ac_term_first, ac_separator, ac_type, ac_multiple
	global query_type, query_ss_type, query_mode, query_input, query_file, query_file_sep
	global verbose

	ontology_file = args.ontology_file
	ontology_type = args.ontology_type
	ontology_file_format = args.ontology_file_format
	ignore_is_a = args.ignore_is_a
	ignore_part_of = args.ignore_part_of
	ignore_has_part = args.ignore_has_part
	ignore_regulates = args.ignore_regulates

	verbose = args.verbose

	EC_include = args.include_EC
	EC_ignore = args.ignore_EC
	tax_include = args.include_tax
	tax_ignore = args.ignore_tax
	ac_file = args.ac_file
	ac_term_first = args.ac_termfirst
	ac_separator = args.ac_sep
	ac_type = args.ac_type
	ac_multiple = args.ac_multiple

	if not ontology_file == None:
		ontology_file = ontology_file[0]
	if not ontology_file_format == None:
		ontology_file_format = ontology_file_format[0]
	if not ontology_type == None:
		ontology_type = ontology_type[0]

	if not ac_file == None:
		ac_file = ac_file[0]
	if not ac_separator == None:
		ac_separator = ac_separator[0]
	if not ac_type == None:
		ac_type = ac_type[0]

	query_type = args.query_type
	query_ss_type = args.query_ss_type
	query_mode = args.query_mode
	query_input = args.query_input
	query_file = args.query_file
	query_file_sep = args.query_file_sep

	if not query_type == None:
		query_type = query_type[0]
	if not query_ss_type == None:
		query_ss_type = query_ss_type[0]
	if not query_mode == None:
		query_mode = query_mode[0]
	if not query_input == None:
		query_input = query_input[0]
	if not query_file == None:
		query_file = query_file[0]
	if not query_file_sep == None:
		query_file_sep = query_file_sep[0]
	#

	#-#-#-#-#-#-#-#-#-#-#-#
	# Load Gene Ontology  #
	#-#-#-#-#-#-#-#-#-#-#-#

def load_ontology():
	global ontology_file, ontology_type, ontology_file_format, ignore_is_a, ignore_part_of, ignore_has_part, ignore_regulates

	ontology_ignore = {}
	ontology_ignore['has_part'] = True
	ontology_ignore['is_a'] = False
	ontology_ignore['regulates'] = False
	ontology_ignore['part_of'] = False
	if ignore_regulates:
		ontology_ignore['regulates'] = True
	if not ignore_has_part:
		ontology_ignore['has_part'] = False
	if ignore_is_a:
		ontology_ignore['is_a'] = True
	if ignore_part_of:
		ontology_ignore['part_of'] = True

	fn,fe = os.path.splitext(ontology_file)
	if fe == '.gz':
		ontology_handle = gzip.open(ontology_file, 'rb')
	else:
		ontology_handle = open(ontology_file, 'r')
	# print ontology_file
	# print ontology_ignore
	# print ontology_type
	# print ontology_file_format
	ontology = ontologies.load(ontology_handle, source_type = ontology_file_format, ontology_type = ontology_type, parameters={'ignore':ontology_ignore})
	ontology_handle.close()
	return ontology
#

#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# load Annotation Corpus  #
	#-#-#-#-#-#-#-#-#-#-#-#-#-#

def load_ac():
	global EC_include, EC_ignore, tax_include, tax_ignore, ac_file, ac_term_first, ac_separator, ac_type, ac_multiple
	global ontology

	ac = AnnotationCorpus.AnnotationCorpus(ontology)
	
	is_plain = False
	if ac_type == 'plain':
		is_plain = True

	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# Second step: set parsing parameters
	# You should fill a dictionary with the proper information. Friendly routines will be provided in future to set parsing parameters easily
	# If you specify incorrect or not pertinent parameters they'll be ignored.
	
	#### For gaf-2 / GOA files:
	if not is_plain:
		params = {}
	
		params['filter'] = {} # filter section is useful to remove undesired annotations

		if not EC_include == None:
			params['filter']['EC'] = {} # EC filtering: select annotations depending on their EC
			params['filter']['EC']['EC'] = EC_include # select which EC accept or reject
			params['filter']['EC']['inclusive'] = True # select which EC accept or reject
		if not EC_ignore == None:
			params['filter']['EC'] = {} # EC filtering: select annotations depending on their EC
			params['filter']['EC']['EC'] = EC_ignore # select which EC accept or reject
			params['filter']['EC']['inclusive'] = False # select which EC accept or reject

		if not tax_include == None:
			params['filter']['taxonomy'] = {}
			params['filter']['taxonomy']['taxonomy'] = tax_include # set properly this field to load only annotations involving proteins/genes of a specific species
			params['filter']['taxonomy']['inclusive'] = True # select which EC accept or reject
		if not tax_ignore == None:
			params['filter']['taxonomy'] = {}
			params['filter']['taxonomy']['taxonomy'] = tax_ignore
			params['filter']['taxonomy']['inclusive'] = False # select which EC accept or reject
		
		params['simplify'] = True # after parsing and filtering, removes additional information such as taxonomy or EC. Useful if you have a huge amount of annotations and not enough memory
	
	#### For plain files:
	if is_plain:
		params = {}

		if ac_multiple:
			params['multiple'] = True # Set to True if there are many associations per line (the object in the first field is associated to all the objects in the other fields within the same line)
		if ac_term_first:
			params['term first'] = True # set to True if the first field of each row is a GO term. Set to False if the first field represents a protein/gene
		
		if not ac_separator == None:
			params['separator'] = ac_separator # select the separtor used to divide fields
	
	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# Third Step: parsing
	# just use parse routine. You have to specify the file to parse, the type of file and (optional) the parameters
	if is_plain:
		print "Loading annotation corpus from plain file " + str(ac_file) + "..."
		ac.parse(ac_file, 'plain', params) # to parse plain files
	else:
		print "Loading annotation corpus from gaf-2 file " + str(ac_file) + "..."
		ac.parse(ac_file, 'GOA', params) # to parse gaf-2 / GOA files

	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	#### additional useful annotation corpus routines
	ac.isConsistent() # check whether the annotations are consistent with the current gene ontology. Useful to check if everything is fine
	# ac.sanitize() # removes annotations not consistent with the current gene ontology. USeful if you loaded an annotation corpus BEFORE loading a gene ontology
	return ac
#

	# these 4 variables contain all the useful data:
	#ac.annotations # set of annotations -> it's a dictionary with genes/proteins as keys. The value for each key is a dictionary with GO Terms annotated for that protein as keys
	#ac.reverse_annotations # set of annotations -> it's  adictionary with terms as keys. The value for each key is a dictionary with genes/proteins annotated for that GO Term as keys
	#ac.obj_set # set of proteins/genes involved in annotations
	#ac.term_set # set of GO Terms involved in annotations
#







	#-#-#-#-#-#-#-#-#-#-#-#-#
	# Load Query from File  #
	#-#-#-#-#-#-#-#-#-#-#-#-#

def load_query_from_file(query_file, query_ss_type, query_mode, query_file_sep):
	print "Loading query from file " + str(query_file) + " [type: " + str(query_ss_type) + "] ..."
	
	h = open(query_file,'r')
	query = []
	for line in h:
		line = line.rstrip('\n')
		line = line.rstrip('\r')
		line = line.split(query_file_sep)

		if query_ss_type == 'obj' or query_ss_type == 'term':
			if query_mode == 'pairs':
				if len(line) < 2:
					continue
				for i in range(0,len(line)):
					for j in range(i+1,len(line)):
						query.append((line[i], line[j]))
			elif query_mode == 'list':
				for i in line:
					query.append(i)
			else:
				raise Exception
		elif query_ss_type == 'objset' or query_ss_type == 'termset':
			if query_mode == 'pairs':
				raise Exception
			elif query_mode == 'list':
				newline = []
				for i in line:
					newline.append(i)
				query.append(newline)
			else:
				raise Exception
		else:
			raise Exception
	
	h.close()
	print "-> Query loaded from file: " + str(len(query)) + " entries."
	return query
#






def start():
	global ontology_file, ontology_type, ignore_is_a, ignore_part_of, ignore_has_part, ignore_regulates, ontology_file_format
	global EC_include, EC_ignore, tax_include, tax_ignore, ac_file, ac_term_first, ac_separator, ac_type, ac_multiple
	global query_type, query_ss_type, query_mode, query_input, query_file, query_file_sep
	global ontology, ac, query
	global verbose

	program_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
	args = parse_args()
	parse_parameters(args)

	if ontology_type == None:
		ontology_type = "Ontology"
	if ontology_file_format == None:
		ontology_file_format = 'obo'

	# print("->Loading ontology\t\t" + str(ontology_file))
	if not ontology_file == 'None':
		ontology = load_ontology()
	# print "-> Ontology correctly loaded: " + str(ontology.node_number()) + " nodes and " +  str(ontology.edge_number()) + " edges."
	# print("->Loading AC\t\t" + str(ac_file))
		ac = load_ac()
	# print ac.annotations
	# print "-> Annotation Corpus correctly loaded: " + str(len(ac.obj_set)) + " objects and " +  str(len(ac.term_set)) + " GO Terms."

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - 

	if query_type == 'SS':

		# if query_ss_type == ['obj', 'term', 'termset', 'objset']

		if query_input == 'ac':
			query = ac.annotations.keys()
		#

		elif query_input == 'ontology':
			if query_ss_type == 'obj':
				query = ac.reverse_annotations.keys()
			elif query_ss_type == 'term':
				query = ontology.nodes.keys()
			else:
				raise Exception
			print "Take care of different ontology roots!"
		#

		elif query_input == 'file':
			query = load_query_from_file(query_file, query_ss_type, query_mode, query_file_sep)
		#

		elif query_input == 'terminal':
			pass
		#

		else:
			raise Exception
		#
		print query
	#

	elif query_type == 'stats':
		pass
	#

	else:
		raise Exception
	#
	sys.exit()
#

if __name__ == "__main__":
	start()
#
