# -*- coding: iso-8859-1 -*-

# Copyright 2011 Marco Mina. All rights reserved.

# This file is part of fastSemSim

# fastSemSim is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# fastSemSim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with fastSemSim.  If not, see <http://www.gnu.org/licenses/>.


'''
This class provides the prototype for Term semantic similarity measures (TSS)

There are two types of Term semantic similarity: a first group that can evaluate the semantic similarity between two sets of terms (groupwise - G_TSS), and a second group that can only evaluate the similarity between pairs of GO terms (pairwise - P_TSS). Each class extending TermSemSim should declare whether it is groupwise or pairwise.

TermSemSim relies on SemSimUtils to perform a lot of tasks (e.g. evaluating Term IC or common ancestors).
A SemSimUtils object can be passed to the constructor as input data. Otherwise, a new instance will be created. Using only one copy of SemSimUtils helps reducing time and space requirements and is strongly recommended.
'''

from __future__ import print_function
import sys
import os
import math
import pandas as pd

try:
	unicode
except (NameError, AttributeError):
	unicode = str #For python3

	#-#-#-#-#-#-#-#-#-#-#
	# class TermSemSim  #
	#-#-#-#-#-#-#-#-#-#-#



class BatchSemSim(object):
	verbose = True

	def __init__(self, semsim, root = None):
		self.semsim = semsim
		self.set_root(root)
		self.set_output(output = None)
	#

	def set_root(self, root=None):
		if isinstance(root, None.__class__):
			root = list(self.semsim.ontology.roots.keys())[0]
		if not root in self.semsim.ontology.roots:
			raise Exception(str(root) + " is not an ontology root.")
		self.root = root
	#

	def set_output(self, output = None, output_params = None):
		'''
		Set the output of a BatchSemSim
		'''
		if isinstance(output, None.__class__): # output is returned as returning variable
			pass
		elif output == 'file': # output is saved to file.
			if isinstance(output_params, str): # Output file
				self.output_file = output_params
			else:
				raise Exception('Uknown ' + 'output_file format.')	
		elif output == 'iterator': # output is saved to file.
			pass
		else:
			raise Exception('Uknown ' + str(output) + ' output format.')
		self.output = output
	#

	# def SemSim(self, term1, term2, root = None):
	# 	'''
	# 	Passthrough function. Invokes directly the SemSim function of the ss object.
	# 	Parameters as in the general SemSim function.
	# 	'''
	# 	if isinstance(root, None.__class__):
	# 		root = self.root
	# 	#
	# 	return self.semsim.SemSim(term1, term2, root = root)
	#


	class Query:
		def __init__(self, query, query_type='pairs', skip_self_similarity=False):
			self.query = query
			self.query_type = query_type
			self.skip_self_similarity = skip_self_similarity
			self.n = len(self.query)
		#

		def len(self):
			if self.query_type == 'pairs':
				return(self.n)
			elif self.query_type == 'pairwise':
				if self.skip_self_similarity == True: # do or do not skip self score
					return((self.n * (self.n - 1))/2)
				#
				return(self.n + (self.n * (self.n - 1))/2)
			elif self.query_type == 'bipartite':
				return(len(self.query[0]) * len(self.query[1]))
			else:
				raise Exception('Unsupported query type:'+str(self.query_type))
		#

		def __iter__(self):
			self.i = 0
			self.j = 0
			if self.skip_self_similarity == True: # do or do not skip self score
				self.j += 1
			return self

		def __next__(self):
			if self.query_type == 'pairs':
				if self.i < self.n:
					i = self.i
					self.i += 1
					return self.query[i]
				else:
					raise StopIteration()
			elif self.query_type == 'pairwise':
				if self.j == self.n: # move to next i
					self.i += 1
					self.j = self.i
					if self.skip_self_similarity == True: # do or do not skip self score
						self.j += 1
				if self.i < self.n and self.j < self.n: # still have some calculations to do
					i = self.i
					j = self.j
					self.j += 1
					return [self.query[i], self.query[j]]
				else:
					raise StopIteration()
			elif self.query_type == 'bipartite':
				if self.j == len(self.query[1]):
					self.i += 1
					self.j = 0
				if self.i == len(self.query[0]):
					raise StopIteration()
				i = self.i
				j = self.j
				self.j += 1
				return [self.query[0][i], self.query[1][j]]
			else:
				raise Exception('Unsupported query type:'+str(self.query_type))
		#
	#


	# test & debug example
	# q = [['O75884', 'Q9NQB0'], ['Q14206', 'Q8IUH3' ]]
	# q2 = ['O75884', 'Q9NQB0', 'Q14206', 'Q8IUH3' ]
	# a = Query(q, query_type = 'pairs')
	# a2 = Query(q2, query_type = 'pairwise')
	# a2b = Query(q2, query_type = 'pairwise', skip_self_similarity=True)

	def SemSim(self, query, query_type='pairs', root=None):
		'''
		Batch Pairwise Semantic Similarity.
		Calculate Semantic similarity in batch mode overmultiple pairs of objects/terms.

		Parameters
		----------
			query: list 
				List of pairs or list of objects or terms or objsets or termsets

			query_type: str
				Type of query. Can be 'pairs' if the list contains pairs of elements to consider; 'pairwise' if the list is a vector of elements for which the SS has to be calculated in a pairwsie fashion; 'bipartite' if the list contains two lists of element. In this case all the pairwise SS between elements of list 1 and list 2 will be calculated.

			root: str, optional
				The root of the ontolgoy to consider. If set to None, the first root (and possibly the only one) will be used.

		Returns
		------------
			Pandas DataFrame with all the SS.

		'''

		if isinstance(root, None.__class__):
			root = self.root
		#

		query_it = self.Query(query, query_type, skip_self_similarity=False)

		done = 0
		total = query_it.len()
		prev_text = ""

		templist = []
		temptab = pd.DataFrame(columns=['obj_1','obj_2','ss'])

		if self.output == 'iterator':
			raise Exception('Iterator not implemented yet.')
		elif self.output == 'file':
			chunk_size = 2000
			temptab.to_csv(self.output_file, sep="\t", header=True, index=False)
		# else:
			# pass

		if self.verbose == True:
			sys.stdout.flush() # <- why?

		for current_query in query_it:
			temp = self.semsim.SemSim(current_query[0], current_query[1], root = self.root)
			# if temp is None and params['core']['verbose'] >= 4:
				# print(self.semsim.log)
			# if not params['output']['cut_thres'] is None:
				# if temp is None or temp <= params['output']['cut_thres']:
					# continue
				# if params['output']['cut_nan']:
					# if temp is None:
						# continue

			# temp = pd.DataFrame([[current_query[0], current_query[1], temp],], columns=['obj_1','obj_2','ss']) # way slower!
			temp = [current_query[0], current_query[1], temp]
			templist.append(temp)
			
			if self.output == 'file':
				if len(templist) >= chunk_size:
					temptab = pd.DataFrame(templist, columns=['obj_1','obj_2','ss'])
					# temptab = pd.concat(templist, sort=False, ignore_index=True) # way slower!
					templist = []
					temptab.to_csv(self.output_file, sep="\t", header=False, index=False)
					temptab = pd.DataFrame(columns=['obj_1','obj_2','ss'])
				#
			elif isinstance(self.output, None.__class__):
				pass
			#

			done+=1
			if self.verbose == True:
				sys.stdout.write("\b"*len(prev_text))
				prev_text = str(done) + ' [%.4f' % (100*done/float(total)) + " %]"
				sys.stdout.write(prev_text)
				sys.stdout.flush()

		# collect output
		if len(templist)>0:
			temptab = pd.DataFrame(templist, columns=['obj_1','obj_2','ss'])
			# temptab = pd.concat(templist, sort=False, ignore_index=True) # way slower!
			templist = []

		if self.output == 'file':
			temptab.to_csv(self.output_file, sep="\t", header=False, index=False)
			temptab = None

		return temptab
	#

	def build_query_from_ac(self):
		query = self.semsim.ac.annotations.keys()
		return(query)
	#

	def build_query_from_ontology(self):
		# query = self.semsim.ac.reverse_annotations.keys()
		query = self.semsim.ontology.nodes.keys()
		return(query)
	#

	def build_query_from_file(self, query_file, params={}):
		h = open(query_file,'r')
		query = []
		for line in h:
			line = line.rstrip('\n')
			line = line.rstrip('\r')
			line = line.split(params['query_file_sep'])
			if params['query_ss_type'] == 'obj' or params['query_ss_type'] == 'term':
				if params['query_mode'] == 'pairs':
					if len(line) < 2:
						continue
					for i in range(0,len(line)):
						for j in range(i+1,len(line)):
							query.append((line[i], line[j]))
				elif params['query_mode'] == 'list':
					for i in line:
						query.append(i)
				else:
					raise Exception(bug_msg)
			elif params['query_ss_type'] == 'objset' or params['query_ss_type'] == 'termset':
				if params['query_mode'] == 'pairs':
					raise Exception('For objsets, cannot load set pairs from single lines of a query file.')
				elif params['query_mode'] == 'list':
					newline = []
					for i in line:
						newline.append(i)
					query.append(newline)
				else:
					raise Exception()
			else:
				raise Exception()
		h.close() # ! This remains open in case of an Exception gets thrown
		return query
	#




	# def det_ss():
	# 	'''
	# 	Determine SS
	# 	'''
	# 	global params, ss

	# 	if params['core']['verbose'] >= 2:
	# 		print("-----------------------------------------------")
	# 		print('-> Evaluating Semantic Similarity...')
	# 	h = None
	# 	if not isinstance(params['output']['out_file'], None.__class__):
	# 		if params['core']['verbose'] >= 2:
	# 			print('Saving SS in file ' + str(params['output']['out_file']))
	# 		h = open(params['output']['out_file'], 'w')
	# 	if params['query_mode'] == 'pairs':
	# 		ss_pairs(h)
	# 	elif params['query_mode'] == 'list':
	# 		ss_pairwise(h)
	# 	else:
	# 		raise Exception
	# 	if not h is None:
	# 		h.close()
	# 	if params['core']['verbose'] >= 2:
	# 		print("-----------------------------------------------")
	# 	# if params['ss']['use_enhanced']:
	# 		# raise Exception
	# 		# ss_pairwise_enhanced(SS, query, ontology, h, cut_thres, cut_nan)
	# #


	
