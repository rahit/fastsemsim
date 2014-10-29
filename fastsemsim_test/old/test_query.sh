#!/bin/bash

export TEST_DIR=$1
export OLD_PP=$TEST_DIR
export PYTHONPATH=$TEST_DIR:$1
export TEST_FILE=test_query.py
# export TEST_FILE=$TEST_DIR/startfastSemSim.py

# SS # term
# for i in `echo max BMA avg`; do 
for i in `echo max`; do 
	MIX="--tmix "$i
	for j in `echo objset termset term obj`; do 
		SSTYPE="--query_ss_type "$j
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss "Jiang and Conrath" $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard $MIX --query_type SS $SSTYPE
		python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice $MIX --query_type SS $SSTYPE
	done
done

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
