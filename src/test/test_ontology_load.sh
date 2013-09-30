#!/bin/bash

export TEST_DIR=$1
export OLD_PP=$TEST_DIR
export PYTHONPATH=$TEST_DIR:$1
export TEST_FILE=test_ontology_load.py
# export TEST_FILE=$TEST_DIR/startfastSemSim.py

python $TEST_FILE --o_type CellOntology -o ./data/Os/CellOntology_2013.09.10.obo --o_file_format obo
python $TEST_FILE --o_type CellOntology -o ./data/Os/CellOntology_filtered_2013.09.10.obo --o_file_format obo

python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo

python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo --o_file_format obo
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml

python $TEST_FILE --o_type Ontology -o ./data/Os/CellOntology_2013.09.10.obo --o_file_format obo
python $TEST_FILE --o_type Ontology -o ./data/Os/CellOntology_filtered_2013.09.10.obo --o_file_format obo

python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo

python $TEST_FILE --o_type Ontology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo --o_file_format obo
python $TEST_FILE --o_type Ontology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo
python $TEST_FILE --o_type Ontology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml

export PYTHONPATH=$OLD_PP