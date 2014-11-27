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

__author__ = "Marco Mina"


from Ontology import AnnotationCorpus
from Ontology import ontologies
import SemSim
from SemSim import ObjSemSim
from SemSim import ObjSetSemSim
from SemSim import SetSemSim
from SemSim import SemSimUtils
# from data import dataset
from fastsemsim import data
import fastsemsim

import sys
import os
import math
import gzip

import argparse

def print_err(*args):
	sys.stderr.write(' '.join(map(str,args)) + '\n')
#


def start():
	'''
	main routine
	'''
	global params, ontology, ac, query, ss, ssutil
	
	params = dict()
	params['core'] = dict()
	params['ontology'] = dict()
	params['ac'] = dict()
	params['query'] = dict()
	params['ss'] = dict()
	params['output'] = dict()

	params['core']['program_dir'] = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
	# params['program_dir'] = '.' # use this with py2exe to build a working binary

	args = parse_cmdline_args()
	set_parameters(args)

	if params['core']['verbose'] >= 2:
		print "fastSemSim started"

	check_ack = check_parameters()
	if not check_ack:
		print "Invalid parameters"
		if params['core']['verbose'] >= 3:
			print_parameters()
		sys.exit()
	else:
		if params['core']['verbose'] >= 1:
			print_parameters()

	# ----- Load ontology and (optionally) ac
	ontology = load_ontology()
	ac = load_ac()
	# ----- SS mode
	if params['core']['task'] == 'SS':
		ssutil = SemSimUtils(ontology, ac)
		ss = init_ss()

		if params['query']['query_input'] == 'file':
			if params['core']['verbose'] >= 2:
				print "-> Loading query from file..."
			query = load_query_from_file()
			if params['core']['verbose'] >= 2:
				print "-> Query loaded from file."
		#
		elif params['query']['query_ss_type'] == 'obj':
			if params['query']['query_input'] == 'ac':
				if params['core']['verbose'] >= 2:
					print "-> Loading query from annotation corpus..."
				query = ac.annotations.keys()
				if params['core']['verbose'] >= 2:
					print "-> Query loaded from annotation corpus"
		#
		elif params['query']['query_ss_type'] == 'term':
			if params['query']['query_input'] == 'ac':
				if params['core']['verbose'] >= 2:
					print "-> Loading query from annotation corpus..."
				query = ac.reverse_annotations.keys()
				# params['ss_root']
				if params['core']['verbose'] >= 2:
					print "-> Query loaded from annotation corpus"
			elif params['query']['query_input'] == 'ontology':
				if params['core']['verbose'] >= 2:
					print "-> Loading query from ontology..."
				query = ontology.nodes.keys()
				# params['ss_root']
				if params['core']['verbose'] >= 2:
					print "-> Query loaded from ontology"
			else:
				pass
		#
		else:
			raise Exception

		if params['core']['verbose'] >= 2:
			print "Query length: " + str(len(query))
		if params['core']['verbose'] >= 3:
			print str(query)

		# ----- Inject IC

		if not params['core']['inject_IC'] == None:
			if params['core']['verbose'] >= 2:
				print "-> Injecting IC from file " + str(params['core']['inject_IC']) + "..."
			ext_IC = load_IC_from_file(params['core']['inject_IC'])
			ss.util.IC = ext_IC
			if params['core']['verbose'] >= 2:
				print "IC injected."

		# ----- Process query

		if params['core']['verbose'] >= 2:
			print '-> Evaluating Semantic Similarity...'

		h = None
		if not params['output']['out_file'] == None:
			if params['core']['verbose'] >= 2:
				print 'Saving SS in file ' + str(params['output']['out_file'])
			h = open(params['output']['out_file'], 'w')
			
		# if params['ss']['use_enhanced']:
			# raise Exception
			# ss_pairwise_enhanced(SS, query, ontology, h, cut_thres, cut_nan)
		elif params['query']['query_mode'] == 'pairs':
			ss_pairs(h)
		elif params['query']['query_mode'] == 'list':
			ss_pairwise(h)
		else:
			raise Exception
		if not h == None:
			h.close()
	# ----- Stats mode
	elif params['core']['task'] == 'stats':

		if params['core']['verbose'] >= 2:
			print "-> Extracting statistics..."

		util = SemSimUtils.SemSimUtils(ontology, ac)
		util.det_IC_table()

		# ----- Inject IC

		if not params['inject_IC'] == None:
			if params['core']['verbose'] >= 2:
				print "-> Injecting IC from file " + str(params['inject_IC']) + "..."
			ext_IC = load_IC_from_file(params['inject_IC'])
			util.IC = ext_IC
			if params['core']['verbose'] >= 2:
				print "IC injected."

		h = None
		if not params['out_file'] == None:
			if params['core']['verbose'] >= 2:
				print "-> Writing IC to file " + str(params['out_file']) + "..."
			h = open(params['out_file'], 'w')
		print_IC(util.IC, h, params['cut_thres'], params['cut_nan'])
		if not h == None:
			h.close()
		if params['core']['verbose'] >= 2:
			print "-> IC extracted."
	#

	else:
		raise Exception
	#

	if params['core']['verbose'] >= 2:
		print '-> Process completed. Quitting.'
	sys.exit()
#








'''
########################################################################################
Command line parameter parsing and help
'''


#Help notes 
params_help = dict()

params_help['ontology'] = 'Ontology. DAG of terms linked in a semantic hierarchy.'
params_help['ontology_file'] = 'File containing the ontology of interest. Only obo and obo-xml formats are currently supported (either gzipped or not). If not provided, a default ontology included in FastSemSim will be used, according to the value of ontology_type parameter.'
params_help['ontology_type'] = 'Ontology type. Currently supported ontologies are: \'generic\', \'GeneOntology\', \'CellOntology\', and \'DiseaseOntology\'. [default: GeneOntology]'
params_help['ontology_file_format'] = 'Ontology file type. Can be either \'obo\' or \'obo-xml\'. Compressed version is automatically detected if the file ends with .tar.gz or tar.bz2 extensions. WARNING: Reading compressed obo files tend to be a really slow process (might take more than 4 minutes to load the Gene Ontology). Compressed obo-xml files, instead, work well.  [default: obo]'
params_help['ignore_has_part'] = 'Whether consider or ignore has_part relationships [default:True]'
params_help['ignore_is_a'] = 'Whether consider or ignore is_a relationships [default:False]'
params_help['ignore_part_of'] = 'Whether consider or ignore part_of relationships [default:False]'
params_help['ignore_regulates'] = 'Whether consider or ignore regulates relationships [default:False]'
params_help['ontology_ignore'] = 'Instruct fastSemSim to ignore the following ontological relationships [default:None]'

params_help['ac'] = 'Annotation Corpus. Associations between objects and terms in the ontology.'
params_help['ac_name'] = 'Annotation Corpus name. The same of ac_file. Will be modified in the future.'
params_help['ac_file'] = 'File containing the Annotation Corpus (AC). g/bzip compressed files are supported, and the file extension must be .tar.bz2 or tar.gz.'
params_help['ac_species'] = 'Load an ac embedded in fastSemSim. Specify the species to be loaded. E.g. human'
params_help['ac_type'] = 'Format of AC file. Currently supported formats are "plain" and "gaf2". [default: gaf2]'
params_help['ac_sep'] = 'Separator used in plain AC files. Use "s" or " " (with quotes) for space, and "t" or \\t for tab. [Default: tab] (plain AC files only)'
params_help['ac_multiple'] = 'If specified, each line of AC file can contain more than a Term or Entry. (plain AC files only)'
params_help['ac_termfirst'] = 'If specified, plain AC files will be interpreted assuming that the first field of each line is an ontology term, and the following fields are the associated entries [the standard behavior is to consider the first field as an entry, and following fields as associated ontology terms. (plain AC files only)'
params_help['include_tax'] = 'If specified, consider only taxonomies specified. Taxonomies must be specified using integer ids. (gaf2 AC files only)'
params_help['ignore_tax'] = 'If specified, ignores the taxonomies specified. Used only with gaf2 files. Taxonomies must be specified using integer ids. This parameter is ignored if --include_tax is specified. (gaf2 AC files only)'
params_help['include_EC'] = 'Defines the Evidence Codes (EC) that will be accepted when loading the annotation corpus. For instance, \'IEA\' allows Electronically inferred annotations to be included in thge annotation corpus. (gaf2 AC files only)'
params_help['ignore_EC'] = 'Specifies which types of annotation will be ignored. (i.e.: --ignore_EC IEA means that IEA annotations will be ignored). This parameter is ignored if --include_EC is specified. (gaf2 AC files only)'

params_help['query'] = 'Query. Parameters and data defining the task that fastSemSim should perform.'
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

params_help['core'] = 'Core parameters'
params_help['IC_table_form_file'] = 'Load Information Content values of GO Terms from an external file.'
params_help['load_params'] = 'Load parameters from the specified file. Additional  parameters specified in the command line overwrite those loaded from the file.'
params_help['save_params'] = 'Save parameters to the specified file.'
params_help['verbose'] = 'Verbosity level. Repeat multiple time to increase verbosity level (i.e. -vvv)'
params_help['task'] = 'Instruct fastSemSim on the task to accomplish. Current supported tasks are: \'SS\', evaluation of Semantic Similarity (SS), and \'stats\', that is extraction of statistics. [default: \'SS\']'



def prbool(string):
	'''
	Parse boolean parameters
	'''
	y_values = ['True', 'true', 'Y', 'y', True, '1', 'Yes', 'yes']
	n_values = ['False', 'false', 'N', 'n', False, '0', 'No', 'no']
	if string in y_values:
		return True
	if string in n_values:
		return False
	msg = 'Cannot interpret %r as a True/False value. Allowed arguments: True, False, true, false, 0, 1, Yes, No, yes, no, Y, N, y, n' % string
	raise argparse.ArgumentTypeError(msg)
	return None
#

def build_cmdline_args_parser():
	'''
	Build a cmdline arg parser
	'''
	parser = argparse.ArgumentParser(
		description='FastSemSim commad line tool',
		prog='FastSemSim', usage=None, epilog=None, 
		fromfile_prefix_chars='@', add_help=True)

	param_ontology = parser.add_argument_group(title='Ontology', description=params_help['ontology'])
	param_ac = parser.add_argument_group(title='Annotation Corpus (AC)', description=params_help['ac'])
	param_ss = parser.add_argument_group(title='Semantic Similarity (SS)', description=params_help['ss'])
	param_query = parser.add_argument_group(title='Query', description=params_help['query'])
	param_output = parser.add_argument_group(title='Output parameters', description=params_help['output'])
	param_core = parser.add_argument_group(title='Core parameters', description=params_help['core'])

	param_core.add_argument('--inject_IC', '--inject_IC_form_file', action='store', default=None, help=params_help['IC_table_form_file'], metavar='inject_IC', dest='inject_IC')
	param_core.add_argument('--verbose', '-v', action='count', default=0, help=params_help['verbose'], dest='verbose')
	param_core.add_argument('--save_params', default=None, help=params_help['save_params'], metavar='save_params', dest='save_params')
	param_core.add_argument('--load_params', default=None, help=params_help['load_params'], metavar='load_params', dest='load_params')
	param_core.add_argument('--task', action='store', default=None, choices=['SS', 'stats'], help=params_help['task'], metavar='task', dest='task')

	param_ontology.add_argument('--ontology_file', action='store', default=None, help=params_help['ontology_file'], metavar='ontology_file', dest='ontology_file')
	param_ontology.add_argument('--ontology_file_format','--o_file_format', action='store', default=None, choices=ontologies.ontology_source_types, help=params_help['ontology_file_format'], metavar='ontology_file_format', dest='ontology_file_format')
	param_ontology.add_argument('--ontology', '--ontology_type', '-o', action='store', default=None, choices=ontologies.ontologies.keys(), help=params_help['ontology_type'], metavar='ontology_type', dest='ontology_type')
	param_ontology.add_argument('--ontology_ignore', action='append', default=[], help=params_help['ontology_ignore'], metavar='ontology_ignore', dest='ontology_ignore')
	param_ontology.add_argument('--ignore_is_a', action='append_const', const='is_a', help=params_help['ignore_is_a'], metavar='ontology_ignore', dest='ontology_ignore')
	param_ontology.add_argument('--ignore_part_of', action='append_const', const='part_of', help=params_help['ignore_part_of'], metavar='ontology_ignore', dest='ontology_ignore')
	param_ontology.add_argument('--ignore_has_part', action='append_const', const='has_part', help=params_help['ignore_has_part'], metavar='ontology_ignore', dest='ontology_ignore')
	param_ontology.add_argument('--ignore_regulates', action='append_const', const='regulates', help=params_help['ignore_regulates'], metavar='ontology_ignore', dest='ontology_ignore')

	param_ac.add_argument('-a','--ac', '--ac_name', action='store', default=None, help=params_help['ac_name'], metavar='ac', dest='ac')
	param_ac.add_argument('--ac_species', action='store', default=None, help=params_help['ac_species'], metavar='ac_species', dest='ac_species')
	param_ac.add_argument('--ac_file', action='store', default=None, help=params_help['ac_file'], metavar='ac_file', dest='ac_file')
	param_ac.add_argument('--ac_type', action='store', default=None, help=params_help['ac_type'], metavar='ac_type', dest='ac_type', choices=AnnotationCorpus.AnnotationCorpusFormat.keys())
	param_ac.add_argument('--ac_sep', action='store', default=None, help=params_help['ac_sep'], metavar='ac_sep', dest='ac_sep')
	param_ac.add_argument('--ac_termfirst', action='store_const', const=True, default=False, help=params_help['ac_termfirst'], metavar='ac_termfirst', dest='ac_termfirst')
	param_ac.add_argument('--ac_multiple', action='store_const', const=True, default=False, help=params_help['ac_multiple'], metavar='ac_multiple', dest='ac_multiple')
	param_ac.add_argument('--include_tax', action='append', default=[], type=int, help=params_help['include_tax'], metavar='tax', dest='include_tax')
	param_ac.add_argument('--ignore_tax', action='append', default=[], type=int, help=params_help['ignore_tax'], metavar='tax', dest='ignore_tax')
	param_ac.add_argument('--include_EC', action='append', default=[], help=params_help['include_EC'], metavar='Evidence Code', dest='include_EC')
	param_ac.add_argument('--ignore_EC', action='append', default=[], help=params_help['ignore_EC'], metavar='Evidence Code', dest='ignore_EC')

	# param_query.add_argument('--query_type', action='store', default='SS', choices=['SS', 'stats'], help=params_help['query_type'], metavar='query_type', dest='query_type')
	param_query.add_argument('--query_ss_type', action='store', default=None, choices=['obj', 'term', 'termset', 'objset'], help=params_help['query_ss_type'], metavar='query_ss_type', dest='query_ss_type')
	param_query.add_argument('--query_mode', action='store', default=None, choices=['list', 'pairs'], help=params_help['query_mode'], metavar='query_mode', dest='query_mode')
	param_query.add_argument('--query_input', action='store', default=None, choices=['ac', 'ontology', 'file'], help=params_help['query_input'], metavar='query_input', dest='query_input')
	param_query.add_argument('--query_file', action='store', default=None, help=params_help['query_file'], metavar='query_file', dest='query_file')
	param_query.add_argument('--query_file_sep', action='store', default=None, help=params_help['query_file_sep'], metavar='query_file_sep', dest='query_file_sep')

	param_ss.add_argument('--tss', '--ss', '-s', '--ss_measure', action='store', default=None, help=params_help['tss_measure'], metavar='tss_measure', dest='tss_measure')
	param_ss.add_argument('--tmix', '--mix', '-m', action='store', default=None, help=params_help['tss_mix'], metavar='tss_mix', dest='tss_mix')
	# param_ss.add_argument('--oss', action='store', nargs=1, default=['single'], help=params_help['oss_measure'], metavar='oss_measure', dest='oss_measure')
	# param_ss.add_argument('--omix', action='store', nargs=1, default=[None], help=params_help['oss_mix'], metavar='oss_mix', dest='oss_mix')
	param_ss.add_argument('--root', '--ontology_root', '--ss_root', action='store', default=None, help=params_help['ss_category'], metavar='ss_category', dest='ss_category')
	param_ss.add_argument('--enhanced', action='store_const', const=True, default=False, help=params_help['ss_enhanced'], metavar='ss_enhanced', dest='ss_enhanced')

	param_output.add_argument('--cut', action='store', default=None, type=float, help=params_help['output_cut'], metavar='output_cut', dest='output_cut')
	param_output.add_argument('--remove_nan', action='store_const', const=True, default=False, help=params_help['output_remove_nan'], metavar='output_remove_nan', dest='output_remove_nan')
	param_output.add_argument('--output_file', '--out_file', action='store', default=None, help=params_help['output_file'], metavar='output_file', dest='output_file')

	return(parser)
#

def parse_cmdline_args():
	'''
	Parse cmdline parameters
	'''
	parser = build_cmdline_args_parser()
	args = parser.parse_args(sys.argv[1:])
	# print(args)
	return args
#

def load_params_from_file(list_file):
	'''
	Load parameters from file
	'''
	gstr = []
	h = open(list_file,'r')
	for line in h:
		line = line.rstrip('\n')
		line = line.rstrip('\r')
		# line = line.rsplit("\t")
		gstr.append(line)
	h.close()
	return gstr
#

def save_params_to_file(list_file, curstr):
	'''
	Save parameters to file
	'''
	h = open(list_file,'w')
	gstr = ''
	for i in curstr:
		# gstr = gstr + " " + str(i)
		h.write(str(i) + "\n")
	# for i in params:
		# h.write("#" + str(i) + "\t" + str(params[i]) + "\n")
	h.close()
#

def set_parameters(args):
	'''
	fill the parameter dictionary with the proper parameters
	'''
	global params

	# Example in case of multipel list
	# ontology_file = args.ontology_file
	# if not ontology_file == None:
		# ontology_file = ontology_file[0]
	# params['ontology']['ontology_file'] = ontology_file
	# params['ontology']['ontology_file_format'] = None
	# if not isinstance(args.ontology_ignore, None.__class__):
		# params['ontology']['ignore'] = list(set(args.ontology_ignore))

	# load parameters from file, if specified
	load_params = args.load_params
	if not load_params == None:
		# load_params = load_params[0]
		curstr = load_params_from_file(load_params)
		parser = build_cmdline_args_parser()
		curpars = parser.parse_args(curstr)
		set_parameters(curpars)
	params['core']['load_params'] = load_params

	# set core parameters
	params['core']['verbose'] = args.verbose
	params['core']['inject_IC'] = args.inject_IC
	params['core']['task'] = args.task

	# set ontology parameters
	params['ontology']['ontology_file'] = args.ontology_file
	params['ontology']['ontology_type'] = args.ontology_type
	params['ontology']['ontology_file_format'] = args.ontology_file_format
	params['ontology']['ignore'] = list(set(args.ontology_ignore))

	# set ac parameters
	params['ac']['ac'] = args.ac
	params['ac']['ac_type'] = args.ac_type
	params['ac']['ac_species'] = args.ac_species
	params['ac']['ac_file'] = args.ac_file
	params['ac']['EC_include'] = list(set(args.include_EC))
	params['ac']['EC_ignore'] = list(set(args.ignore_EC))
	params['ac']['tax_include'] = list(set(args.include_tax))
	params['ac']['tax_ignore'] = list(set(args.ignore_tax))
	params['ac']['ac_multiple'] = args.ac_multiple
	params['ac']['ac_separator'] = args.ac_sep
	params['ac']['ac_term_first'] = args.ac_termfirst

	# set query parameters
	params['query']['query_ss_type'] = args.query_ss_type
	params['query']['query_mode'] = args.query_mode
	params['query']['query_input'] = args.query_input
	params['query']['query_file_sep'] = args.query_file_sep
	params['query']['query_file'] = args.query_file

	# set ss parameters
	params['ss']['ss_root'] = args.ss_category
	params['ss']['use_enhanced'] = args.ss_enhanced
	params['ss']['tss_measure'] = args.tss_measure
	params['ss']['tss_mix'] = args.tss_mix
	# params['oss_measure'] = oss_measure
	# params['oss_mix'] = oss_mix

	# set output parameters
	params['output']['cut_thres'] = args.output_cut
	params['output']['out_file'] = args.output_file
	params['output']['cut_nan'] = args.output_remove_nan

	# Load/write configuration to/from file	
	save_params = args.save_params
	if not save_params == None:
		# save_params = save_params[0]
		save_params_to_file(save_params, args)
	params['core']['save_params'] = save_params

	return params
#

def check_parameters():
	'''
	Check whether the set of parameters is formally correct to run a query
	'''
	global params

	if params['core']['verbose'] >= 3:
		print "# Raw parameters"
		print str(params)
		print "# \n"

	# Check core parameters
	if isinstance(params['core']['task'], None.__class__):
		params['core']['task'] = 'SS'

	# Check ontology parameters
	if isinstance(params['ontology']['ontology_type'], None.__class__):
		if isinstance(params['ontology']['ontology_file'], None.__class__):
			raise Exception('An ontology must be defined. Either specify a valid ontology type, or provide a filename. See the ontology_file parameter in the help.')
		params['ontology']['ontology_type'] = "Ontology"
	if not isinstance(params['ontology']['ontology_file'], None.__class__):
		if isinstance(params['ontology']['ontology_file_format'], None.__class__):
			params['ontology']['ontology_file_format'] = 'obo'

	# Check annotation corpus parameters
	params['ac']['is_defined'] = True
	if isinstance(params['ac']['ac'], None.__class__) and isinstance(params['ac']['ac_species'], None.__class__) and isinstance(params['ac']['ac_file'], None.__class__):
		params['ac']['is_defined'] = False
	elif not isinstance(params['ac']['ac_file'], None.__class__):
		params['ac']['ac'] = None
		params['ac']['ac_species'] = None
		if isinstance(params['ac']['ac_type'], None.__class__):
			params['ac']['ac_type'] = 'GOA'
	elif not isinstance(params['ac']['ac'], None.__class__):
		params['ac']['ac_species'] = None
	if not isinstance(params['ac']['EC_include'], None.__class__):
		params['ac']['EC_ignore'] = None
	if not isinstance(params['ac']['tax_include'], None.__class__):
		params['ac']['tax_ignore'] = None

	# Check query parameters
	if params['core']['task'] == 'SS':
		if isinstance(params['query']['query_file'], None.__class__):
			if isinstance(params['query']['query_input'], None.__class__):
				pass
			elif params['query']['query_input'] == 'file':
				raise Exception("The selected query input is file, but no query file has been specified.")
		else:
			params['query']['query_input'] = 'file'

		if isinstance(params['query']['query_ss_type'], None.__class__):
			if params['ac']['is_defined']:
				params['query']['query_ss_type'] = 'obj'
			else:
				params['query']['query_ss_type'] = 'term'

		if params['query']['query_ss_type'] == 'obj' or params['query']['query_ss_type'] == 'objset':
			if not params['ac']['is_defined']:
				raise Exception("An annotation corpus is required for the query_type: " + str(params['query']['query_ss_type']) + ". See the help notes (ac_file parameter)")
			if isinstance(params['query']['query_input'], None.__class__):
				params['query_input'] = 'ac'
		elif params['query']['query_ss_type'] == 'term' or params['query']['query_ss_type'] == 'termset':
			if isinstance(params['query']['query_input'], None.__class__):
				params['query_input'] = 'ontology'		
		if params['query']['query_input'] == 'ac':
			if not params['ac']['is_defined']:
				raise Exception("An annotation corpus is required for the query_input: " + str(params['query']['query_input']))

		if isinstance(params['query']['query_mode'], None.__class__):
			if params['query']['query_input'] == 'ac':
				params['query_mode'] = 'list'
			if params['query']['query_input'] == 'ontology':
				params['query_mode'] = 'list'
			if params['query']['query_input'] == 'file':
				raise Exception("The query_mode parameter must be specified if a query file is provided.")

		if params['query']['query_ss_type'] == 'objset' or params['query']['query_ss_type'] == 'termset':
			if params['query']['query_input'] == 'ac' or params['query']['query_input'] == 'ontology':
				raise Exception("The query_type cannot be set to sets if the query source is ac or ontology.")

		if params['query']['query_mode'] == 'pairs':
			if params['query']['query_input'] == 'ac' or params['query']['query_input'] == 'ontology':
				raise Exception("The query_mode cannot be set to pairs if the query is ac or ontology.")
			elif params['query']['query_ss_type'] == 'termset' or params['query']['query_ss_type'] == 'objset':
				raise Exception("The query_mode cannot be set to pairs if the query is file and the type is a set.")

	# Check SS parameters
	if params['core']['task'] == 'SS':
		if isinstance(params['ss']['tss_measure'], None.__class__):
			params['ss']['tss_measure'] = 'SimGIC'
		if isinstance(params['ss']['tss_mix'], None.__class__):
			params['ss']['tss_mix'] = 'BMA'
		if params['ss']['use_enhanced']:
			raise Exception("Enhanced version of Resnik is not available in this release.")

	return True
#


def print_parameters():
	'''
	Print the parameters selected
	'''

	global params

	print("\n-----------------------------------------------")
	print("FastSemSim " + str(fastsemsim.__version__) + " - Copyright 2011-2014")
	print("-----------------------------------------------")
	print("-> [Core]")
	print("Task: \t" + str(params['core']['task']))
	if not isinstance(params['core']['save_params'], None.__class__):
		print("Saving params to file: \t" + str(params['core']['save_params']))
	if not isinstance(params['core']['load_params'], None.__class__):
		print("Loading params from file: \t" + str(params['core']['load_params']))
	if not isinstance(params['core']['inject_IC'], None.__class__):
		print("Injecting IC from file: \t" + str(params['core']['inject_IC']))
	print("Verbosity: \t" + str(params['core']['verbose']))

	print("\n-> [Ontology]")
	if not isinstance(params['ontology']['ontology_file'], None.__class__):
		print("Ontology type: \t" + str(params['ontology']['ontology_type']))
		print("Ontology file: \t" + str(params['ontology']['ontology_file']))
		print("Ontology file format: \t" + str(params['ontology']['ontology_file_format']))
	else:
		print("Ontology: \t" + str(params['ontology']['ontology_type']))
	print("Ontological relationships ignored: \t" + str(params['ontology']['ignore']))
	
	print("\n-> [Annotation Corpus]")
	if not params['ac']['is_defined']:
		print("No Annotation Corpus specified.")
	else:
		if not isinstance(params['ac']['ac_file'], None.__class__):
			print("Annotation Corpus file: \t" + str(params['ac']['ac_file']))
			print("Annotation Corpus file type: \t" + str(params['ac']['ac_type']))
			if params['ac']['ac_type'] == 'plain':
				print("Annotation Corpus file - multiple assocaitions per line: \t" + str(params['ac']['multiple']))
				print("Annotation Corpus file - separator: \t" + str(params['ac']['separator']))
				print("Annotation Corpus file - ontological term first: \t" + str(params['ac']['ac_term_first']))
				# if params['ac']['ac_term_first']:
				# 	print("AC file row format: \tontology term -> object")
				# else:
				# 	print("AC file row format: \tobject -> ontology term")
				# print("Multiple associations per line: \t" + str(params['ac']['ac_multiple']))
			else:
				print("AC relationships ignored: \t" + str(params['ac']['EC_ignore']))
				print("AC relationships considered: \t" + str(params['ac']['EC_include']))
				print("AC taxa ignored: \t" + str(params['ac']['tax_ignore']))
				print("AC taxa considered: \t" + str(params['ac']['tax_include']))
		else:
			print("Annotation Corpus: \t" + str(params['ac']['ac']))
			print("Annotation Corpus: \t" + str(params['ac']['ac_species']))
			print("AC relationships ignored: \t" + str(params['ac']['EC_ignore']))
			print("AC relationships considered: \t" + str(params['ac']['EC_include']))
			print("AC taxa ignored: \t" + str(params['ac']['tax_ignore']))
			print("AC taxa considered: \t" + str(params['ac']['tax_include']))

	if params['core']['task'] == 'SS':
		print("\n-> [SS]")
		print("SS measure: \t" + str(params['ss']['tss_measure']) + "\nMix strategy: \t" + str(params['ss']['tss_mix']))
		print("Ontology category: \t" + str(params['ss']['ss_root']))
		print("Use enhanced Resnik: \t" + str(params['ss']['use_enhanced']))		
	elif params['core']['task'] == 'stats':
		pass

	print("\n-> [Query]")
	print("SS query type: \t" + str(params['query']['query_ss_type']))
	print("SS query mode: \t" + str(params['query']['query_mode']))
	print("SS query input: \t" + str(params['query']['query_input']))
	if params['query']['query_input'] == 'file':
		print("SS query file: \t" + str(params['query']['query_file']))
		print("SS query file separator: \t\'" + str(params['query']['query_file_sep']) + "\'")

	print("\n-> [Output]")
	if not params['output']['out_file'] == None:
		print("Output file: \t" + str(params['output']['out_file']))
	else:
		print("Output: \tconsole")
	print("Cut-off threshold: \t" + str(params['output']['cut_thres']))
	print("Remove NaN: \t" + str(params['output']['cut_nan']))
	print("-----------------------------------------------")
#




def load_ontology():
	'''
	Load ontology
	'''
	global params

	if params['core']['verbose'] >= 2:
		print("-----------------------------------------------")
		print "-> Loading ontology ..."

	ontology_ignore = params['ontology']['ignore']
	ontology = ontologies.load(params['ontology']['ontology_file'], source_type = params['ontology']['ontology_file_format'], ontology_type = params['ontology']['ontology_type'], parameters={'ignore':ontology_ignore})
	if isinstance(ontology, None.__class__):
		raise Exception("Ontology not correctly loaded: ")

	if params['core']['verbose'] >= 2:
		# print "source: " + str(source)
		# print "source_type: " + str(source_type)
		# print "ontology_type: " + str(ontology_type)
		# print "ignore_parameters: " + str(ontology_ignore)
		print "Ontology roots: " + str(ontology.roots.keys())
		print "Number of nodes: " + str(ontology.node_number())
		print "Number of edges: " + str(ontology.edge_number())
		print "\nType and number of edges:\n-------------\n" + str(ontology.edges['type'].value_counts())
		print "-------------"
		print "Outer edges (link to other ontologies): " + str(ontology.edges.loc[ontology.edges['inner'] == False].shape[0])
		print "Inter edges (link between different namespaces - within the same ontology): " + str(ontology.edges.loc[(ontology.edges['intra'] == False) & (ontology.edges['inner'] == True)].shape[0])
		# print "-------------"
	print("-----------------------------------------------")
	
	return ontology
#







def load_ac():
	'''
	Load the Annotation Corpus
	'''
	global params
	global ontology

	ac = None
	if params['ac']['is_defined']:
		if params['core']['verbose'] >= 2:
			print("-----------------------------------------------")
			print "-> Loading annotation corpus..."
	
		ac = AnnotationCorpus.AnnotationCorpus(ontology)
		if not isinstance(params['ac']['ac_file'], None.__class__): # should not be necessary!!!
			params['ac']['ac'] = None
			params['ac']['ac_species'] = None

		if not isinstance(params['ac']['ac'], None.__class__):
			builtin_dataset = data.dataset.Dataset()
			selected_source = builtin_dataset.get_default_annotation_corpus(ontology.name, params['ac']['ac_species'])
			if selected_source is None:
				return None

			params['ac']['ac_file'] = selected_source['file']
			params['ac']['ac_type'] = selected_source['filetype']

		#-#-#-#-#-#-#-#-#-#-#-#-#-#
		# Second step: set parsing parameters
		# You should fill a dictionary with the proper information. Friendly routines will be provided in future to set parsing parameters easily
		# If you specify incorrect or not pertinent parameters they'll be ignored.
		
		#### For gaf-2 / GOA files:
		if not params['ac']['ac_type'] == 'plain':
			ac_params = {}
			ac_params['filter'] = {} # filter section is useful to remove undesired annotations
			if not params['ac']['EC_include'] == None:
				ac_params['filter']['EC'] = {} # EC filtering: select annotations depending on their EC
				ac_params['filter']['EC']['EC'] = params['ac']['EC_include'] # select which EC accept or reject
				ac_params['filter']['EC']['inclusive'] = True # select which EC accept or reject
			if not params['ac']['EC_ignore'] == None:
				ac_params['filter']['EC'] = {} # EC filtering: select annotations depending on their EC
				ac_params['filter']['EC']['EC'] = params['ac']['EC_ignore'] # select which EC accept or reject
				ac_params['filter']['EC']['inclusive'] = False # select which EC accept or reject

			if not params['ac']['tax_include'] == None:
				ac_params['filter']['taxonomy'] = {}
				ac_params['filter']['taxonomy']['taxonomy'] = params['ac']['tax_include'] # set properly this field to load only annotations involving proteins/genes of a specific species
				ac_params['filter']['taxonomy']['inclusive'] = True # select which EC accept or reject
			if not params['ac']['tax_ignore'] == None:
				ac_params['filter']['taxonomy'] = {}
				ac_params['filter']['taxonomy']['taxonomy'] = params['ac']['tax_ignore']
				ac_params['filter']['taxonomy']['inclusive'] = False # select which EC accept or reject
			
			ac_params['simplify'] = True # after parsing and filtering, removes additional information such as taxonomy or EC. Useful if you have a huge amount of annotations and not enough memory
		
		#### For plain files:
		elif params['ac']['ac_type'] == 'plain':
			ac_params = {}

			if params['ac']['ac_multiple']:
				ac_params['multiple'] = True # Set to True if there are many associations per line (the object in the first field is associated to all the objects in the other fields within the same line)
			if params['ac']['ac_term_first']:
				ac_params['term first'] = True # set to True if the first field of each row is a GO term. Set to False if the first field represents a protein/gene
			
			if not params['ac']['ac_separator'] == None:
				ac_params['separator'] = params['ac']['ac_separator'] # select the separtor used to divide fields
		
		#-#-#-#-#-#-#-#-#-#-#-#-#-#
		# Third Step: parsing
		# just use parse routine. You have to specify the file to parse, the type of file and (optional) the parameters
		ac.parse(params['ac']['ac_file'], params['ac']['ac_type'], ac_params) # to parse plain files

		#-#-#-#-#-#-#-#-#-#-#-#-#-#
		#### additional useful annotation corpus routines
		ac.isConsistent() # check whether the annotations are consistent with the current gene ontology. Useful to check if everything is fine
		# ac.sanitize() # removes annotations not consistent with the current gene ontology. USeful if you loaded an annotation corpus BEFORE loading a gene ontology
		# print "-> Annotation Corpus correctly loaded: " + str(len(ac.obj_set)) + " objects and " +  str(len(ac.term_set)) + " GO Terms."

		if params['core']['verbose'] >= 2:
			print "ac - Number of annotated proteins: " + str(len(ac.annotations))
			print "ac - Number of annotated terms: " + str(len(ac.reverse_annotations))
			print("-----------------------------------------------")
	#
	return ac

	# these 4 variables contain all the useful data:
	#ac.annotations # set of annotations -> it's a dictionary with genes/proteins as keys. The value for each key is a dictionary with GO Terms annotated for that protein as keys
	#ac.reverse_annotations # set of annotations -> it's  adictionary with terms as keys. The value for each key is a dictionary with genes/proteins annotated for that GO Term as keys
	#ac.obj_set # set of proteins/genes involved in annotations
	#ac.term_set # set of GO Terms involved in annotations
#









def init_ss():
	'''
	Initialize SS class
	'''
	global ontology, ac, ssutil
	global params

	if params['core']['verbose'] >= 2:
		print("-----------------------------------------------")
		print "-> Initializing semantic similarity..."

	if not isinstance(params['ss']['ss_root'], None.__class__):
		params['ss']['ss_root'] = ss.ontology.name2id(params['ss']['ss_root'], alt_check=False)
	else:
		params['ss']['ss_root'] = ontology.roots.keys()[0]
	if isinstance(params['ss']['ss_root'], None.__class__):
		print_err("The ontology root required does not exists.")
		return None


	do_log = False
	if params['core']['verbose'] >= 4:
		do_log = True

	if params['query']['query_ss_type'] == 'term':
		tss_class = SemSimMeasures.select_term_SemSim(params['ss']['tss_measure'])
		tss = tss_class(ontology, ac, ssutil, do_log=do_log)
		ss = tss
	elif params['query']['query_ss_type'] == 'obj':
		oss = ObjSemSim.ObjSemSim(ontology, ac, params['ss']['tss_measure'], params['ss']['tss_mix'], ssutil, do_log = do_log)
		ss = oss
	elif params['query']['query_ss_type'] == 'termset':
		oss = SetSemSim.SetSemSim(ontology, ac, params['ss']['tss_measure'], params['ss']['tss_mix'], ssutil, do_log = do_log)
		ss = oss
	elif params['query']['query_ss_type'] == 'objset':
		oss = ObjSetSemSim.ObjSetSemSim(ontology, ac, params['ss']['tss_measure'], params['ss']['tss_mix'], ssutil, do_log = do_log)
		ss = oss
	else:
		raise Exception
	#
	# if params['use_enhanced']:
	# 	print "Enhanced version of Resnik is currently not available in this release. It will be included as soon as possible."
	# 	sys.exit()
	# 	raise Exception
	# #

	if params['core']['verbose'] >= 2:
		print "-> Semantic similarity initialized."
		print "-> Ontology root: " + str(params['ss']['ss_root'])
		print("-----------------------------------------------")

	return ss
#









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







#####################
	# Pairs Sem Sim #
#####################

def ss_pairs(out):
	global params
	global ss

	scores = []
	done = 0
	total = len(query)
	if not out == None:
		if params['core']['verbose'] >= 0:
			print "Evluating semantic similarity between " + str(len(query)) + " pairs."
			prev_text = ""
			sys.stdout.write("Done: ")
	sys.stdout.flush()
	for i in range(0,len(query)):
		temp = ss.SemSim(query[i][0], query[i][1], params['ss']['ss_root'])
		if temp == None and params['core']['verbose'] >= 4:
			print ss.log
		#scores.append((pairs[i][0],pairs[i][1],temp))
		done+=1
		if not params['output']['cut_thres'] == None:
			if temp == None or temp <= params['output']['cut_thres']:
				continue
			if params['output']['cut_nan']:
				if temp == None:
					continue
		if out == None:
			print str(query[i][0]) + "\t" + str(query[i][1]) + "\t" + str(temp)
		else:
			out.write(str(query[i][0]) + "\t" + str(query[i][1]) + "\t" + str(temp) + "\n")
			if params['core']['verbose'] >= 0:
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

	scores = {}
	done = 0
	total = len(query)*(len(query)+1)/2

	if not out == None:
		if params['core']['verbose'] >= 0:
			print "Evluating pairwise semantic similarity between " + str(len(query)) + " entities (" + str(len(query)*(len(query)+1)/2) + " pairs)"
			prev_text = ""
			sys.stdout.write("Done: ")
	sys.stdout.flush()
	for i in range(0,len(query)):
		# if params['query_ss_type'] == 'obj':
		# scores[pairs[i]] = {}
		for j in range(i,len(query)):
			temp = ss.SemSim(query[i],query[j],params['ss']['ss_root'])
			if temp == None and params['core']['verbose'] >= 4:
				print ss.log
			#scores[pairs[i]][pairs[j]] = temp
			done+=1
			if not params['output']['cut_thres'] == None:
				if temp == None or temp <= params['output']['cut_thres']:
					continue
			if params['output']['cut_nan']:
				if temp == None:
					continue
			if out == None:
				print str(query[i]) + "\t" + str(query[j]) + "\t" + str(temp)
			else:
				out.write(str(query[i]) + "\t" + str(query[j]) + "\t" + str(temp) + "\n")
				if params['core']['verbose'] >= 0:
					sys.stdout.write("\b"*len(prev_text))
					prev_text = str(done) + ' [%.4f' % (100*done/float(total)) + " %]"
					sys.stdout.write(prev_text)
					sys.stdout.flush()
	#return scores
#



def print_IC(IC, out, cut_thres=None, cut_nan=False):
	# global params
	global ontology

	# print "Evluating pairwise semantic similarity between " + str(len(pairs)) + " GO Terms (" + str(len(pairs)*(len(pairs)-1)/2) + " pairs)"
	# scores = {}
	done = 0
	# total = len(pairs)*(len(pairs)-1)/2

	# if verbose:
	# 	prev_text = ""
	# 	sys.stdout.write("Done: ")
	# 	sys.stdout.flush()
	for i in IC:
		# i = query[j]
		# scores[pairs[i]] = {}
		# for j in range(i+1,len(pairs)):
		# temp = SS.SemSim(pairs[i],pairs[j])
		#scores[pairs[i]][pairs[j]] = temp
		done+=1
		temp = IC[i]
		if not cut_thres == None:
			if temp == None or temp <= cut_thres:
				continue
		if cut_nan:
			if temp == None:
				continue
		if out == None:
			print str(ontology.id2name(i)) + "\t" + str(temp)
		else:
			out.write(str(ontology.id2name(i)) + "\t" + str(temp) + "\n")
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
		# if not str(line[1]) == 'None': 
			# line[1] = float(line[1])
		# IC[line[0]] = line[1]
		temo = ontology.name2id(line[0])
		if type(temo) == list:
			if len(temo) == 1:
				temo = temo[0]
			else:
				raise Exception
		if str(line[1]) == 'None':
			IC[temo] = None
		else:
			# try:
			IC[temo] = float(line[1])
			# except Exception:
				# IC[temo] = None


	h.close()
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

# def init_enhanced_ss(go, ac, termss='Resnik', mixp="BMA", params = None):

# 	print "Initializing Semantic Similarity class..."
# 	SS = fastResnikSemSim.fastResnikSemSim(ac, go, termss, mixp, params)
# 	print "-> Semantic Similarity class ready"
# 	return SS
# #



# def ss_pairwise_enhanced(SS, pairs = None, ontology = 'BP', out = None, cut_thres = None, cut_none = False):
# 	#print "Evluating pairwise semantic similarity between " + str(len(pairs)) + " entities (" + str(len(pairs)*(len(pairs)-1)/2) + " pairs)"
# 	out_h = out
# 	if out==None:
# 		out_h = sys.stdout
# 	tct = cut_thres
# 	if cut_none and cut_thres == None:
# 		tct = -1
# 	SS.SemSim(ontology, out, tct)
# #

if __name__ == "__main__":
	start()
#
# 