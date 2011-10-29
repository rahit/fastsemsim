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

'''
This class reads plain annotation corpus files.
#Plain format 1: protein ID - Term ID
#Plain format 1: protein ID - Taxonomy - Term ID
#Plain format 3: protein ID - Taxonomy - Term ID - EC
'''
import sys
#import copy
from GO import GeneOntology
#from GO.AnnotationCorpus import AnnotationCorpus

class PlainAnnotationCorpus():
	separator = '\t'
	comment = '#'

	def __init__(self, parameters=None, ac = None):
		self.ac = ac
		if self.ac == None:
			#ac = AnnotationCorpus()
			print "Unexpected Error"
			sys.exit()
		self.parameters = parameters

	def interpret_parameters(self):
		self.obj_first = True
		self.one_association_per_line = True
		if self.parameters == None:
			return
		if len(self.parameters) > 0:
			self.obj_first = self.parameters[0]
			if len(self.parameters) > 1:
				self.one_association_per_line = self.parameters[1]

	def set_fields(self):
		self.ac.reset_fields()

	def parse(self, fname):
		self.interpret_parameters()
		self.set_fields()
		if type(fname) is str:
			stream = open(fname, 'r')
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
			if line[0] == self.comment:
				continue
			line = line.split(self.separator)
			if len(line) == 0:
				continue
			if len(line) < 2:
				print("Strange line: " + str(line))
				continue
			temp_to_add = []
			if self.one_association_per_line:
				if self.obj_first:
					obj_id = line[0]
					term = line[1]
				else:
					obj_id = line[1]
					term = line[0]
				temp_to_add.append(obj_id, term)
			else:
				obj_id = line[0]
				for i in range(1,len(line)):
					term = line[i]
					temp_to_add.append(obj_id, term)

			for i in temp_to_add:
				obj_id = i[0]
				term = i[1]
				if ac.exclude_GO_root:
					if term == GeneOntology.BP_root:
						continue
					if term == GeneOntology.CC_root:
						continue
					if term == GeneOntology.MF_root:
						continue
				term = int(term[3:])
				if not ac.go == None and not ac.go.alt_ids == None:
					if not term in ac.go.alt_ids:
						#print(str(term) + " not in GO.")
						continue
					if not term in ac.go.nodes_edges:
						#print(str(term) + " obsolete.")
						continue
					if not term == ac.go.alt_ids[term]:
						#print("Remapping " + str(term) + " to " + str(ac.go.alt_ids[term])
						term = ac.go.alt_ids[term]
							
				#### Build up genes set
				if obj_id not in ac.obj_set:
					ac.obj_set[obj_id] = {}
				if term not in ac.term_set:
					ac.term_set[term] = {}
				#### Build up annotations set
				if obj_id not in ac.annotations:
					ac.annotations[obj_id] = {}
				if term not in ac.annotations[obj_id]:
					ac.annotations[obj_id][term] = {}
				#### Build up reverse annotations set
				if term not in ac.reverse_annotations:
					ac.reverse_annotations[term] = {}
				if obj_id not in ac.reverse_annotations[term]:
					ac.reverse_annotations[term][obj_id] = {}
			lines_counter += 1
			#if ac.SHOW_PROCESS and (lines_counter%(filenum/20)==0):
				#print("Lines processed: " + str(lines_counter) + " on " + str(filenum) + " (" + str(int(100*float(lines_counter)/float(filenum))) + "%)")
		if type(fname) is str:
			stream.close()
		return True
