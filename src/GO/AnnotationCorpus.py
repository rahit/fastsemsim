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

####
#@desc Class to handle Annotation Corpora. It consists of 4 hash tables (dict)
'''
annotations: dict with protein ids as primary key. Each key is associated with a dict of annotations associated to the protein. Each annotation is a key itself (the term code in the GO is used as key), and it is associated to the EC/REF of the annotation. Multiple EC for the same annotation are possible.

reverse annotations: dict with term codes in the GO as primary key. Each key is associated with a dict of annotations associated to the term. Each annotation is a key itself (the protein ids are used as keys), and it is associated to the EC/REF of the annotation. Multiple EC for the same annotation are possible.

obj_set: set of proteins present in the annotation table, connected with the taxon id of the organism they belong to. This table is useful to filter out proteins from uninteresting species.

term_set: set of terms present in the annotation table.

If a GO is passed as input data, annotation corpus is corrected removing obsolete annotations and resolving alternative ids.
'''

import sys
import copy
#from pairs import rowscounter
#from GO import GeneOntology
import GeneOntology
import GOAAnnotationCorpus
import PlainAnnotationCorpus

class AnnotationCorpus:
	exclude_GO_root = True
	go = None
	#SHOW_PROCESS_THRESHOLD = 50000
	
	annotations = {}
	reverse_annotations = {}
	obj_set = {}
	term_set = {}

	taxonomy_filter = {}
	EC_filter = {}
	EC_filter_inclusive = True
	
	def __init__(self, tree=None):
		self.go = tree
		self.reset()

	def reset(self):
		self.annotations = {}
		self.reverse_annotations = {}
		self.obj_set = {}
		self.term_set = {}

	def __deepcopy__(self, memo):
		a = AnnotationCorpus(self.go)
		a.exclude_GO_root = self.exclude_GO_root
		a.go = self.go
		a.annotations = copy.deepcopy(self.annotations, memo)
		a.reverse_annotations = copy.deepcopy(self.reverse_annotations, memo)
		a.obj_set = copy.deepcopy(self.obj_set, memo)
		a.term_set= copy.deepcopy(self.term_set, memo)
		a.taxonomy_filter = copy.deepcopy(self.taxonomy_filter, memo)
		a.EC_filter = copy.deepcopy(self.EC_filter, memo)
		a.EC_filter_inclusive = self.EC_filter_inclusive
		return a

	#def isinEC(self,s):

	#def get_annotations(self):
		#finale = {}
		#for i in self.annotations:
			#finale[i] = {}
			#for j in self.annotations[i]:
				#finale[i][j] = {}
		#return finale

	#def get_reverse_annotations(self):
		#finale = {}
		#for i in self.reverse_annotations:
			#finale[i] = {}
			#for j in self.reverse_annotations[i]:
				#finale[i][j] = {}
		#return finale

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

	def set_taxonomy_filter(self, tax):
		self.taxonomy_filter = tax
	def reset_taxonomy_filter(self):
		self.taxonomy_filter = {}
	def set_EC_filter(self, tax):
		self.EC_filter = tax
	def reset_EC_filter(self):
		self.EC_filter = {}
	def set_EC_filter_rule(self, inclusive):
		self.EC_filter_inclusive = inclusive
	def reset_EC_filter_rule(self):
		self.EC_filter_inclusive = True
		
	def constrain(self):
		if len(self.taxonomy_filter) == 0 and len(self.EC_filter) == 0:
			return
		temp_annotations = {}
		temp_reverse_annotations = {}
		temp_obj_set = {}
		temp_term_set = {}

		if not len(self.taxonomy_filter) == 0:
			for i in self.obj_set:
				if self.obj_set[i] in self.taxonomy_filter:
					temp_obj_set[i] = self.obj_set[i]
		else:
			temp_obj_set = self.obj_set ### be careful! This is not a copy

		if len(self.EC_filter) > 0:
			for i in temp_obj_set:
				#temp_annotations[i] = {}
				for j in self.annotations[i]:
					for k in self.annotations[i][j]:
						if (k in self.EC_filter and self.EC_filter_inclusive) or (k not in self.EC_filter and not self.EC_filter_inclusive):
							if i not in temp_annotations:
								temp_annotations[i] = {}
							if j not in temp_annotations[i]:
								temp_annotations[i][j] = {}
							temp_annotations[i][j][k] = self.annotations[i][j][k]
			for i in self.reverse_annotations:
				for j in self.reverse_annotations[i]:
					if j in temp_obj_set:
						for k in self.reverse_annotations[i][j]:
							if (k in self.EC_filter and self.EC_filter_inclusive) or (k not in self.EC_filter and not self.EC_filter_inclusive):
								if i not in temp_reverse_annotations:
									temp_reverse_annotations[i] = {}
									temp_term_set[i] = {}
								if j not in temp_reverse_annotations[i]:
									temp_reverse_annotations[i][j] = {}
								temp_reverse_annotations[i][j][k] = self.reverse_annotations[i][j][k]
		else:
			for i in temp_obj_set:
				temp_annotations[i] = self.annotations[i]
			for i in self.reverse_annotations:
				for j in self.reverse_annotations[i]:
					if j in temp_obj_set:
						if i not in temp_reverse_annotations:
							temp_reverse_annotations[i] = {}
							temp_term_set[i] = {}
						temp_reverse_annotations[i][j] = self.reverse_annotations[i][j]

		self.annotations = temp_annotations
		self.obj_set = temp_obj_set
		self.reverse_annotations = temp_reverse_annotations
		self.term_set = temp_term_set

	def load(self, fname, ftype):
		self.parse(fname, ftype)

	def parse(self, fname, ftype, params=None):
		if ftype is 'GOA':
			temp = GOAAnnotationCorpus.GOAAnnotationCorpus()
			return temp.parse(fname, self)
		elif ftype is 'plain':
			temp = PlainAnnotationCorpus.PlainAnnotationCorpus()
			temp.objfirst = True
			if not(params == None):
				if 'AC_OBJ_FIRST' in params:
					temp.objfirst = True
				elif 'AC_TERM_FIRST' in params:
					temp.objfirst = False
			return temp.parse(fname, self)


if __name__ == "__main__":
	tree = GeneOntology.get_go_graph(open(sys.argv[1]))
	print("Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.V.__len__()) + ". Edges: " + str(tree.E.__len__()))
	
	gp = AnnotationCorpus(tree)

	tax_filter = {}
	tax_filter['taxon:103351'] = []
	tax_filter['taxon:10335'] = []
	tax_filter['taxon:10338'] = []
	tax_filter['taxon:341980'] = []
	tax_filter['taxon:103354'] = []
	tax_filter['taxon:103353'] = []
	tax_filter['taxon:103352'] = []
	tax_filter['taxon:154633'] = []
	tax_filter['taxon:103387'] = []
	tax_filter['taxon:103385'] = []
	tax_filter['taxon:103380'] = []
	tax_filter['taxon:103355'] = []
	tax_filter['taxon:103350'] = []
	#gp.set_taxonomy_filter(tax_filter)
	gp.reset_taxonomy_filter()
	EC_filter = {}
	EC_filter['IES'] = []
	#gp.set_EC_filter(EC_filter)
	gp.reset_EC_filter()
	gp.parse(sys.argv[2])
	gp.set_EC_filter(EC_filter)
	#gp.reset_EC_filter()
	gp.set_taxonomy_filter(tax_filter)
	gp.constrain()
	
	print("Annotated proteins: " + str(len(gp.annotations)))
	print("Annotated terms: " + str(len(gp.reverse_annotations)))
	
	for i in gp.annotations:
		print(i + ": " + str(gp.annotations[i]))
	for i in gp.reverse_annotations:
		print(i + ": " + str(gp.reverse_annotations[i]))
	#for i in gp.obj_set:
		#print(i + ": " + str(gp.obj_set[i])