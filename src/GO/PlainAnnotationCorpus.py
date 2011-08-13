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

__author__="Marco Mina"
#@mail marco.mina.85@gmail.com
#@version 1.0
#@desc This class reads plain annotation corpus files.
#Plain format 1: protein ID - Term ID
#Plain format 1: protein ID - Taxonomy - Term ID
#Plain format 3: protein ID - Taxonomy - Term ID - EC
#In all the cases each row defines just 1 annotation.
#### annotations: dict with protein ids as primary key. Each key is associated with a dict of annotations associated to the protein. Each annotation is a key itself (the term code in the GO is used as key), and it is associated to the EC/REF of the annotation. Multiple EC for the same annotation are possible.
#
#### reverse annotations: dict with term codes in the GO as primary key. Each key is associated with a dict of annotations associated to the term. Each annotation is a key itself (the protein ids are used as keys), and it is associated to the EC/REF of the annotation. Multiple EC for the same annotation are possible.
#
#### obj_set: set of proteins present in the annotation table, connected with the taxon id of the organism they belong to. This table is useful to filter out proteins from uninteresting species.
#
####
import sys
import copy
#from pairs import rowscounter
#from GO import GeneOntology
import GeneOntology
import AnnotationCorpus

class PlainAnnotationCorpus():
	separator = '\t'
	objfirst = False
	
	#def __init__(self, tree=None):
		#AnnotationCorpus.__init__(tree)

	# deepcopy missing but not needed for now.
	#def load(self, fname):
		#self.parse(fname, self)
			
	def parse(self, fname, trueclass):
		if type(fname) is str:
			stream = open(fname)
		else:
			stream = fname
		#filenum = rowcount(fname);
		#if filenum > self.SHOW_PROCESS_THRESHOLD:
			#print(fname + " has " + str(filenum) + " lines."
			#self.SHOW_PROCESS = True;
		#else:
		#self.SHOW_PROCESS = False;
		lines_counter = 0
		for line in stream:
			line = line.rstrip('\n')
			line = line.rstrip('\r')
			line = line.split(self.separator)
			if len(line) == 0:
				continue
			if len(line) < 2:
				print("Strange line: " + str(line))
				continue
			if self.objfirst:
				obj_id = line[0]
				term = line[1]
			else:
				obj_id = line[1]
				term = line[0]
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
					#print(str(term) + " not in GO.")
					continue
				if not term in trueclass.go.nodes_edges:
					#print(str(term) + " obsolete.")
					continue
				if not term == trueclass.go.alt_ids[term]:
					#print("Remapping " + str(term) + " to " + str(trueclass.go.alt_ids[term])
					term = trueclass.go.alt_ids[term]
						
			#### Build up genes set
			if obj_id not in trueclass.obj_set:
				trueclass.obj_set[obj_id] = {}
			if term not in trueclass.term_set:
				trueclass.term_set[term] = {}
			#### Build up annotations set
			if obj_id not in trueclass.annotations:
				trueclass.annotations[obj_id] = {}
			if term not in trueclass.annotations[obj_id]:
				trueclass.annotations[obj_id][term] = {}
			#### Build up reverse annotations set
			if term not in trueclass.reverse_annotations:
				trueclass.reverse_annotations[term] = {}
			if obj_id not in trueclass.reverse_annotations[term]:
				trueclass.reverse_annotations[term][obj_id] = {}
			lines_counter += 1
			#if trueclass.SHOW_PROCESS and (lines_counter%(filenum/20)==0):
				#print("Lines processed: " + str(lines_counter) + " on " + str(filenum) + " (" + str(int(100*float(lines_counter)/float(filenum))) + "%)")
		if type(fname) is str:
			stream.close()
		return True


if __name__ == "__main__":
	tree = GeneOntology.load_GO_XML(open(sys.argv[1]))
	print "Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())
	
	gp = PlainAnnotationCorpus(tree)
	gp.parse(sys.argv[2])
	for i in gp.annotations:
		print(str(i) + ": " + str(gp.annotations[i]))
	gp.check_consistency()
	gp.sanitize()
