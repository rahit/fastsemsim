# -*- coding: iso-8859-1 -*-

# Copyright 2011 Marco Mina. All rights reserved.

# This file is part of fastSemSim

# fastSemSim is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# fastSemSim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with fastSemSim.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function
try:
	unicode
except (NameError, AttributeError):
	unicode = str #For python3

# print "fastsemsim/data/dataset.py"

import pandas as pd
# import sys
import os

from fastsemsim import ontology

ontology_aliases = {
	'GeneOntology' : 'GeneOntology',
	'geneontology' : 'GeneOntology',
	'GO' : 'GeneOntology',
	'go' : 'GeneOntology',
	'DiseaseOntology' : 'DiseaseOntology',
	'diseaseontology' : 'DiseaseOntology',
	'DO' : 'DiseaseOntology',
	'do' : 'DiseaseOntology',
	'CellOntology' : 'CellOntology',
	'cellontology' : 'CellOntology',
	'CO' : 'CellOntology',
	'co' : 'CellOntology',
	'FFOntology' : 'FFOntology',
	'FF' : 'FFOntology',
	'GenericOntology' : 'GenericOntology',
	'Ontology' : 'Ontology',
}

class Dataset(object):
	'''
	This class keeps track of the dataset of ontologies and annotation corpora included in fastSemSim.
	The file data/dataset.txt is read to collect the list of embedded ontologies and annotation corpora.
	'''

	def __init__(self, descriptor=None):
		'''
		Initialize class structures. Use the descriptor parameter to specify a dataset descriptor file.
		By default, the file data/dataset.txt will be used.
		'''
		# program_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
		# print "dataset.py: " + program_dir
		self.populate(descriptor)
		# print self.dataset
	#

	def populate(self, descriptor=None):
		'''
		Initialize class structures. Use the descriptor parameter to specify a dataset descriptor file.
		By default, the file data/dataset.txt will be used.
		'''
		descriptor_null = False
		if descriptor == None:
			descriptor_null = True
		if descriptor_null:
			program_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
			# print program_dir
			descriptor = program_dir + '/dataset.txt'
		self.dataset = pd.read_csv(descriptor, sep="\t", comment="#", header=0).dropna(how='all')
		self.dataset.index = self.dataset['name']
		if descriptor_null:
			program_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")  + "/"
			self.dataset['file'] = program_dir + self.dataset['file']
			# print self.dataset
	#

	def get_dataset(self, dataset_name):
		'''
		Return the required dataset
		'''
		# if not dataset_name in self.dataset.index:
			# return None
		return self.dataset.loc[self.dataset['name'] == dataset_name] # return the selected ontology or ac
	#

##############
# Ontology section
##############
	def list_ontologies(self):
		return(self.dataset.loc[self.dataset['type'] == 'O'])
	#

	def get_ontology(self, ontology_name=None, ontology_type='GeneOntology'):
		'''
		Return the required ontology
		'''
		if (ontology_name == None) & (ontology_type == None):
			raise Exception('At least one between ontology_type and ontology_name must be provided.')

		if ontology_type in ontology_aliases: # mapping aliases
			ontology_type = ontology_aliases[ontology_type]

		current_options = self.dataset.loc[self.dataset['type'] == 'O']
		if not ontology_type == None:
			current_options = current_options.loc[current_options['ontology'] == ontology_type]

		if not ontology_name == None:
			current_options = current_options.loc[current_options['name'] == ontology_name]

		return current_options
#

	def get_default_ontology(self, ontology_type='GeneOntology'):
		'''
		Return the default embedded ontology of the ontology_type type
		'''
		selected = self.get_ontology(ontology_name = None, ontology_type=ontology_type)
		if selected.shape[0] == 0:
			return None
		return selected.iloc[0] # return the first (preferred) ontology
	#


##############
# AC section
##############
	def list_acs(self):
		return(self.dataset.loc[self.dataset['type'] == 'AC'])
	#

	def get_annotation_corpus(self, ac_name=None, ontology_type=None, ac_species=None):
		'''
		Return the required annotation corpus
		'''
		if (ac_name == None) & (ontology_type == None):
			raise Exception('At least one between ontology_type and ac_name must be provided.')

		if ontology_type in ontology_aliases: # mapping aliases
			ontology_type = ontology_aliases[ontology_type]
			
		current_options = self.dataset.loc[self.dataset['type'] == 'AC']
		if not ontology_type == None:
			current_options = current_options.loc[current_options['ontology'] == ontology_type]

		if not ac_name == None:
			current_options = current_options.loc[current_options['name'] == ac_name]

		if not ac_species == None:
			current_options = current_options.loc[current_options['species'] == ac_species]

		return current_options
	#

	def get_default_annotation_corpus(self, ontology_type='GeneOntology', ac_species='human'):
		'''
		Return the default annotation corpus for the selected species, and compatible with the ontology specified by the ontology parameter.
		'''
		selected = self.get_annotation_corpus(ac_name = None, ontology_type = ontology_type, ac_species = ac_species)
		if selected.shape[0] == 0:
			return None
		return selected.iloc[0] # return the first (preferred) ontology
	#
#
