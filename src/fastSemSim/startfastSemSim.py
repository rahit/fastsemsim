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
from fastSemSim.SemSim import SemSimMeasures
from fastSemSim.SemSim import ObjSemSim
from fastSemSim.SemSim import ObjSetSemSim
from fastSemSim.SemSim import SetSemSim

from fastSemSim.fastResnik import fastResnikSemSim
# from fastSemSim.SemSim import SemSimUtils

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
params_help['query_type'] = 'Instruct fastSemSim on the task to accomplish. Current supported tasks are: \'SS\', evaluation of Semantic Similarity (SS), and \'stats\', that is extraction of statistics. [default: \'SS\']'
params_help['query_ss_type'] = 'Current supported query types for SS are: evaluation of Semantic Similarity (SS) between pairs of ontology terms (\'term\'), sets of ontology terms (\'termset\'), pairs of objects annotated with ontology terms (\'obj\'), and sets of objects annotated with ontology terms (\'objset\'). [default: \'term\']'
params_help['query_mode'] = 'Whether input query is supplied as pairs of entries or a list of entries. \'pair\': input query should be considered as a set of pairs. \'list\': consier input as a list of entries. In the former case fastSemSim evaluates semantic similarity scores of each pair; in the latter, instead, each entry is compared to each other. [default: \'list\']'
params_help['query_input'] = 'Query input mode. Can be \'ontology\', \'ac\', or \'file\'. [default: \'ac\']'
params_help['query_file'] = 'File with the input query.'
params_help['query_file_sep'] = 'Character used in query file to separate entries. Use \'s\' for space, and \'t\' for tab. [Default: \'t\' (tab)]'

params_help['ss'] = 'Semantic Similarity settings.'
params_help['tss_measure'] = "Semantic similarity measure to use between ontology terms. Can be 'Resnik','SimGIC','Lin','Jiang and Conrath','SimIC','Dice','TO','NTO','Jaccard','Czekanowski-Dice','Cosine','G-SESAME', .... [Default: Resnik]"
params_help['tss_mix'] = 'The mixing strategy to use when merging term SSs. (if term SS measure requires it). Can be "max", "BMA" (best match average), or "avg". [Default: BMA]'
# params_help['oss_measure'] = "Semantic similarity measure to use between objects. [Default: Resnik]"
# params_help['oss_mix'] = 'The mixing strategy to use when merging obj SSs. (if object SS measure requires it). Can be "max", "BMA" (best match average), or "avg". [Default: BMA]'
params_help['ss_category'] = 'The ontology category/namespace to use, if any. It must be one of the roots of the ontology. If not specified, one of the roots of the ontology will be used at random.'
params_help['ss_enhanced'] = 'Use the fast implementation of the semantic similarity measure. Currently only Resnik max is supported. Forces -l and -u. Overrides -p and -q. This limitation will be removed in the future.'

params_help['output'] = 'Output parameters'
params_help['output_file'] = 'Output file. If not specified, results will be printed on the console.'
params_help['output_cut'] = 'Do not print/save pairs whose semantic similarity is smaller or equal to the specified threshold. This drastically reduces the size of output data for whole proteome comparison. If not specified, all numeric output data will be stored/written.'
params_help['output_remove_nan'] = 'Do not print/save pairs without semantic similarity (otherwise a "None" score is assigned). This drastically reduces the size of output data for whole proteome comparison. If not specified, all output data will be stored/written.'

params_help['advanced'] = 'Advanced parameters'
params_help['IC_table_form_file'] = 'Load Information Content values of GO Terms from an external file.'
params_help['load_params'] = 'Load parameters from the specified file. Additional  parameters specified in the command line overwrite those loaded from the file.'
params_help['save_params'] = 'Save parameters to the specified file.'
params_help['verbose'] = 'Verbosity level. Repeat multiple time to increase verbosity level (i.e. -vvv)'


	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# Cmd line parameter parsing  #
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def print_err(*args):
    sys.stderr.write(' '.join(map(str,args)) + '\n')

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
	param_ontology.add_argument('--ontology_file_format','--o_file_format', action='store', nargs=1, default=None, help=params_help['ontology_file_format'], metavar='ontology_file_format', dest='ontology_file_format')
	param_ontology.add_argument('--ontology_type', '--o_type', action='store', nargs=1, default='GeneOntology', help=params_help['ontology_type'], metavar='ontology_type', dest='ontology_type')
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

	param_query.add_argument('--query_type', action='store', nargs=1, default=['SS'], choices=['SS', 'stats'], help=params_help['query_type'], metavar='query_type', dest='query_type')
	param_query.add_argument('--query_ss_type', action='store', nargs=1, default=['obj'], choices=['obj', 'term', 'termset', 'objset'], help=params_help['query_ss_type'], metavar='query_ss_type', dest='query_ss_type')
	param_query.add_argument('--query_mode', action='store', nargs=1, default=['list'], choices=['list', 'pairs'], help=params_help['query_mode'], metavar='query_mode', dest='query_mode')
	param_query.add_argument('--query_input', action='store', nargs=1, default=['ac'], choices=['ac', 'ontology', 'file', 'terminal'], help=params_help['query_input'], metavar='query_input', dest='query_input')
	param_query.add_argument('--query_file', action='store', nargs=1, default=None, help=params_help['query_file'], metavar='query_file', dest='query_file')
	param_query.add_argument('--query_file_sep', action='store', nargs=1, default=['\t'], help=params_help['query_file_sep'], metavar='query_file_sep', dest='query_file_sep')

	param_ss.add_argument('--tss', '--ss', '-s', action='store', nargs=1, default=['Resnik'], help=params_help['tss_measure'], metavar='tss_measure', dest='tss_measure')
	param_ss.add_argument('--tmix', '--mix', '-m', action='store', nargs=1, default=['BMA'], help=params_help['tss_mix'], metavar='tss_mix', dest='tss_mix')
	# param_ss.add_argument('--oss', action='store', nargs=1, default=['single'], help=params_help['oss_measure'], metavar='oss_measure', dest='oss_measure')
	# param_ss.add_argument('--omix', action='store', nargs=1, default=[None], help=params_help['oss_mix'], metavar='oss_mix', dest='oss_mix')
	param_ss.add_argument('--root', '--ontology_root', action='store', nargs=1, default=None, help=params_help['ss_category'], metavar='ss_category', dest='ss_category')
	param_ss.add_argument('--enhanced', action='store_const', const=True, default=False, help=params_help['ss_enhanced'], metavar='ss_enhanced', dest='ss_enhanced')

	param_output.add_argument('--cut', action='store', nargs=1, default=None, type=float, help=params_help['output_cut'], metavar='output_cut', dest='output_cut')
	param_output.add_argument('--remove_nan', action='store', nargs=1, default=False, type=prbool, help=params_help['output_remove_nan'], metavar='output_remove_nan', dest='output_remove_nan')
	param_output.add_argument('--output_file', '--out_file', action='store', nargs=1, default=None, help=params_help['output_file'], metavar='output_file', dest='output_file')

	param_extended.add_argument('--IC_table', '--IC_table_form_file', action='store', nargs=1, default=None, help=params_help['IC_table_form_file'], metavar='IC_table', dest='IC_table')
	param_extended.add_argument('--verbose', '-v', action='count', default=None, help=params_help['verbose'], dest='verbose')
	param_extended.add_argument('--save_params', nargs=1, default=None, help=params_help['save_params'], metavar='save_params', dest='save_params')
	param_extended.add_argument('--load_params', nargs=1, default=None, help=params_help['load_params'], metavar='load_params', dest='load_params')

	args = parser.parse_args()
	# print(args)
	return args
#

def parse_parameters(args):
	global params
	# global ontology_file, ontology_type, ontology_file_format, ignore_is_a, ignore_part_of, ignore_has_part, ignore_regulates
	# global EC_include, EC_ignore, tax_include, tax_ignore, ac_file, ac_term_first, ac_separator, ac_type, ac_multiple
	# global query_type, query_ss_type, query_mode, query_input, query_file, query_file_sep
	# global ss_root, tss_mix, tss_measure, use_enhanced
	# global cut_thres, out_file, cut_nan
	# global verbose, ext_IC_table, load_params, save_params

	load_params = args.load_params
	if not load_params == None:
		load_params = load_params[0]
	save_params = args.save_params
	if not save_params == None:
		save_params = save_params[0]

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
	query_ss_type = args.query_ss_type
	query_mode = args.query_mode
	query_input = args.query_input
	query_file = args.query_file
	query_file_sep = args.query_file_sep

	ss_root = args.ss_category
	use_enhanced = args.ss_enhanced
	tss_mix = args.tss_mix
	tss_measure = args.tss_measure
	# oss_mix = args.oss_mix
	# oss_measure = args.oss_measure

	cut_thres = args.output_cut
	out_file = args.output_file
	cut_nan = args.output_remove_nan
	
	verbose = args.verbose
	ext_IC_table = args.IC_table

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
	if not tss_mix == None:
		tss_mix = tss_mix[0]
	if not tss_measure == None:
		tss_measure = tss_measure[0]

	if not ext_IC_table == None:
		ext_IC_table = ext_IC_table[0]

	params = dict()

	params['ontology_file'] = ontology_file
	params['ontology_type'] = ontology_type
	params['ontology_file_format'] = ontology_file_format
	params['ignore_regulates'] = ignore_regulates
	params['ignore_has_part'] = ignore_has_part
	params['ignore_part_of'] = ignore_part_of
	params['ignore_is_a'] = ignore_is_a

	params['EC_include'] = EC_include	
	params['EC_ignore'] = EC_ignore
	params['ac_multiple'] = ac_multiple
	params['ac_type'] = ac_type
	params['ac_separator'] = ac_separator
	params['ac_term_first'] = ac_term_first
	params['ac_file'] = ac_file
	params['tax_ignore'] = tax_ignore
	params['tax_include'] = tax_include

	params['query_type'] = query_type
	params['query_ss_type'] = query_ss_type
	params['query_mode'] = query_mode
	params['query_input'] = query_input
	params['query_file_sep'] = query_file_sep
	params['query_file'] = query_file

	params['ss_root'] = ss_root
	params['use_enhanced'] = use_enhanced
	params['tss_measure'] = tss_measure
	params['tss_mix'] = tss_mix
	# params['oss_measure'] = oss_measure
	# params['oss_mix'] = oss_mix

	params['cut_thres'] = cut_thres
	params['out_file'] = out_file
	params['cut_nan'] = cut_nan

	params['verbose'] = verbose
	params['ext_IC_table'] = ext_IC_table
	params['save_params'] = save_params
	params['load_params'] = load_params

	return params
#

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # 












	#-#-#-#-#-#-#-#-#-#
	# Load Ontology   #
	#-#-#-#-#-#-#-#-#-#

def load_ontology():
	global params
	# global ontology_file, ontology_type, ontology_file_format, ignore_is_a, ignore_part_of, ignore_has_part, ignore_regulates

	ontology_ignore = {}
	ontology_ignore['has_part'] = True
	ontology_ignore['is_a'] = False
	ontology_ignore['regulates'] = False
	ontology_ignore['part_of'] = False
	if params['ignore_regulates']:
		ontology_ignore['regulates'] = True
	if not params['ignore_has_part']:
		ontology_ignore['has_part'] = False
	if params['ignore_is_a']:
		ontology_ignore['is_a'] = True
	if params['ignore_part_of']:
		ontology_ignore['part_of'] = True

	fn,fe = os.path.splitext(params['ontology_file'])
	if fe == '.gz':
		ontology_handle = gzip.open(params['ontology_file'], 'rb')
	else:
		ontology_handle = open(params['ontology_file'], 'r')
	# print ontology_file
	# print ontology_ignore
	# print ontology_type
	# print ontology_file_format
	ontology = ontologies.load(ontology_handle, source_type = params['ontology_file_format'], ontology_type = params['ontology_type'], parameters={'ignore':ontology_ignore})
	ontology_handle.close()
	return ontology
#









	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# load Annotation Corpus  #
	#-#-#-#-#-#-#-#-#-#-#-#-#-#

def load_ac():
	# global EC_include, EC_ignore, tax_include, tax_ignore, ac_file, ac_term_first, ac_separator, ac_type, ac_multiple
	global params
	global ontology


	ac = AnnotationCorpus.AnnotationCorpus(ontology)
	
	is_plain = False
	if params['ac_type'] == 'plain':
		is_plain = True

	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# Second step: set parsing parameters
	# You should fill a dictionary with the proper information. Friendly routines will be provided in future to set parsing parameters easily
	# If you specify incorrect or not pertinent parameters they'll be ignored.
	
	#### For gaf-2 / GOA files:
	if not is_plain:
		ac_params = {}
	
		ac_params['filter'] = {} # filter section is useful to remove undesired annotations

		if not params['EC_include'] == None:
			ac_params['filter']['EC'] = {} # EC filtering: select annotations depending on their EC
			ac_params['filter']['EC']['EC'] = params['EC_include'] # select which EC accept or reject
			ac_params['filter']['EC']['inclusive'] = True # select which EC accept or reject
		if not params['EC_ignore'] == None:
			ac_params['filter']['EC'] = {} # EC filtering: select annotations depending on their EC
			ac_params['filter']['EC']['EC'] = params['EC_ignore'] # select which EC accept or reject
			ac_params['filter']['EC']['inclusive'] = False # select which EC accept or reject

		if not params['tax_include'] == None:
			ac_params['filter']['taxonomy'] = {}
			ac_params['filter']['taxonomy']['taxonomy'] = params['tax_include'] # set properly this field to load only annotations involving proteins/genes of a specific species
			ac_params['filter']['taxonomy']['inclusive'] = True # select which EC accept or reject
		if not params['tax_ignore'] == None:
			ac_params['filter']['taxonomy'] = {}
			ac_params['filter']['taxonomy']['taxonomy'] = params['tax_ignore']
			ac_params['filter']['taxonomy']['inclusive'] = False # select which EC accept or reject
		
		ac_params['simplify'] = True # after parsing and filtering, removes additional information such as taxonomy or EC. Useful if you have a huge amount of annotations and not enough memory
	
	#### For plain files:
	if is_plain:
		ac_params = {}

		if params['ac_multiple']:
			ac_params['multiple'] = True # Set to True if there are many associations per line (the object in the first field is associated to all the objects in the other fields within the same line)
		if params['ac_term_first']:
			ac_params['term first'] = True # set to True if the first field of each row is a GO term. Set to False if the first field represents a protein/gene
		
		if not params['ac_separator'] == None:
			ac_params['separator'] = params['ac_separator'] # select the separtor used to divide fields
	
	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# Third Step: parsing
	# just use parse routine. You have to specify the file to parse, the type of file and (optional) the parameters
	if is_plain:
		# print "Loading annotation corpus from plain file " + str(ac_file) + "..."
		ac.parse(params['ac_file'], 'plain', ac_params) # to parse plain files
	else:
		# print "Loading annotation corpus from gaf-2 file " + str(ac_file) + "..."
		ac.parse(params['ac_file'], 'GOA', ac_params) # to parse gaf-2 / GOA files

	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	#### additional useful annotation corpus routines
	ac.isConsistent() # check whether the annotations are consistent with the current gene ontology. Useful to check if everything is fine
	# ac.sanitize() # removes annotations not consistent with the current gene ontology. USeful if you loaded an annotation corpus BEFORE loading a gene ontology
	# print "-> Annotation Corpus correctly loaded: " + str(len(ac.obj_set)) + " objects and " +  str(len(ac.term_set)) + " GO Terms."
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

def load_query_from_file():
	global params
	# global query_file, query_ss_type, query_mode, query_file_sep

	# print "Loading query from file " + str(query_file) + " [type: " + str(query_ss_type) + "] ..."
	
	h = open(params['query_file'],'r')
	query = []
	for line in h:
		line = line.rstrip('\n')
		line = line.rstrip('\r')
		line = line.split(params['query_file_sep'])

		if params['query_ss_type'] == 'obj' or params['query_ss_type'] == 'term':
			if params['query_mode'] == 'pairs':
				if len(line) < 2:
					continue
				for i in range(0,len(line)):
					for j in range(i+1,len(line)):
						query.append((line[i], line[j]))
			elif params['query_mode'] == 'list':
				for i in line:
					query.append(i)
			else:
				raise Exception
		elif params['query_ss_type'] == 'objset' or params['query_ss_type'] == 'termset':
			if params['query_mode'] == 'pairs':
				raise Exception
			elif params['query_mode'] == 'list':
				newline = []
				for i in line:
					newline.append(i)
				query.append(newline)
			else:
				raise Exception
		else:
			raise Exception
	
	h.close()
	# print "-> Query loaded from file: " + str(len(query)) + " entries."
	return query
#






	#-#-#-#-#-#-#-#-#-#-#-#
	# Semantic Similarity #
	#-#-#-#-#-#-#-#-#-#-#-#

def init_ss():
	global ontology, ac
	global params
	# global ss_root, tss_mix, tss_measure, use_enhanced
	# global query_ss_type

	# print "-> Initializing Semantic Similarity object. Mode: " + str(query_ss_type) + ". Term Sem Sim: " +  str(tss_mix) + ". Term mixing strategy: " + str(tss_measure) + ". Obj mixing strategy: " +  str(oss_mix)

	if params['query_ss_type'] == 'term':
		tss_class = SemSimMeasures.select_term_SemSim(params['tss_measure'])
		tss = tss_class(ontology, ac, None, do_log=True)
		ss = tss
	elif params['query_ss_type'] == 'obj':
		oss = ObjSemSim.ObjSemSim(ontology, ac, params['tss_measure'], params['tss_mix'], None, do_log = True)
		ss = oss
	elif params['query_ss_type'] == 'termset':
		oss = SetSemSim.SetSemSim(ontology, ac, params['tss_measure'], params['tss_mix'], None, do_log = True)
		ss = oss
	elif params['query_ss_type'] == 'objset':
		oss = ObjSetSemSim.ObjSetSemSim(ontology, ac, params['tss_measure'], params['tss_mix'], None, do_log = True)
		ss = oss
	else:
		raise Exception
	#

	if params['use_enhanced']:
		raise Exception
	#

	return ss
#



	#-#-#-#-#-#-#-#-#
	# Pairs Sem Sim #
	#-#-#-#-#-#-#-#-#

def ss_pairs(out):
	global params
	global ss


	print "Evluating semantic similarity between " + str(len(query)) + " pairs."
	scores = []
	done = 0
	total = len(query)
	if params['verbose'] > 2:
		prev_text = ""
		sys.stdout.write("Done: ")
		sys.stdout.flush()
	for i in range(0,len(query)):
		temp = ss.SemSim(query[i][0], query[i][1], params['ss_root'])
		#scores.append((pairs[i][0],pairs[i][1],temp))
		done+=1
		if not params['cut_thres'] == None:
			if temp == None or temp <= params['cut_thres']:
				continue
			if params['cut_nan']:
				if temp == None:
					continue
		if out == None:
			print str(query[i][0]) + "\t" + str(query[i][1]) + "\t" + str(temp)
		else:
			out.write(str(query[i][0]) + "\t" + str(query[i][1]) + "\t" + str(temp) + "\n")
			if params['verbose'] > 2:
				sys.stdout.write("\b"*len(prev_text))
				prev_text = str(done) + ' [%.4f' % (100*done/float(total)) + " %]"
				sys.stdout.write(prev_text)
				sys.stdout.flush()
	#return scores
#



	#-#-#-#-#-#-#-#-#-#-#
	# Pairwise Sem Sim  #
	#-#-#-#-#-#-#-#-#-#-#

def ss_pairwise(out):
	global params
	global ss
	global query

	print "Evluating pairwise semantic similarity between " + str(len(query)) + " entities (" + str(len(query)*(len(query)-1)/2) + " pairs)"
	scores = {}
	done = 0
	total = len(query)*(len(query)-1)/2

	if params['verbose'] >= 1:
		prev_text = ""
		sys.stdout.write("Done: ")
		sys.stdout.flush()
	for i in range(0,len(query)):
		# if params['query_ss_type'] == 'obj':
		# scores[pairs[i]] = {}
		for j in range(i,len(query)):
			temp = ss.SemSim(query[i],query[j],params['ss_root'])
			if temp == None:
				print ss.log
			#scores[pairs[i]][pairs[j]] = temp
			done+=1
			if not params['cut_thres'] == None:
				if temp == None or temp <= params['cut_thres']:
					continue
			if params['cut_nan']:
				if temp == None:
					continue
			if out == None:
				print str(query[i]) + "\t" + str(query[j]) + "\t" + str(temp)
			else:
				out.write(str(query[i]) + "\t" + str(query[j]) + "\t" + str(temp) + "\n")
				if params['verbose'] > 2:
					sys.stdout.write("\b"*len(prev_text))
					prev_text = str(done) + ' [%.4f' % (100*done/float(total)) + " %]"
					sys.stdout.write(prev_text)
					sys.stdout.flush()
	#return scores
#



def print_IC(IC, query, out, cut_thres=None, cut_nan=False):
	global params

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
		IC[line[0]] = line[1]
		IC[ontology.name2id(line[0])] = line[1]

	h.close()
	print "-> IC loaded from file: " + str(len(IC)) + " entries."
	return IC
#




# 	#-#-#-#-#-#-#-#-#-#-#-#-#
# 	# Load Query from File  #
# 	#-#-#-#-#-#-#-#-#-#-#-#-#

# def load_query_from_ac(ac):
# 	query = ac.obj_set.keys()
# 	print "-> Query loaded from Annotation Corpus: " + str(len(query)) + " entries."
# 	return query
# #

# def load_query_from_SS(SS, ontology=None):
# 	#print ontology
# 	#print SS.util.BP_ontology
# 	#print SS.util.MF_ontology
# 	#print SS.util.CC_ontology
# 	if ontology == SS.util.BP_ontology:
# 		query = list(SS.util.offspring[SS.util.go.BP_root])
# 	elif ontology == SS.util.MF_ontology:
# 		query = list(SS.util.offspring[SS.util.go.MF_root])
# 	elif ontology == SS.util.CC_ontology:
# 		query = list(SS.util.offspring[SS.util.go.CC_root])
# 	elif ontology == None:
# 		query = list(SS.util.offspring[SS.util.go.BP_root])
# 		query.extend(list(SS.util.offspring[SS.util.go.MF_root]))
# 		query.extend(list(SS.util.offspring[SS.util.go.CC_root]))
# 	else:
# 		return None
# 	#print str(query)
# 	print "-> Query loaded from the Gene Ontology: " + str(len(query)) + " entries."
	
# 	return query
# #

# def load_query_from_util(util, ontology=None):
# 	#print ontology
# 	#print SS.util.BP_ontology
# 	#print SS.util.MF_ontology
# 	#print SS.util.CC_ontology
# 	if ontology == util.BP_ontology:
# 		query = list(util.offspring[util.go.BP_root])
# 	elif ontology == util.MF_ontology:
# 		query = list(util.offspring[util.go.MF_root])
# 	elif ontology == util.CC_ontology:
# 		query = list(util.offspring[util.go.CC_root])
# 	elif ontology == None:
# 		query = list(util.offspring[util.go.BP_root])
# 		query.extend(list(util.offspring[util.go.MF_root]))
# 		query.extend(list(util.offspring[util.go.CC_root]))
# 	else:
# 		return None
# 	#print str(query)
# 	print "-> Query loaded from the Gene Ontology: " + str(len(query)) + " entries."
	
# 	return query
# #



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



def check_parameters():
	global params
	# global ontology_file, ontology_type, ontology_file_format, ignore_is_a, ignore_part_of, ignore_has_part, ignore_regulates
	# global EC_include, EC_ignore, tax_include, tax_ignore, ac_file, ac_term_first, ac_separator, ac_type, ac_multiple
	# global ss_root, tss_mix, tss_measure, use_enhanced
	# global query_type, query_ss_type, query_mode, query_input, query_file, query_file_sep
	# global cut_thres, out_file, cut_nan
	# global verbose, ext_IC_table

	if params['ontology_file'] == None:
		raise Exception
		params['ontology_file'] = program_dir + "/data/GO_filtered_2013.07.26.obo-xml.gz"
	if params['ontology_type'] == None:
		params['ontology_type'] = "Ontology"
	if params['ontology_file_format'] == None:
		params['ontology_file_format'] = 'obo'

	if params['use_enhanced']:
		params['tss_measure'] = 'Resnik'
		params['tss_mix'] = 'max'

	if params['query_ss_type'] == 'obj' or params['query_ss_type'] == 'objset':
		if params['ac_file'] == None:
			print "An annotation corpus is required in " + str(params['query_ss_type']) + "mode. See the help notes (ac_file parameter)"
			return False
		if params['ontology_file'] == None:
			print "An ontology_type must be selected. See the help notes (ontology_file parameter)"
			return False
	elif params['query_ss_type'] == 'term' or  params['query_ss_type'] == 'termset':
		if params['ontology_file'] == None:
			print "An ontology_type must be selected. See the help notes (ontology_file parameter)"
			return False
	else:
		print "Unrecognized query_type " + params['query_ss_type']
		return False

	if params['query_ss_type'] == 'objset':
		if params['query_input'] == 'ontology' or params['query_input'] == 'ac':
			print_err("Cannot read objset from ac or ontology.")
			return False
		if params['query_input'] == 'file' and params['query_mode'] == 'pairs':
			print_err("Cannot read query pairs from file in objset mode")
			return False
	if params['query_ss_type'] == 'termset':
		if params['query_input'] == 'ontology' or params['query_input'] == 'ac':
			print_err("Cannot read objset from ac or ontology.")
			return False
		if params['query_input'] == 'file' and params['query_mode'] == 'pairs':
			print_err("Cannot read query pairs from file in termset mode")
			return False

	if params['query_input'] == 'ontology' and params['query_mode'] == 'pairs':
		print_err("Incompatible query input (ontology) and query mode (pairs).")
		return False
	if params['query_input'] == 'ac' and params['query_mode'] == 'pairs':
		print_err("Incompatible query input (ac) and query mode (pairs).")
		return False

	if not params['EC_include'] == None:
		params['EC_ignore'] = None
	if not params['tax_include'] == None:
		params['tax_ignore'] = None

	return True
	#

def start():
	# global input parameter variables
	# global ontology_file, ontology_type, ontology_file_format, ignore_is_a, ignore_part_of, ignore_has_part, ignore_regulates
	# global EC_include, EC_ignore, tax_include, tax_ignore, ac_file, ac_term_first, ac_separator, ac_type, ac_multiple
	# global ss_root, tss_mix, tss_measure, use_enhanced
	# global query_type, query_ss_type, query_mode, query_input, query_file, query_file_sep
	# global cut_thres, out_file, cut_nan
	# global verbose, ext_IC_table
	# global variables
	global params
	global ontology, ac, query, ss
	global program_dir

	program_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
	#program_dir = '.' # use this with py2exe to build a working binary

	args = parse_args()
	params = parse_parameters(args)

	if not check_parameters():
		sys.exit()

	if params['verbose'] >= 4:
		print str(params)

	if params['verbose'] >= 2:
		print("-----------------------------------------------")
		print("FastSemSim 0.8 - Copyright 2011-2013 Marco Mina")
		print("-----------------------------------------------")
		print("Ontology:\t" + str(params['ontology_file']))
		print("Annotation Corpus:\t" + str(params['ac_file']))
		print("Annotation Corpus type:\t" + str(params['ac_type']))
		if params['ac_type'] == 'gaf2':
			print("Consider EC:\t\t\t" + str(params['EC_include']))
			print("Ignore EC:\t\t\t" + str(params['EC_ignore']))
			print("Consider Taxonomy:\t\t" + str(params['tax_include']))
			print("Ignore Taxonomy:\t\t" + str(params['tax_ignore']))
		elif params['ac_type'] == 'plain':
			if params['ac_term_first']:
				print("AC Row format:\t\t\tGO Term -> Entry")
			else:
				print("AC Row format:\t\t\tEntry -> GO Term")
			print("Many associations per line:\t" + str(params['ac_multiple']))
		print("Query type: \t\t\t" + str(params['query_type']))
		if params['query_mode'] == 'all':
			print("Query mode: \t\t\tfrom Annotation Corpus")
		else:
			print("Query mode: \t\t\t" + str(params['query_mode']))
			print("Query file: \t\t" + str(params['query_file']))
			print("Query file separator: \t\t\'" + str(params['query_file_sep']) + "\'")
		if not params['out_file'] == None:
			print("Output file: \t\t\t" + str(params['out_file']))
		else:
			print("Output \t\t\t\tto console")
		print("SS measure: \t\t\t" + str(params['tss_measure']) + " " + str(params['tss_mix']))
		print("GO category: \t\t\t" + str(params['ss_root']))
		print("Using enhanced version:\t\t" + str(params['use_enhanced']))
		print("-----------------------------------------------")


# ----- Load ontology
	if params['verbose'] >= 1:
		print "-> Loading ontology from " + str(params['ontology_file']) + "..."
	ontology = load_ontology()
	if params['verbose'] >= 1:
		print "-> Ontology correctly loaded: " + str(ontology.node_number()) + " nodes and " +  str(ontology.edge_number()) + " edges."

# ----- Load annotation corpus

	ac = None
	if not params['ac_file'] == None:
		if params['verbose'] >= 1:
			print "-> Loading annotation corpus from " + str(params['ac_file']) + "..."
		ac = load_ac()
		if params['verbose'] >= 1:
			print "-> Annotation corpus loaded."

# ----- SS mode

	if params['query_type'] == 'SS':
		# ----- Generate SS
		ss = init_ss()


		if params['query_ss_type'] == 'obj':
			if params['query_input'] == 'ac':
				query = ac.annotations.keys()
		#

		elif params['query_ss_type'] == 'term':
			if params['query_input'] == 'ac':
				query = ac.reverse_annotations.keys()
			elif params['query_input'] == 'ontology':
				query = ontology.nodes.keys()
			else:
				raise Exception
			print "Take care of different ontology roots!"
		#

		elif params['query_input'] == 'file':
			query = load_query_from_file()
		#

		elif params['query_input'] == 'terminal':
			pass
		#

		else:
			raise Exception

		if params['verbose'] >= 3:
			print str(query)

		# ----- Inject IC

		if not params['ext_IC_table'] == None:
			raise Exception
			print 'Injecting GO terms IC from ' + params['ext_IC_table'] + "..."
			ext_IC = load_IC_from_file(params['ext_IC_table'])
			ss.util.IC = ext_IC

		# ----- Process query

		print 'Processing query...'
		print params['out_file']
		# sdf

		h = None
		if not params['out_file'] == None:
			h = open(params['out_file'], 'w')
			
		if params['use_enhanced']:
			raise Exception
			# ss_pairwise_enhanced(SS, query, ontology, h, cut_thres, cut_nan)
		elif params['query_mode'] == 'pairs':
			ss_pairs(h)
		elif params['query_mode'] == 'list':
			ss_pairwise(h)
		else:
			raise Exception
		if not h == None:
			h.close()
		sys.exit()

	#

# ----- Stats mode

	elif params['query_type'] == 'stats':
		util = SemSimUtils.SemSimUtils(ontology, ac)
		util.det_IC_table()

		if params['query_mode'] == 'all':
			query = load_query_from_util(util, ontology)
		else:
			query = load_query_from_file(params['query_file'], params['query_mode'], params['query_separator'])

		h = None
		if not params['out_file'] == None:
			h = open(params['out_file'], 'w')
		print_IC(util.IC, query, h, params['cut_thres'], params['cut_nan'])
		if not h == None:
			h.close()
		sys.exit()
	#

	else:
		raise Exception
	#
	sys.exit()
#

if __name__ == "__main__":
	start()
#
