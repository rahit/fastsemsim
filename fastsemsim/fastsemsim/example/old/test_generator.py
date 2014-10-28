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

import sys
import os
import math
import gzip

import argparse

'''
Generate bash command lines for testing fastSemSim command line tool
'''

# export TEST=$2

# rm $TEST
# touch $TEST

# echo "export TEST_DIR=\$1" >> $TEST
# echo "export OLD_PP=\$PYTHONPATH" >> $TEST
# echo "export PYTHONPATH=\$PYTHONPATH:\$TEST_DIR" >> $TEST
# echo "export TEST_FILE=\$TEST_DIR/startfastSemSim.py" >> $TEST

# Extensive test on
# 1- different ontologies
# 2- different ss
# 3- different mix
# 4- different ac
# 5- different query
# 6- different output

# TEST_DIR=$1
# TEST_FILE=${TEST_DIR}/startfastSemSim.py
# export OLD_PP=$PYTHONPATH
# export PYTHONPATH=$PYTHONPATH:$TEST_DIR

# GO_g = [[0,],[1,5,6],[2,3,4,7,8,9,10,11,12]]
# AC_g = [[0],[1,2],[3,4,5,6]]
# GO_AC_system = [(0,0), (1,0), (1,1), (2,0), (2,2)]

# QUERYTYPE_g = [[0,],[1,],[2,],[3,]]
# QUERY_INPUT_g = [[0,],[1,],[2,],[3,], [4,], [5,], [6,], [7,]]
# QUERY_system=	[(0, 0), (0, 1), (0, 6), (0, 7),
# 				(1,6), (1,7),
# 				(2,1), (2,3), (2,4), (2,5),
# 				(3,3), (3,4), (3,5)
# 				]

# {
# 	'CellOntology':{
# 		'void':{
# 		},
# 	  },
# 	'DiseaseOntology':{
# 		'void':{
# 		},
# 		'DiseaseOntologyAC':{
# 			'term'
# 		},
# 	  },
# 	'GeneOntology':{
# 		'void':{
# 		},
# 		'GeneOntologyAC':{
# 			'term': {'ac':{}, 'go':{}},
# 			'obj': {'ac':{}},
# 			'termset': {''={}},
# 			'objset': {''={}},
# 		},
# 	  }
# }

def gen_command_lines(GO, AC, QUERYTYPE, QUERY_INPUT, MIX_STRATS, SSMEASURE, OUTF, VERBOSITY):
	for i,iv in GO.items():
	 if iv:
	 	for j, jv in AC.items():
	 	 if jv:
	 	 	for k, kv in QUERYTYPE.items():
	 	 	 if kv:
	 	 	 	for l, lv in QUERY_INPUT.items():
	 	 	 	 if lv:
	 	 	 	 	for m, mv in MIX_STRATS.items():
	 	 	 	 	 if mv:
	 	 	 	 	 	for n, nv in SSMEASURE.items():
	 	 	 	 	 	 if nv:
	 	 	 	 	 	 	for o, ov in OUTF.items():
	 	 	 	 	 	 	 if ov:
	 	 	 	 	 	 		for p, pv in VERBOSITY.items():
	 	 	 	 	 	 	 	 if pv:
		 	 	 	 	 	 	 	go = i
									ac = j
									query_type = k
									query_input = l
									mix_strats = m
									ssmeasure = n
									out_file = o
									verbosity = p
									

									# line = "python " + fastSemSim_command + " " + go + " " + ac + " " + ssmeasure + " " + mix_strats + " " + query_type + " " + query_input + " " + verbosity + " " + out_file
									line =  fastSemSim_command + " " + go + " " + ac + " " + ssmeasure + " " + mix_strats + " " + query_type + " " + query_input + " " + verbosity + " " + out_file
									print line
#


fastSemSim_command = ''
fastSemSim_command = sys.argv[1]

VERBOSITY=	{ "-v" : True 
			}

OUTF = {	"" : True,
			"--out_file test_output.txt" : False
		}


GO = {	"--o_type CellOntology" : False, # 0
		"--o_type DiseaseOntology" : True, # 1
		"--o_type GeneOntology" : False, # 2
		"--o_type Ontology" : False, # 3
		"" : False, # 4
		"--o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo" : False, # 5
		"--o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo" : False, # 6
		"--o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml" : False, # 7
		"--o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo --o_file_format obo" : False, # 8
		"--o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo" : False, # 9
		"--o_type Ontology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml" : False, # 10
		"--o_type Ontology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo --o_file_format obo" : False, # 11
		"--o_type Ontology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo" : False # 12
	}


AC = { 	"" : False, # 0
		"-a ./data/ACs/DO_human_ac_plain.txt --ac_type plain" : True, # 1
		# "-a ./data/ACs/DO_human_ac_gaf2.txt --ac_type gaf2" : False, # 2
		"-a ./data/ACs/gene_association.goa_yeast --ac_type gaf2" : False, # 3
		"-a ./data/ACs/gene_association.goa_mgi --ac_type gaf2" : False, # 4
		"-a ./data/ACs/gene_association.goa_fly --ac_type gaf2" : False, # 5
		"-a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst" : False # 6
	}


QUERYTYPE = {	"--query_ss_type term --query_type SS" : True, # 0
				"--query_ss_type termset --query_type SS" : True, # 1
				"--query_ss_type obj --query_type SS" : True, # 2
				"--query_ss_type objset --query_type SS" : True # 3
			}



QUERY_INPUT = {	"--query_input ontology" : False, # 0
				"--query_input ac" : False, # 1
				"--query_input file --query_file  ./data/query/DO_list_query.txt --query_mode list" : False, # 2
				"--query_input file --query_file  ./data/query/DO_list_objset_query.txt --query_mode list" : True, # 2
				"--query_input file --query_file  ./data/query/GO_fly_list_query.txt --query_mode list" : False, # 3
				"--query_input file --query_file  ./data/query/GO_fly_pairs_query.txt --query_mode pairs" : False, # 4
				"--query_input file --query_file  ./data/query/GO_fly_pairs_query.txt --query_mode list" : False, # 5
				"--query_input file --query_file  ./data/query/GO_term_pairs_query.txt --query_mode pairs" : False, # 6
				"--query_input file --query_file  ./data/query/GO_term_list_query.txt --query_mode list"  : False # 7
			}


MIX_STRATS = {	"--tmix BMA" : True,
				"--tmix avg" : False,
				"--tmix max" : False
			}

# SSMEASURE="SimRel G-SESAME Cosine SimICND SimICNP Resnik Lin SimGIC SimUI Jiang-Conrath SimIC Dice TO NTO Jaccard Czekanowski-Dice"
SSMEASURE = {	"--tss SimRel" : False,
				"--tss G-SESAME" : False,
				"--tss Cosine" : False,
				"--tss SimICND" : True,
				"--tss SimICNP" : False,
				"--tss Resnik" : False,
				"--tss Lin" : False,
				"--tss SimUI" : False,
				"--tss SimIC" : False,
				"--tss Dice" : False,
				"--tss Jiang-Conrath" : False,
				"--tss Czekanowski-Dice" : False,
				"--tss Jaccard" : False,
				"--tss NTO" : False,
				"--tss TO" : False,
				"" : False,
				"--tss SimGIC" : False
			}

gen_command_lines(GO, AC, QUERYTYPE, QUERY_INPUT, MIX_STRATS, SSMEASURE, OUTF, VERBOSITY)

GO = {	
		"--o_type GeneOntology" : True, # 2
		"--o_type Ontology" : True, # 3
		"" : True, # 4
		"--o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml" : True, # 7
		"--o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo --o_file_format obo" : False, # 8
		"--o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo" : True, # 9
		"--o_type Ontology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml" : True, # 10
		"--o_type Ontology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo --o_file_format obo" : False, # 11
		"--o_type Ontology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo" : False # 12
	}


AC = { 	"" : True, # 0
		"-a ./data/ACs/gene_association.goa_yeast --ac_type gaf2" : False, # 3
		"-a ./data/ACs/gene_association.goa_mgi --ac_type gaf2" : False, # 4
		"-a ./data/ACs/gene_association.goa_fly --ac_type gaf2" : True, # 5
		"-a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst" : False # 6
	}


QUERYTYPE = {	"--query_ss_type term --query_type SS" : True, # 0
				"--query_ss_type termset --query_type SS" : True, # 1
				"--query_ss_type obj --query_type SS" : True, # 2
				"--query_ss_type objset --query_type SS" : True # 3
			}



QUERY_INPUT = {	"--query_input ontology" : False, # 0
				"--query_input ac" : False, # 1
				"--query_input file --query_file  ./data/query/GO_fly_list_query.txt --query_mode list" : True, # 3
				"--query_input file --query_file  ./data/query/GO_fly_pairs_query.txt --query_mode pairs" : False, # 4
				"--query_input file --query_file  ./data/query/GO_fly_pairs_query.txt --query_mode list" : False, # 5
				"--query_input file --query_file  ./data/query/GO_term_pairs_query.txt --query_mode pairs" : False, # 6
				"--query_input file --query_file  ./data/query/GO_term_list_query.txt --query_mode list"  : False # 7
			}


MIX_STRATS = {	"--tmix BMA" : True,
				"--tmix avg" : False,
				"--tmix max" : False
			}

# SSMEASURE="SimRel G-SESAME Cosine SimICND SimICNP Resnik Lin SimGIC SimUI Jiang-Conrath SimIC Dice TO NTO Jaccard Czekanowski-Dice"
SSMEASURE = {	"--tss SimRel" : False,
				"--tss G-SESAME" : False,
				"--tss Cosine" : False,
				"--tss SimICND" : True,
				"--tss SimICNP" : False,
				"--tss Resnik" : False,
				"--tss Lin" : False,
				"--tss SimUI" : False,
				"--tss SimIC" : False,
				"--tss Dice" : False,
				"--tss Jiang-Conrath" : False,
				"--tss Czekanowski-Dice" : False,
				"--tss Jaccard" : False,
				"--tss NTO" : False,
				"--tss TO" : False,
				"" : False,
				"--tss SimGIC" : False
			}

gen_command_lines(GO, AC, QUERYTYPE, QUERY_INPUT, MIX_STRATS, SSMEASURE, OUTF, VERBOSITY)
