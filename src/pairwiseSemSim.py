#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""This program determines the distribution of semantic similarity scores for sets of proteins
"""
__author__="Marco Mina"
__email__="marco.mina.85@gmail.com"

from GO import AnnotationCorpus
from GO import PlainAnnotationCorpus
from GO import GeneOntology
from SemSim import ObjSemSim
from SemSim import SemSimUtils
from SemSim import ResnikSemSim
from SemSim import maxSemSim
from pairs import *
import sys
import os

if __name__ == "__main__":
	symb = "\t"
	UNION = 'UNION'

	#np = pairsparser.PairsParser(symb)
	#np.reset()
	#np.parse(sys.argv[3]) #### Load complexes
	#complexes = np.nets
	#print "Complexes: " + str(len(complexes))
	
	#for k in complexes:
		#test_set = complexes[k].items()
		#print "-------- -------------------------"
		#for i in range(0,len(test_set)):
			#print "--------"
			#for j in range(i+1,len(test_set)):
				#print str(test_set[i][0]) + "\t" +  str(test_set[j][0])
	#sys.exit()
	#### load ontology
	tree = GeneOntology.get_go_graph(open(sys.argv[1]))
	#print "Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.V.__len__()) + ". Edges: " + str(tree.E.__len__())
	print("Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num()))
	#### load annotations
	#gp = AnnotationCorpus.AnnotationCorpus(tree)
	gp = PlainAnnotationCorpus.PlainAnnotationCorpus(tree)
	
	gp.parse(sys.argv[2])
	gp.check_consistency()
	print("Annotated proteins: " + str(len(gp.annotations)))
	print("Annotated terms: " + str(len(gp.reverse_annotations)))

	SS = ObjSemSim.ObjSemSim(gp, tree, "Resnik", "BMA", None)
	ontology = "BP"
	
	ssscores = {}
	
	#for k in complexes:
		#ssscores[k] = []
		#test_set = complexes[k].items()
		#conta = 0
		#for i in range(0,len(test_set)):
			#for j in range(i+1,len(test_set)):
				#test = SS.SemSim(test_set[i][0],test_set[j][0],ontology)
				#ssscores[k].append((test_set[i][0],test_set[j][0],test))
	#outfile = open(sys.argv[4], 'w')
	#for k in ssscores:
		#for i in ssscores[k]:
			#outfile.write(str(k) + "\t" + str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + "\n")
	#outfile.close()
	#outfile = open(sys.argv[3], 'w')
	#complexes = gp.annotations
	#test_set = complexes.items()
	#conta = 0
	#for i in range(0,len(test_set)):
		#ssscores[test_set[i][0]] = {}
		#if i%(len(test_set)/100)==0:
			#print("Done " + str(i) + " on " + str(len(test_set)))
		#for j in range(i+1,len(test_set)):
			#if j%(len(test_set)/100)==0:
				#print("Done " + str(j) + " on " + str(len(test_set)))
			#test = SS.SemSim(test_set[i][0],test_set[j][0],ontology)
			##ssscores[test_set[i][0]][test_set[j][0]]= test
			#outfile.write(str(test_set[i][0]) + "\t" + str(test_set[j][0]) + "\t" + str(test) + "\n")
	##for k in ssscores:
		##for i in ssscores[k]:
			##outfile.write(str(k) + "\t" + str(i) + "\t" + str(ssscores[k][i]) + "\n")
	#outfile.close()

     outfile = open(sys.argv[3], 'w')
        outfile1 = open(sys.argv[4], 'w')
        complexes = gp.annotations
        test_set = complexes.items()
        conta = 0
        for i in range(0,len(test_set)):
                outfile1.write(str(test_set[i]) + "\n")
                ssscores[test_set[i][0]] = {}
                if i%(len(test_set)/100)==0:
                        print "Done " + str(i) + " on " + str(len(test_set))
                for j in range(i+1,len(test_set)):
                        if j%(len(test_set)/100)==0:
                                print "Done " + str(j) + " on " + str(len(test_set))
                        test = SS.SemSim(test_set[i][0],test_set[j][0],ontology)
                        #ssscores[test_set[i][0]][test_set[j][0]]= test
                        #outfile.write(str(test_set[i][0]) + "\t" + str(test_set[j][0]) + "\t" + str(test) + "\n")
                        outfile.write(str(test) + "\n")
        #for k in ssscores:
                #for i in ssscores[k]:
                        #outfile.write(str(k) + "\t" + str(i) + "\t" + str(ssscores[k][i]) + "\n")
        outfile.close()
        outfile1.close()
