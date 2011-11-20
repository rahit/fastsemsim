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
@mail marco.mina.85@gmail.com
@version 1.0
@desc 
Utility to load Gene Ontology DAG and manipulate it.
It keeps into account term attributes such as "obsolete" and "alternative" ids.

Function load_GO_XML(file_stream) loads XML files. It returns a GeneOntology object.
"""

IS_A = 0
PART_OF = 1
BP_root = "GO:0008150"
MF_root = "GO:0003674"
CC_root = "GO:0005575"

import types
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

def go_name2id(code):
	return int(code[3:])

def go_id2name(code):
	return "GO:" + '0'*(7 - len(str(code))) + str(code)
	
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
class GeneOntology:

	def name2id(self, codes, alt_check = True):
		nid = None
		if type(codes) is str:
			nid = go_name2id(codes)
		elif type(codes) is int:
			nid = codes
		elif type(codes) is dict or type(codes) is list:
			nid = []
			for i in codes:
				tnid = go_2ids(i)
				if alt_check:
					tnid = self.alt_ids[tnid]
				nid.append(tnid)
			return nid
		if alt_check:
			nid = self.alt_ids[nid]
		return nid

	def id2name(self, codes, alt_check = False):
		if alt_check:
			print "go_2names - alt_check not yet implemented."
		sid = None
		if type(codes) is int:
			sid = go_id2name(codes)
		elif type(codes) is str:
			sid = codes
		elif type(codes) is dict or type(codes) is list:
			sid= []
			for i in codes:
				sid.append(go_2names(i))
		return sid

	"""
		Nodes are GO terms. Edges are links between GO Terms within GO.
	"""
	def __init__(self, terms, edges, alt_ids):
		self.nodes_edges = {}
		self.edges_nodes = {}
		self.next_edge = 0

		self.edge_types = [0 for i in range(len(edges))]
		for (u,v,z) in edges:
			self.add_edge(u,v,z)
		self.alt_ids = alt_ids
		self.obsolete_ids = {}
		for i in self.alt_ids:
			if i not in self.nodes_edges:
				self.obsolete_ids[i] = {}

	def add_node(self,n):
		if n not in self.nodes_edges:
			self.nodes_edges[n] = []
		else:
			raise(Exception, 'Node ' + str(n) + ' is already in the graph')

	def add_edge(self, go1, go2, edge_type):
		"""
		Edge type might be IS_A, PART_OF, ???
		"""
		while self.next_edge in self.edges_nodes:
			self.next_edge += 1
		e = self.next_edge
		self.next_edge += 1

		if go1 not in self.nodes_edges:
			self.add_node(go1)
		if go2 not in self.nodes_edges:
			self.add_node(go2)

		self.edges_nodes[e] = (go1,go2)
		self.nodes_edges[go1].append(e)
		if go1 != go2:
			self.nodes_edges[go2].append(e)
		self.edge_types[e] = edge_type
		return e

	def node_num(self):
		return len(self.nodes_edges)
	def edge_num(self):
		return len(self.edges_nodes)

def load_GO_XML(file_stream):
	parser = make_parser()
	handler = GOHandler()
	parser.setContentHandler(handler)
	parser.parse(file_stream)
	return GeneOntology(handler.terms, handler.edges, handler.alt_ids)


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

class GOHandler(ContentHandler):
	ignore_part_of = False
	
	def __init__(self,):
		self.isId, self.isIsA, self.isPartOf, self.isaltId, self.isRelationship = 0,0,0,0,0
		self.isRelationshipTo, self.isRelationshipType = 0,0
		self.inTerm = 0
		self.edges = []
		self.terms = []
		self.alt_ids = {}
		self.id = ''
		
	def startElement(self, name, attrs):
		if name == 'term':
			self.inTerm = 1
		if self.inTerm == 1:
			if name == 'id':
				self.isId = 1
				self.id = ''
			elif name == 'is_a':
				self.isIsA = 1
				self.isa = ''
			elif name == 'part_of':
				self.isPartOf = 1
				self.partof = ''
			elif name == 'alt_id':
				self.isaltId = 1
				self.curaltid = ''
			elif name == 'relationship':
				self.isRelationship = 1
			elif name == 'type':
				if self.isRelationship:
					self.isRelationshipType = 1
					self.parent_type = ''
			elif name == 'to':
				if self.isRelationship:
					self.isRelationshipTo = 1
					self.parent = ''
	
	def endElement(self, name):
		if self.inTerm == 1:
			if name == 'term':
				self.terms.append(self.id)
				self.alt_ids[self.id] = self.id
				self.inTerm = 0
			elif name == 'id':
				self.isId = 0
				self.id = go_name2id(self.id)
			elif name == 'is_a':
				#print "original is_a"
				self.isIsA = 0
				self.edges.append( (self.id, go_name2id(self.isa), IS_A ) )
			elif name == 'part_of':
				print "original part_of"
				self.isPartOf = 0
				self.edges.append( (self.id, go_name2id(self.partof), PART_OF ) )
			elif name == 'alt_id':
				#print "original alt_id"
				self.isaltId = 0
				self.alt_ids[go_name2id(self.curaltid)] = self.id
			elif name == 'relationship':
				self.isRelationship = 0
			elif name == 'type':
				if self.isRelationship:
					self.isRelationshipType = 0
					#self.parent_type = ''
			elif name == 'to':
				if self.isRelationship:
					self.isRelationshipTo = 0
					if str(self.parent_type) == 'part_of' and not self.ignore_part_of:
						self.edges.append( (self.id, go_name2id(self.parent), PART_OF ) )
					elif self.parent_type == 'is_a':
						self.edges.append( (self.id, go_name2id(self.parent), IS_A ) )
	
	def characters(self, ch):
		if self.isId == 1:
			self.id += ch
		elif self.isIsA == 1:
			self.isa += ch
		elif self.isPartOf == 1:
			self.partof += ch
		elif self.isaltId == 1:
			self.curaltid += ch
		elif self.isRelationshipTo == 1:
			self.parent += ch
		elif self.isRelationshipType == 1:
			self.parent_type += ch
			#print "set: " + ch