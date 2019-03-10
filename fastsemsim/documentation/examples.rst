Examples and use cases
======================================================

In this section real example code and use case scenarios are proposed.

Loading the Gene Ontology
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example the Gene Ontology embedded in FastSemSim is loaded.
The quick example loads the Gene Ontology in one simple call. The more complete example explores some of the parameters that can be used. 

Please refer to the FastSemSim API section for a detailed description of the function to load ontologies.

The complete example code is available in the file fastsemsim/examples/load_ontology.py within the source tarball of FastSemSim.

The quick way
-------------------------

::

	# Import fastsemsim
	import fastsemsim

	ontology = fastsemsim.load_ontology(ontology_type = 'GeneOntology')


A more comprehensive example
------------------------------

::

	# Import fastsemsim
	import fastsemsim

	# Select the type of ontology (GeneOntology, ...)
	ontology_type = 'GeneOntology'
	# ontology_type = 'CellOntology'
	# ontology_type = 'DiseaseOntology'

	# Select the relatioships to be ignored. For the GeneOntology, has_part is ignore by default, for CellOntology, lacks_plasma_membrane_part is ignored by default
	# ontology_parameters =	{}
	# ontology_parameters =	{'ignore':{}}
	# ontology_parameters =	{'ignore':{'has_part':True, 'occurs_in':True, 'happens_during':True}}
	ignore_parameters =	{'ignore':{'regulates':False, 'has_part':True, 'negatively_regulates':False, 'positively_regulates':False, 'occurs_in':False, 'happens_during':True, 'lacks_plasma_membrane_part':True}}

	# Select the source file type (obo or obo-xml)
	ontology_file_type = 'obo'

	# Select the ontology source file name. If None, the default ontology_type included in fastsemsim will be used
	ontology_source_file = None


	ontology = fastsemsim.load_ontology(source_file = ontology_source_file, file_type = ontology_file_type, ontology_type = ontology_type, ontology_descriptor = None, parameters=ignore_parameters)



Loading the human Gene Ontology annotation corpus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example the human Gene Ontology annotation corpus for Uniprot Proteins embedded in FastSemSim is loaded.
The quick example loads the Annotation Corpus in one simple line. The more complete example explores some of the parameters that can be used. 
Note that in any case an ontology has to be already loaded.

Please refer to the FastSemSim API section for a detailed description of the function to load acs.

The complete example code is available in the file fastsemsim/examples/load_go_annotation_corpus.py within the source tarball of FastSemSim.

The quick way
-------------------------

::

	ac = fastsemsim.load_ac(ontology, ac_species = 'human')




A more comprehensive example
------------------------------

::

	# Select the ac source file name. If None, the default ac included in fastsemsim for the ac_species will be used
	ac_source_file = None

	ac_species = 'human'
	# ac_species = 'arabidopsis'
	# ac_species = 'fly'
	# ac_species = 'mouse'
	# ac_species = 'rat'
	# ac_species = 'worm'
	# ac_species = 'zebrafish'

	# ac_source_file_type = 'plain'
	ac_source_file_type = 'gaf-2.0'

	ac_params = {}

	# gaf-2.0 ac
	ac_params['filter'] = {} # filter section is useful to remove undesired annotations
	ac_params['filter']['EC'] = {} # EC filtering: select annotations depending on their EC
	# ac_params['filter']['EC']['EC'] = EC_include # select which EC accept or reject
	# ac_params['filter']['EC']['inclusive'] = True # select which EC accept or reject
	# ac_params['filter']['EC'] = {} # EC filtering: select annotations depending on their EC
	# ac_params['filter']['EC']['EC'] = EC_ignore # select which EC accept or reject
	# ac_params['filter']['EC']['inclusive'] = False # select which EC accept or reject

	ac_params['filter']['taxonomy'] = {}
	# ac_params['filter']['taxonomy']['taxonomy'] = tax_include # set properly this field to load only annotations involving proteins/genes of a specific species
	# ac_params['filter']['taxonomy']['inclusive'] = True # select which taxonomy accept or reject
	# ac_params['filter']['taxonomy'] = {}
	# ac_params['filter']['taxonomy']['taxonomy'] = tax_ignore
	# ac_params['filter']['taxonomy']['inclusive'] = False # select which EC accept or reject
	# ac_params['simplify'] = True # after parsing and filtering, removes additional information such as taxonomy or EC. Useful if you have a huge amount of annotations and not enough memory


	ac_descriptor = fastsemsim.dataset.get_default_annotation_corpus(ontology_type=ontology_type, ac_species=ac_species)
	ac = fastsemsim.load_ac(ontology, source_file=None, file_type=None, species=None, ac_descriptor=ac_descriptor, params=ac_params)







Calculating a semantic similarity 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once an ontology (and possibly an annotation corpus) has been loaded, semantic similarity scores can be calculated.
As in the previous examples, a first quick glance at some simple code is presented, followed by a more complex example.

Note that in any case an ontology (and the annotation corpus, if required) has to be already loaded.

Please refer to the FastSemSim API section for a detailed description of the function to initialize semantic similarity measures and calculate semantic similarity scores.

The complete example code is available in the file fastsemsim/examples/calculate_ss_on_go.py within the source tarball of FastSemSim.


The quick way
-------------------------

In this quick example we tell fastSemSim we wish to initialize the Resnik semantic similarity measure between proteins in the annotation corpus (using the parameter semsin_type='obj'. as Resnik is a term pairwise measure, we also need to say how to mix the single term-term similarities (mixing_strategy parameter).
The returned object can then be used (by invoking its method SemSim) to calculate similarities between two proteins.

::

	# Parameters for the SS
	semsim_type='obj'
	semsim_measure='Resnik'
	mixing_strategy='max'

	# Initializing semantic similarity
	ss = fastsemsim.init_semsim(ontology = ontology, ac = ac, semsim_type = semsim_type, semsim_measure = semsim_measure, mixing_strategy = mixing_strategy)

	# Calculating SS for some pairs of proteins...
	res = ss.SemSim('O75884', 'Q9NQB0')
	print(res)


Calculating semantic similarity - batch mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The previous minimal example is sufficient to calculate a semantic similarity score.
Suppose we want to calculate the semantic similarity in a pairwise fashion between all the pairs of proteins within a given set. Of course, we could use the object built in the quick example from above, and repeteadly invoke it within a loop cycling through all the protein pairs. Albeit feasible, this is not very efficient and requires some programming effort.
For this reasons, FastSemSim provides a 'batch mode' to calculate semantic simialrity between several pairs/groups of protein.

::

	# Parameters for the SS
	semsim_type='obj'
	semsim_measure='Resnik'
	mixing_strategy='max'
	ss_util=None
	semsim_do_log=False
	semsim_params={}

	# Initializing batch Semantic Similarity onject... 
	ssbatch = fastsemsim.init_batchsemsim(ontology = ontology, ac = ac, semsim_type = semsim_type, semsim_measure = semsim_measure, mixing_strategy = mixing_strategy, ss_util = ss_util, do_log = semsim_do_log, params = semsim_params)
	
	# Same as before, using the pairwise ss as template...
	ssbatch2 = fastsemsim.init_batchsemsim(ontology = ontology, ac = ac, semsim=ss)


	# Calculating pairwise SS in batch mode for a list of proteins...

	batch_query_pairs = [['O75884', 'Q9NQB0'], ['Q14206', 'Q8IUH3' ]]
	res = ssbatch.SemSim(query=batch_query_pairs, query_type='pairs')

	batch_query_pairwise = ['O75884', 'Q9NQB0', 'Q14206', 'Q8IUH3' ]
	res2 = ssbatch.SemSim(query=batch_query_pairwise, query_type='pairwise')

	res_long = ssbatch.SemSim(query= 10*batch_query_pairwise, query_type='pairwise')
	res_very_long = ssbatch.SemSim(query= 30*batch_query_pairwise, query_type='pairwise')
	res_very_very_long = ssbatch.SemSim(query= 100*batch_query_pairwise, query_type='pairwise')

	res_long_v2 = ssbatch2.SemSim(query= 10*batch_query_pairwise, query_type='pairwise')
	

	%%timeit
	res_very_very_long = ssbatch.SemSim(query= 10*batch_query_pairwise, query_type='pairwise')




Putting all together
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is a complete minimal example to calculate the semantic similaity between two proteins over the gene ontology

::

	# Import fastsemsim
	import fastsemsim

	ontology = fastsemsim.load_ontology(ontology_type = 'GeneOntology')
	ac = fastsemsim.load_ac(ontology, ac_species = 'human')
	ssbatch = fastsemsim.init_batchsemsim(ontology = ontology, ac = ac, semsim_type = 'obj', semsim_measure = 'resnik', mixing_strategy = 'BMA')

	# Calculating pairwise SS in batch mode for a list of proteins...
	ssbatch.set_root('molecular_function')
	ssbatch.set_output(output = 'console')
	batch_query_pairs = [['O75884', 'Q9NQB0'], ['Q14206', 'Q8IUH3' ]]
	res = ssbatch.SemSim(query=batch_query_pairs, query_type='pairs'


	ssbatch.set_root('biological_process')
	ssbatch.set_output(output = None)
	batch_query_pairwise = ['O75884', 'Q9NQB0', 'Q14206', 'Q8IUH3' ]
	res2 = ssbatch.SemSim(query=batch_query_pairwise, query_type='pairwise')



Divers
----------------------------------





