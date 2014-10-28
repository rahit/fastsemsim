# ./fastSemSim.sh  -o ../../Os/GeneOntology_full_2014.09.09.obo --ontology_type GeneOntology -a test/data/ACs/gene_association.goa_yeast --tss SimGIC --query_input ontology --query_ss_type term

from fastSemSim.Ontology import ontologies
from fastSemSim.Ontology import AnnotationCorpus
import sys
import os
import math
import gzip
import argparse
import pandas as pd

go = ontologies.load('../../Os/GeneOntology_full_2014.09.09.obo', source_type = 'obo', ontology_type = 'GeneOntology')

reload(AnnotationCorpus)
ac = AnnotationCorpus.AnnotationCorpus(go)
ac.parse( './test/data/ACs/gene_association.goa_yeast', 'GOA')
dati_pd = pd.read_csv('./test/data/ACs/gene_association.goa_yeast', sep="\t", skiprows=1, header=-1, index_col=False)
dati_pd.columns = ['db','id','name','?','term','pmid','evidence','?','object type','name again','alias','obj type','taxonomy','date?','source db?','?','?']

# from previous gaf-2 parser
	# self.temp_taxonomy = line[12][6:]
	# temp = self.temp_taxonomy.rsplit('|')
	# if len(temp) > 1:
	# 	self.temp_taxonomy = temp[0]
	# self.temp_obj = line[1]
	# self.temp_term = line[4]
	# self.temp_EC = line[6]
	# self.temp_reference = line[5]
	# self.temp_GO = line[8]
