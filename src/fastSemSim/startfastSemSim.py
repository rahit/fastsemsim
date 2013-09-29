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

from fastSemSim.Ontology import AnnotationCorpus
from fastSemSim.Ontology import ontologies
from fastSemSim.SemSim import ObjSemSim
from fastSemSim.SemSim import TermSemSim
from fastSemSim.fastResnik import fastResnikSemSim
from fastSemSim.SemSim import SemSimMeasures
from fastSemSim.SemSim import SemSimUtils
from fastSemSim.SemSim import TermSemSim

import sys
import os
import math
import gzip

import argparse

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # 
params_help = dict()

params_help['ontology'] = 'Ontology. DAG of terms linked in a semantic hierarchy.'
params_help['ontology_file'] = 'File containing the ontology of interest. Only obo and obo-xml formats are currently supported (either gzipped or not). If not provided, a default ontology included in FastSemSim will be used, according to the value of ontology_type parameter.'
params_help['ontology_type'] = 'Ontology type. Currently supported ontologies are: \'generic\', \'GeneOntology\', \'CellOntology\', and \'DiseaseOntology\'. [default: GeneOntology]'
params_help['ontology_file_format'] = 'Ontology file type. Can be either \'obo\' or \'obo-xml\'. Compressed version is automatically detected if the file ends with .tar.gz or tar.bz2 extensions. WARNING: Reading compressed obo files tend to be a really slow process (might take more than 4 minutes to load the Gene Ontology). Compressed obo-xml files, instead, work well.  [default: obo]'
params_help['ignore_has_part'] = 'Whether consider or ignore has_part relationships [default:True]'
params_help['ignore_is_a'] = 'Whether consider or ignore is_a relationships [default:False]'
params_help['ignore_part_of'] = 'Whether consider or ignore part_of relationships [default:False]'
params_help['ignore_regulates'] = 'Whether consider or ignore regulates relationships [default:False]'

params_help['ac'] = 'Annotation Corpus. Associations between objects and terms in the ontology.'
params_help['ac_file'] = 'File containing the Annotation Corpus (AC). g/bzip compressed files are supported, and the file extension must be .tar.bz2 or tar.gz.'
params_help['ac_type'] = 'Format of AC file. Currently supported formats are "plain" and "gaf2". [default: gaf2]'
params_help['ac_sep'] = 'Separator used in plain AC files. Use "s" or " " (with quotes) for space, and "t" or \\t for tab. [Default: tab] (plain AC files only)'
params_help['ac_multiple'] = 'If specified, each line of AC file can contain more than a Term or Entry. (plain AC files only)'
params_help['ac_termfirst'] = 'If specified, plain AC files will be interpreted assuming that the first field of each line is an ontology term, and the following fields are the associated entries [the standard behavior is to consider the first field as an entry, and following fields as associated ontology terms. (plain AC files only)'
params_help['include_tax'] = 'If specified, consider only taxonomies specified. Taxonomies must be specified using integer ids. (gaf2 AC files only)'
params_help['ignore_tax'] = 'If specified, ignores the taxonomies specified. Used only with gaf2 files. Taxonomies must be specified using integer ids. This parameter is ignored if --include_tax is specified. (gaf2 AC files only)'
params_help['include_EC'] = 'Defines the Evidence Codes (EC) that will be accepted when loading the annotation corpus. For instance, \'IEA\' allows Electronically inferred annotations to be included in thge annotation corpus. (gaf2 AC files only)'
params_help['ignore_EC'] = 'Specifies which types of annotation will be ignored. (i.e.: --ignore_EC IEA means that IEA annotations will be ignored). This parameter is ignored if --include_EC is specified. (gaf2 AC files only)'

params_help['query'] = 'Query. Parameters and data defining the task that fastSemSim should perform.'
params_help['query_type'] = 'Instruct fastSemSim on the task to accomplish. Current supported tasks are: evaluation of Semantic Similarity (SS) between pairs or sets of ontology terms (\'term\'), evaluation of Semantic Similarity (SS) between pairs or sets of objects annotated with ontology terms (\'ac\'), and the evaluation of ontology terms\' Information Content (\'IC\'). [default: \'ac\']'
params_help['query_mode'] = 'Whether Semantic Similarity should be calculated between pairs of entries, or between all the input  Either all, list or pairs. all: same as query_all. pairs: Whether the input query should be considered as a set of pairs \'pair\', or a list of entries \'list\'. In the former case, evaluates semantic similarity scores of each pair; in the latter, instead, each entry is compared to each other. [\'list\' is the default] (considered only when query_type is either ac or term)'
params_help['query_file'] = 'Specifies the file with the query. If not specified, the behavior will be the same as if -u is used.'
params_help['query_sep'] = 'Character used in query file to separate query entries. Use "s" for space, and "t" for tab. [Default: tab]'
params_help['query_all'] = 'Use all the entries in the annotation corpus/ontology to build the query. Automatically sets query_mode to list'
# params_help['query_ontology'] = 'Evaluate the semantic similarity between GO Terms. The query file should contain GO Term entries instead of proteins/genes. The GO category is ignored, but the GO Terms must come from the same category.'

params_help['ss'] = 'Semantic Similarity settings.'
params_help['ss_category'] = 'The ontology category/namespace to use, if any. It must be one of the roots of the ontology. If not specified, one of the roots of the ontology will be used at random.'
params_help['ss_enhanced'] = 'Use the fast implementation of the semantic similarity measure. Currently only Resnik max is supported. Forces -l and -u. Overrides -p and -q. This limitation will be removed in the future.'
params_help['ss_mix'] = 'The mixing strategy to use (if the SS measure requires it). [Default: BMA]. Can be "max", "BMA", or "avg".'
params_help['ss_measure'] = "The semantic similarity measure to use. Can be 'Resnik','SimGIC','Lin','Jiang and Conrath','SimIC','Dice','TO','NTO','Jaccard','Czekanowski-Dice','Cosine','G-SESAME', .... [Default: Resnik]"

params_help['output'] = 'Output parameters'
params_help['output_file'] = 'Output file. If not specified, results will be printed on the console.'
params_help['output_cut'] = 'Do not print/save pairs whose semantic similarity is smaller or equal to the specified threshold. This drastically reduces the size of output data for whole proteome comparison. If not specified, all numeric output data will be stored/written.'
params_help['output_remove_nan'] = 'Do not print/save pairs without semantic similarity (otherwise a "None" score is assigned). This drastically reduces the size of output data for whole proteome comparison. If not specified, all output data will be stored/written.'

params_help['advanced'] = 'Advanced parameters'
params_help['IC_table_form_file'] = 'Load Information Content values of GO Terms from an external file.'
params_help['verbose'] = 'Verbosity level. Repeat multiple time to increase verbosity level (i.e. -vvv)'


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

	param_ontology = parser.add_argument_group(title='Ontology', description=params_help['ontology'])
	param_ac = parser.add_argument_group(title='Annotation Corpus (AC)', description=params_help['ac'])
	param_ss = parser.add_argument_group(title='Semantic Similarity (SS)', description=params_help['ss'])
	param_query = parser.add_argument_group(title='Query', description=params_help['query'])
	param_output = parser.add_argument_group(title='Output parameters', description=params_help['output'])
	param_extended = parser.add_argument_group(title='Advanced parameters', description=params_help['advanced'])

	param_ontology.add_argument('--ontology', '--ontology_file', '-o', action='store', nargs=1, default=None, help=params_help['ontology_file'], metavar='ontology_file', dest='ontology_file')
	param_ontology.add_argument('--ontology_file_format', action='store', nargs=1, default=None, help=params_help['ontology_file_format'], metavar='ontology_file_format', dest='ontology_file_format')
	param_ontology.add_argument('--ontology_type', action='store', nargs=1, default='GeneOntology', help=params_help['ontology_type'], metavar='ontology_type', dest='ontology_type')
	param_ontology.add_argument('--ignore_has_part', action='store', nargs='?', default=True, type=prbool, help=params_help['ignore_has_part'], metavar='ignore_has_part', dest='ignore_has_part')
	param_ontology.add_argument('--ignore_is_a', action='store', nargs='?', default=False, type=prbool, help=params_help['ignore_is_a'], metavar='ignore_is_a', dest='ignore_is_a')
	param_ontology.add_argument('--ignore_part_of', action='store', nargs='?', default=False, type=prbool, help=params_help['ignore_part_of'], metavar='ignore_part_of', dest='ignore_part_of')
	param_ontology.add_argument('--ignore_regulates', action='store', nargs='?', default=False, type=prbool, help=params_help['ignore_regulates'], metavar='ignore_regulates', dest='ignore_regulates')

	param_ac.add_argument('-a','--ac', '--ac_file', action='store', nargs=1, default=None, help=params_help['ac_file'], metavar='ac_file', dest='ac_file')
	param_ac.add_argument('--ac_type', action='store', nargs=1, default=['gaf2'], help=params_help['ac_type'], metavar='ac_type', dest='ac_type', choices=['gaf2','plain'])
	param_ac.add_argument('--ac_sep', action='store', nargs=1, default=['\t'], help=params_help['ac_sep'], metavar='ac_sep', dest='ac_sep')
	param_ac.add_argument('--ac_termfirst', action='store_const', const=True, default=False, help=params_help['ac_termfirst'], metavar='ac_termfirst', dest='ac_termfirst')
	param_ac.add_argument('--ac_multiple', action='store_const', const=True, default=False, help=params_help['ac_multiple'], metavar='ac_multiple', dest='ac_multiple')
	param_ac.add_argument('--include_tax', action='append', nargs='+', default=None, type=int, help=params_help['include_tax'], metavar='tax', dest='include_tax')
	param_ac.add_argument('--ignore_tax', action='append', nargs='+', default=None, type=int, help=params_help['ignore_tax'], metavar='tax', dest='ignore_tax')
	param_ac.add_argument('--include_EC', action='append', nargs='+', default=None, help=params_help['include_EC'], metavar='Evidence Code', dest='include_EC')
	param_ac.add_argument('--ignore_EC', action='append', nargs='+', default=None, help=params_help['ignore_EC'], metavar='Evidence Code', dest='ignore_EC')

	param_query.add_argument('--query_type', action='store', nargs=1, default=[None], choices=['ac', 'term', 'IC'], help=params_help['query_type'], metavar='query_type', dest='query_type')
	param_query.add_argument('--query_mode', action='store', nargs=1, default=['all'], choices=['all', 'list', 'pairs'], help=params_help['query_mode'], metavar='query_mode', dest='query_mode')
	param_query.add_argument('--query_file', action='store', nargs=1, default=None, help=params_help['query_file'], metavar='query_file', dest='query_file')
	param_query.add_argument('--query_sep', action='store', nargs=1, default=['\t'], help=params_help['query_sep'], metavar='query_sep', dest='query_sep')
	param_query.add_argument('--query_all', action='store_const', const=['all'], help=params_help['query_all'], metavar='query_all', dest='query_mode')
	# param_query.add_argument('--query_GOterm', action='store_const', const=['term'], help=params_help['query_GO'], metavar='query_GO', dest='query_type')

	param_ss.add_argument('--ss', '-s', action='store', nargs=1, default=['Resnik'], help=params_help['ss_measure'], metavar='ss_measure', dest='ss_measure')
	param_ss.add_argument('--mix', '-m', action='store', nargs=1, default=['BMA'], help=params_help['ss_mix'], metavar='ss_mix', dest='ss_mix')
	param_ss.add_argument('--root', '-ontology_root', action='store', nargs=1, default=None, help=params_help['ss_category'], metavar='ss_category', dest='ss_category')
	param_ss.add_argument('--enhanced', action='store_const', const=True, default=False, help=params_help['ss_enhanced'], metavar='ss_enhanced', dest='ss_enhanced')

	param_output.add_argument('--cut', action='store', nargs=1, default=None, type=float, help=params_help['output_cut'], metavar='output_cut', dest='output_cut')
	param_output.add_argument('--remove_nan', action='store', nargs=1, default=False, type=prbool, help=params_help['output_remove_nan'], metavar='output_remove_nan', dest='output_remove_nan')
	param_output.add_argument('--output_file', action='store', nargs=1, default=None, help=params_help['output_file'], metavar='output_file', dest='output_file')

	param_extended.add_argument('--IC_table', '--IC_table_form_file', action='store', nargs=1, default=None, help=params_help['IC_table_form_file'], metavar='IC_table', dest='IC_table')
	param_extended.add_argument('--verbose', '-v', action='count', default=None, help=params_help['verbose'], dest='verbose')

	args = parser.parse_args()
	print(args)
	return args
#

def parse_parameters(args):
	# global input parameters
	global ontology_file, ontology_type, ontology_file_format, ignore_is_a, ignore_part_of, ignore_has_part, ignore_regulates
	global EC_include, EC_ignore, tax_include, tax_ignore, ac_file, ac_term_first, ac_separator, ac_type, ac_multiple
	global use_enhanced
	global ss_root, ss_mix, ss_measure
	global query_mode, query_type, query_file, query_separator
	global cut_thres, out_file, cut_nan
	global verbose, ext_IC_table


	ontology_file = args.ontology_file
	ontology_type = args.ontology_type
	ontology_file_format = args.ontology_file_format
	ignore_is_a = args.ignore_is_a
	ignore_part_of = args.ignore_part_of
	ignore_has_part = args.ignore_has_part
	ignore_regulates = args.ignore_regulates

	EC_include = args.include_EC
	EC_ignore = args.ignore_EC
	tax_include = args.include_tax
	tax_ignore = args.ignore_tax
	ac_file = args.ac_file
	ac_term_first = args.ac_termfirst
	ac_separator = args.ac_sep
	ac_type = args.ac_type
	ac_multiple = args.ac_multiple

	query_type = args.query_type
	query_mode = args.query_mode
	query_separator = args.query_sep
	query_file = args.query_file

	ss_root = args.ss_category
	use_enhanced = args.ss_enhanced
	ss_mix = args.ss_mix
	ss_measure = args.ss_measure

	cut_thres = args.output_cut
	out_file = args.output_file
	cut_nan = args.output_remove_nan
	
	verbose = args.verbose
	ext_IC_table = args.IC_table

	if not query_type == None:
		query_type = query_type[0]
	if not query_mode == None:
		query_mode = query_mode[0]
	if not query_separator == None:
		query_separator = query_separator[0]
	if not query_file == None:
		query_file = query_file[0]

	if not ac_file == None:
		ac_file = ac_file[0]
	if not ac_separator == None:
		ac_separator = ac_separator[0]
	if not ac_type == None:
		ac_type = ac_type[0]


	if not cut_thres == None:
		cut_thres = cut_thres[0]
	if not out_file == None:
		out_file = out_file[0]

	if not ontology_file == None:
		ontology_file = ontology_file[0]
	if not ontology_file_format == None:
		ontology_file_format = ontology_file_format[0]
	if not ontology_type == None:
		ontology_type = ontology_type[0]
	if not ss_root == None:
		ss_root = ss_root[0]
	if not ss_mix == None:
		ss_mix = ss_mix[0]
	if not ss_measure == None:
		ss_measure = ss_measure[0]

	if not ext_IC_table == None:
		ext_IC_table = ext_IC_table[0]
#

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # 












	#-#-#-#-#-#-#-#-#-#
	# Load Ontology   #
	#-#-#-#-#-#-#-#-#-#

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
	
def init_ss():
	global ss_mix, ss_measure, ss_params
	global ontology, ac
	# Semantic similarity between Genes/proteins 
	# The basic approach here is to create a "SemSim" object with some fixed parameters, and then use it to evaluate the semantic similarity between paris of proteins/genes

	#### First step: create a SemSim object
	# You must create an ObjSemSim object providing the following parameters:
	# 1) annotation corpus, 2) gene ontology, 3) pairwise or goupwise term semantic similarity name, 4)mixing strategy (only for pairwise term semantic similarity measures), 5 (optional) additional parameters

	print "Initializing Semantic Similarity class..."
	ss = ObjSemSim.ObjSemSim(ac, ontology, ss_measure, ss_mix, ss_params)
	print "-> Semantic Similarity class ready"
	return ss
#


def init_term_ss():
	global ss_mix, ss_measure, ss_params
	global ontology, ac

	# Semantic similarity between Genes/proteins 
	# The basic approach here is to create a "SemSim" object with some fixed parameters, and then use it to evaluate the semantic similarity between paris of proteins/genes

	#### First step: create a SemSim object
	# You must create an ObjSemSim object providing the following parameters:
	# 1) annotation corpus, 2) gene ontology, 3) pairwise or goupwise term semantic similarity name, 4)mixing strategy (only for pairwise term semantic similarity measures), 5 (optional) additional parameters
	print "Initializing Semantic Similarity class..."
	try:
		TermSemSimClass = SemSimMeasures.selectTermSemSim(ss_measure)
		TSS = TermSemSimClass(ac, ontology)
	except TermSemSim.MissingAcException as e:
		print e.message
		return None
	return TSS
#



#### Second step: use the ObjSemSim object to determine the semantic similarity between two proteins
	# You have to specify the GO Category to use ("MF", "BP", "CC") and the names of the two proteins. If the proteins or the category are not valid or not present in the annotation corpus, then None will be returned
#









	#-#-#-#-#-#-#-#-#
	# Pairs Sem Sim #
	#-#-#-#-#-#-#-#-#

def ss_pairs(SS, pairs, ontology, out, cut_thres = None, cut_none=False):
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
			if temp == None or temp <= cut_thres:
				continue
			if cut_none:
				if temp == None:
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

def ss_term_pairs(SS, pairs, ontology, out, cut_thres = None, cut_none=False):
	print "Evluating semantic similarity between " + str(len(pairs)) + " pairs."
	scores = []
	done = 0
	total = len(pairs)
	if verbose:
		prev_text = ""
		sys.stdout.write("Done: ")
		sys.stdout.flush()
	for i in range(0,len(pairs)):
		temp = SS.SemSim(pairs[i][0],pairs[i][1])
		#scores.append((pairs[i][0],pairs[i][1],temp))
		done+=1
		if not cut_thres == None:
			if temp == None or temp <= cut_thres:
				continue
			if cut_none:
				if temp == None:
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

def ss_pairwise(SS, pairs, ontology, out, cut_thres = None, cut_none=False):
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
				if temp == None or temp <= cut_thres:
					continue
			if cut_none:
				if temp == None:
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


def ss_term_pairwise(SS, pairs, ontology, out, cut_thres = None, cut_none=False):
	print "Evluating pairwise semantic similarity between " + str(len(pairs)) + " GO Terms (" + str(len(pairs)*(len(pairs)-1)/2) + " pairs)"
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
			temp = SS.SemSim(pairs[i],pairs[j])
			#scores[pairs[i]][pairs[j]] = temp
			done+=1
			if not cut_thres == None:
				if temp == None or temp <= cut_thres:
					continue
			if cut_none:
				if temp == None:
					continue
			if out == None:
				print str(pairs[i]) + "\t" + str(pairs[j]) + "\t" + str(temp)
			else:
				out.write(pairs[i] + "\t" + pairs[j] + "\t" + str(temp) + "\n")
				if verbose:
					sys.stdout.write("\b"*len(prev_text))
					prev_text = str(done) + ' [%.4f' % (100*done/float(total)) + " %]"
					sys.stdout.write(prev_text)
					sys.stdout.flush()
	#return scores
#

def print_IC(IC, query, out, cut_thres=None, cut_nan=False):
	# print "Evluating pairwise semantic similarity between " + str(len(pairs)) + " GO Terms (" + str(len(pairs)*(len(pairs)-1)/2) + " pairs)"
	# scores = {}
	done = 0
	# total = len(pairs)*(len(pairs)-1)/2

	# if verbose:
	# 	prev_text = ""
	# 	sys.stdout.write("Done: ")
	# 	sys.stdout.flush()
	for j in range(0,len(query)):
		i = query[j]
		# scores[pairs[i]] = {}
		# for j in range(i+1,len(pairs)):
		# temp = SS.SemSim(pairs[i],pairs[j])
		#scores[pairs[i]][pairs[j]] = temp
		if i not in IC:
			continue
		done+=1
		temp = IC[i]
		if not cut_thres == None:
			if temp == None or temp <= cut_thres:
				continue
		if cut_nan:
			if temp == None:
				continue
		if out == None:
			print str(GeneOntology.go_id2name(i)) + "\t" + str(temp)
		else:
			out.write(str(GeneOntology.go_id2name(i)) + "\t" + str(temp) + "\n")
			# if verbose:
			# 	sys.stdout.write("\b"*len(prev_text))
			# 	prev_text = str(done) + ' [%.4f' % (100*done/float(total)) + " %]"
			# 	sys.stdout.write(prev_text)
			# 	sys.stdout.flush()
	#return scores
#


	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# Process several files within a single folder  #
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


#def int_do():
	#ss_pairwise(SS, query, ontology, h)

#def do_test(wf='log_Tempi.txt'):
def do_test():
	#global query

	if not out_file == None:
		if not os.path.exists(out_file):
			os.makedirs(out_file)

	#tempi = []
	#t = timeit.Timer(int_do)
	dirList=os.listdir(query_dir)
	
	for fname in dirList:
		print fname
		query = load_query_from_file(query_dir+"/"+fname, query_type, query_separator)
		h = None
		#h = open("/dev/null", 'w')
		
		h = open(out_file + "/" + os.path.splitext(fname) + '.ss', 'w')
		
		#tt = time.clock()
		ss_pairwise(SS, query, ontology, h)
		#tt = time.clock() - tt
		
		#tempi.append((fname,tt))
		#print(tt)
		if not h == None:
			h.close()
	#h = open(wf, 'w')
	#for i in tempi:
		#h.write(str(i[0]) + "\t" + str(i[1]) + "\n")
	#h.close()
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

def load_IC_from_file(list_file, separator = '\t'):
	# print "Loading query from file " + str(list_file) + " [type: " + str(f_type) + "] ..."
	
	h = open(list_file,'r')
	IC = {}
	for line in h:
		line = line.rstrip('\n')
		line = line.rstrip('\r')
		line = line.rsplit(separator)
		if not str(line[1]) == 'None': 
			line[1] = float(line[1])
		IC[GeneOntology.go_name2id(line[0])] = line[1]

	h.close()
	print "-> IC loaded from file: " + str(len(IC)) + " entries."
	return IC
#




	#-#-#-#-#-#-#-#-#-#-#-#-#
	# Load Query from File  #
	#-#-#-#-#-#-#-#-#-#-#-#-#

def load_query_from_ac(ac):
	query = ac.obj_set.keys()
	print "-> Query loaded from Annotation Corpus: " + str(len(query)) + " entries."
	return query
#

def load_query_from_SS(SS, ontology=None):
	#print ontology
	#print SS.util.BP_ontology
	#print SS.util.MF_ontology
	#print SS.util.CC_ontology
	if ontology == SS.util.BP_ontology:
		query = list(SS.util.offspring[SS.util.go.BP_root])
	elif ontology == SS.util.MF_ontology:
		query = list(SS.util.offspring[SS.util.go.MF_root])
	elif ontology == SS.util.CC_ontology:
		query = list(SS.util.offspring[SS.util.go.CC_root])
	elif ontology == None:
		query = list(SS.util.offspring[SS.util.go.BP_root])
		query.extend(list(SS.util.offspring[SS.util.go.MF_root]))
		query.extend(list(SS.util.offspring[SS.util.go.CC_root]))
	else:
		return None
	#print str(query)
	print "-> Query loaded from the Gene Ontology: " + str(len(query)) + " entries."
	
	return query
#

def load_query_from_util(util, ontology=None):
	#print ontology
	#print SS.util.BP_ontology
	#print SS.util.MF_ontology
	#print SS.util.CC_ontology
	if ontology == util.BP_ontology:
		query = list(util.offspring[util.go.BP_root])
	elif ontology == util.MF_ontology:
		query = list(util.offspring[util.go.MF_root])
	elif ontology == util.CC_ontology:
		query = list(util.offspring[util.go.CC_root])
	elif ontology == None:
		query = list(util.offspring[util.go.BP_root])
		query.extend(list(util.offspring[util.go.MF_root]))
		query.extend(list(util.offspring[util.go.CC_root]))
	else:
		return None
	#print str(query)
	print "-> Query loaded from the Gene Ontology: " + str(len(query)) + " entries."
	
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



def ss_pairwise_enhanced(SS, pairs = None, ontology = 'BP', out = None, cut_thres = None, cut_none = False):
	#print "Evluating pairwise semantic similarity between " + str(len(pairs)) + " entities (" + str(len(pairs)*(len(pairs)-1)/2) + " pairs)"
	out_h = out
	if out==None:
		out_h = sys.stdout
	tct = cut_thres
	if cut_none and cut_thres == None:
		tct = -1
	SS.SemSim(ontology, out, tct)
#



####----####----####----####----####----####----####----####----####----####----####----####----####----####----####----####----



def print_usage():
	h = open(program_dir + "/fastSemSim_commandline.txt", 'r')
	for i in h:
		i = i.rstrip("\n")
		i = i.rstrip("\r")
		i = i.rstrip("\n")
		print(i)
	h.close()
#








def start():
	# global input parameter variables
	global ontology_file, ontology_type, ontology_file_format, ignore_is_a, ignore_part_of, ignore_has_part, ignore_regulates
	global EC_include, EC_ignore, tax_include, tax_ignore, ac_file, ac_term_first, ac_separator, ac_type, ac_multiple
	global use_enhanced
	global ss_root, ss_mix, ss_measure
	global query_mode, query_type, query_file, query_separator
	global cut_thres, out_file, cut_nan
	global verbose, ext_IC_table
	# global variables
	global ontology, ac, query, ss
	global program_dir

	program_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
	#program_dir = '.' # use this with py2exe to build a working binary

	args = parse_args()
	parse_parameters(args)


	if ontology_file == None:
		ontology_file = program_dir + "/data/GO_filtered_2013.07.26.obo-xml.gz"
	if ontology_type == None:
		ontology_type = "GeneOntology"
	if ontology_file_format == None:
		ontology_file_format = 'obo-xml'


	query_dir = None
	# check if enhanced mode has been selected
	if use_enhanced:
		query_mode = 'all'
		ss_measure = 'Resnik'
		ss_mix = 'max'
		query_type = 'ac'

	if query_type == None:
		if ac_file == None:
			query_type = 'term'
		else:
			query_type = 'ac'

	if query_type == 'ac':
		if ac_file == None:
			print "An annotation corpus is required in " + query_type + "mode. See the help notes (ac_file parameter)"
			sys.exit()
		if ontology_file == None:
			print "A category of GO must be selected in " + query_type + "mode. See the help notes (ontology parameter)"
			sys.exit()
	elif query_type == 'IC':
		if ac_file == None:
			print "An annotation corpus is required in " + query_type + "mode. See the help notes (ac_file parameter)"
			sys.exit()
	elif query_type == 'term':
		if ontology_file == None:
			print "A category of GO must be selected in " + query_type + "mode. See the help notes (ontology parameter)"
			sys.exit()
	else:
		print "Unrecognized query_type " + query_type
		sys.exit()	

	if not query_mode == 'all':
		if query_file == None and query_dir == None:
			print "A query must to be specified in " + str(query_mode) + ". See help notes for further details."
			sys.exit()

	if not EC_include == None:
		EC_ignore = None
	if not tax_include == None:
		tax_ignore = None

	print("-----------------------------------------------")
	print("FastSemSim 0.8 - Copyright 2011-2013 Marco Mina")
	print("-----------------------------------------------")
	print("Gene Ontology:\t\t" + str(ontology_file))
	print("Annotation Corpus:\t\t" + str(ac_file))
	print("Annotation Corpus type:\t" + str(ac_type))
	if ac_type == 'gaf2':
		print("Consider EC:\t\t\t" + str(EC_include))
		print("Ignore EC:\t\t\t" + str(EC_ignore))
		print("Consider Taxonomy:\t\t" + str(tax_include))
		print("Ignore Taxonomy:\t\t" + str(tax_ignore))
	elif ac_type == 'plain':
		if ac_term_first:
			print("AC Row format:\t\t\tGO Term -> Entry")
		else:
			print("AC Row format:\t\t\tEntry -> GO Term")
		print("Many associations per line:\t" + str(ac_multiple))
	print("Query type: \t\t\t" + str(query_type))
	if query_mode == 'all':
		print("Query mode: \t\t\tfrom Annotation Corpus")
	else:
		print("Query mode: \t\t\t" + query_mode)
		print("Query file: \t\t" + str(query_file))
		print("Query file separator: \t\t\'" + str(query_separator) + "\'")
	if not out_file == None:
		print("Output file: \t\t\t" + str(out_file))
	else:
		print("Output \t\t\t\tto console")
	print("SS measure: \t\t\t" + str(ss_measure) + " " + str(ss_mix))
	print("GO category: \t\t\t" + str(ss_root))
	print("Using enhanced version:\t\t" + str(use_enhanced))
	print("-----------------------------------------------")

	print "-> Loading Gene Ontology from " + str(ontology_file) + "..."
	ontology = load_ontology()
	print "-> Ontology correctly loaded: " + str(ontology.node_number()) + " nodes and " +  str(ontology.edge_number()) + " edges."

	ac = None
	if not ac_file == None:
		ac = load_ac()


	if query_type == 'term':
		ss = init_term_ss(ontology, ac, ss_measure, ss_mix)
		if ss == None:
			sys.exit()

		if not ext_IC_table == None:
			print 'Injecting GO terms IC from ' + ext_IC_table
			ext_IC = load_IC_from_file(ext_IC_table)
			ss.util.IC = ext_IC

		if query_mode == 'all':
			query = load_query_from_SS(ss, ontology_root)
		else:
			query = load_query_from_file(query_file, query_mode, query_separator)

		h = None
		if not out_file == None:
			h = open(out_file, 'w')
		if query_mode == 'pairs':
			ss_term_pairs(ss, query, ontology, h, cut_thres, cut_nan)
		else:
			ss_term_pairwise(ss, query, ontology, h, cut_thres, cut_nan)
		if not h == None:
			h.close()
		sys.exit()
	#

	elif query_type == 'ac':
		if not use_enhanced:
			ss = init_ss(ontology, ac, ss_measure, ss_mix)
		else:
			ss = init_enhanced_ss(ontology, ac, ss_measure, ss_mix)

		if not ext_IC_table == None:
			ext_IC = load_IC_from_file(ext_IC_table)
			# print 'Read from IC table not yet implemented.'
			SS.util.IC = ext_IC
		#if not query_dir == None:
			#do_test(out_file)
			#sys.exit()
			
		if query_mode == 'all':
			query = load_query_from_ac(ac)
		else:
			query = load_query_from_file(query_file, query_mode, query_separator)
		h = None
		if not out_file == None:
			h = open(out_file, 'w')
			
		if use_enhanced:
			ss_pairwise_enhanced(SS, query, ontology, h, cut_thres, cut_nan)
		elif query_mode == 'pairs':
			ss_pairs(SS, query, ontology, h, cut_thres, cut_nan)
		else:
			ss_pairwise(ss, query, ontology, h, cut_thres, cut_nan)
		if not h == None:
			h.close()
		sys.exit()
	#

	elif query_type == 'IC':
			util = SemSimUtils.SemSimUtils(ac, ontology)
			util.det_IC_table()

			if query_mode == 'all':
				query = load_query_from_util(util, ontology)
			else:
				query = load_query_from_file(query_file, query_mode, query_separator)

			h = None
			if not out_file == None:
				h = open(out_file, 'w')
			print_IC(util.IC, query, h, cut_thres, cut_nan)
			if not h == None:
				h.close()
			sys.exit()
	#

	else: # query_type == 'term'
		raise Exception		

#

if __name__ == "__main__":
	start()
#
