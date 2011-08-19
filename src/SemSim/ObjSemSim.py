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
This class provides the prototype for a generic Protein (or more in general, an Object) Semantic Similarity measure (PSS)
"""

from GO import AnnotationCorpus
from GO import GeneOntology
from SemSim.SemSimUtils import *
from SemSim.TermSemSim import *
from SemSim.MixSemSim import *
from  SemSim.SemSimMeasures import *

import sys
import os
import math

class ObjSemSim:
	def pick_TSS(self):
		if not self.TSS in SemSimMeasures:
			print("Semantic Similarity Measure not available.")
			return TermSemSim(self.annotation_corpus, self.go, self.util)
		else:
			return SemSimMeasures[self.TSS][0](self.annotation_corpus, self.go, self.util)

	def pick_mixSS(self):
		if not self.mixSS in MixingStrategies:
			print("Mixing Strategy not available.")
			return MixSemSim(self.annotation_corpus, self.go)
		else:
			return MixingStrategies[self.mixSS](self.annotation_corpus, self.go)

	def __init__(self, ac, go, TSS = None, MSS = None, util = None):
		self.go = go
		self.annotation_corpus = ac
		self.util = util
		self.TSS = TSS
		self.mixSS = MSS
		if self.util == None:
			self.util = SemSimUtils(self.annotation_corpus, self.go)
			self.util.det_offspring_table()
			self.util.det_ancestors_table()
			self.util.det_freq_table()
			self.util.det_GO_division()
			self.util.det_ICs_table()
		if self.TSS is None:
			self.TSS = TermSemSim(self.annotation_corpus, self.go, self.util)
		elif type(self.TSS) is str:
			self.TSS = self.pick_TSS()
		else:
			pass
		if self.mixSS is None:
			self.mixSS = MixSemSim(self.annotation_corpus, self.go)
		elif type(self.mixSS) is str:
			self.mixSS = self.pick_mixSS()
		else:
			pass

	def int_format_data(self, obj, onto):
		if not obj in self.annotation_corpus.annotations:
			print(str(obj) + " not found in Annotation Corpus!")
			return None
		terms = []
		for i in self.annotation_corpus.annotations[obj]:
			if i in self.go.obsolete_ids:
				#print(str(i) + " obsolete!"
				continue
			if i not in self.util.GO_division:
				print(str(i) + " not in GO!")
			elif self.util.GO_division[i] is onto:
				terms.append(i)
		return terms
		
	def SemSim(self, obj1, obj2, ontology):
		#### translate into id format & check data
		if ontology is self.util.BP_ontology:
			onto = self.util.BP_root
		elif ontology is self.util.MF_ontology:
			onto = self.util.MF_root
		elif ontology is self.util.CC_ontology:
			onto = self.util.CC_root
		else:
			print("No valid ontology selected.")
			return None
		t1 = self.int_format_data(obj1, onto)
		if t1 is  None:
			return None
		t2 = self.int_format_data(obj2, onto)
		if t2 is  None:
			return None
		return self.int_SemSim(t1, t2)

	def int_SemSim(self, term1, term2):
		if term1 is None or term2 is None or len(term1) == 0 or len(term2) == 0:
			return None
		#print self.TSS
		#print self.TSS.SS_type
		if self.TSS.SS_type is self.TSS.P_TSS:
			sscore = self.mixSS.SemSim(term1, term2, self.TSS)
		elif self.TSS.SS_type is self.TSS.G_TSS:
			sscore = self.TSS.SemSim(term1, term2)
		else:
			raise "Semantic Similarity measure not properly configured."
		return sscore

#if __name__ == "__main__":
	
	#inf = open('random_human_pp.txt','r')
	#human_pairs = []
	#for line in inf:
		#line = line.rstrip('\n')
		#line = line.rstrip('\r')
		#line = line.rsplit('\t')
		#human_pairs.append((line[0], line[1]))
		#print("\"" + line[0] + "\"" + line[1] + "\"")
	##yeast_test_set = ["A8DNB8","A2P2R3", "A2P2R3","A5Z2X5","A8DNA4","A8DNB7","A8DNB8","B0CLU6"]
	##test_set = yeast_test_set
	#test_set = human_pairs
	#inf.close()
	
	##SS_Resnik_max = config(sys.argv[1], sys.argv[2], "Resnik", "max")
	
	##### load ontology
	#tree = GeneOntology.get_go_graph(open(sys.argv[1]))
	#print("Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.V.__len__()) + ". Edges: " + str(tree.E.__len__()))
	
	##### load annotations
	#gp = AnnotationCorpus.AnnotationCorpus(tree)
	#gp.parse(sys.argv[2])
	
	#gp.check_consistency()
	#print("Annotated proteins: " + str(len(gp.annotations)))
	#print("Annotated terms: " + str(len(gp.reverse_annotations)))
	
	#ssu = SemSimUtils(gp, tree)
	#ssu.det_offspring_table()
	#ssu.det_ancestors_table()
	#ssu.det_freq_table()
	#ssu.det_GO_division()
	#ssu.det_ICs_table()

	#SS_Resnik_avg = ObjSemSim(gp, tree, "Resnik", "avg", ssu)

	#for i in range(len(test_set)):
		##for j in range(i+1, len(test_set)):
			#test = SS_Resnik_max.SemSim(test_set[i][0],test_set[i][1],"MF")
			#print(str(test_set[i][0]) + "\t" + str(test_set[i][1]) + "\t" + str(test))
	#print("-----------------------------------------------------------------")
