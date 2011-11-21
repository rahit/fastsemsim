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
along with fastfastSemSim.SemSim.  If not, see <http://www.gnu.org/licenses/>.
'''

from fastSemSim.SemSim.ResnikSemSim import *
from fastSemSim.SemSim.LinSemSim import *
from fastSemSim.SemSim.JiangConrathSemSim import *
from fastSemSim.SemSim.SimGICSemSim import *
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

'''
Struct SemSimMeasures.
Contains a list of all available SS measures.
It is built as a dictionary. SS measure names are used as keys. Each entry is a tuple with the following structure:
(class pointer, Pairwise flag, )
'''
SemSimMeasures = {
'Resnik' : (ResnikSemSim, True),
'SimGIC': (SimGICSemSim, False),
'Lin' :(LinSemSim, True),
'Jiang and Conrath' :(JiangConrathSemSim, True),
'SimIC' :(SimICSemSim, True),
'Dice' :(DiceSemSim, False),
'TO' :(SimTOSemSim, False),
'NTO' :(SimNTOSemSim, False),
'Jaccard' :(JaccardSemSim, False),
'Czekanowski-Dice' :(CzekanowskiDiceSemSim, False),
'Cosine' :(CosineSemSim, False),
'G-SESAME' :(GSESAMESemSim, True)

}

'''
Struct MixingStrategies.
Contains a list of all available mixing strategies
It is built as a dictionary. Mixing strategy names are used as keys. Each entry is a tuple with the following structure:
(class pointer, )
'''
MixingStrategies = {
'max':(maxSemSim),
'BMA':(BMASemSim),
'avg':(avgSemSim)
}
