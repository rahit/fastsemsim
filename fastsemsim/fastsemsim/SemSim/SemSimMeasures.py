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

from fastSemSim.SemSim.ResnikSemSim import *
from fastSemSim.SemSim.LinSemSim import *
from fastSemSim.SemSim.JiangConrathSemSim import *
from fastSemSim.SemSim.SimGICSemSim import *
from fastSemSim.SemSim.SimUISemSim import *
from fastSemSim.SemSim.SimICSemSim import *
from fastSemSim.SemSim.SimRelSemSim import *
from fastSemSim.SemSim.avgSemSim import *
from fastSemSim.SemSim.maxSemSim import *
from fastSemSim.SemSim.BMASemSim import *
from fastSemSim.SemSim.DiceSemSim import *
from fastSemSim.SemSim.SimTOSemSim import *
from fastSemSim.SemSim.SimNTOSemSim import *
from fastSemSim.SemSim.JaccardSemSim import *
from fastSemSim.SemSim.CzekanowskiDiceSemSim import *
from fastSemSim.SemSim.CosineSemSim import *
from fastSemSim.SemSim.GSESAMESemSim import *
from fastSemSim.SemSim.SimICNDSemSim import *
from fastSemSim.SemSim.SimICNPSemSim import *
# from fastSemSim.SemSim.ObjSemSim import *
# from fastSemSim.SemSim.TermSemSim import *

'''
Struct term_SemSim_measures.
Contains a list of all available term SS measures.
It is built as a dictionary. SS measure names are used as keys. Each entry is a tuple with the following structure:
(Class Name, is Pairwise flag, )
'''
term_SemSim_measures = {
# present in version 0.6
	'Resnik' : (ResnikSemSim, True),
	'SimGIC': (SimGICSemSim, False),
	'SimUI': (SimUISemSim, False),
	'Lin' :(LinSemSim, True),
	'Jiang-Conrath' :(JiangConrathSemSim, True),
	'SimRel' :(SimRelSemSim, True),
	'SimIC' :(SimICSemSim, True),
	'Dice' :(DiceSemSim, False),
	'TO' :(SimTOSemSim, False),
	'NTO' :(SimNTOSemSim, False),
	'Jaccard' :(JaccardSemSim, False),
	'Czekanowski-Dice' :(CzekanowskiDiceSemSim, False),
	'Cosine' :(CosineSemSim, False),
	'G-SESAME' :(GSESAMESemSim, True),
	'SimICND' :(ICNDSemSim, True),
	'SimICNP' :(ICNPSemSim, True),
# new in version 0.7
	#'Cosine' :(CosineSemSim, False),
}


'''
Struct mix_strategies.
Contains a list of all available mixing strategies
It is built as a dictionary. Mixing strategy names are used as keys. Each entry is a tuple with the following structure:
(class pointer, )
'''
mix_strategies = {
	'max':(maxSemSim, ),
	'BMA':(BMASemSim, ),
	'avg':(avgSemSim, )
}

# '''
# Struct obj_SemSim_measures.
# Contains a list of all available obj sem sim measures
# It is built as a dictionary. Mixing strategy names are used as keys. Each entry is a tuple with the following structure:
# (class pointer, )
# '''
# obj_SemSim_measures = {
# 	'obj':(ObjSemSim)
# }

	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# select Term Sem Sim     #
	#-#-#-#-#-#-#-#-#-#-#-#-#-#

	# the function selectTermSemSim helps retrieving the proper class implementing a given Term Sem Sim.
	# It takes in input the name (str) of the Term Sem Similarity
	# It returns the class to be used. Just call the class constructor to instantiante an object.

def select_term_SemSim(tss_name):
	if not tss_name in term_SemSim_measures:
		raise "Semantic Similarity measure not available."
		return None
	else:
		return term_SemSim_measures[tss_name][0]
#

def select_mix_SemSim(mix_name):
	if not mix_name in mix_strategies:
		raise "Semantic Similarity measure not available."
		return None
	else:
		return mix_strategies[mix_name][0]
#

# def select_obj_SemSim(oss_name='obj'):
# 	if not oss_name in obj_SemSim_measures:
# 		raise "Semantic Similarity measure not available."
# 		return None
# 	else:
# 		return obj_SemSim_measures[oss_name][0]
# #
