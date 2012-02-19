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
This is an example program.
It loads a Gene Ontology, an annotation corpus (in GOA GAF-2 format) and evaluate Resnik Sem Sim between all the pairs of GO Terms from BP ontology present in the annotation corpus.
"""

from fastSemSim.GO import AnnotationCorpus
from fastSemSim.GO import GeneOntology
#from fastSemSim.SemSim import TermSemSim
from fastSemSim.SemSim import SemSimMeasures
import sys

if __name__ == "__main__":
	
	# example data
	if len(sys.argv) < 3:
		go_file = "GO_2011-09-16.obo-xml"
		ac_file = "gene_association.goa_fly"
	else:
		go_file = sys.argv[1]
		ac_file = sys.argv[2]


	#-#-#-#-#-#-#-#-#-#-#-#
	# Load Gene Ontology  #
	#-#-#-#-#-#-#-#-#-#-#-#

	print "Loading Gene Ontology from " + str(go_file) + "..."
	go = GeneOntology.load_GO_XML(open(go_file))
	print "-> Ontology correctly loaded: " + str(go.node_num()) + " nodes and " +  str(go.edge_num()) + " edges."
	print ""



	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# load Annotation Corpus  #
	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	ac = AnnotationCorpus.AnnotationCorpus(go)
	print "Loading annotation corpus from gaf-2 file " + str(ac_file) + "..."
	ac.parse(ac_file,'GOA') # to parse gaf-2 / GOA files
	ac.sanitize()
	print "-> Annotation Corpus correctly loaded. Annotated terms: " + str(len(ac.reverse_annotations)) + ". Annotated proteins: " + str(len(ac.annotations)) 
	print ""




	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# Term Semantic Similarity  #
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	
	# Semantic similarity between GO Terms
	# The basic approach here is to create a "SemSim" object with some fixed parameters, and then use it to evaluate the semantic similarity between pairs or groups of GO Terms

	print "Term Semantic similarity example (Resnik)"

	#### First step: select the proper Term Sem Sim
	# simply use SemSimMeasures.selectTermSemSim specifying the Term Sem Sim to use (Resnik in the example)
	# for a complete list of currently available Term Sem Sim see SemSimMeasures.py file
	
	TermSemSimClass = SemSimMeasures.selectTermSemSim('Resnik')
	
	#### Second step: create a Term Sem Sim object providing the following parameters:
	# 1) annotation corpus, 2) gene ontology, 3 (optional) SemSimUtil instance [it's safe not to provide it]
	# Just use the class returned by TermSemSim.selectTermSemSim
	
	TSS = TermSemSimClass(ac, go)
	#### Third step: set further parameters
	# since additional parameters are measure-dependent you must check each single measure to learn which parameters are available
	# The only general parameter is whether or not to perform a sanity check on input data
	# Sanity check verifies whether input data are consistent with current GO and whether a Sem Sim measure can be evaluated between them
	# For example, all the GO Terms in the same query have to come from the same GO Category, and they must not be obsolete
	# Disabling Sanity Check improves computation speed, but input data have to be correct or incorrect results might be returned
	
	TSS.setSanityCheck(False) # Disables sanity check on query data. Speeds up computation, but if input data are inconsistent results might be incorrect
	TSS.setSanityCheck(True) # Disables sanity check on query data. Computation is slightly slower, but output data are guaranteed to be correct

	#### Fourth step: determine Term semantic similarity
	# Simply use TSS.SemSim(X,Y) to evaluate the Sem Sim between X and Y.
	# Depending on the type of Term Sem Sim used (pairwise or groupwise) input can be a list of terms or single terms.

	# The following line simply retrieves a set of Go Terms present in current annotation corpus and belonging to BP category
	test_set = TSS.util.intersection(ac.reverse_annotations.keys(), TSS.util.offspring[go.BP_root]).keys()
	
	limit = 20
	done = 0
	for i in range(len(test_set)):
		if done >= limit:
			break
		for j in range(i+1, len(test_set)):
			done += 1
			if done > limit:
				break
			mat = TSS.SemSim(test_set[i], test_set[j])
			print "-> " + str(go.id2name(test_set[i])) + " - " + str(go.id2name(test_set[j])) + ": " + str(mat)
			if done >= limit:
				break
	print ""
#



	print "Term Semantic similarity example (Resnik) passing GO Terms directly in integer format (not using id2name utility)"
	#### Fifth step: determine Term semantic similarity between custom terms.
	# The code is the same as in step four. Here go.id2name is not used. This is to demonstrate how GO Temrs can be passed directly as numbers, as well as in the usual "GO:1234567" format.

	custom_list= [7052, 22, 42254, 6412, 16070, 7067, 82, 7095, 71841, 71842]
	done = 0
	for i in range(len(custom_list)):
		for j in range(i, len(custom_list)):
			done += 1
			mat = TSS.SemSim(custom_list[i], custom_list[j])
			#print "-> " + str(go.id2name(custom_list[i])) + " - " + str(go.id2name(custom_list[j])) + ": " + str(mat)
			print "-> " + str(custom_list[i]) + \
						" [" + str(TSS.util.IC[custom_list[i]]) + \
						"] - " + str(custom_list[j]) + \
						" [" + str(TSS.util.IC[custom_list[j]]) + "] : " + \
						str(mat)  # \

						#+ " - " + str(TSS.util.det_MICA(custom_list[i], custom_list[j])) + \
						#" - " + str(TSS.util.ancestors[custom_list[i]]) + \
						#" - " + str(TSS.util.ancestors[custom_list[j]])
	print ""
