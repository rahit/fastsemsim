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
This class provides a fast implementation of Resnik max
"""

from fastSemSim.GO import AnnotationCorpus
from fastSemSim.GO import GeneOntology
from fastSemSim.SemSim import ObjSemSim
from fastSemSim.SemSim import SemSimUtils
from fastSemSim.SemSim import ResnikSemSim
from fastSemSim.SemSim import maxSemSim
from fastSemSim.SemSim import TermSemSim
import sys
import os
import math
import copy

class fastResnikSemSim(ObjSemSim.ObjSemSim):
	IC_based = True

	def __init__(self, ac, go, TSS = 'Resnik', MSS = 'max', util = None):
		self.go = go
		self.ac = ac
		self.util = util
		
		self.TSS = TSS
		self.mixSS = MSS
		
		#### To be fixed when more enhaced versions will be available
		#if self.TSS is None:
			#self.TSS = TermSemSim(self.ac, self.go, self.util)
		#elif type(self.TSS) is str:
			#self.TSS = self.pick_TSS()
		#else:
			#pass
		#if self.mixSS is None:
			#self.mixSS = MixSemSim(self.ac, self.go)
		#elif type(self.mixSS) is str:
			#self.mixSS = self.pick_mixSS()
		#else:
			#pass

		if self.util == None:
			self.util = SemSimUtils.SemSimUtils(self.ac, self.go)
			self.util.det_IC_table()
#



	def get_direct_annotations(self, obj, onto):
		if not obj in self.ac.annotations:
			print(str(obj) + " not found in Annotation Corpus!")
			return None
		terms = []
		for i in self.ac.annotations[obj]:
			#print i
			if i in self.go.obsolete_ids:
				#print(str(i) + " obsolete!")
				continue
			if i not in self.util.GO_root:
				print(str(i) + " not in GO!")
			elif self.util.GO_root[i] is onto:
				terms.append(i)
		return terms

	def extend_direct_annotations(self, terms):
		allterms = self.util.get_ancestors(terms)
		return allterms.keys()
		
	def int_format_data(self, obj, onto):
		terms = self.get_direct_annotations(obj, onto)
		return self.extend_direct_annotations(terms)
#






	def int_SemSim(self, onto):
		self.scores = {}
		self.matrice = []
		self.matrice_names = []
		# sort Terms by Term IC
		temp_IC = {}
		temp_temps = self.util.get_ancestors(self.ac.reverse_annotations.keys())
		for i in temp_temps:
			if not i in self.go.obsolete_ids:
				temp_IC[i] = self.util.IC[i]
		self.sortedTerms = sorted(temp_IC, key  = temp_IC.__getitem__, reverse=True)
		self.sortedTermsDict = {}
		for i in range(0,len(self.sortedTerms)):
			 self.sortedTermsDict[self.sortedTerms[i]] = i
		#print(str(self.sortedTerms))
		conta = 0
		# populate table... each row is a proteins
		pos = 0
		
		print("Preprocessing annotation corpora...")
		for i in self.ac.annotations:
			#print "processing " + str(conta) + " on " + str(len(self.ac.annotations))
			conta += 1
			temp_row = len(self.sortedTerms)*[0]
			temp_annot = self.int_format_data(i, onto)
			#print str(temp_row)
			for j in temp_annot:
				#print str(i)
				#print str(len(self.sortedTermsDict))
				#print str(self.sortedTermsDict[i])
				#print str(len(self.sortedTerms))
				temp_row[self.sortedTermsDict[j]] = 1
			#print temp_row
			self.matrice.append(temp_row)
			#print i
			self.matrice_names.append(i) #[i] = pos 
			pos += 1
		#main loop
		
		print("Evaluating semantic similarities between " + str(len(self.ac.annotations)))
		total = len(self.matrice)
		done = 0
		#if verbose:
		prev_text = ""
		sys.stdout.write("Done: ")
		sys.stdout.flush()
		
		for i in range(0,len(self.matrice)):
			#print("Processing " + str(i) + " on " + str(len(self.matrice)) + ": " + str(self.matrice_names[i]))
			temp_scores = {}
			temp_missing = [x for x in range(i+1, len(self.matrice))]
			#print(str(len(temp_missing)))
			k = 0
			while k < len(self.matrice[i]):
				if self.matrice[i][k] == 0:
					k += 1
				else:
					j = 0
					while j < len(temp_missing):
						if self.matrice[temp_missing[j]][k] == 1:
							 temp_scores[self.matrice_names[temp_missing[j]]] = self.util.IC[self.sortedTerms[k]]
							 #temp_scores[self.matrice_names[temp_missing[j]]] = self.sortedTerms[k]
							 #temp_missing[j] = temp_missing[len(temp_missing) - 1]
							 temp_missing.pop(j)
						else:
							j += 1

					k += 1
			for j in temp_missing:
				#print j
				self.matrice_names[j]
				#print temp_missing[j]
				temp_scores[self.matrice_names[j]] = 0
			#print temp_scores
			#print("Size of last added vector: " + str(len(temp_scores)))
			#print("-------------------")
			#if verbose:
			done += 1
			sys.stdout.write("\b"*len(prev_text))
			prev_text = str(done) + ' [%.4f' % (100*done/float(total)) + " %]"
			sys.stdout.write(prev_text)
			sys.stdout.flush()
					
			if self.stream1 is None:
				if self.matrice_names[i] in self.scores:
					print "Errore"
				self.scores[self.matrice_names[i]] = temp_scores
				print("Size of score matrix: " + str(len(self.scores)))
			else:	
				#self.stream1.write(str(self.matrice_names[i]) + " - " + str(k) + ": " + str(temp_scores[k]) + "\n")
				for k in temp_scores:
					self.stream1.write(str(self.matrice_names[i]) + "\t" + str(k) + "\t" + str('%.4f' %temp_scores[k]) + "\n")


	def SemSim(self, ontology, stream1 = None):
		self.stream1 = stream1
		#self.stream2 = stream2
		#### translate into id format & check data
		if ontology == self.util.BP_ontology:
			onto = self.go.BP_root
		elif ontology == self.util.MF_ontology:
			onto = self.go.MF_root
		elif ontology == self.util.CC_ontology:
			onto = self.go.CC_root
		else:
			print("No valid ontology selected.")
			return None
		#t1 = self.int_format_data(obj1, onto)
		#if t1 is  None:
			#return None
		#t2 = self.int_format_data(obj2, onto)
		#if t2 is  None:
			#return None
		##print(t1
		##print(t2
		return self.int_SemSim(onto)
#

#if __name__ == "__main__":
	##### load ontology
	#tree = GeneOntology.parse(sys.argv[1])
	#print "Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())

	#gp = AnnotationCorpus.AnnotationCorpus(tree)
	#gp.parse(sys.argv[2],'gaf-2.0')

	#print("Annotated proteins: " + str(len(gp.annotations)))
	#print("Annotated terms: " + str(len(gp.reverse_annotations)))
	#print("Check annotation corpus consistency... " + str(gp.check_consistency()))

	##### create SemSimUtils class
	#ssu = SemSimUtils.SemSimUtils(gp, tree)
	#ssu.det_offspring_table()
	#ssu.det_ancestors_table()
	#ssu.det_freq_table()
	#ssu.det_GO_division()
	#ssu.det_ICs_table()
	#print "------------ IC list -----------"
	#for i in ssu.IC:
		#print str(i) + "\t" + str(ssu.IC[i])
	#print "------------ end IC list -----------"
	#SS = fastResnikSemSim(gp, tree, ssu)
	
	#ontology = str(sys.argv[4]) # "MF" or "BP" or "CC"
	#print ontology
	#outfile1 = open(sys.argv[3], 'w')
	#SS.SemSim(ontology, outfile1)
	#outfile1.close()
	#sys.exit(0)
