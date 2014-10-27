#!/bin/bash

export TEST_FILE=startfastSemSim.py

# python $TEST_FILE --go_type CellOntology -g ../../Os/CellOntology_2013.09.10.obo --go_file_format obo
# python $TEST_FILE --go_type CellOntology -g ../../Os/CellOntology_filtered_2013.09.10.obo --go_file_format obo

# python $TEST_FILE --go_type DiseaseOntology -g ../../Os/DiseaseOntology_Human_2013.09.09.obo --go_file_format obo

python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo --go_file_format obo -a examples/gene_association.mgi --ac_type gaf2
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_full_2013.09.10.obo --go_file_format obo -a examples/gene_association.mgi --ac_type gaf2
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --go_file_format obo-xml -a examples/gene_association.mgi --ac_type gaf2

# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo --go_file_format obo -a examples/gene_association.goa_human --ac_type gaf2
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_full_2013.09.10.obo --go_file_format obo -a examples/gene_association.goa_human --ac_type gaf2
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --go_file_format obo-xml -a examples/gene_association.goa_human --ac_type gaf2

# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo --go_file_format obo -a examples/gene_association.rgd --ac_type gaf2
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_full_2013.09.10.obo --go_file_format obo -a examples/gene_association.rgd --ac_type gaf2
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --go_file_format obo-xml -a examples/gene_association.rgd --ac_type gaf2

# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo --go_file_format obo -a examples/gene_association.goa_yeast --ac_type gaf2
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_full_2013.09.10.obo --go_file_format obo -a examples/gene_association.goa_yeast --ac_type gaf2
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --go_file_format obo-xml -a examples/gene_association.goa_yeast --ac_type gaf2

# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo --go_file_format obo -a examples/gene_association.goa_fly --ac_type gaf2
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_full_2013.09.10.obo --go_file_format obo -a examples/gene_association.goa_fly --ac_type gaf2
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --go_file_format obo-xml -a examples/gene_association.goa_fly --ac_type gaf2

# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo --go_file_format obo -a examples/gene_association.sgd --ac_type gaf2
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_full_2013.09.10.obo --go_file_format obo -a examples/gene_association.sgd --ac_type gaf2
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --go_file_format obo-xml -a examples/gene_association.sgd --ac_type gaf2

# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo --go_file_format obo -a examples/gene_association.fb --ac_type gaf2
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_full_2013.09.10.obo --go_file_format obo -a examples/gene_association.fb --ac_type gaf2
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --go_file_format obo-xml -a examples/gene_association.fb --ac_type gaf2

# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo --go_file_format obo -a examples/plain_ac_example.txt --ac_type plain --ac_GOfirst
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_full_2013.09.10.obo --go_file_format obo -a examples/plain_ac_example.txt --ac_type plain --ac_GOfirst
# python $TEST_FILE --go_type GeneOntology -g ../../Os/GeneOntology_filtered_2013.09.10.obo-xml.gz --go_file_format obo-xml -a examples/plain_ac_example.txt --ac_type plain --ac_GOfirst
