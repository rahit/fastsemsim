# -*- coding: iso-8859-1 -*-
#@author Marco Mina
#@mail marco.mina.85@gmail.com
#@version 1.0
"""
@desc 
Utility to load Gene Ontology DAG and manipulate it.
It keeps into account term attributes such as "obsolete" and "alternative" ids.

Function load_GO_XML(file_stream) loads XML files. It returns a GeneOntology object.
"""

IS_A = 0
PART_OF = 1

import types
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

def get_goid(id):
	return int(id[3:])

class GOHandler(ContentHandler):
	def __init__(self,):
		self.isId, self.isIsA, self.isPartOf, self.isaltId = 0,0,0,0
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
	
	def endElement(self, name):
		if self.inTerm == 1:
			if name == 'term':
				self.terms.append(self.id)
				self.alt_ids[self.id] = self.id
				self.inTerm = 0
			elif name == 'id':
				self.isId = 0
				self.id = get_goid(self.id)
			elif name == 'is_a':
				self.isIsA = 0
				self.edges.append( (self.id, get_goid(self.isa), IS_A ) )
			elif name == 'part_of':
				self.isPartOf = 0
				self.edges.append( (self.id, get_goid(self.partof), PART_OF ) )
			elif name == 'alt_id':
				self.isaltId = 0
				self.alt_ids[get_goid(self.curaltid)] = self.id
	
	def characters(self, ch):
		if self.isId == 1:
			self.id += ch
		elif self.isIsA == 1:
			self.isa += ch
		elif self.isPartOf == 1:
			self.partof += ch
		elif self.isaltId == 1:
			self.curaltid += ch

class GeneOntology:
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
