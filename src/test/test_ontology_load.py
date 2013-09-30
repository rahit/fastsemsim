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

	param_go.add_argument('-o','--ontology', '--ontology_file', action='store', nargs=1, default=None, help=None, metavar='ontology_file', dest='ontology_file')
	param_go.add_argument('--ontology_file_format','--o_file_format', action='store', nargs=1, default=None, help=None, metavar='ontology_file_format', dest='ontology_file_format')
	param_go.add_argument('--ontology_type', '--o_type', action='store', nargs=1, default=None, help=None, metavar='ontology_type', dest='ontology_type')
	param_go.add_argument('--ignore_has_part', action='store', nargs='?', default=True, type=prbool, help=None, metavar='ignore_has_part', dest='ignore_has_part')
	param_go.add_argument('--ignore_is_a', action='store', nargs='?', default=False, type=prbool, help=None, metavar='ignore_is_a', dest='ignore_is_a')
	param_go.add_argument('--ignore_part_of', action='store', nargs='?', default=False, type=prbool, help=None, metavar='ignore_part_of', dest='ignore_part_of')
	param_go.add_argument('--ignore_regulates', action='store', nargs='?', default=False, type=prbool, help=None, metavar='ignore_regulates', dest='ignore_regulates')
	param_go.add_argument('--verbose', '-v', action='count', default=None, help=None, dest='verbose')

	args = parser.parse_args()
	# print(args)
	return args


def parse_parameters(args):
	global ontology_file, ontology_type, ignore_is_a, ignore_part_of, ignore_has_part, ignore_regulates, ontology_file_format
	global verbose

	ontology_file = args.ontology_file
	ontology_type = args.ontology_type
	ontology_file_format = args.ontology_file_format
	ignore_is_a = args.ignore_is_a
	ignore_part_of = args.ignore_part_of
	ignore_has_part = args.ignore_has_part
	ignore_regulates = args.ignore_regulates

	verbose = args.verbose

	if not ontology_file == None:
		ontology_file = ontology_file[0]
	if not ontology_file_format == None:
		ontology_file_format = ontology_file_format[0]
	if not ontology_type == None:
		ontology_type = ontology_type[0]

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

def start():
	global ontology_type, ontology_file, ontology_file_format
	global ontology
	
	program_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
	args = parse_args()
	parse_parameters(args)

	if ontology_type == None:
		ontology_type = "Ontology"
	if ontology_file_format == None:
		ontology_file_format = 'obo'

	print("->Testing ontology\t\t" + str(ontology_file))
	ontology = load_ontology()
	print ontology.nodes
	print "-> Ontology correctly loaded: " + str(ontology.node_number()) + " nodes and " +  str(ontology.edge_number()) + " edges."
	sys.exit()
#

if __name__ == "__main__":
	start()
#
