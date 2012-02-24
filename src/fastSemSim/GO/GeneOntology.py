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
#--------------------------------------------------------------------------
"""
@mail marco.mina.85@gmail.com
@version 1.0
@desc GeneOntology class handles Gene Ontology

Function load_GO_XML(file_stream) loads XML files. It returns a GeneOntology object.
"""
import types
import os
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import gzip

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# constants and macro
# assume the GO ids are in the standard format "GO:" + 7 digit number
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

IS_A = 0
PART_OF = 1
REGULATES = 2
POS_REG = 3
NEG_REG = 4

BP_root = "GO:0008150"
MF_root = "GO:0003674"
CC_root = "GO:0005575"

def go_name2id(code):
	return int(code[3:])

def go_id2name(code):
	return "GO:" + '0'*(7 - len(str(code))) + str(code)
	
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# GeneOntology class
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

class GeneOntology:
	
	BP_root = 8150
	MF_root = 3674
	CC_root = 5575

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# public functions and variables that should be used 
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

	nodes_edges = None
	edges_nodes = None
	parents = None
	children = None
	alt_ids = None
	obsolete_ids = None

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

	def node_num(self):
		return len(self.nodes_edges)

	def edge_num(self):
		return len(self.edges_nodes)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# internal functions
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

	def __init__(self, terms, edges, alt_ids):
		self.nodes_edges = {}
		self.edges_nodes = {}
		self.obsolete_ids = {}
		self.alt_ids = alt_ids
		self.parents = {}
		self.children = {}

		self.next_edge = 0
		self.edge_types = [0 for i in range(len(edges))]
		for (u,v,z) in edges:
			self.int_add_edge(u,v,z)
		for i in self.alt_ids:
			if self.alt_ids[i] not in self.nodes_edges:
				#if not i == self.alt_ids[i]:
						#print str(i) + " --> " + str(self.alt_ids[i]) + ": obsolete"
				self.obsolete_ids[i] = {}

		for i in self.nodes_edges:
			self.parents[i] = []
			self.children[i] = []
			for j in self.nodes_edges[i]:
				if self.edges_nodes[j][0] == i:
					self.parents[i].append(self.edges_nodes[j][1])
				else:
					self.children[i].append(self.edges_nodes[j][0])

	def int_add_node(self,n):
		if n not in self.nodes_edges:
			self.nodes_edges[n] = []
		else:
			raise(Exception, 'Node ' + str(n) + ' is already in the graph')

	def int_add_edge(self, go1, go2, edge_type):
		"""
		Edge type might be IS_A, PART_OF, ???
		"""
		while self.next_edge in self.edges_nodes:
			self.next_edge += 1
		e = self.next_edge
		self.next_edge += 1

		if go1 not in self.nodes_edges:
			self.int_add_node(go1)
		if go2 not in self.nodes_edges:
			self.int_add_node(go2)

		self.edges_nodes[e] = (go1,go2)
		self.nodes_edges[go1].append(e)
		if go1 != go2:
			self.nodes_edges[go2].append(e)
		self.edge_types[e] = edge_type
		return e
#







#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# load_GO_XML: function to load an obo-xml file
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
def load_GO_XML(file_stream): # kept for backward compatibility. Should use load or parse instead
	return load(file_stream)
#


def parse(file_stream):
	return load(file_stream)
#


def load(file_stream):
	if type(file_stream) == file or type(file_stream) == gzip.GzipFile:
		file_stream_handle = file_stream
	
	elif type(file_stream) == str:
		fn,fe = os.path.splitext(file_stream)
		if fe == '.gz':
			file_stream_handle = gzip.open(file_stream, 'rb')
		else:
			file_stream_handle = open(file_stream, 'r')
	
	else:
	 raise Exception
	
	parser = make_parser()
	handler = OboXmlParser()
	parser.setContentHandler(handler)
	parser.parse(file_stream_handle)
	
	if type(file_stream) == str:
		file_stream_handle.close()

	return GeneOntology(handler.terms, handler.edges, handler.alt_ids)
#







#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# OboXmlParser: Class to parse GO obo-xml files
# Given an obo-xml file builds a GeneOntology object parsing it
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

class OboXmlParser(ContentHandler):
	ignore_part_of = False
	ignore_regulates = False
	
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
				#print "original part_of"
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
					elif str(self.parent_type) == 'regulates' and not self.ignore_regulates:
						self.edges.append( (self.id, go_name2id(self.parent), REGULATES ) )
					elif str(self.parent_type) == 'positively_regulates' and not self.ignore_regulates:
						self.edges.append( (self.id, go_name2id(self.parent), POS_REG ) )
					elif str(self.parent_type) == 'negatively_regulates' and not self.ignore_regulates:
						self.edges.append( (self.id, go_name2id(self.parent), NEG_REG ) )
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