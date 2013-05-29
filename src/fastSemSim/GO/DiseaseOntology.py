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
@desc DiseaseOntology class handles DiseaseOntology

Function load_DO(file_stream) loads DO in OBO files. It returns a DiseaseOntology object.
"""
import types
import os
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import gzip
import Ontology

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# constants and macro
# assume the DO ids are in the standard format "DOID:" + 7 digit number
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

# IS_A = 0
# PART_OF = 1
# REGULATES = 2
# POS_REG = 3
# NEG_REG = 4
# HAS_PART = 5

def do_name2id(code):
	return int(code[5:])

def do_id2name(code):
	# assumption: GO terms are 5 + 7 characters long.
	return "DOID:" + '0'*(7 - len(str(code))) + str(code)
	
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# GeneOntology class
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

class DiseaseOntology(Ontology.Ontology):
	
	# BP_root_str = "GO:0008150"
	# MF_root_str = "GO:0003674"
	# CC_root_str = "GO:0005575"

	# BP_root = do_name2id(BP_root_str)
	# MF_root = do_name2id(MF_root_str)
	# CC_root = do_name2id(CC_root_str)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# public functions and variables that should be used 
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

	alt_ids = None
	obsolete_ids = None

	def name2id(self, codes, alt_check = True):
		nid = None
		if type(codes) is str:
			nid = do_name2id(codes)
			nid = self.name2id(nid, alt_check)
		elif type(codes) is int:
			nid = codes
			if alt_check:
				if nid in self.alt_ids:
					nid = self.alt_ids[nid]
		elif type(codes) is dict or type(codes) is list:
			nid = []
			for i in codes:
				if type(i) is str:
					tnid = do_name2id(i)
				else:
					tnid = i
				if alt_check:
					if tnid in self.alt_ids:
						tnid = self.alt_ids[tnid]
				nid.append(tnid)
		return nid

	def id2name(self, codes, alt_check = False):
		if alt_check:
			print "id2name - alt_check not yet implemented."
		sid = None
		if type(codes) is int:
			sid = do_id2name(codes)
		elif type(codes) is str:
			sid = codes
		elif type(codes) is dict or type(codes) is list:
			sid= []
			for i in codes:
				if type(i) is int:
					tnid = do_id2name(i)
				else:
					tnid = i
				sid.append(tnid)
		return sid

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# internal functions
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

	def __init__(self, terms, edges, alt_ids):
		Ontology.Ontology.__init__(self)
		self.obsolete_ids = {}
		self.alt_ids = alt_ids
		self.edges['type'] = []


		# self.edge_types = [0 for i in range(len(edges))]
		for (u,v,z) in edges:
			ce = self._add_edge(v, u, False)
			self.edges['type'].append(z)

		for i in self.alt_ids:
			if self.alt_ids[i] not in self.nodes:
				#if not i == self.alt_ids[i]:
		# 				#print str(i) + " --> " + str(self.alt_ids[i]) + ": obsolete"
				self.obsolete_ids[i] = {}

		# for i in self.nodes_edges:
		# 	self.parents[i] = []
		# 	self.children[i] = []
		# 	for j in self.nodes_edges[i]:
		# 		if self.edges_nodes[j][0] == i:
		# 			self.parents[i].append(self.edges_nodes[j][1])
		# 		else:
		# 			self.children[i].append(self.edges_nodes[j][0])

	# def int_add_node(self,n):
	# 	if n not in self.nodes_edges:
	# 		self.nodes_edges[n] = []
	# 	else:
	# 		raise(Exception, 'Node ' + str(n) + ' is already in the graph')

	# def int_add_edge(self, go1, go2, edge_type):
	# 	"""
	# 	Edge type might be IS_A, PART_OF, ???
	# 	"""
	# 	while self.next_edge in self.edges_nodes:
	# 		self.next_edge += 1
	# 	e = self.next_edge
	# 	self.next_edge += 1

	# 	if go1 not in self.nodes_edges:
	# 		self.int_add_node(go1)
	# 	if go2 not in self.nodes_edges:
	# 		self.int_add_node(go2)

	# 	self.edges_nodes[e] = (go1,go2)
	# 	self.nodes_edges[go1].append(e)
	# 	if go1 != go2:
	# 		self.nodes_edges[go2].append(e)
	# 	self.edge_types[e] = edge_type
	# 	return e
#







#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# load_GO_XML: function to load an obo-xml file
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

def load_GO_XML(file_stream, ignore_part_of=False, ignore_regulates=False): # kept for backward compatibility.
	return load(file_stream, parameters={'ignore':{'part_of':ignore_part_of, 'regulates':ignore_regulates}})
#


def parse(file_stream, parameters={}):
	return load(file_stream, parameters)
#


def load(file_stream, parameters={}):
	go = None

	if type(file_stream) == unicode:
		file_stream = str(file_stream)
	if type(file_stream) == str:
		fn,fe = os.path.splitext(file_stream)
		if fe == '.gz':
			file_stream_handle = gzip.open(file_stream, 'rb')
		else:
			file_stream_handle = open(file_stream, 'r')
	else: # assume that the passed object is a file stream
		file_stream_handle = file_stream
	
	
	if 'type' in parameters:
		if parameters['type'] == 'obo-xml':
			parser = make_parser()
			handler = OboXmlParser(parameters)
			parser.setContentHandler(handler)
			parser.parse(file_stream_handle)
			go = GeneOntology(handler.terms, handler.edges, handler.alt_ids)
		else:
			print "GeneOntology load: Unknown file format: " + str(parameters['type'])
			raise Exception

	else: # default assumption: obo-xml GO
		parser = make_parser()
		handler = OboXmlParser(parameters)
		parser.setContentHandler(handler)
		parser.parse(file_stream_handle)
		go = GeneOntology(handler.terms, handler.edges, handler.alt_ids)
	
	if type(file_stream) == str:
		file_stream_handle.close()
	return go
#







#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# OboXmlParser: Class to parse GO obo-xml files
# Given an obo-xml file builds a GeneOntology object parsing it
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

class OboXmlParser(ContentHandler):
	
	def __init__(self, parameters = {}):
		self.isId, self.isIsA, self.isPartOf, self.isaltId, self.isRelationship = 0,0,0,0,0
		self.isObsolete, self.isReplacedBy, self.isConsider = 0,0,0
		self.isRelationshipTo, self.isRelationshipType = 0,0
		self.inTerm = 0
		self.curobsolete = False
		self.edges = []
		self.terms = []
		self.alt_ids = {}
		self.id = ''
		self.ignore_part_of = False
		self.ignore_regulates = False
		self.ignore_has_part = True ### NOTE has part ignored by default!
		self.ignore_is_a = False
		
		if 'ignore' in parameters and type(parameters['ignore']) == dict:
			ignore = parameters['ignore']
			if 'part_of' in ignore:
				self.ignore_part_of = bool(ignore['part_of'])
			if 'regulates' in ignore:
				self.ignore_regulates = bool(ignore['regulates'])
			if 'has_part' in ignore:
				self.ignore_has_part = bool(ignore['has_part'])
			if 'is_a' in ignore:
				self.ignore_is_a = bool(ignore['is_a'])
#


	def startElement(self, name, attrs):
		if name == 'term':
			self.inTerm = 1
		elif self.inTerm == 1:
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
			elif name == 'is_obsolete':
				self.isObsolete = 1
			elif name == 'replaced_by':
				self.isReplacedBy = 1
				self.currepid = ''
				#print "replaced_by"
			elif name == 'consider':
				self.isConsider = 1
				#print "consider"
#


	def endElement(self, name):
		if self.inTerm == 1:
			if name == 'term':
				self.terms.append(self.id)
				self.alt_ids[self.id] = self.id
				self.curobsolete = False
				self.inTerm = 0
			elif name == 'id':
				self.isId = 0
				self.id = do_name2id(self.id)
			elif name == 'is_a':
				if self.curobsolete:
					#print "Inconsistent"
					raise Exception
				self.isIsA = 0
				if not self.ignore_is_a:
					self.edges.append( (self.id, do_name2id(self.isa), IS_A ) )
			elif name == 'part_of':
				if self.curobsolete:
					raise Exception
				#print "original part_of"
				self.isPartOf = 0
				if not self.ignore_part_of:
					self.edges.append( (self.id, do_name2id(self.partof), PART_OF ) )
			elif name == 'alt_id':
				#print "original alt_id"
				self.isaltId = 0
				self.alt_ids[do_name2id(self.curaltid)] = self.id
			elif name == 'relationship':
				if self.curobsolete:
					raise Exception
				self.isRelationship = 0
			elif name == 'type':
				if self.isRelationship:
					self.isRelationshipType = 0
					#self.parent_type = ''
			elif name == 'to':
				if self.isRelationship:
					self.isRelationshipTo = 0
					if str(self.parent_type) == 'part_of' and not self.ignore_part_of:
						self.edges.append( (self.id, do_name2id(self.parent), PART_OF ) )
					elif str(self.parent_type) == 'regulates' and not self.ignore_regulates:
						self.edges.append( (self.id, do_name2id(self.parent), REGULATES ) )
					elif str(self.parent_type) == 'positively_regulates' and not self.ignore_regulates:
						self.edges.append( (self.id, do_name2id(self.parent), POS_REG ) )
					elif str(self.parent_type) == 'negatively_regulates' and not self.ignore_regulates:
						self.edges.append( (self.id, do_name2id(self.parent), NEG_REG ) )
					elif self.parent_type == 'is_a' and not self.ignore_is_a:
						self.edges.append( (self.id, do_name2id(self.parent), IS_A ) )
					elif self.parent_type == 'has_part' and not self.ignore_has_part:
						self.edges.append( (self.id, do_name2id(self.parent), HAS_PART ) )
			elif name == 'is_obsolete':
				if self.isObsolete:
					self.isObsolete = 0
			elif name == 'replaced_by':
				#if self.isReplacedBy == 1:
				self.alt_ids[self.id] = do_name2id(self.currepid)
				self.isReplacedBy = 0
			elif name == 'consider':
				if self.isConsider:
					self.isConsider = 0
#


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
		elif self.isObsolete == 1:
			self.curobsolete = bool(ch)
		elif self.isReplacedBy == 1:
			self.currepid += ch
		elif self.isConsider == 1:
			pass
#
