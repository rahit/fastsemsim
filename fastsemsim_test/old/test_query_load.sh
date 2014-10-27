#!/bin/bash

export TEST_DIR=$1
export OLD_PP=$TEST_DIR
export PYTHONPATH=$TEST_DIR:$1
export TEST_FILE=test_query_load.py
# export TEST_FILE=$TEST_DIR/startfastSemSim.py

# SS

# SS # file 

# SS # file # list # term
python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --query_type SS --query_ss_type term --query_mode list --query_input file --query_file ./data/fly_list_example.txt
python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo-xml -a ./data/ACs/gene_association.goa_human --ac_type gaf2 --query_type SS --query_ss_type term --query_mode list --query_input file --query_file  ./data/fly_list_example.txt
python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst --query_type SS --query_ss_type term --query_mode list --query_input file --query_file  ./data/fly_list_example.txt
python $TEST_FILE --o_type DiseaseOntology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type term --query_mode list --query_input file --query_file  ./data/fly_list_example.txt
python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type term --query_mode list --query_input file --query_file  ./data/fly_list_example.txt

# SS # file # pairs # term
python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --query_type SS --query_ss_type term --query_mode pairs --query_input file --query_file ./data/fly_pairs_example.txt
python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo-xml -a ./data/ACs/gene_association.goa_human --ac_type gaf2 --query_type SS --query_ss_type term --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt
python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst --query_type SS --query_ss_type term --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt
python $TEST_FILE --o_type DiseaseOntology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type term --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt
python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type term --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt

# SS # file # list # obj
python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --query_type SS --query_ss_type obj --query_mode list --query_input file --query_file ./data/fly_list_example.txt
python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo-xml -a ./data/ACs/gene_association.goa_human --ac_type gaf2 --query_type SS --query_ss_type obj --query_mode list --query_input file --query_file  ./data/fly_list_example.txt
python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst --query_type SS --query_ss_type obj --query_mode list --query_input file --query_file  ./data/fly_list_example.txt
python $TEST_FILE --o_type DiseaseOntology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type obj --query_mode list --query_input file --query_file  ./data/fly_list_example.txt
python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type obj --query_mode list --query_input file --query_file  ./data/fly_list_example.txt

# SS # file # pairs # obj
python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --query_type SS --query_ss_type obj --query_mode pairs --query_input file --query_file ./data/fly_pairs_example.txt
python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo-xml -a ./data/ACs/gene_association.goa_human --ac_type gaf2 --query_type SS --query_ss_type obj --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt
python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst --query_type SS --query_ss_type obj --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt
python $TEST_FILE --o_type DiseaseOntology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type obj --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt
python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type obj --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt

# SS # file # list # termset
python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --query_type SS --query_ss_type termset --query_mode list --query_input file --query_file ./data/fly_list_example.txt
python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo-xml -a ./data/ACs/gene_association.goa_human --ac_type gaf2 --query_type SS --query_ss_type termset --query_mode list --query_input file --query_file  ./data/fly_list_example.txt
python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst --query_type SS --query_ss_type termset --query_mode list --query_input file --query_file  ./data/fly_list_example.txt
python $TEST_FILE --o_type DiseaseOntology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type termset --query_mode list --query_input file --query_file  ./data/fly_list_example.txt
python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type termset --query_mode list --query_input file --query_file  ./data/fly_list_example.txt

# SS # file # pairs # termset
# python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --query_type SS --query_ss_type termset --query_mode pairs --query_input file --query_file ./data/fly_pairs_example.txt
# python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo-xml -a ./data/ACs/gene_association.goa_human --ac_type gaf2 --query_type SS --query_ss_type termset --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt
# python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst --query_type SS --query_ss_type termset --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt
# python $TEST_FILE --o_type DiseaseOntology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type termset --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt
# python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type termset --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt

# SS # file # list # objset
python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --query_type SS --query_ss_type objset --query_mode list --query_input file --query_file ./data/fly_list_example.txt
python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo-xml -a ./data/ACs/gene_association.goa_human --ac_type gaf2 --query_type SS --query_ss_type objset --query_mode list --query_input file --query_file  ./data/fly_list_example.txt
python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst --query_type SS --query_ss_type objset --query_mode list --query_input file --query_file  ./data/fly_list_example.txt
python $TEST_FILE --o_type DiseaseOntology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type objset --query_mode list --query_input file --query_file  ./data/fly_list_example.txt
python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type objset --query_mode list --query_input file --query_file  ./data/fly_list_example.txt

# SS # file # pairs # objset
# python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --query_type SS --query_ss_type objset --query_mode pairs --query_input file --query_file ./data/fly_pairs_example.txt
# python $TEST_FILE --o_type GeneOntology -o None --o_file_format obo-xml -a ./data/ACs/gene_association.goa_human --ac_type gaf2 --query_type SS --query_ss_type objset --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt
# python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst --query_type SS --query_ss_type objset --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt
# python $TEST_FILE --o_type DiseaseOntology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type objset --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt
# python $TEST_FILE --o_type Ontology -o None --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type objset --query_mode pairs --query_input file --query_file  ./data/fly_pairs_example.txt


# SS # term # list

# SS # term # list # ontology
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --query_type SS --query_ss_type term --query_mode list --query_input ontology
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml -a ./data/ACs/gene_association.goa_human --ac_type gaf2 --query_type SS --query_ss_type term --query_mode list --query_input ontology
# python $TEST_FILE --o_type Ontology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst --query_type SS --query_ss_type term --query_mode list --query_input ontology
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type term --query_mode list --query_input ontology
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type term --query_mode list --query_input ontology

# SS # term # list # ac
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --query_type SS --query_ss_type term --query_mode list --query_input ac
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml -a ./data/ACs/gene_association.goa_human --ac_type gaf2 --query_type SS --query_ss_type term --query_mode list --query_input ac
# python $TEST_FILE --o_type Ontology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst --query_type SS --query_ss_type term --query_mode list --query_input ac
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type term --query_mode list --query_input ac
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type term --query_mode list --query_input ac

# SS # obj # list

# SS # obj # list # ontology
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --query_type SS --query_ss_type obj --query_mode list --query_input ontology
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml -a ./data/ACs/gene_association.goa_human --ac_type gaf2 --query_type SS --query_ss_type obj --query_mode list --query_input ontology
# python $TEST_FILE --o_type Ontology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst --query_type SS --query_ss_type obj --query_mode list --query_input ontology
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type obj --query_mode list --query_input ontology
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type obj --query_mode list --query_input ontology

# SS # obj # list # ac
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --query_type SS --query_ss_type obj --query_mode list --query_input ac
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml -a ./data/ACs/gene_association.goa_human --ac_type gaf2 --query_type SS --query_ss_type obj --query_mode list --query_input ac
# python $TEST_FILE --o_type Ontology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst --query_type SS --query_ss_type obj --query_mode list --query_input ac
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type obj --query_mode list --query_input ac
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type SS --query_ss_type obj --query_mode list --query_input ac

# stats
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --query_type stats
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --o_file_format obo-xml -a ./data/ACs/gene_association.goa_human --ac_type gaf2 --query_type stats
python $TEST_FILE --o_type Ontology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/plain_GO_ac_example.txt --ac_type plain --ac_termfirst --query_type stats
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type stats
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --query_type stats


export PYTHONPATH=$OLD_PP
