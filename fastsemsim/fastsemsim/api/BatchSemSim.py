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

	def SemSim(self, term1, term2, root = None):
		'''
		Passthrough function. Invokes directly the SemSim function of the ss object.
		Parameters as in the general SemSim function.
		'''
		if isinstance(root, None.__class__):
			root = self.root
		#
		return self.semsim.SemSim(term1, term2, root = root)
	#


	def semsim_pairs(self, query):
		'''
		Pairwise Semantic Similarity

		Parameters
		----------
			query: list or record of pairs of objects or terms or objsets or termsets


		'''

		done = 0
		total = len(query)
		prev_text = ""

		if self.output == 'iterator':
			raise Exception('Iterator not implemented yet.')
		elif self.output == 'file':
			chunk_size = 2000
			temptab = pd.DataFrame(columns=['obj_1','obj_2','ss'])
			temptab.to_csv(self.output_file, sep="\t", header=True, index=False)
		else:
			temptab = pd.DataFrame(columns=['obj_1','obj_2','ss'])
		
		if self.verbose == True:
			sys.stdout.flush() # <- why?

		for i in range(0,len(query)):
			temp = self.semsim.SemSim(query[i][0], query[i][1], root = self.root)
			# if temp == None and params['core']['verbose'] >= 4:
				# print(self.semsim.log)
			done+=1
			# if not params['output']['cut_thres'] == None:
				# if temp == None or temp <= params['output']['cut_thres']:
					# continue
				# if params['output']['cut_nan']:
					# if temp == None:
						# continue
			if self.output == 'file':
				# print(str(query[i][0]) + "\t" + str(query[i][1]) + "\t" + str(temp))
				temptab.loc[i] = [query[i][0], query[i][1], temp]
				if temptab.shape[0] >= chunk_size:
					temptab.to_csv(self.output_file, sep="\t", header=False, index=False)
					temptab = pd.DataFrame(columns=['obj_1','obj_2','ss'])
				#
			elif isinstance(self.output, None.__class__):
				temptab.loc[i] = [query[i][0], query[i][1], temp]
			#
			if self.verbose == True:
				sys.stdout.write("\b"*len(prev_text))
				prev_text = str(done) + ' [%.4f' % (100*done/float(total)) + " %]"
				sys.stdout.write(prev_text)
				sys.stdout.flush()

		if self.output == 'file':
			temptab.to_csv(self.output_file, sep="\t", header=False, index=False)
			temptab = None

		return temptab
	#



		#-#-#-#-#-#-#-#-#-#-#
		# Pairwise Sem Sim  #
		#-#-#-#-#-#-#-#-#-#-#
	def semsim_list(self, query):
		'''
		List Semantic Similarity
		'''
		scores = {}
		done = 0
		total = len(query)*(len(query)+1)/2

		if not self.out == None:
			if params['core']['verbose'] >= 0:
				print("Evluating pairwise semantic similarity between " + str(len(query)) + " entities (" + str(len(query)*(len(query)+1)/2) + " pairs)")
				prev_text = ""
				sys.stdout.write("Done: ")
			chunk_size = 2000
			temptab = pd.DataFrame(columns=['obj_1','obj_2','ss'])
			temptab.to_csv(self.out, sep="\t", header=True, index=False)
		sys.stdout.flush()
		for i in range(0,len(query)):
			# if params['query_ss_type'] == 'obj':
			# scores[pairs[i]] = {}
			for j in range(i,len(query)):
				temp = self.semsim.SemSim(query[i],query[j],params['ss']['ss_root'])
				if temp == None and params['core']['verbose'] >= 4:
					print(self.semsim.log)
				#scores[pairs[i]][pairs[j]] = temp
				done+=1
				if not params['output']['cut_thres'] == None:
					if temp == None or temp <= params['output']['cut_thres']:
						continue
				if params['output']['cut_nan']:
					if temp == None:
						continue
				if self.out == None:
					print(str(query[i]) + "\t" + str(query[j]) + "\t" + str(temp))
				else:
					# print(temptab)
					# print(i*(len(query))+j)
					temptab.loc[i*(len(query))+j] = [query[i], query[j], temp]
					if temptab.shape[0] >= chunk_size:
						temptab.to_csv(self.out, sep="\t", header=False, index=False)
						temptab = pd.DataFrame(columns=['obj_1','obj_2','ss'])
					if params['core']['verbose'] >= 0:
						sys.stdout.write("\b"*len(prev_text))
						prev_text = str(done) + ' [%.4f' % (100*done/float(total)) + " %]"
						sys.stdout.write(prev_text)
						sys.stdout.flush()
		if not self.out is None:
			temptab.to_csv(self.out, sep="\t", header=False, index=False)
		return scores
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
	# 	if not h == None:
	# 		h.close()
	# 	if params['core']['verbose'] >= 2:
	# 		print("-----------------------------------------------")
	# 	# if params['ss']['use_enhanced']:
	# 		# raise Exception
	# 		# ss_pairwise_enhanced(SS, query, ontology, h, cut_thres, cut_nan)
	# #


	
