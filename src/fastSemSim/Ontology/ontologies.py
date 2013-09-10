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
@desc Parser module: load/store ontologies
'''

"""
Current implementation can only handle single-scope ontologies.
"""

import types
import os
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import gzip
import Ontology
import DiseaseOntology
import CellOntology
import GeneOntology

'''
Struct ontologies.
Contains a list of all available ontologies.
It is built as a dictionary. ontology names are used as keys. Each entry is a tuple with the following structure:
(Class Name, )
'''
ontologies = {
	'GeneOntology' : (GeneOntology.GeneOntology, ),
	'DiseaseOntology' : (DiseaseOntology.DiseaseOntology, ),
	'CellOntology' : (CellOntology.CellOntology, ),
	'GenericOntology' : (Ontology.Ontology, )
}

def parse(source, parameters={}):
	return load(source, parameters)
#

def load(source, source_type = 'obo', ontology_type = 'GeneOntology', parameters={}):
	ontology = None
	namespace = None

	# generate source file handle
	if type(source) == unicode:
		source = str(source)
	if type(source) == str:
		fn,fe = os.path.splitext(source)
		if fe == '.gz':
			source_handle = gzip.open(source, 'rb')
		else:
			source_handle = open(source, 'r')
	else: # assume that the passed object is a file stream
		source_handle = source

	# select proper input parser
	if 'ontology_type' in parameters:
		ontology_type = parameters['ontology_type']
	if ontology_type in ontologies:
		ontology_class = ontologies[ontology_type][0]
	else:
		raise Exception
	if 'source_type' in parameters:
		source_type = parameters['source_type']

	# parse data
	if source_type == 'obo-xml':
		parser = make_parser()
		handler = OboXmlParser(ontology_class, parameters)
		parser.setContentHandler(handler)
		parser.parse(source_handle)
	elif source_type == 'obo':
		handler = OboParser(ontology_class, parameters)
		handler.parse(source_handle)
		namespace = handler.namespace
	else:
		# print "GeneOntology load: Unknown file format: " + str(parameters['type'])
		raise Exception

	# postprocess data, if required
	if 'ignore' in parameters and 'inter' in parameters['ignore'] and parameters['ignore']['inter']:
		for i in range(0, len(handler.edges)):
			(u,v,z) = handler.edges[i] 
			if not namespace == None:
				vn = None
				un = None
				if u in namespace:
					un = namespace[u]
				if v in namespace:
					vn = namespace[v]
				if not un == vn:
					handler.edges[i] = None	
	
	# build ontology
	ontology = ontology_class(handler.terms, handler.edges, handler.alt_ids, namespace)

	if type(source) == str: # if original source was a handle, close input file
		source_handle.close()
	return ontology
#


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# OboParser: Class to parse obo files
# Parse input file
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

class OboParser:

	def __init__(self, ontology_class, parameters = {}):
		self.ontology_class = ontology_class
		self.edges = []
		self.terms = []
		self.alt_ids = {}
		self.namespace = {}
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

	term_tag = '[Term]'
	typedef_tag = '[Typedef]'

	def find_next_term(self):
	    # read each line until it has a certain start, and then puts the start tag back
	    while True:
	        # pos = self.handle.tell()
	        line = self.handle.readline()
	        if not line:
	            break
	        if line.startswith(self.term_tag):
	            # self.handle.seek(pos)
	            return True
	    return False
	#

	def strip_tag(self, st):
		return st.split(":", 1)[1].strip()

	def parse(self, _handle):
		self.handle = _handle
		while True:
			
			# go to next [Term]
			if not self.find_next_term():
				break
			
			# collect al Term info
			lines = []
			while 1:
				pos = self.handle.tell()
				line = self.handle.readline()
				if not line:
					break
				if line.startswith(self.typedef_tag) or line.startswith(self.term_tag):
					self.handle.seek(pos)
					break
				lines.append(line)

			# process Term info
			got_id = False
			got_isa = False
			got_pof = False
			is_obsolete = False
			curid = None
			namespace = None
			for line in lines:
				if line.startswith("id:"):
					curid = self.strip_tag(line)
					curid = self.ontology_class._name2id(curid)
					got_id = True
				elif line.startswith("alt_id:"):
					curaltid = self.strip_tag(line)
					# if curaltid.startswith('CL:'): # Why is it here?
					self.alt_ids[self.ontology_class._name2id(curaltid)] = curid
				elif line.startswith("replaced_by:"):
					curaltid = self.strip_tag(line)
					# if curaltid.startswith('CL:'): # Why is it here?
					self.alt_ids[curid] = self.ontology_class._name2id(curaltid)
				elif line.startswith("namespace:"):
					namespace = self.strip_tag(line)
					self.namespace[curid] = namespace
	            # elif line.startswith("name:"):
	            #     rec.name = after_colon(line)
	            # elif line.startswith("namespace:"):
	            #     rec.namespace = after_colon(line)
				elif line.startswith("is_obsolete:") and self.strip_tag(line)=="true":
					is_obsolete = True
					if got_isa:
						raise Exception
				elif line.startswith("is_a:"):
					isa = self.strip_tag(line).split()[0]
					got_isa = True
					if is_obsolete:
						raise Exception
					if not self.ignore_is_a:
						self.edges.append( (curid, self.ontology_class._name2id(isa), Ontology.IS_A ) )
				elif line.startswith("part_of:"):
					pof = self.strip_tag(line).split()[0]
					got_pof = True
					if is_obsolete:
						raise Exception
					if not self.ignore_part_of:
						self.edges.append( (curid, self.ontology_class._name2id(pof), Ontology.PART_OF ) )
				elif line.startswith("relationship:"):
					if is_obsolete:
						raise Exception
					cline = self.strip_tag(line).split()
					ctype = cline[0]
					cto = cline[1]
					if str(ctype) == 'part_of' and not self.ignore_part_of:
						self.edges.append( (curid, self.ontology_class._name2id(cto), Ontology.PART_OF ) )
					elif str(ctype) == 'regulates' and not self.ignore_regulates:
						self.edges.append( (curid, self.ontology_class._name2id(cto), Ontology.REGULATES ) )
					elif str(ctype) == 'positively_regulates' and not self.ignore_regulates:
						self.edges.append( (curid, self.ontology_class._name2id(cto), Ontology.POS_REG ) )
					elif str(ctype) == 'negatively_regulates' and not self.ignore_regulates:
						self.edges.append( (curid, self.ontology_class._name2id(cto), Ontology.NEG_REG ) )
					elif str(ctype) == 'is_a' and not self.ignore_is_a:
						self.edges.append( (curid, self.ontology_class._name2id(cto), Ontology.IS_A ) )
					elif str(ctype) == 'has_part' and not self.ignore_has_part:
						self.edges.append( (curid, self.ontology_class._name2id(cto), Ontology.HAS_PART ) )

			# commit Term info
			if is_obsolete:
				continue
			if not got_id:
				raise Exception
			self.terms.append(curid)
			self.alt_ids[curid] = curid

	#
#


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# OboXmlParser: Class to parse GO obo-xml files
# Given an obo-xml file builds a GeneOntology object parsing it
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

class OboXmlParser(ContentHandler):
	
	def __init__(self, ontology_class, parameters = {}):
		self.ontology_class = ontology_class
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
				self.id = self.ontology_class._name2id(self.id)
			elif name == 'is_a':
				if self.curobsolete:
					#print "Inconsistent"
					raise Exception
				self.isIsA = 0
				if not self.ignore_is_a:
					self.edges.append( (self.id, self.ontology_class._name2id(self.isa), Ontology.IS_A ) )
			elif name == 'part_of':
				if self.curobsolete:
					raise Exception
				#print "original part_of"
				self.isPartOf = 0
				if not self.ignore_part_of:
					self.edges.append( (self.id, self.ontology_class._name2id(self.partof), Ontology.PART_OF ) )
			elif name == 'alt_id':
				#print "original alt_id"
				self.isaltId = 0
				self.alt_ids[self.ontology_class._name2id(self.curaltid)] = self.id
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
						self.edges.append( (self.id, self.ontology_class._name2id(self.parent), Ontology.PART_OF ) )
					elif str(self.parent_type) == 'regulates' and not self.ignore_regulates:
						self.edges.append( (self.id, self.ontology_class._name2id(self.parent), Ontology.REGULATES ) )
					elif str(self.parent_type) == 'positively_regulates' and not self.ignore_regulates:
						self.edges.append( (self.id, self.ontology_class._name2id(self.parent), Ontology.POS_REG ) )
					elif str(self.parent_type) == 'negatively_regulates' and not self.ignore_regulates:
						self.edges.append( (self.id, self.ontology_class._name2id(self.parent), Ontology.NEG_REG ) )
					elif self.parent_type == 'is_a' and not self.ignore_is_a:
						self.edges.append( (self.id, self.ontology_class._name2id(self.parent), Ontology.IS_A ) )
					elif self.parent_type == 'has_part' and not self.ignore_has_part:
						self.edges.append( (self.id, self.ontology_class._name2id(self.parent), Ontology.HAS_PART ) )
			elif name == 'is_obsolete':
				if self.isObsolete:
					self.isObsolete = 0
			elif name == 'replaced_by':
				#if self.isReplacedBy == 1:
				self.alt_ids[self.id] = self.ontology_class._name2id(self.currepid)
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
