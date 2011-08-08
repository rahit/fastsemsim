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

__author__="Marco Mina"
#@mail marco.mina.85@gmail.com
#@version 1.0
#@desc This class reads plain annotation corpus files.
#Plain format 1: protein ID - Term ID
#Plain format 1: protein ID - Taxonomy - Term ID
#Plain format 3: protein ID - Taxonomy - Term ID - EC
#In all the cases each row defines just 1 annotation.
#### annotations: dict with protein ids as primary key. Each key is associated with a dict of annotations associated to the protein. Each annotation is a key itself (the term code in the GO is used as key), and it is associated to the EC/REF of the annotation. Multiple EC for the same annotation are possible.
#
#### reverse annotations: dict with term codes in the GO as primary key. Each key is associated with a dict of annotations associated to the term. Each annotation is a key itself (the protein ids are used as keys), and it is associated to the EC/REF of the annotation. Multiple EC for the same annotation are possible.
#
#### obj_set: set of proteins present in the annotation table, connected with the taxon id of the organism they belong to. This table is useful to filter out proteins from uninteresting species.
#
####
import sys
#from pairs import rowscounter

class PlainAnnotationCorpus:
	BP_root = "GO:0008150"
	MF_root = "GO:0003674"
	CC_root = "GO:0005575"
	exclude_GO_root = True
	SHOW_PROCESS_THRESHOLD = 50000
	separator = '\t'
	#### final tables to be filled and used
	
	annotations = {}
	reverse_annotations = {}
	obj_set = {}

	original_annotations = {}
	original_reverse_annotations = {}
	original_obj_set = {}
	original_term_set = {}
	
	annotations = {}
	reverse_annotations = {}
	obj_set = {}
	term_set = {}
	obsoletes = {}

	taxonomy_filter = {}
	EC_filter = {}
	EC_filter_inclusive = True
	
	def __init__(self, tree=None):
		self.go = tree
		
	def check_consistency(self):
		if self.go is None:
			return None
		valid = True
		for i in self.reverse_annotations:
			if not i in self.go.alt_ids:
				print("Term " + str(i) + " not found in GO.")
				valid = False
				continue
			if not i in self.go.nodes_edges:
				if self.go.alt_ids[i] == i:
					print("Term " + str(i) + " is an obsolete id.")
					self.obsoletes[i] = {}
				else:
					print("Term " + str(i) + " is an alternative id.")
					valid = False
					continue
		if valid:
			print("Annotation Corpus is consistent.")
			
	def parse(self, fname):
		self.annotations = {}
		self.obj_set = {}
		self.reverse_annotations = {}

		#filenum = rowcount(fname);
		#if filenum > self.SHOW_PROCESS_THRESHOLD:
			#print(fname + " has " + str(filenum) + " lines."
			#self.SHOW_PROCESS = True;
		#else:
		self.SHOW_PROCESS = False;
		stream = open(fname)
		lines_counter = 0
		for line in stream:
			line = line.rstrip('\n')
			line = line.rstrip('\r')
			line = line.split(self.separator)
			if len(line) == 0:
				continue
			if len(line) < 2:
				print("Strange line: " + str(line))
				continue
			obj_id = line[1]
			term = line[0]
			#term = int(term[3:])
			
			if self.exclude_GO_root:
				if term == self.BP_root:
					continue
				if term == self.CC_root:
					continue
				if term == self.MF_root:
					continue
			term = int(term[3:])
			if not self.go == None and not self.go.alt_ids == None:
				if not term in self.go.alt_ids:
					print(str(term) + " not in GO. Error")
					sys.exit(1)
				else:
					if not term == self.go.alt_ids[term]:
						#print("Remapping " + str(term) + " to " + str(self.go.alt_ids[term])
						term = self.go.alt_ids[term]
						
			#### Build up genes set
			if obj_id not in self.obj_set:
				self.obj_set[obj_id] = {}
			#### Build up annotations set
			if obj_id not in self.annotations:
				self.annotations[obj_id] = {}
			if term not in self.annotations[obj_id]:
				self.annotations[obj_id][term] = {}
			#### Build up reverse annotations set
			if term not in self.reverse_annotations:
				self.reverse_annotations[term] = {}
			if obj_id not in self.reverse_annotations[term]:
				self.reverse_annotations[term][obj_id] = {}
			lines_counter += 1
			if self.SHOW_PROCESS and (lines_counter%(filenum/20)==0):
				print("Lines processed: " + str(lines_counter) + " on " + str(filenum) + " (" + str(int(100*float(lines_counter)/float(filenum))) + "%)")
		stream.close()
		self.original_annotations = self.annotations
		self.original_obj_set = self.obj_set
		self.original_reverse_annotations = self.reverse_annotations
		
	def invalidate_secondary_data(self):
		self.n_proteins = -1
		self.n_terms = -1
		self.n_annotated_proteins = -1
		#self.n_most_annotated_protein = ''
		
	def det_secondary_data(self):
		self.n_proteins = len(self.obj_id)
		self.n_term = len(self.reverse_annotations)
		self.n_annotated_proteins = self.n_proteins
		for i in self.annotations:
			if len(self.annotations[i])==0:
				self.n_annotated_proteins -= 1

if __name__ == "__main__":
	gp = PlainAnnotationCorpus()
	gp.parse(sys.argv[1])
	for i in gp.annotations:
		print(str(i) + ": " + str(gp.annotations[i]))
