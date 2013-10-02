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
import FFOntology

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
	'FFOntology' : (FFOntology.FFOntology, ),
	'GenericOntology' : (Ontology.Ontology, ),
	'Ontology' : (Ontology.Ontology, )
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
		# namespace = handler.namespace
	else:
		# print "GeneOntology load: Unknown file format: " + str(parameters['type'])
		raise Exception

	# # postprocess data, if required
	# if 'ignore' in parameters and 'inter' in parameters['ignore'] and parameters['ignore']['inter']:
	# 	for i in range(0, len(handler.edges)):
	# 		(u,v,z) = handler.edges[i] 
	# 		if not namespace == None:
	# 			vn = None
	# 			un = None
	# 			if u in namespace:
	# 				un = namespace[u]
	# 			if v in namespace:
	# 				vn = namespace[v]
	# 			if not un == vn:
	# 				handler.edges[i] = None	
	
	# build ontology
	ontology = ontology_class(handler.terms, handler.edges, handler.alt_ids, handler.namespace, handler.extra_edges)

	for i in handler.terms:
		if not i in ontology.nodes:
			print i
	for i in ontology.nodes:
		if not i in handler.terms:
			print i

	if type(source) == str: # if original source was a handle, close input file
		source_handle.close()
	return ontology
#


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# OboParser: Class to parse obo files
# Parse input file
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

class OboParser:

	term_tag = '[Term]'
	typedef_tag = '[Typedef]'

	id_tag = "id:"
	alt_id_tag = "alt_id:"
	replaced_by_tag = "replaced_by:"
	namespace_tag = "namespace:"
	is_obsolete_tag = "is_obsolete:"
	is_a_tag = "is_a:"
	part_of_tag = "part_of:"
	relationship_tag = "relationship:"

	def __init__(self, ontology_class, parameters = {}):
		self.ontology_class = ontology_class

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
	
		# Initialize structures
		self.edges = [] # set of relationships between terms. Only primary terms from current ontology are allowed here, and should be present in terms
		self.extra_edges = [] # set of relationships between terms. Only primary terms from current ontology are allowed here, and should be present in terms
		self.terms = {} # ids of primary terms contained in the ontology. Only terms from current ontology are allowed here
		self.alt_ids = {}
		self.namespace = {}

	#


	'''
	Find next block of informations
	'''
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

	'''
	Strip tag from line; strip trailing and ending spaces and return characters
	'''
	def strip_tag(self, st):
		return st.split(":", 1)[1].strip()


	def parse(self, _handle):
		self.handle = _handle
		while True:

			# go to next [Term]
			if not self.find_next_term():
				break

			# collect lines from current block. Stop when find another block
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

			# process info in captured block
			# block variables
			got_term = False
			inner_term = False
			term_id = None
			obsolete_term = False
			term_namespace = None
			term_alt_ids = {}			
			got_rel = False
			term_rel = []
			term_extra_rel = []

			for line in lines:

				if line.startswith(self.id_tag):
					if got_term:
						raise Exception
					curid = self.strip_tag(line)
					term_id = self.ontology_class._name2id(curid)
					if term_id == None:
						term_id = curid
						inner_term = False
					else:
						inner_term = True
					got_term = True
				#

				elif line.startswith(self.alt_id_tag):
					if not got_term:
						raise Exception
					if not inner_term:
						continue
					curaltname = self.strip_tag(line)
					curaltid = self.ontology_class._name2id(curaltname, strict = True) # modify strict to allow refs to external ontologies
					if not curaltid == None:
						if curaltid not in term_alt_ids:
							term_alt_ids[curaltid] = []
						term_alt_ids[curaltid].append(term_id)
						# elif self.alt_ids[curaltid] == curaltid:
							# pass # if a term is present and is not obsolete (is already in alt_ids and references to itself, then DO NOT overwrite it)
						# else:
							# print "Warning: Ignoring inconsistent redefinition of alternative term " + str(self.ontology_class._id2name(curaltid)) + ", already defined as " + str(self.ontology_class._id2name(self.alt_ids[curaltid])) + ", to " + str(self.ontology_class._id2name(curid))
							# raise Exception
					else:
						print "Warning: Ignoring alternative id " + str(curaltname) + " of term " + str(self.ontology_class._id2name(term_id)) + ", since it belongs to a different ontology."
				#

				elif line.startswith(self.replaced_by_tag):
					if not got_term:
						raise Exception
					if not inner_term:
						continue
					curaltname = self.strip_tag(line)
					curaltid = self.ontology_class._name2id(curaltname, strict = True) # modify strict to allow refs to external ontologies
					if not curaltid == None:
						if term_id not in term_alt_ids:
							term_alt_ids[term_id] = []
						term_alt_ids[term_id].append(curaltid)
						# if curid not in self.alt_ids:
						# 	self.alt_ids[curid] = curaltid
						# else:
							# print "Warning: Multiple alternative ids not supported yet. Term " + str(self.ontology_class._id2name(curid)) + ", already remapped to " + str(self.ontology_class._id2name(self.alt_ids[curid])) + ", will not be mapped to " + str(self.ontology_class._id2name(curaltid))
				#			

				elif line.startswith(self.namespace_tag):
					if not got_term:
						raise Exception
					namespace = self.strip_tag(line)
					self.namespace[term_id] = namespace
	            # elif line.startswith("name:"):
	            #     rec.name = after_colon(line)
	            # elif line.startswith("namespace:"):
	            #     rec.namespace = after_colon(line)
	            #

				elif line.startswith(self.is_obsolete_tag) and self.strip_tag(line)=="true":
					if not got_term:
						raise Exception
					if got_rel:
						raise Exception
					obsolete_term = True
				#

				elif line.startswith(self.is_a_tag):
					if not got_term:
						raise Exception
					if obsolete_term:
						raise Exception
					if not inner_term:
						continue
					if not self.ignore_is_a:
						isaname = self.strip_tag(line).split()[0]
						isa = self.ontology_class._name2id(isaname)
						if not isa == None:
							got_rel = True
							term_rel.append( (term_id, isa, Ontology.IS_A ) )
						else:
							term_extra_rel.append( (term_id, isaname, Ontology.IS_A ) )
							# self.edges.append( (curid, isa, Ontology.IS_A ) )
				#

				elif line.startswith(self.part_of_tag):
					if not got_term:
						raise Exception
					if obsolete_term:
						raise Exception
					if not inner_term:
						continue
					if not self.ignore_part_of:
						pofname = self.strip_tag(line).split()[0]
						pof = self.ontology_class._name2id(pofname)
						if not pof == None:
							got_rel = True
							term_rel.append( (term_id, pof, Ontology.PART_OF ) )
						else:
							term_extra_rel.append( (term_id, pofname, Ontology.PART_OF ) )
				#

				elif line.startswith(self.relationship_tag):
					if not got_term:
						raise Exception
					if obsolete_term:
						raise Exception
					if not inner_term:
						continue
					cline = self.strip_tag(line).split()
					ctype = cline[0]
					ctoname = cline[1]
					cto = self.ontology_class._name2id(ctoname)
					if not cto == None:
						got_rel = True
						if str(ctype) == 'part_of' and not self.ignore_part_of:
							term_rel.append( (term_id, cto, Ontology.PART_OF ) )
						elif str(ctype) == 'regulates' and not self.ignore_regulates:
							term_rel.append( (term_id, cto, Ontology.REGULATES ) )
						elif str(ctype) == 'positively_regulates' and not self.ignore_regulates:
							term_rel.append( (term_id, cto, Ontology.POS_REG ) )
						elif str(ctype) == 'negatively_regulates' and not self.ignore_regulates:
							term_rel.append( (term_id, cto, Ontology.NEG_REG ) )
						elif str(ctype) == 'is_a' and not self.ignore_is_a:
							term_rel.append( (term_id, cto, Ontology.IS_A ) )
						elif str(ctype) == 'has_part' and not self.ignore_has_part:
							term_rel.append( (term_id, cto, Ontology.HAS_PART ) )
					else:
						if str(ctype) == 'part_of' and not self.ignore_part_of:
							term_extra_rel.append( (term_id, ctoname, Ontology.PART_OF ) )
						elif str(ctype) == 'regulates' and not self.ignore_regulates:
							term_extra_rel.append( (term_id, ctoname, Ontology.REGULATES ) )
						elif str(ctype) == 'positively_regulates' and not self.ignore_regulates:
							term_extra_rel.append( (term_id, ctoname, Ontology.POS_REG ) )
						elif str(ctype) == 'negatively_regulates' and not self.ignore_regulates:
							term_extra_rel.append( (term_id, ctoname, Ontology.NEG_REG ) )
						elif str(ctype) == 'is_a' and not self.ignore_is_a:
							term_extra_rel.append( (term_id, ctoname, Ontology.IS_A ) )
						elif str(ctype) == 'has_part' and not self.ignore_has_part:
							term_extra_rel.append( (term_id, ctoname, Ontology.HAS_PART ) )
				#

			# commit Term info
			if not got_term:
				raise Exception
			if not inner_term:
				continue
				self.namespace[term_id] = term_namespace
			if not obsolete_term:
				if term_id in self.terms:
					raise Exception
				self.terms[term_id] = None
				for i in term_rel:
					self.edges.append( i )
				for i in term_extra_rel:
					self.extra_edges.append( i )
			for i in term_alt_ids:
				if not i in self.alt_ids:
					self.alt_ids[i] = term_alt_ids[i] # if a term is present and is not obsolete, then overwrite any previous alt_ids mapping
				else:
					for j in term_alt_ids[i]:
						self.alt_ids[i].append(j)
		#
	#
#


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# OboXmlParser: Class to parse GO obo-xml files
# Given an obo-xml file builds a GeneOntology object parsing it
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

class OboXmlParser(ContentHandler):
	
	def __init__(self, ontology_class, parameters = {}):
		self.ontology_class = ontology_class # type of ontology to load

		self.edges = [] # set of relationships between terms. Only primary terms from current ontology are allowed here, and should be present in terms
		self.extra_edges = [] # set of relationships between terms. Only primary terms from current ontology are allowed here, and should be present in terms
		self.terms = {} # ids of primary terms contained in the ontology. Only terms from current ontology are allowed here
		self.alt_ids = {}
		self.namespace = {}

		# self.terms['id'] = {}
		# self.terms['alt_id'] = {}
		# self.terms['obsolete'] = {}
		# self.terms['namespace'] = {}

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

		self.isId, self.isIsA, self.isPartOf, self.isaltId, self.isRelationship = 0,0,0,0,0
		self.isObsolete, self.isReplacedBy, self.isConsider = 0,0,0
		self.isRelationshipTo, self.isRelationshipType = 0,0
		self.inTerm = 0

		self.curobsolete = False
		self.id = None
		self.got_term = False
		self.inner_term = False
		self.term_namespace = None
		self.term_alt_ids = {}
		self.got_rel = False
		self.term_rel = []
		self.term_extra_rel = []


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
				if not self.got_term:
					raise Exception
				if self.inner_term:
					self.namespace[self.id] = self.term_namespace
					if not self.curobsolete:
						if self.id in self.terms:
							raise Exception
						self.terms[self.id] = None
						for i in self.term_rel:
							self.edges.append( i )
						for i in self.term_extra_rel:
							self.extra_edges.append( i )
					for i in self.term_alt_ids:
						if not i in self.alt_ids:
							self.alt_ids[i] = self.term_alt_ids[i] # if a term is present and is not obsolete, then overwrite any previous alt_ids mapping
						else:
							for j in self.term_alt_ids[i]:
								self.alt_ids[i].append(j)

				self.curobsolete = False
				self.id = None
				self.got_term = False
				self.inner_term = False
				self.term_namespace = None
				self.term_alt_ids = {}
				self.got_rel = False
				self.term_rel = []
				self.term_extra_rel = []
				self.inTerm = 0
			#

			elif name == 'id':
				self.isId = 0
				self.got_term = True
				self.id = self.ontology_class._name2id(self.id)
				if not self.id == None:
					self.inner_term = True
			#

			elif name == 'alt_id':
				self.isaltId = 0
				if not self.got_term:
					raise Exception
				if not self.inner_term:
					return
				curaltid = self.ontology_class._name2id(self.curaltid, strict = True) # modify strict to allow refs to external ontologies
				if not curaltid == None:
					if curaltid not in self.term_alt_ids:
						self.term_alt_ids[curaltid] = []
					self.term_alt_ids[curaltid].append(self.id)
				#

			elif name == 'is_obsolete':
				if self.isObsolete:
					self.isObsolete = 0
			#

			elif name == 'replaced_by':
				self.isReplacedBy = 0
				if not self.got_term:
					raise Exception
				if not self.inner_term:
					return
				currepid = self.ontology_class._name2id(self.currepid, strict = True) # modify strict to allow refs to external ontologies
				if not currepid == None:
					if self.id not in self.term_alt_ids:
						self.term_alt_ids[self.id] = []
					self.term_alt_ids[self.id].append(currepid)
			#

			elif name == 'consider':
				if self.isConsider:
					self.isConsider = 0
			#

			elif name == 'is_a':
				self.isIsA = 0
				if self.curobsolete:
					#print "Inconsistent"
					raise Exception
				if not self.inner_term:
					return
				if not self.ignore_is_a:
					isaid = self.ontology_class._name2id(self.isa)
					if not isaid == None:
						self.got_rel = True
						self.term_rel.append( (self.id, isaid, Ontology.IS_A ) )
					else:
						self.term_extra_rel.append( (self.id, self.isa, Ontology.IS_A ) )
			#

			elif name == 'part_of':
				self.isPartOf = 0
				if self.curobsolete:
					#print "Inconsistent"
					raise Exception
				if not self.inner_term:
					return
				if not self.ignore_part_of:
					partofid = self.ontology_class._name2id(self.partof)
					if not partofid == None:
						self.got_rel = True
						self.term_rel.append( (self.id, partofid, Ontology.PART_OF ) )
					else:
						self.term_extra_rel.append( (self.id, self.partof, Ontology.PART_OF ) )
			#

			elif name == 'relationship':
				if self.curobsolete:
					raise Exception
				self.isRelationship = 0
			#

			elif name == 'type':
				if self.isRelationship:
					self.isRelationshipType = 0
					#self.parent_type = ''
			#

			elif name == 'to':
				if self.isRelationshipTo:
					self.isRelationshipTo = 0
					if not self.got_term:
						raise Exception
					if self.curobsolete:
						raise Exception
					if not self.inner_term:
						return
					cto = self.ontology_class._name2id(self.parent)
					if not cto == None:
						self.got_rel = True
						if str(self.parent_type) == 'part_of' and not self.ignore_part_of:
							self.term_rel.append( (self.id, cto, Ontology.PART_OF ) )
						elif str(self.parent_type) == 'regulates' and not self.ignore_regulates:
							self.term_rel.append( (self.id, cto, Ontology.REGULATES ) )
						elif str(self.parent_type) == 'positively_regulates' and not self.ignore_regulates:
							self.term_rel.append( (self.id, cto, Ontology.POS_REG ) )
						elif str(self.parent_type) == 'negatively_regulates' and not self.ignore_regulates:
							self.term_rel.append( (self.id, cto, Ontology.NEG_REG ) )
						elif self.parent_type == 'is_a' and not self.ignore_is_a:
							self.term_rel.append( (self.id, cto, Ontology.IS_A ) )
						elif self.parent_type == 'has_part' and not self.ignore_has_part:
							self.term_rel.append( (self.id, cto, Ontology.HAS_PART ) )
					else:
						if str(self.parent_type) == 'part_of' and not self.ignore_part_of:
							self.term_extra_rel.append( (self.id, self.parent, Ontology.PART_OF ) )
						elif str(self.parent_type) == 'regulates' and not self.ignore_regulates:
							self.term_extra_rel.append( (self.id, self.parent, Ontology.REGULATES ) )
						elif str(self.parent_type) == 'positively_regulates' and not self.ignore_regulates:
							self.term_extra_rel.append( (self.id, self.parent, Ontology.POS_REG ) )
						elif str(self.parent_type) == 'negatively_regulates' and not self.ignore_regulates:
							self.term_extra_rel.append( (self.id, self.parent, Ontology.NEG_REG ) )
						elif self.parent_type == 'is_a' and not self.ignore_is_a:
							self.term_extra_rel.append( (self.id, self.parent, Ontology.IS_A ) )
						elif self.parent_type == 'has_part' and not self.ignore_has_part:
							self.term_extra_rel.append( (self.id, self.parent, Ontology.HAS_PART ) )
			#
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
#
