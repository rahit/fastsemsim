# -*- coding: iso-8859-1 -*-
"""
This class provides the prototype for a generic Term Semantic Similarity measure (TSS)

"""

from GO import AnnotationCorpus
from GO import GeneOntology
from SemSimUtils import *
import sys
import os
import math

class TermSemSim:
	P_TSS = "Pairwise"
	G_TSS = "Groupwise"
	SS_type = P_TSS
	IC_based = False

	def __init__(self, ac, go, util = None):
		self.go = go
		self.annotation_corpus = ac
		self.util = util
		if self.util == None:
			self.util = SemSimUtils(ac, go)
			self.ssu.det_offspring_table()
			self.ssu.det_ancestors_table()
			self.ssu.det_freq_table()
			self.ssu.det_GO_division()
			self.ssu.det_ICs_table()

	def int_format_data(self, term1):
		"""
		Return None if:
		- an id is not in the GO tree
		- ids come from from different ontologies.
		"""
		id1 = self.util.go_2ids(term1)
		#print(id1
		if self.SS_type is self.P_TSS:
			if type(id1) is int:
				if id1 in self.go.nodes_edges:
					#print("Valid id P."
					out_ids = id1
				else:
					print("Term " + str(i) + " not present in the GO.")
					return None
				if self.IC_based and not out_ids in self.util.IC:
					print("Term " + str(out_ids) + " does not have an IC.")
					return None
			else:
					print("More than one term passed to a pairwise term SS measure.")
					return None
		elif self.SS_type is self.G_TSS:
			if type(id1) is int:
				temp_id1 = []
				temp_id1.append(id1)
			else:
				temp_id1 = id1
			current_onto = None
			for i in temp_id1:
				if i not in self.go.nodes_edges:
					print("Term " + str(i) + " not present in the GO.")
					return None
				if current_onto is None:
					current_onto = self.util.root[i]
				elif not current_onto is self.util.root[i]:
					print("Terms are not from the same ontology")
					return None
				if self.IC_based and not i in self.util.IC:
					print("Term " + str(i) + " does not have an IC.")
					return None
			out_ids = temp_id1
		return out_ids

	def SemSim(self, term1, term2):
		"""
		Terms are supposed to come from the same ontology.
		Check is enabled by default. I should allow to disable the check to improve performance.
		"""
		#### translate into id format & check data.
		if term1 is None or term2 is None:
			return None
		id1 = self.int_format_data(term1)
		id2 = self.int_format_data(term2)
		if id1 is None or id2 is None or (self.SS_type is self.G_TSS and len(id1) == 0) or (self.SS_type is self.G_TSS and len(id2) == 0):
			print(str(term1) + " or " + str(term2) + "   not valid.")
			return None
		if self.SS_type is self.P_TSS:
			if not self.util.root[id1] == self.util.root[id2]:
				print("Terms are not from the same ontology")
				return None
		elif self.SS_type is self.G_TSS:
			for i in id1:
				t1 = i
				break
			for i in id2:
				t2 = i
				break
			if not self.util.root[t1] == self.util.root[t2]:
				print("Terms are not from the same ontology")
				return None
		return self.int_SemSim(id1, id2)

	def int_SemSim(self, term1, term2):
		gene1anc = self.util.ancestors[term1]
		gene2anc = self.util.ancestors[term2]
		return None

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

	TSS = TermSemSim(gp, tree, ssu)
	test = TSS.SemSim("GO:0008150","GO:0008150")
	print(test)
	test = TSS.SemSim("GO:0000001","GO:0009987")
	print(test)