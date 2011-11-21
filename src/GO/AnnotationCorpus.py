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

'''
This class provides a unified interface to handle Annotation Corpora.

annotations: dict with protein ids as primary key. Each key is associated with a dictionary of GO Terms annotated for the protein. Detailed information, when available, are included as values within the latter dictionary.

reverse_annotations: dict with GO Terms as primary key. Each key is associated with a dict of proteins/gene products annotated with the GO term.

obj_set: set of proteins/gene products present in the annotation table, connected with the taxon id of the organism they belong to, when this information is available. This table is useful to filter out proteins from uninteresting species.

term_set: set of terms present in the annotation table.

If a GO object is passed as input data, annotation corpus is corrected removing obsolete annotations and resolving alternative ids.
This can be done later by calling sanitize method after supplying a valid GO object.

general_parameters: filtering options and parameters that apply in general
specific_parameters: parameter that should be used to load a particular file format

Each type of file carries different types of information. How to deal with that? Every operation is rerouted to the original file parser, that will take care of it. This is good since it avoids to duplicate data. 

general methods:

initialize
reset
parse
sanitize
isConsistent
GROUP: filtering
	filter
	set_filter
simplify: withdraw all the information but object, terms and annotations
get <- retrieve the set of annotations. Output format? without any parameter the simplified one.
'''

import sys
import copy

from GO.GeneOntology import *
from GO.PlainAnnotationCorpus import PlainAnnotationCorpus
from GO.GAF2AnnotationCorpus import GAF2AnnotationCorpus

AnnotationCorpusFormat = {'gaf-2.0':GAF2AnnotationCorpus,
													'gaf-1.0':None,
													'GOA':GAF2AnnotationCorpus,
													'plain':PlainAnnotationCorpus
													}

FILTER_PARAM = 'filter'

class AnnotationCorpus:
	exclude_GO_root = True

	taxonomy_filter = {}
	EC_filter = {}
	EC_filter_inclusive = True
	
	def __init__(self, go=None):
		self.go = go
		self.reset()

	def reset(self):
		self.annotations = {}
		self.reverse_annotations = {}
		self.obj_set = {}
		self.term_set = {}
		
		self.filters = {}
		self.reset_fields()

	def reset_fields(self):
		self.obj_fields = []
		self.term_fields = []
		self.annotations_fields = []
		self.reverse_annotations_fields = []
		self.obj_field2pos= {}
		self.term_field2pos= {}
		self.annotations_field2pos= {}
		self.reverse_annotations_field2pos= {}

	def __deepcopy__(self, memo):
		a = AnnotationCorpus(self.go)
		a.exclude_GO_root = self.exclude_GO_root
		a.annotations = copy.deepcopy(self.annotations, memo)
		a.reverse_annotations = copy.deepcopy(self.reverse_annotations, memo)
		a.obj_set = copy.deepcopy(self.obj_set, memo)
		a.term_set= copy.deepcopy(self.term_set, memo)
		a.filter_taxonomy = copy.deepcopy(self.filter_taxonomy, memo)
		a.filter_EC = copy.deepcopy(self.filter_EC, memo)
		a.filter_EC_inclusive = self.filter_EC_inclusive
		a.filters = copy.deepcopy(self.filters, memo)
		a.obj_fields = self.obj_fields
		a.term_fields = copy.deepcopy(self.term_fields, memo)
		a.annotations_fields = copy.deepcopy(self.annotations_fields, memo)
		a.reverse_annotations_fields = copy.deepcopy(self.reverse_annotations_fields, memo)
		a.obj_field2pos= copy.deepcopy(self.obj_field2pos, memo)
		a.term_field2pos= copy.deepcopy(self.term_field2pos, memo)
		a.annotations_field2pos= copy.deepcopy(self.annotations_field2pos, memo)
		a.reverse_annotations_field2pos= copy.deepcopy(self.reverse_annotations_field2pos, memo)
		return a

	def sanitize(self):
		if self.go is None:
			print("No GO specified. Consistency check not available")
			return False
		valid = True
		for i in self.reverse_annotations.keys():
			if not i in self.go.alt_ids:
				#print("Term " + str(i) + " not found in GO.")
				for j in self.reverse_annotations[i]:
					del self.annotations[j][i]
				del self.reverse_annotations[i]
				continue
			if not i in self.go.nodes_edges:
				if self.go.alt_ids[i] == i:
					#print("Term " + str(i) + " is an obsolete id.")
					for j in self.reverse_annotations[i]:
						del self.annotations[j][i]
						if len(self.annotations[j])==0:
							del self.annotations[j]
							del self.obj_set[j]
					del self.reverse_annotations[i]
					del self.term_set[i]
				else:
					#print("Term " + str(i) + " is an alternative id.")
					for j in self.reverse_annotations[i]:
						if not self.go.alt_ids[i] in self.annotations[j]:
							self.annotations[j][self.go.alt_ids[i]] = self.annotations[j][i]
						else:
							for k in self.annotations[j][i]:
								if not k in self.annotations[j][self.go.alt_ids[i]]:
									self.annotations[j][self.go.alt_ids[i]][k] = self.annotations[j][i][k]
						del self.annotations[j][i]
					del self.reverse_annotations[i]
					del self.term_set[i]
					continue
		return True

	def isConsistent(self):
		return self.check_consistency()

	def check_consistency(self):
		if self.go is None:
			print("No GO specified. Consistency check not available")
			return False
		valid = True
		for i in self.reverse_annotations:
			if not i in self.go.alt_ids:
				print("Term " + str(i) + " not found in GO.")
				valid = False
				continue
			if not i in self.go.nodes_edges:
				if self.go.alt_ids[i] == i:
					print("Term " + str(i) + " is an obsolete id.")
					#self.obsoletes[i] = {}
					valid = False
				else:
					print("Term " + str(i) + " is an alternative id.")
					valid = False
					continue
		return valid

	def setFilter(self, field, selector):
		self.filters[field] = selector

	def set_filters(self, inf):
		if 'taxonomy' in inf:
			self.set_taxonomy_filter(inf['taxonomy'])
		if 'EC' in inf:
			self.set_EC_filter(inf['EC'])

	def reset_filter(self, field):
		if field in self.filters:
			del self.filters[field]

	def set_taxonomy_filter(self, tax):
		self.filter_taxonomy = tax
		self.setFilter('taxonomy', self.taxonomy_selector)

	def reset_taxonomy_filter(self):
		self.reset_filter('taxonomy')
		self.filter_taxonomy = None

	def set_EC_filter(self, EC, inclusive = False):
		self.filter_EC = EC
		self.filter_EC_inclusive = inclusive
		self.setFilter('EC', self.EC_selector)
		
	def reset_EC_filter(self):
		self.reset_filter('EC')
		self.filter_EC = None

	def taxonomy_selector(self, taxonomy):
		if self.filter_taxonomy == taxonomy:
			return True
		return False

	def EC_selector(self, EC):
		if self.filter_EC == EC and self.filter_EC_inclusive:
			return True
		elif not self.filter_EC == EC and not self.filter_EC_inclusive:
			return True
		return False

	def constrain(self):
		if len(self.filters)==0:
			return

		for cf in self.filters:
			if cf in self.obj_field2pos:
				cp = self.obj_field2pos[cf]
				cff = self.filters[cf]
				temp_obj_set = {}
				for i in self.obj_set:
					if cff(self.obj_set[i]):
						temp_obj_set[i] = self.obj_set[i]
				self.obj_set = temp_obj_set

		for cf in self.filters:
			if cf in self.term_field2pos:
				cp = self.term_field2pos[cf]
				cff = self.filters[cf]
				temp_term_set = {}
				for i in self.term_set:
					if cff(self.term_set[i]):
						temp_term_set[i] = self.term_set[i]
				self.term_set = temp_term_set

		temp_annotations = {}
		temp_reverse_annotations = {}
		for i in self.obj_set:
			for j in self.annotations[i]:
				if j in self.term_set:
							if i not in temp_annotations:
								temp_annotations[i] = {}
							if j not in temp_annotations[i]:
								temp_annotations[i][j] = self.annotations[i][j]
							if j not in temp_reverse_annotations:
								temp_reverse_annotations[j] = {}
							if i not in temp_reverse_annotations[j]:
								temp_reverse_annotations[j][i] = self.reverse_annotations[j][i]
		self.annotations = temp_annotations
		self.reverse_annotations = temp_reverse_annotations

		temp_to_apply = []
		for cf in self.filters:
			if cf in self.annotations_field2pos:
				cp = self.annotations_field2pos[cf]
				cff = self.filters[cf]
				temp_to_apply.append((cff, cp))

		if len(temp_to_apply) > 0:
			temp_annotations = {}
			temp_reverse_annotations = {}
			for i in self.annotations:
				for j in self.annotations[i]:
					for k in self.annotations[i][j]: # assume k is ... what? a tuple or a key???
						temp_keep = True
						for ct in temp_to_apply:
							if not ct[0](k[ct[1]]): # version for list
								temp_keep = False
							#if not ct[0](self.annotations[i][j][k][ct[1]]): # version for dict
								#temp_keep = False
							if temp_keep:
								#del self.annotations[i][j][k]
								if i not in temp_annotations:
									temp_annotations[i] = {}
								if j not in temp_annotations[i]:
									temp_annotations[i][j] = {} # ? are you sure?
								temp_annotations[i][j][k] = self.annotations[i][j][k] # works for dict only, not for lists!
								if j not in temp_reverse_annotations:
									temp_reverse_annotations[j] = {}
								if i not in temp_annotations[j]:
									temp_reverse_annotations[j][i] = {} # ? are you sure?
								temp_reverse_annotations[j][i][k] = self.reverse_annotations[j][i][k] # works for dict only, not for lists!
			self.annotations = temp_annotations
			self.reverse_annotations = temp_reverse_annotations

			temp_obj_set = {}
			temp_term_set = {}
			for i in self.annotations:
				temp_obj_set[i] = {}
				for j in self.annotations[i]:
					if j not in temp_term_set:
						temp_term_set[j] = {}
			self.obj_set = temp_obj_set
			self.term_set = temp_term_set

	def load(self, fname, ftype):
		self.parse(fname, ftype)

	def parse(self, fname, ftype, params=None):
		self.reset()
		if not params == None and FILTER_PARAM in params:
			self.set_filters(params[FILTER_PARAM])
		if ftype in AnnotationCorpusFormat:
			temp = AnnotationCorpusFormat[ftype](params, self)
			return temp.parse(fname)
		else:
			print "AnnotationCorpus.py: Format not recognized"
			return None
