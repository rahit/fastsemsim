# -*- coding: iso-8859-1 -*-
"""
This class provides the prototype for a generic Protein (or more in general, an Object) Semantic Similarity measure (PSS)
"""

from GO import AnnotationCorpus
from GO import GeneOntology
from SemSim import SemSimUtils
from SemSimUtils import *
from TermSemSim import *
from ResnikSemSim import *
from LinSemSim import *
from JiangConrathSemSim import *
from SimGICSemSim import *
from MixSemSim import *
from BMASemSim import *
from avgSemSim import *
from maxSemSim import *
import sys
import os
import math

class ObjSemSim:
	def pick_TSS(self):
		if self.TSS == 'Resnik':
			print("Select Resnik")
			return ResnikSemSim(self.annotation_corpus, self.go, self.util)
		elif self.TSS == 'Lin':
			return LinSemSim(self.annotation_corpus, self.go, self.util)
		elif self.TSS == 'JC':
			return JiangConrathSemSim(self.annotation_corpus, self.go, self.util)
		elif self.TSS == 'SimGIC':
			return SimGICSemSim(self.annotation_corpus, self.go, self.util)
		return TermSemSim(self.annotation_corpus, self.go, self.util)

	def pick_mixSS(self):
		if self.mixSS == 'max':
			return maxSemSim(self.annotation_corpus, self.go)
		elif self.mixSS == 'avg':
			return avgSemSim(self.annotation_corpus, self.go)
		elif self.mixSS == 'BMA':
			return BMASemSim(self.annotation_corpus, self.go)
		return MixSemSim(self.annotation_corpus, self.go)

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
			if i in self.annotation_corpus.obsoletes:
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
		#print(t1
		#print(t2
		return self.int_SemSim(t1, t2)

	def int_SemSim(self, term1, term2):
		if term1 is None or term2 is None or len(term1) == 0 or len(term2) == 0:
			return None
		if self.TSS.SS_type is self.TSS.P_TSS:
			sscore = self.mixSS.SemSim(term1, term2, self.TSS)
		elif self.TSS.SS_type is self.TSS.G_TSS:
			sscore = self.TSS.SemSim(term1, term2)
		else:
			print("Unrecognized TSS.")
			sys.exit(1)
		return sscore

#class ObjSemSimConfigurator:
	
	#def config(gofile, goafile, tss, mixs):
		##### load ontology
		#tree = GeneOntology.get_go_graph(open(sys.argv[1]))
		#print("Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.V.__len__()) + ". Edges: " + str(tree.E.__len__())
		
		##### load annotations
		#gp = AnnotationCorpus.AnnotationCorpus(tree)
		#gp.parse(sys.argv[2])
		
		#gp.check_consistency()
		#print("Annotated proteins: " + str(len(gp.annotations))
		#print("Annotated terms: " + str(len(gp.reverse_annotations))
		
		#ssu = SemSimUtils(gp, tree)
		#ssu.det_offspring_table()
		#ssu.det_ancestors_table()
		#ssu.det_freq_table()
		#ssu.det_GO_division()
		#ssu.det_ICs_table()
		#oss = ObjSemSim(gp, tree, ResnikSemSim(gp, tree, ssu), avgSemSim(gp, tree), ssu)
		#return oss

if __name__ == "__main__":
	
	inf = open('random_human_pp.txt','r')
	human_pairs = []
	for line in inf:
		line = line.rstrip('\n')
		line = line.rstrip('\r')
		line = line.rsplit('\t')
		human_pairs.append((line[0], line[1]))
		print("\"" + line[0] + "\"" + line[1] + "\"")
	#yeast_test_set = ["A8DNB8","A2P2R3", "A2P2R3","A5Z2X5","A8DNA4","A8DNB7","A8DNB8","B0CLU6"]
	#test_set = yeast_test_set
	test_set = human_pairs
	inf.close()
	
	#SS_Resnik_max = config(sys.argv[1], sys.argv[2], "Resnik", "max")
	
	#### load ontology
	tree = GeneOntology.get_go_graph(open(sys.argv[1]))
	print("Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.V.__len__()) + ". Edges: " + str(tree.E.__len__()))
	
	#### load annotations
	gp = AnnotationCorpus.AnnotationCorpus(tree)
	gp.parse(sys.argv[2])
	
	gp.check_consistency()
	print("Annotated proteins: " + str(len(gp.annotations)))
	print("Annotated terms: " + str(len(gp.reverse_annotations)))
	
	ssu = SemSimUtils(gp, tree)
	ssu.det_offspring_table()
	ssu.det_ancestors_table()
	ssu.det_freq_table()
	ssu.det_GO_division()
	ssu.det_ICs_table()
	
	#bpc = 0
	#mfc = 0
	#ccc = 0
	#for i in gp.reverse_annotations:
		#if i in ssu.root:
			#if ssu.root[i] is ssu.BP_root:
				#bpc += 1
			#if ssu.root[i] is ssu.MF_root:
				#print(i
				#mfc += 1
			#if ssu.root[i] is ssu.CC_root:
				#ccc += 1
	#print(bpc
	#print(mfc
	#print(ccc
	#for i in ssu.IC:
		##if i in ssu.root and ssu.root[i] is ssu.MF_root:
		#print(str(i) + "   " + str(ssu.IC[i])
		#pass
	
	for i in gp.annotations:
		print(str(i))

	
	#print("Lunghezza: " + str(len(gp.reverse_annotations[6355]))
	#sys.exit()
	#### create SemSimUtils class


	SS_Resnik_avg = ObjSemSim(gp, tree, "Resnik", "avg", ssu)
	SS_Lin_avg = ObjSemSim(gp, tree, LinSemSim(gp, tree, ssu), avgSemSim(gp, tree), ssu)
	SS_Resnik_max = ObjSemSim(gp, tree, ResnikSemSim(gp, tree, ssu), maxSemSim(gp, tree), ssu)
	SS_Lin_max = ObjSemSim(gp, tree, LinSemSim(gp, tree, ssu), maxSemSim(gp, tree), ssu)
	SS_JC_avg = ObjSemSim(gp, tree, JiangConrathSemSim(gp, tree, ssu), maxSemSim(gp, tree), ssu)
	SS_JC_max = ObjSemSim(gp, tree, JiangConrathSemSim(gp, tree, ssu), avgSemSim(gp, tree), ssu)
	SS_SimGIC = ObjSemSim(gp, tree, SimGICSemSim(gp, tree, ssu), None, ssu)
	#test = SS_Resnik_avg.SemSim("A8DNB8","A5Z2X5","BP")
	#print(test
	
	#inf = open('random_human_pp.txt','r')
	#human_pairs = []
	#for line in inf:
		#line = line.rsplit('\t')
		#human_pairs.append((line[0], line[1]))
	##yeast_test_set = ["A8DNB8","A2P2R3", "A2P2R3","A5Z2X5","A8DNA4","A8DNB7","A8DNB8","B0CLU6"]
	##test_set = yeast_test_set
	#test_set = human_pairs
	#inf.close()
	for i in range(len(test_set)):
		#for j in range(i+1, len(test_set)):
			test = SS_Resnik_max.SemSim(test_set[i][0],test_set[i][1],"MF")
			print(str(test_set[i][0]) + "\t" + str(test_set[i][1]) + "\t" + str(test))
	print("-----------------------------------------------------------------")
	#test = SS_Lin_avg.SemSim("A8DNB8","A2P2R3","BP")
	#print(test
	#test = SS_Resnik_max.SemSim("A1Z0J1","E1AXJ8","BP")
	#print(test
	#test = SS_Lin_max.SemSim("A8DNB8","A2P2R3","BP")
	#print(test
	#test = SS_JC_max.SemSim("A1Z0J1","E1AXJ8","BP")
	#print(test
	#test = SS_JC_avg.SemSim("A1Z0J1","E1AXJ8","BP")
	#print(test
	#test = SS_SimGIC.SemSim("A1Z0J1","E1AXJ8","BP")
	#print(test
	#test = SS_SimGIC.SemSim("A1Z0J1","E1AXJ8","MF")
	#print(test
	#test = SS_SimGIC.SemSim("A1Z0J1","E1AXJ8","CC")
	#print(test