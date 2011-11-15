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
This class provides a template for using fastSemSim
"""

from GO import AnnotationCorpus
from GO import GeneOntology
from SemSim import ObjSemSim
import sys
import os
import math

if __name__ == "__main__":
	
	# Input section
	
	#### load ontology
	tree = GeneOntology.load_GO_XML(open(sys.argv[1]))
	print "Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())

	gp = AnnotationCorpus.AnnotationCorpus(tree)	
	gp.parse(sys.argv[2],'plain')

	print("Annotated proteins: " + str(len(gp.annotations)))
	print("Annotated terms: " + str(len(gp.reverse_annotations)))
	print("Check annotation corpus consistency... " + str(gp.check_consistency()))

#------------------------------------------------------------------------------------------------------------------------------------

	# Elaboration

	#### To calculate SS between a pair of objects
	'''
	SS = ObjSemSim.ObjSemSim(gp, tree, "Resnik", "BMA", None)
	ontology = "MF"
	test = SS.SemSim(obj1,obj2,ontology)
	'''

	#### To calculate SS between set of pairs of objects, loaded from a file
	'''
	SS = ObjSemSim.ObjSemSim(gp, tree, "Resnik", "BMA", None)
	ontology = "MF"
	inf = open(sys.argv[3],'r')
	pairs = []
	for line in inf:
		line = line.rstrip('\n')
		line = line.rstrip('\r')
		line = line.rsplit('\t')
		pairs.append((line[0], line[1]))
	inf.close()
	scores = []
	for i in range(1,len(pairs)):
		scores.append(pairs[i][0],pairs[i][1],SS.SemSim(pairs[i][0],pairs[i][1],ontology))
	'''

	#### To calculate pairwise SS between element within a list loaded from a file
	'''
	SS = ObjSemSim.ObjSemSim(gp, tree, "Resnik", "BMA", None)
	ontology = "MF"
	inf = open(sys.argv[3],'r')
	pairs = []
	for line in inf:
		line = line.rstrip('\n')
		line = line.rstrip('\r')
		pairs.append(line)
	inf.close()
	scores = {}
	for i in range(1,len(pairs)):
		scores[pairs[i]] = {}
		for j in range(i+1,len(pairs)):
			scores[pairs[i]][pairs[j]] = SS.SemSim(pairs[i],pairs[j],ontology)
	'''

	#### To calculate pairwise SS between element within a list loaded from annotation corpus
	'''
	SS = ObjSemSim.ObjSemSim(gp, tree, "Resnik", "BMA", None)
	ontology = "MF"
	pairs = gp.obj_set.keys()
	scores = {}
	for i in range(1,len(pairs)):
		scores[pairs[i]] = {}
		for j in range(i+1,len(pairs)):
			scores[pairs[i]][pairs[j]] = SS.SemSim(pairs[i],pairs[j],ontology)
	'''

	#### Output to file, integrable with calculation code to avoid memory problems
	#file, p1, p2, score
	#file, score
	#files: score, list of names
	#file, matrix
	
	#threshold
#------------------------------------------------------------------------------------------------------------------------------------
