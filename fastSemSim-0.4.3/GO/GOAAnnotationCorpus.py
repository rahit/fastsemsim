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

'''
#@desc Class to parse GOA Annotation Corpora
'''

import sys
import copy
#from pairs import rowscounter
import GeneOntology
import AnnotationCorpus

class GOAAnnotationCorpus():
	separator = '\t'

	def __init__(self, parameters=None):
		pass

	def parse(self, fname, trueclass):
		if type(fname) is str:
			stream = open(fname)
		else:
			stream = fname
			
		#if self.go==None:
			#print("No GO available.")
		#elif self.go.alt_ids == None:
			#print("No alternative id mapping table available.")

		#filenum = rowscounter.bufcount(fname);
		#if filenum > self.SHOW_PROCESS_THRESHOLD:
			#print(fname + " has " + str(filenum) + " lines.")
			#self.SHOW_PROCESS = True;
		#else:
			#self.SHOW_PROCESS = False;
		lines_counter = 0
		for line in stream:
			line = line.rstrip('\n')
			line = line.rstrip('\r')
			line = line.split(self.separator)
			if len(line) == 0:
				#print("1")
				continue
			if len(line) < 14:
				#print("2: " + str(line))
				continue
			taxon = line[12]
			if len(trueclass.taxonomy_filter) > 0:
				if taxon not in trueclass.taxonomy_filter:
					continue
			EC = line[6]
			obj_id = line[1]
			obj_name = line[2]
			term = line[4]
			if trueclass.exclude_GO_root:
				if term == GeneOntology.BP_root:
					continue
				if term == GeneOntology.CC_root:
					continue
				if term == GeneOntology.MF_root:
					continue
			term = int(term[3:])
			if not trueclass.go == None and not trueclass.go.alt_ids == None:
				if not term in trueclass.go.alt_ids:
					#print(str(term) + " not found in GO.")
					continue
				if not term in trueclass.go.nodes_edges:
					#print(str(term) + " is obsolete.")
					continue
				if not term == trueclass.go.alt_ids[term]:
					#print("Remapping " + str(term) + " to " + str(trueclass.go.alt_ids[term])
					term = trueclass.go.alt_ids[term]

			reference = line[5]

			GO = line[8]
			#### Build up genes set
			if obj_id not in trueclass.obj_set:
				trueclass.obj_set[obj_id] = taxon
			if term not in trueclass.term_set:
				trueclass.term_set[term] = {}
			#### Build up annotations set
			if obj_id not in trueclass.annotations:
				trueclass.annotations[obj_id] = {}
			if term not in trueclass.annotations[obj_id]:
				trueclass.annotations[obj_id][term] = {}
			if (len(trueclass.EC_filter) == 0) or ((EC in trueclass.EC_filter and trueclass.EC_filter_inclusive) or (EC not in trueclass.EC_filter and not trueclass.EC_filter_inclusive)):
				if EC not in trueclass.annotations[obj_id][term]:
					trueclass.annotations[obj_id][term][EC] = []
				trueclass.annotations[obj_id][term][EC].append((reference))
			#### Build up reverse annotations set
			if term not in trueclass.reverse_annotations:
				trueclass.reverse_annotations[term] = {}
			if obj_id not in trueclass.reverse_annotations[term]:
				trueclass.reverse_annotations[term][obj_id] = {}
			if (len(trueclass.EC_filter) == 0) or ((EC in trueclass.EC_filter and trueclass.EC_filter_inclusive) or (EC not in trueclass.EC_filter and not trueclass.EC_filter_inclusive)):
				if EC not in trueclass.reverse_annotations[term][obj_id]:
					trueclass.reverse_annotations[term][obj_id][EC] = []
				trueclass.reverse_annotations[term][obj_id][EC].append((reference))
			
			lines_counter += 1
			#if trueclass.SHOW_PROCESS and (lines_counter%(filenum/20)==0):
				#print("Lines processed: " + str(lines_counter) + " on " + str(filenum) + " (" + str(int(100*float(lines_counter)/float(filenum))) + "%)")
		stream.close()
		return True

#if __name__ == "__main__":
	#tree = GeneOntology.load_GO_XML(open(sys.argv[1]))
	#print "Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())
	
	#gp = GOAAnnotationCorpus(tree)
	
	#tax_filter = {}
	#tax_filter['taxon:103351'] = []
	#tax_filter['taxon:10335'] = []
	#tax_filter['taxon:10338'] = []
	#tax_filter['taxon:341980'] = []
	#tax_filter['taxon:103354'] = []
	#tax_filter['taxon:103353'] = []
	#tax_filter['taxon:103352'] = []
	#tax_filter['taxon:154633'] = []
	#tax_filter['taxon:103387'] = []
	#tax_filter['taxon:103385'] = []
	#tax_filter['taxon:103380'] = []
	#tax_filter['taxon:103355'] = []
	#tax_filter['taxon:103350'] = []
	##gp.set_taxonomy_filter(tax_filter)
	#gp.reset_taxonomy_filter()
	#EC_filter = {}
	#EC_filter['IES'] = []
	##gp.set_EC_filter(EC_filter)
	#gp.reset_EC_filter()
	#gp.parse(sys.argv[2])
	#gp.set_EC_filter(EC_filter)
	#gp.set_EC_filter_rule(False)
	##gp.reset_EC_filter()
	##gp.set_taxonomy_filter(tax_filter)
	#gp.constrain()
	
	#print("Annotated proteins: " + str(len(gp.annotations)))
	#print("Annotated terms: " + str(len(gp.reverse_annotations)))
	
	#for i in gp.annotations:
		#print(str(i) + ": " + str(gp.annotations[i]))
	#for i in gp.reverse_annotations:
		#print(str(i) + ": " + str(gp.reverse_annotations[i]))

	#clone = copy.deepcopy(gp)
	##for i in gp.obj_set:
		##print(str(i) + ": " + str(gp.obj_set[i]))
	#for i in gp.annotations:
		#print(str(i) + ": " + str(len(gp.annotations[i])))
		#print(str(i) + ": " + str(len(clone.annotations[i])))
	#for i in gp.reverse_annotations:
		#print(str(i) + ": " + str(len(gp.reverse_annotations[i])))
		#print(str(i) + ": " + str(len(clone.reverse_annotations[i])))

	#print(clone.check_consistency())
	#clone.sanitize()