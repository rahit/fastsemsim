#!/bin/bash

export TEST_DIR=$1
export OLD_PP=$TEST_DIR
export PYTHONPATH=$TEST_DIR:$1
export TEST_FILE=test_term_ss.py
# export TEST_FILE=$TEST_DIR/startfastSemSim.py


python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss SimRel
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss G-SESAME
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss Cosine
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss SimICND
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss SimICNP

python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss Resnik
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss Lin
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss SimGIC
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss SimUI
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss "Jiang and Conrath"
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss SimIC
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss Dice
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss TO
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss NTO
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss Jaccard
python $TEST_FILE --o_type GeneOntology -o ./data/Os/GeneOntology_full_2013.09.10.obo --o_file_format obo -a ./data/ACs/gene_association.mgi --ac_type gaf2 --tss Czekanowski-Dice

python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP

python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss "Jiang and Conrath"
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice

python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP

python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss "Jiang and Conrath"
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard
python $TEST_FILE --o_type DiseaseOntology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice



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
