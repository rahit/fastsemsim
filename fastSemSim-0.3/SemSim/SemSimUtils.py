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

"""
This class provides some routines to calculate basic properties used by different SS measures.
In particular this class provides code for evaluating:

- term ICs
- term frequency within an annotation corpus
- term's ancestors
- term's offspring
- terms's children
- terms's parents
- MICA/DCA/LCA
- term's distance

TODO:
- term depth
- terms common ancestors (between two terms or two sets of terms)
            I could use pairs module to to this!
"""

from GO import AnnotationCorpus
from GO import GeneOntology
import sys
import os
import math

class SemSimUtils:
	BP_root = "GO:0008150"
	MF_root = "GO:0003674"
	CC_root = "GO:0005575"
	BP_ontology = "BP"
	MF_ontology = "MF"
	CC_ontology = "CC"

	go = None
	annotation_corpus = None
	parents = None
	children = None
	ancestors = None
	offspring = None
	IC = None
	freq = None
	GO_division = None
	
	def __init__(self, ac, go):
		self.go = go
		self.annotation_corpus = ac
		self.init_structures()

	def go_name2id(self,code):
		return int(code[3:])

	def go_id2name(self,code):
		return "GO:" + '0'*(7 - len(str(code))) + str(code)

	def go_2ids(self, codes):
		if type(codes) is str:
			return self.go_name2id(codes)
		elif type(codes) is int:
			return codes
		elif type(codes) is dict or type(codes) is list:
			ids = []
			for i in codes:
				ids.append(self.go_2ids(i))
			return ids

	def go_2names(self, codes):
		if type(codes) is int:
			return self.go_id2name(codes)
		elif type(codes) is str:
			return codes
		elif type(codes) is dict or type(codes) is list:
			ids = []
			for i in codes:
				ids.append(self.go_2names(i))
			return ids

	def init_structures(self):
		self.parents = {}
		self.children = {}
		for i in self.go.nodes_edges:
			self.parents[i] = [] #### perche' non usare dicts?
			self.children[i] = [] #### perche' non usare dicts?
			for j in self.go.nodes_edges[i]:
				if self.go.edges_nodes[j][0] == i:
					self.parents[i].append(self.go.edges_nodes[j][1])
				else:
					#print(str(i) + " " + str(j)
					self.children[i].append(self.go.edges_nodes[j][0])

	def det_offspring(self, goid):
		if goid not in self.children:
			return set()
		anc = set()
		anc.add(goid)
		processed = {}
		queue = []
		for i in self.children[goid]:
			queue.append(i)
		#print(queue
		while len(queue) > 0:
			t = queue.pop()
			anc.add(t)
			#print(child_going[t]
			for tp in self.children[t]:
				#print(tp
				if tp not in processed:
					queue.append(tp)
			processed[t] = 0
		return anc

	def det_ancestors(self, goid):
		if goid not in self.parents:
			return set()
		anc = set()
		anc.add(goid)
		processed = {}
		queue = []
		for i in self.parents[goid]:
			queue.append(i)
		#print(queue
		while len(queue) > 0:
			t = queue.pop()
			anc.add(t)
			#print(parent_going[t]
			for tp in self.parents[t]:
				#print(tp
				if tp not in processed:
					queue.append(tp)
			processed[t] = 0
		return anc

	def det_offspring_table(self):
		self.offspring = {}
		for i in self.go.nodes_edges:
			self.offspring[i] = self.det_offspring(i)

	def det_ancestors_table(self):
		self.ancestors = {}
		for i in self.go.nodes_edges:
			self.ancestors[i] = self.det_ancestors(i)

	def det_GO_division(self):
		BP_GO = self.offspring[self.go_name2id(self.BP_root)]
		MF_GO = self.offspring[self.go_name2id(self.MF_root)]
		CC_GO = self.offspring[self.go_name2id(self.CC_root)]
		assigns = {}
		for i in BP_GO:
			assigns[i] = self.BP_root
		for i in MF_GO:
			assigns[i] = self.MF_root
		for i in CC_GO:
			assigns[i] = self.CC_root
		self.GO_division = assigns
		self.root = self.GO_division

	def det_freq(self,term_id):
		freq = 0
		children_set = self.offspring[term_id]
		for j in children_set:
			if j in self.annotation_corpus.reverse_annotations:
				freq += len(self.annotation_corpus.reverse_annotations[j])
		return freq

	def det_freq_table(self):
		self.freqs = {}
		for i in self.go.nodes_edges:
			self.freqs[i] = self.det_freq(i)
		#for i in self.annotation_corpus.reverse_annotations:
			#if not i in self.go.nodes_edges:
				#print("Errore: " + str(i)
				#sys.exit(1)

	def det_IC(self, term_id):
		if term_id in self.freqs:
			if self.freqs[term_id] == 0:
				return -1
			if self.GO_division[term_id] == self.BP_root:
				rootf = self.freqs[self.go_name2id(self.BP_root)]
			elif self.GO_division[term_id] == self.MF_root:
				rootf = self.freqs[self.go_name2id(self.MF_root)]
			elif self.GO_division[term_id] == self.CC_root:
				rootf = self.freqs[self.go_name2id(self.CC_root)]
			temp_IC = -math.log(float(self.freqs[term_id])/float(rootf))
			return temp_IC
		else:
			return -1

	def det_ICs_table(self):
		self.IC = {}
		for i in self.go.nodes_edges:
			temp_IC = self.det_IC(i)
			if not temp_IC == -1:
				self.IC[i] = temp_IC
			#else:				#### without this IC will not be complete
				#self.IC[i] = -1 ####

	def det_MICA(self, term1, term2):
		gene1anc = self.ancestors[term1]
		gene2anc = self.ancestors[term2]
		maxIC = 0
		maxterm = -1
		for i in gene1anc:
			if i in gene2anc:
				if self.IC[i] >= maxIC:
					maxIC = self.IC[i]
					maxterm = i
		return maxterm

	def int_merge_sets(self, set1, set2):
		ca = {}
		for i in set1:
			ca[i] = None
		for i in set2:
			ca[i] = None
		return ca
		
	def det_common_ancestors(self, term1, term2):
		if type(term1) is int:
			gene1anc = self.ancestors[term1]
		else:
			gene1anc = {}
			for i in term1:
				gene1anc = self.int_merge_sets(gene1anc, self.ancestors[i])
		if type(term2) is int:
			gene2anc = self.ancestors[term2]
		else:
			gene2anc = {}
			for i in term2:
				gene2anc = self.int_merge_sets(gene2anc, self.ancestors[i])
		#gene1anc = self.ancestors[term1]
		#gene2anc = self.ancestors[term2]
		ca = {}
		for i in gene1anc:
			if i in gene2anc:
				ca[i] = None
		return ca

	def get_ancestors(self, term1):
		if type(term1) is int:
			if term1 not in self.ancestors:
				return {}
			gene1anc = self.ancestors[term1]
		else:
			gene1anc = {}
			for i in term1:
				if i not in self.ancestors:
					continue
				gene1anc = self.int_merge_sets(gene1anc, self.ancestors[i])
		ca = {}
		for i in gene1anc:
			ca[i] = None
		return ca
		
	def det_ancestors_union(self, term1, term2):
		if type(term1) is int:
			if term1 not in self.ancestors:
				return {}
			gene1anc = self.ancestors[term1]
		else:
			gene1anc = {}
			for i in term1:
				if i not in self.ancestors:
					continue
				gene1anc = self.int_merge_sets(gene1anc, self.ancestors[i])
		#print(gene1anc
		if type(term2) is int:
			if term2 not in self.ancestors:
				return {}
			gene2anc = self.ancestors[term2]
		else:
			gene2anc = {}
			for i in term2:
				if i not in self.ancestors:
					continue
				gene2anc = self.int_merge_sets(gene2anc, self.ancestors[i])
		#print(gene2anc
		ca = {}
		for i in gene1anc:
			ca[i] = None
		for i in gene2anc:
			ca[i] = None
		return ca

if __name__ == "__main__":
	#### load ontology
	tree = GeneOntology.get_go_graph(open(sys.argv[1]))
	print("Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.V.__len__()) + ". Edges: " + str(tree.E.__len__()))
	
	#### load annotations
	gp = AnnotationCorpus.AnnotationCorpus(tree)
	gp.parse(sys.argv[2])

	#### create SemSimUtils class
	ssu = SemSimUtils(gp, tree)
	ssu.det_offspring_table()
	ssu.det_ancestors_table()
	ssu.det_freq_table()
	ssu.det_GO_division()
	ssu.det_ICs_table()
	for i in ssu.IC:
		print(str(ssu.go_id2name(i)) + '\t' + str(ssu.IC[i]))
		
	for i in ssu.annotation_corpus.reverse_annotations:
		if not i in ssu.go.nodes_edges:
			print("Obsolete term: " + str(i))