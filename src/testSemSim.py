# -*- coding: iso-8859-1 -*-
"""
This class provides check tests for ObjSemSim class
"""

from GO import AnnotationCorpus
from GO import GeneOntology
from SemSim import ObjSemSim
from SemSim import SemSimUtils
from SemSim import ResnikSemSim
from SemSim import maxSemSim
import sys
import os

if __name__ == "__main__":
	#### load ontology
	tree = GeneOntology.load_GO_XML(open(sys.argv[1]))
	print "Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())
	#print "Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.V.__len__()) + ". Edges: " + str(tree.E.__len__())
	#### load annotations
	gp = AnnotationCorpus.AnnotationCorpus(tree)
	gp.parse(sys.argv[2])
	
	gp.check_consistency()
	print "Annotated proteins: " + str(len(gp.annotations))
	print "Annotated terms: " + str(len(gp.reverse_annotations))

	#for i in gp.annotations:
		#print str(i)

	ssu = SemSimUtils.SemSimUtils(gp, tree)
	ssu.det_offspring_table()
	ssu.det_ancestors_table()
	ssu.det_freq_table()
	ssu.det_GO_division()
	ssu.det_ICs_table()
			
	#SS_Resnik_avg = ObjSemSim.ObjSemSim(gp, tree, "Resnik", "avg", None)
	#ssu = SS_Resnik_avg.util
	#SS_Lin_avg = ObjSemSim.ObjSemSim(gp, tree, "Lin", "avg", ssu)
	SS_Resnik_BMA = ObjSemSim.ObjSemSim(gp, tree, "Resnik", "BMA", None)
	#for i in SS_Resnik_BMA.util.IC:
		#print str(i) + "\t" + SS_Resnik_BMA.util.GO_division[i] + "\t" + str(SS_Resnik_BMA.util.IC[i])
	#sys.exit()
	#SS_Resnik_max = ObjSemSim.ObjSemSim(gp, tree, "Resnik", "max", None)
	#SS_Resnik_max2 = ObjSemSim.ObjSemSim(gp, tree, ResnikSemSim.ResnikSemSim(gp, tree, ssu), maxSemSim.maxSemSim(gp, tree), SS_Resnik_max.util)
	#SS_Lin_max = ObjSemSim.ObjSemSim(gp, tree, "Lin", "max", ssu)
	#SS_JC_avg = ObjSemSim.ObjSemSim(gp, tree, "JC", "avg", ssu)
	#SS_JC_max = ObjSemSim.ObjSemSim(gp, tree, "JC", "max", ssu)
	SS_SimGIC = ObjSemSim.ObjSemSim(gp, tree, "SimGIC", None, ssu)

	#print SS_Resnik_max
	#print SS_Resnik_max.TSS
	#print SS_Resnik_max.mixSS
	
	#sys.exit()
	#inf = open('random_human_pp.txt','r')
	inf = open(sys.argv[3],'r')
	human_pairs = []
	for line in inf:
		line = line.rstrip('\n')
		line = line.rstrip('\r')
		#line = line.rsplit('\t')
		#human_pairs.append((line[0], line[1]))
		#line = line.rsplit('\t')
		human_pairs.append(line)
		#print "\"" + line[0] + "\"" + line[1] + "\""
	test_set = human_pairs
	inf.close()
	
	for i in range(len(test_set)):
		for j in range(i+1, len(test_set)):
			#test = SS_Resnik_BMA.SemSim(test_set[i],test_set[j],"MF")
			test = SS_Resnik_BMA.SemSim(test_set[i],test_set[i],"MF")
			#for i in gp.annotations:
			#print "------------------------------"
			#print str(gp.annotations[test_set[i]])
			#print "--------"
			#print str(gp.annotations[test_set[j]])
			#print str(test_set[i][0]) + "\t" + str(test_set[i][1]) + "\t" + str(test)
			print str(test_set[i]) + "\t" + str(test_set[j]) + "\t" + str(test)
			#print "------------------------------"
	print "-----------------------------------------------------------------"