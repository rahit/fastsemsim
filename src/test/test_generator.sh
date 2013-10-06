#!/bin/bash

#!/bin/bash

# '''
# Copyright 2011 Marco Mina. All rights reserved.
# 
# This file is part of fastSemSim
# 
# fastSemSim is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# fastSemSim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with fastSemSim.  If not, see <http://www.gnu.org/licenses/>.
# '''

# Generate bash command lines for testing fastSemSim command line tool


# export TEST=$2

# rm $TEST
# touch $TEST

# echo "export TEST_DIR=\$1" >> $TEST
# echo "export OLD_PP=\$PYTHONPATH" >> $TEST
# echo "export PYTHONPATH=\$PYTHONPATH:\$TEST_DIR" >> $TEST
# echo "export TEST_FILE=\$TEST_DIR/startfastSemSim.py" >> $TEST

# Extensive test on
# 1- different ontologies
# 2- different ss
# 3- different mix
# 4- different ac
# 5- different query
# 6- different output

TEST_DIR=$1
TEST_FILE=${TEST_DIR}/startfastSemSim.py
export OLD_PP=$PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$TEST_DIR

GO="--o_type CellOntology"
GO="--o_type DiseaseOntology"
GO="--o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo"
GO="--o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml"
GO="--o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo --o_file_format obo"
GO=""
GO="--o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo"

AC="-a ./data/ACs/DO_human_ac_plain.txt --ac_type plain"
AC="-a ./data/ACs/DO_human_ac_gaf2.txt --ac_type gaf2"
AC="-a ./data/ACs/gene_association.goa_yeast --ac_type gaf2"
AC="-a ./data/ACs/gene_association.goa_mgi --ac_type gaf2"
AC="-a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst"
AC=""
AC="-a ./data/ACs/gene_association.goa_fly --ac_type gaf2"

QUERYTYPE="--query_ss_type term --query_type SS"
QUERYTYPE="--query_ss_type termset --query_type SS"
QUERYTYPE="--query_ss_type obj --query_type SS"
QUERYTYPE="--query_ss_type objset --query_type SS"

QUERY_INPUT="--query_input ontology"
QUERY_INPUT="--query_input ac"
QUERY_INPUT="--query_input file --query_file  ./data/query/DO_list_query.txt --query_mode list"
QUERY_INPUT="--query_input file --query_file  ./data/query/GO_fly_list_query.txt --query_mode list"
QUERY_INPUT="--query_input file --query_file  ./data/query/GO_fly_pairs_query.txt --query_mode pairs"
QUERY_INPUT="--query_input file --query_file  ./data/query/GO_fly_pairs_query.txt --query_mode list"

MIX_STRATS="--tmix BMA"
MIX_STRATS="--tmix avg"
MIX_STRATS="--tmix max"

# SSMEASURE="SimRel G-SESAME Cosine SimICND SimICNP Resnik Lin SimGIC SimUI Jiang-Conrath SimIC Dice TO NTO Jaccard Czekanowski-Dice"
SSMEASURE="--tss SimRel"
SSMEASURE="--tss G-SESAME"
SSMEASURE="--tss Cosine"
SSMEASURE="--tss SimICND"
SSMEASURE="--tss SimICNP"
SSMEASURE="--tss Resnik"
SSMEASURE="--tss Lin"
SSMEASURE="--tss SimUI"
SSMEASURE="--tss SimIC"
SSMEASURE="--tss Dice"
SSMEASURE="--tss Jiang-Conrath"
SSMEASURE="--tss Czekanowski-Dice"
SSMEASURE="--tss Jaccard"
SSMEASURE="--tss NTO"
SSMEASURE="--tss TO"
SSMEASURE=""
SSMEASURE="--tss SimGIC"

# VERBOSITY=""
# VERBOSITY="-vv"
# VERBOSITY="-vvv"
# VERBOSITY="-vvvv"
VERBOSITY="-v"


OUTF=""
OUTF="--out_file test_output.txt"


echo python $TEST_FILE ${GO} ${AC} ${SSMEASURE} ${MIX_STRATS} ${QUERYTYPE} ${QUERY_INPUT} ${VERBOSITY} ${OUTF}


# # SS # termset
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss "Jiang and Conrath" --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --query_type SS --query_ss_type term


# # SS # obj
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss "Jiang and Conrath" --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --query_type SS --query_ss_type term


# # SS # objset
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss "Jiang and Conrath" --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --query_type SS --query_ss_type term
# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --query_type SS --query_ss_type term

# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss "Jiang and Conrath" --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --query_type SS --query_ss_type term
# python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --query_type SS --query_ss_type term

# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss SimRel --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss G-SESAME --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss Cosine --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss SimICND --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss SimICNP --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss Resnik --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss Lin --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss SimGIC --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss SimUI --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss "Jiang and Conrath" --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss SimIC --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss Dice --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss TO --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss NTO --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss Jaccard --query_type SS --query_ss_type term
# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss Czekanowski-Dice --query_type SS --query_ss_type term

# python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain

# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2
# # python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml -a ./data/ACs/gene_association.mgi --ac_type gaf2

# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.goa_human --ac_type gaf2
# # python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml -a ./data/ACs/gene_association.goa_human --ac_type gaf2

# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.rgd --ac_type gaf2
# # python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml -a ./data/ACs/gene_association.rgd --ac_type gaf2

# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.goa_yeast --ac_type gaf2
# # python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml -a ./data/ACs/gene_association.goa_yeast --ac_type gaf2

# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.goa_fly --ac_type gaf2
# # python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml -a ./data/ACs/gene_association.goa_fly --ac_type gaf2

# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.sgd --ac_type gaf2
# # python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml -a ./data/ACs/gene_association.sgd --ac_type gaf2

# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.fb --ac_type gaf2
# # python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml -a ./data/ACs/gene_association.fb --ac_type gaf2

# python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst
# # python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst


export PYTHONPATH=$OLD_PP
