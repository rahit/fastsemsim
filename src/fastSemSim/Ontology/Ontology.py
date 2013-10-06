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

@mail marco.mina.85@gmail.com
@version 2.0
@desc Ontology is the basic class representing ontologies representable with multirooted connected DAGs.
'''

"""
Supported ontologies are those representable as multirooted DAGs. It is not required DAGs to be disconnected, but 'inter-DAG' edges are required to be specified. Class Ontology provides a function is_consistent that checks whether this contraints is satisfied. Inconsistent DAGs are NOT currently usable.

Different datastructures can be used to represent ontologies. The section Variables lists a set of different alternatives. Currently Ontology is tuned for using a parent-children and a node-edge representation.

Superclasses can extend the basic datastructure with additional layers of information. 
"""

IS_A = 0
PART_OF = 1
REGULATES = 2
POS_REG = 3
NEG_REG = 4
HAS_PART = 5

'''
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
'''

class Ontology:

	debug = False
	gen_error = False

	@staticmethod
	def _id2name(code, strict=True):
		# return "generic:" + '0'*(7 - len(str(code))) + str(code)
		return str(code) # watch out for Unicode strings
	#

	@staticmethod
	def _name2id(code, strict=True):
		# return int(code.split(":", 1)[1])
		return str(code) # watch out for Unicode strings
	#


	def name2id(self, codes, alt_check = True):
		nid = None
		if type(codes) is dict or type(codes) is list:
			nid = []
			for i in codes:
				# if type(i) is str:
					# tnid = go_name2id(i)
					tnid = Ontology._name2id(i, strict=True)
				# else:
					# tnid = i
					if alt_check:
						if tnid in self.alt_ids:
							tnid = self.alt_ids[tnid]
					nid.append(tnid)
		else:
		# if type(codes) is str:
			# nid = go_name2id(codes)
			nid = Ontology._name2id(codes, strict=True)
		# elif type(codes) is int:
			# nid = codes
			if alt_check:
				if nid in self.alt_ids:
					nid = self.alt_ids[nid]
		return nid
	#

	def id2name(self, codes, alt_check = False):
		if alt_check:
			if self.debug:
				print "id2name - alt_check not yet implemented."
		sid = None
		if type(codes) is dict or type(codes) is list:
			sid= []
			for i in codes:
				# if type(i) is int:
				tnid = Ontology._id2name(i, strict = True)
				# else:
					# tnid = i
				sid.append(tnid)
		# if type(codes) is int:
			# sid = Ontology._id2name(codes)
		else:
		 # type(codes) is str:
			# sid = codes
			sid = Ontology._id2name(codes, strict = True)
		return sid
	#

	def node_number(self):
		return len(self.nodes)

	def edge_number(self):
		return self.next_edge

	def __init__(self, terms, edges, alt_ids = None, namespace = None, extra_edges = None):
		self.nodes = {}
		self.edges = {}
		self.edges['inter'] = {}
		self.edges['nodes'] = []
		self.parents = {}
		self.children = {}
		self.next_edge = 0

		self.alt_ids = alt_ids
		self.obsolete_ids = {}
		self.edges['type'] = []
		self.extra_edges = {}
		self.extra_edges = extra_edges # ! does not respect the structure of normal edges

		for i in edges:
			if i == None:
				continue
			(child,parent,z) = i
			ce = self._add_edge(parent, child, False)
			self.edges['type'].append(z)
			if (not namespace == None) and (child in namespace) and (parent in namespace) and (not namespace[parent] == namespace[child]):
				self.edges['inter'][ce] = True
		if not self.alt_ids == None:
			for i in self.alt_ids:
				if i in self.nodes:
					if self.gen_error:
						raise Exception # it means there are inconsistencies!
					if self.debug:
						print "Warning: Ignoring inconsistent redefinition of valid term " + str(self._id2name(i)) + " as an alternative of " + str(self._id2name(self.alt_ids[i]))
					# raise Exception # it means there are inconsistencies!
		self.det_roots()
	#

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
						# print str(i) + "-" + str(current)
						break
					pass
				tempq.append(i)
		# print len(temp)
		# print self.node_number()
		if len(temp) < self.node_number():
			consistent = False
		return consistent
	#

	# verify if a term is valid (not obsolete and inside the ontology). Single terms are required. Does not work with lists/dicts.
	def is_valid(self, term):
		if term in self.nodes:
			return True
		return False
#
