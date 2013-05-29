# -*- coding: iso-8859-1 -*-
'''
Copyright 2011-2013 Marco Mina. All rights reserved.

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
#--------------------------------------------------------------------------
"""
@mail marco.mina.85@gmail.com
@version 2.0
@desc Ontology class is the basic datastructure representing multirooted connected DAGs.

"""

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# Ontology class
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-


class Ontology:

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# variables 
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

	_use_parent_children_ = True
	_use_node_edges_ = True

	# available_data_structs = ('dicts', '')
	roots = {} # ids of roots 
	# data_structs = []

# data struct 1: nodes and edges
	nodes = {} # each node is a list of edge ids
	edges = {} # dict. Each key is an attrib of the edge

	# variant 1(1a)
	# edges['inter'] = [] # list. Whether the edge is inter-category or not
	# variant 1(1b)
	edges['inter'] = {} # list. Whether the edge is inter-category or not

	# variant 1(2a)
	# edges['parent'] = [] # list. Parent node id
	# edges['child'] = [] # list. Child node id
	# variant 1(2b)
	edges['nodes'] = [] # list. (parent, child) node ids

	# additional 1(3a)
	# edges['attrib'] = [] # list. Additional attributes
	
# data struct 2: nodes and edges, edges handled as table using numpy
	# import numpy as np
	# nodes = {} # each node is a list of edge ids
	# edges = np.zeros(shape=(0,3)) # numpy array. column 1: parent, column 2: child, column 3: inter-category, column 4: attribs
	# FIX PROBLEM OF ONLY INT IN MATRIX

# data struct 3: parents and children
	#variant 3(1a)
	parents = {} # dict. key: node id, value: dict of parents {}
	children = {} # dict. key: node id, value: dict of children {}
	#variant 3(1b)
	# parents = [] # list. pos: node id, value: dict of parents {}
	# children = [] # list. pos: node id, value: dict of children {}

# ? node names are int and sequential? We assume they are NOT. It implies variant 3(1b) requires a mapping structure as well. It implies a potential overhead?

# data struct 3: ??
	# alt_ids = None
	# obsolete_ids = None


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# functions
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

	def node_number(self):
		return len(self.nodes)

	def edge_number(self):
		return self.next_edge

	def __init__(self):
		nodes = {}
		edges = {}
		edges['inter'] = {}
		edges['nodes'] = []
		parents = {}
		children = {}

		self.next_edge = 0

# populate data struct 1
	def _add_node(self,n):
		if n not in self.nodes:
			self.nodes[n] = []
		else:
			raise(Exception, 'Node ' + str(n) + ' already in the ontology')
	#

	def _add_edge(self, parent, child, inter=False):
		# while self.next_edge in self.edges_nodes:
		# 	self.next_edge += 1
		e = self.next_edge
		self.next_edge += 1
		if e >= len(self.edges['nodes']):
			self.edges['nodes'].append(None)
		if parent not in self.nodes:
			self._add_node(parent)
		if child not in self.nodes:
			self._add_node(child)

		self.edges['nodes'][e] = (parent, child)
		if inter:
			self.edges['inter'][e] = True
		self.nodes[parent].append(e)
		if parent != child:
			self.nodes[child].append(e)
		return e
	#

	def _s1_to_s2(self): # given data struct 1, generates data struct 2
		self.parents = {}
		self.children = {}
		for j in self.nodes:
			self.parents[j] = {}
			self.children[j] = {}
		for i in range(0, len(self.edges['nodes'])):
			self.parents[self.edges['nodes'][i][1]][self.edges['nodes'][i][0]] = i
			self.children[self.edges['nodes'][i][0]][self.edges['nodes'][i][1]] = i
	#

	def det_roots(self): # determines roots (nodes without parents)
		# using data struct 1
		if len(self.parents) == 0:
			self._s1_to_s2()
		self.roots = {}
		for i in self.parents:
			if len(self.parents[i]) == 0:
				self.roots[i] = None
	#

	def is_consistent(self): # verifies the Ontology is consistent
		self.det_roots()
		consistent = True
		inc = {}
		temp = {}
		tempq = []
		for i in self.roots:
			tempq.append(i)
			temp[i] = i
		while len(tempq) > 0:
			current = tempq.pop()
			current_cat = temp[current]
			current_children = self.children[current]
			# print current_children
			for i in current_children:
				if current_children[i] in self.edges['inter'] and self.edges['inter'][current_children[i]]:
					# print('CASO INTER')
					continue
				if not i in temp:
					temp[i] = current_cat
					# print str(i) + ' gets ' + str(current_cat)
				else:
					if not temp[i] == current_cat:
						consistent = False
						# print "happens"
						print i
						break
					pass
				tempq.append(i)
		# print len(temp)
		# print self.node_number()
		if len(temp) < self.node_number():
			consistent = False
		return consistent
	#

#
