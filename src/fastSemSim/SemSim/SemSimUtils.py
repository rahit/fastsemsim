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

from fastSemSim.GO import AnnotationCorpus
from fastSemSim.GO import Ontology
import sys
import os
import math


class SemSimUtils:
	
# internal functions

# variables available
	# BP_ontology = "BP"
	# MF_ontology = "MF"
	# CC_ontology = "CC"

	go = None
	ac = None
	ancestors = None
	offspring = None
	IC = None
	freq = None
	GO_root = None
	p = None
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#internal functions

	def __init__(self, ac, go):
		self.go = go
		self.ac = ac
		self.int_det_offspring_table()
		self.int_det_ancestors_table()
		self.int_det_GO_root()

		#self.det_freq_table()
		#self.det_ICs_table()

	def int_det_offspring_table(self):
		self.offspring = {}
		for i in self.go.nodes:
			self.offspring[i] = self.int_det_offspring(i)

	def int_det_ancestors_table(self):
		self.ancestors = {}
		for i in self.go.nodes:
			self.ancestors[i] = self.int_det_ancestors(i)

	def int_det_offspring(self, goid):
		if goid not in self.go.children:
			return set()
		anc = set()
		anc.add(goid)
		processed = {}
		queue = []
		for i in self.go.children[goid]:
			queue.append(i)
		#print(queue
		while len(queue) > 0:
			t = queue.pop()
			anc.add(t)
			#print(child_going[t]
			for tp in self.go.children[t]:
				#print(tp
				if tp not in processed:
					queue.append(tp)
			processed[t] = 0
		return anc

	def int_det_ancestors(self, goid):
		if goid not in self.go.parents:
			return set()
		anc = set()
		anc.add(goid)
		processed = {}
		queue = []
		for i in self.go.parents[goid]:
			queue.append(i)
		#print(queue
		while len(queue) > 0:
			t = queue.pop()
			anc.add(t)
			#print(parent_going[t]
			for tp in self.go.parents[t]:
				#print(tp
				if tp not in processed:
					queue.append(tp)
			processed[t] = 0
		return anc

	def int_det_GO_root(self):
		#BP_GO = self.offspring[self.go.name2id(self.go.BP_root)]
		#MF_GO = self.offspring[self.go.name2id(self.go.MF_root)]
		#CC_GO = self.offspring[self.go.name2id(self.go.CC_root)]
		BP_GO = self.offspring[self.go.BP_root]
		MF_GO = self.offspring[self.go.MF_root]
		CC_GO = self.offspring[self.go.CC_root]
		assigns = {}
		for i in BP_GO:
			#if i in assigns:
				#raise Exception
			assigns[i] = self.go.BP_root
		for i in MF_GO:
			#if i in assigns:
				#raise Exception
			assigns[i] = self.go.MF_root
		for i in CC_GO:
			#if i in assigns:
				#raise Exception
			assigns[i] = self.go.CC_root
		self.GO_root = assigns

	def int_det_freq(self,term_id):
		freq = 0
		children_set = self.offspring[term_id]
		for j in children_set:
			if j in self.ac.reverse_annotations:
				freq += len(self.ac.reverse_annotations[j])
		return freq

	def int_det_freq_table(self):
		self.freq = {}
		for i in self.go.nodes:
			self.freq[i] = self.int_det_freq(i)

	def int_det_p_table(self):
		self.p = {}
		for i in self.go.nodes:
			self.p[i] = self.int_det_p(i)

	def int_det_p(self,term_id):
		if self.freq == None:
			self.int_det_freq_table()
		if not term_id in self.freq:
			return None
		if self.freq[term_id] == float(0):
			return float(0)
		rootf = self.freq[self.GO_root[term_id]]
		temp_p = float(self.freq[term_id])/float(rootf)
		return temp_p

	def int_det_IC(self, term_id):
		pr = self.int_det_p(term_id)
		if pr == None:
			return None
		if pr == float(0):
			return None
		pr = -math.log(pr)
		if pr == float(-0):
			pr = -pr 
		return pr

	def int_det_IC_table(self):
		self.IC = {}
		conta = 0
		for i in self.go.nodes:
			conta+= 1
			#print conta
			#print len(self.go.nodes_edges)
			temp_IC = self.int_det_IC(i)
			#if not temp_IC == None:
			self.IC[i] = temp_IC

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# public functions

# ASSUMPTION: Terms are passed as integers or lists of integers, not as strings!

	def det_IC_table(self):
		self.int_det_IC_table()
		return self.IC

	def det_IC(self,term):
		id = self.go.name2id(term)
		if self.IC == None:
			self.det_IC_table()
		if id in self.IC:
			return self.IC[id]
		return None

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

	def intersection(self, set1, set2):
		ca = {}
		for i in set1:
			if i in set2:
				ca[i] = None
		return ca

	def difference(self, set1, set2):
		ca = {}
		for i in set1:
			if not i in set2:
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
