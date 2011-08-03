# -*- coding: iso-8859-1 -*-
####
#@author Marco Mina
#@mail marco.mina.85@gmail.com
#@version 1.0
#@desc Class to handle Annotation Corpora. It consists of 4 hash tables (dict)
'''
annotations: dict with protein ids as primary key. Each key is associated with a dict of annotations associated to the protein. Each annotation is a key itself (the term code in the GO is used as key), and it is associated to the EC/REF of the annotation. Multiple EC for the same annotation are possible.

reverse annotations: dict with term codes in the GO as primary key. Each key is associated with a dict of annotations associated to the term. Each annotation is a key itself (the protein ids are used as keys), and it is associated to the EC/REF of the annotation. Multiple EC for the same annotation are possible.

obj_set: set of proteins present in the annotation table, connected with the taxon id of the organism they belong to. This table is useful to filter out proteins from uninteresting species.

term_set: set of terms present in the annotation table.

'''

import sys
#from pairs import rowscounter
from GO import GeneOntology

class AnnotationCorpus:
	BP_root = "GO:0008150"
	MF_root = "GO:0003674"
	CC_root = "GO:0005575"
	exclude_GO_root = True
	SHOW_PROCESS_THRESHOLD = 50000
	separator = '\t'
	#### final tables to be filled and used
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
	#def isinEC(self,s):

	def get_simplified_data(self):
		finale = {}
		for i in self.annotations:
			finale[i] = {}
			for j in self.annotations[i]:
				finale[i][j] = {}
		return finale

	def constrain(self):
		if len(self.taxonomy_filter) == 0 and len(self.EC_filter) == 0:
			return
		temp_annotations = {}
		temp_reverse_annotations = {}
		temp_obj_set = {}
		if not len(self.taxonomy_filter) == 0:
			for i in self.original_obj_set:
				if self.original_obj_set[i] in self.taxonomy_filter:
					temp_obj_set[i] = self.original_obj_set[i]
		else:
			temp_obj_set = self.original_obj_set ### be careful! This is not a copy

		if len(self.EC_filter) > 0:
			for i in temp_obj_set:
				temp_annotations[i] = {}
				for j in self.original_annotations[i]:
					for k in self.original_annotations[i][j]:
						if (k in self.EC_filter and self.EC_filter_inclusive) or (k not in self.EC_filter and not self.EC_filter_inclusive):
							if j not in temp_annotations[i]:
								temp_annotations[i][j] = {}
							temp_annotations[i][j][k] = self.original_annotations[i][j][k]
			for i in self.original_reverse_annotations:
				for j in self.original_reverse_annotations[i]:
					if j in temp_obj_set:
						for k in self.original_reverse_annotations[i][j]:
							if (k in self.EC_filter and self.EC_filter_inclusive) or (k not in self.EC_filter and not self.EC_filter_inclusive):
								if i not in temp_reverse_annotations:
									temp_reverse_annotations[i] = {}
								if j not in temp_reverse_annotations[i]:
									temp_reverse_annotations[i][j] = {}
								temp_reverse_annotations[i][j][k] = self.original_reverse_annotations[i][j][k]
		else:
			for i in temp_obj_set:
				temp_annotations[i] = self.original_annotations[i]
			for i in self.original_reverse_annotations:
				for j in self.original_reverse_annotations[i]:
					if j in temp_obj_set:
						if i not in temp_reverse_annotations:
							temp_reverse_annotations[i] = {}
						temp_reverse_annotations[i][j] = self.original_reverse_annotations[i][j]

		self.annotations = temp_annotations
		self.obj_set = temp_obj_set
		self.reverse_annotations = temp_reverse_annotations
		self.term_set = self.reverse_annotations

	def parse(self, fname):
		self.annotations = {}
		self.obj_set = {}
		self.reverse_annotations = {}
		self.term_set = {}

		if self.go==None:
			print("No GO available.")
		elif self.go.alt_ids == None:
			print("No alternative id mapping table available.")
				
		#filenum = rowscounter.bufcount(fname);
		#if filenum > self.SHOW_PROCESS_THRESHOLD:
			#print(fname + " has " + str(filenum) + " lines.")
			#self.SHOW_PROCESS = True;
		#else:
			#self.SHOW_PROCESS = False;
		stream = open(fname)
		lines_counter = 0
		for line in stream:
			line = line.rstrip('\n')
			line = line.rstrip('\r')
			line = line.split(self.separator)
			if len(line) == 0:
				print("1")
				continue
			if len(line) < 14:
				print("2: " + str(line))
				continue
			taxon = line[12]
			if len(self.taxonomy_filter) > 0:
				if taxon not in self.taxonomy_filter:
					continue
			EC = line[6]
			obj_id = line[1]
			obj_name = line[2]
			term = line[4]
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

			reference = line[5]

			GO = line[8]
			#### Build up genes set
			if obj_id not in self.obj_set:
				self.obj_set[obj_id] = taxon
			#### Build up annotations set
			if obj_id not in self.annotations:
				self.annotations[obj_id] = {}
			if term not in self.annotations[obj_id]:
				self.annotations[obj_id][term] = {}
			if (len(self.EC_filter) == 0) or ((EC in self.EC_filter and self.EC_filter_inclusive) or (EC not in self.EC_filter and not self.EC_filter_inclusive)):
				if EC not in self.annotations[obj_id][term]:
					self.annotations[obj_id][term][EC] = []
				self.annotations[obj_id][term][EC].append((reference))
			#### Build up reverse annotations set
			if term not in self.reverse_annotations:
				self.reverse_annotations[term] = {}
			if obj_id not in self.reverse_annotations[term]:
				self.reverse_annotations[term][obj_id] = {}
			if (len(self.EC_filter) == 0) or ((EC in self.EC_filter and self.EC_filter_inclusive) or (EC not in self.EC_filter and not self.EC_filter_inclusive)):
				if EC not in self.reverse_annotations[term][obj_id]:
					self.reverse_annotations[term][obj_id][EC] = []
				self.reverse_annotations[term][obj_id][EC].append((reference))
			
			lines_counter += 1
			#if self.SHOW_PROCESS and (lines_counter%(filenum/20)==0):
				#print("Lines processed: " + str(lines_counter) + " on " + str(filenum) + " (" + str(int(100*float(lines_counter)/float(filenum))) + "%)")
		stream.close()
		self.original_annotations = self.annotations
		self.original_obj_set = self.obj_set
		self.original_reverse_annotations = self.reverse_annotations
		self.original_term_set = self.original_reverse_annotations
		self.term_set = self.original_reverse_annotations
		
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

	#def term_stats(self,term):
		#if self.n_proteins == -1:
			#det_secondary_data()
		#if term in self.reverse_annotations:
			#count = len(self.reverse_annotations[term])
			#freq = float(count)/float(self.n_annotated_proteins)
			##IC 

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

	#def sanitize(self, go = None):
		#redo = False
		#if not go is None:
			#self.go = go
			#redo = True
		#if self.go is None:
			#print("Go not provided. Cannot sanitize annotation corpus."
			#return None
		#if redo:
			#pass
		#for i in self.reverse_annotation:
			#if not i in self.go.nodes_edges 
			
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