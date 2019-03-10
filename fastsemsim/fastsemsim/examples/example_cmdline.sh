#/bin/bash

# This command line runs fastsemsim comman-line with the parameters in file example_cmdline_params.

fastsemsim --load_params example_cmdline_params.txt

# The previous command is equivalent to running the following command:
# fastsemsim -vvv --task SS -o GeneOntology --ac fly  --query_input file --query_mode pairs --query_ss_type obj  --ontology_ignore positively_regulates --ontology_ignore negatively_regulates --ontology_ignore regulates --cut 0.9 --query_file data/GO_fly_pairs_query.txt  --tss Resnik --tmix BMA --root biological_process --ignore_EC TAS --query_file_sep "   "

# The file example_cmdline_params.txt was automatically built by fastSemSim by running this line adding the parameter  --save_params example_cmdline_params.txt:
# fastsemsim -vvv --task SS -o GeneOntology --ac fly  --query_input file --query_mode pairs --query_ss_type obj  --ontology_ignore positively_regulates --ontology_ignore negatively_regulates --ontology_ignore regulates --cut 0.9 --query_file data/GO_fly_pairs_query.txt  --tss Resnik --tmix BMA --root biological_process --ignore_EC TAS --query_file_sep "   " --save_params example_cmdline_params.txt



fastsemsim --ontology_type GeneOntology --query_ss_type obj --tss Resnik --mix BMA --query_input ac --ac_species human  -vv --root molecular_function
fastsemsim --ontology_type GeneOntology --query_ss_type obj --tss Resnik --mix BMA --query_input ac --ac_species human  -vv --root molecular_function --remove_nan
fastsemsim --ontology_type DiseaseOntology --query_ss_type obj --tss Resnik --mix BMA --query_input ac --ac_species human  -vv --output_file temp.txt --remove_nan

fastsemsim --ontology_type DiseaseOntology --query_ss_type term --tss Resnik --mix BMA --query_input ontology --ac_species human  -vv --output_file temp.txt --remove_nan

fastsemsim --ontology_type DiseaseOntology --ac_species human  -vv --task stats
fastsemsim --ontology_type GeneOntology --ac_species human  -vv --task stats


fastsemsim --ontology_type DiseaseOntology --ac_species human  -vv --task stats --save_params example_cmdline_params.txt
fastsemsim  --load_params example_cmdline_params.txt