#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
'''
Copyright 2011-2019 Marco Mina. All rights reserved.

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

from __future__ import print_function
try:
	unicode
except (NameError, AttributeError):
	unicode = str #For python3

from fastsemsim import ontology
from fastsemsim import ac
from fastsemsim import data
from fastsemsim import semsim


# --------------------------------------------
# Export some convenient entrypoint functions to load ontologies and annotation corpora

# entrypoint object: dataset
# Entrypoint function: list available ontologies and annotation corpora
dataset = data.dataset
list_ontologies = dataset.list_ontologies
list_acs = dataset.list_acs


# Helping function: load ontology
# load_ontology = ontology.load # base version form ontology module. No dataset check
def load_ontology(source_file = None, file_type = 'obo', ontology_type = 'GeneOntology', ontology_descriptor = None, parameters={}):
	if not ontology_descriptor == None:
		selected_source = ontology_descriptor
		# print(selected_source)
		source_file = selected_source['file']
		file_type = selected_source['filetype']
		ontology_type = selected_source['ontology']		
	elif source_file == None:
		selected_source = dataset.get_default_ontology(ontology_type)
		# print(selected_source)
		if selected_source is None:
			return None
		source_file = selected_source['file']
		file_type = selected_source['filetype']
		ontology_type = selected_source['ontology']

	return(ontology.load(source_file = source_file, file_type = file_type, ontology_type = ontology_type, parameters = parameters))
#

# Entrypoint function: load Annotation corpus
AnnotationCorpus = ac.AnnotationCorpus
# Helping function: load annotation corpus
# load_ac = ac.load_ac # base version from ac module. No dataset check
def load_ac(ontology, source_file = None, file_type = None, species = None, ac_descriptor = None, params={}):
	if not ac_descriptor == None:
		selected_source = ac_descriptor
		source_file = selected_source['file']
		file_type = selected_source['filetype']
		fontologytype = selected_source['ontology']
	elif source_file == None:
		selected_source = dataset.get_default_annotation_corpus(ontology_type = ontology.name, ac_species = species)
		# print(selected_source)
		if selected_source is None:
			return None
		source_file = selected_source['file']
		file_type = selected_source['filetype']
		fontologytype = selected_source['ontology']

	return(ac.load_ac(ontology=ontology, source_file=source_file, file_type=file_type, params=params))
#

# Entrypoint function: init a SemSim object
# semsim_types = ('obj', 'term', 'objset', 'termset')
def init_semsim(ontology, ac=None, semsim_type = 'obj', semsim_measure='Resnik', mixing_strategy='max', ss_util=None, do_log = False, params={}):
	semsim_class = semsim.select_term_semsim(semsim_measure)
	mix_class = semsim.select_mix_strategy(mixing_strategy)
#
	# util = SemSimUtils(ontology, ac)
	# util.det_IC_table()
	ss = None
	if semsim_type == 'term':
		ss = semsim_class(ontology, ac, ss_util=ss_util, do_log=do_log)
	elif semsim_type == 'obj':
		ss = semsim.ObjSemSim(ontology, ac, semsim_measure, mixing_strategy, ss_util, do_log = do_log)
	elif semsim_type == 'termset':
		ss = semsim.SetSemSim(ontology, ac, semsim_measure, mixing_strategy, ss_util, do_log = do_log)
	elif semsim_type == 'objset':
		ss = semsim.ObjSetSemSim(ontology, ac, semsim_measure, mixing_strategy, ss_util, do_log = do_log)
	else:
		raise Exception
	return(ss)
#
