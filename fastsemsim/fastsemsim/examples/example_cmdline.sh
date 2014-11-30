

# fastsemsim -vvv --task SS -o GeneOntology --ac fly  --query_input file --query_mode pairs --query_ss_type obj  --ontology_ignore positively_regulates --ontology_ignore negatively_regulates --ontology_ignore regulates --cut 0.9 --query_file data/GO_fly_pairs_query.txt  --tss Resnik --tmix BMA --root biological_process --ignore_EC TAS --query_file_sep "   " --save_params example_cmdline_params.txt

fastsemsim --load_params example_cmdline_params.txt


