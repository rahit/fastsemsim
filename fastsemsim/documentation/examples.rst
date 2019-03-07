Examples and use cases: Putting all together
======================================================

Loading the Gene Ontology embedded in fastsemsim
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Loading an ontology from a file or a descriptor (more about descriptors in section FastSemSim Datasets) is as simple as running a single line of code using the entrypoint function fastsemsim.load_ontology

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



Loading the human Gene Ontology annotation corpus for Uniprot Proteins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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







Calculating semantic similarity 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

	# Parameters for the SS
	semsim_type='obj'
	semsim_measure='Resnik'
	mixing_strategy='max'
	ss_util=None
	semsim_do_log=False
	semsim_params={}


	# Initializing semantic similarity
	ss = fastsemsim.init_semsim(ontology = ontology, ac = ac, semsim_type = semsim_type, semsim_measure = semsim_measure, mixing_strategy = mixing_strategy, ss_util = ss_util, do_log = semsim_do_log, params = semsim_params)


	# Calculating SS for some pairs of proteins...

	res = ss.SemSim('O75884', 'Q9NQB0')
	print(res)


Calculating semantic similarity - batch mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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



Divers
----------------------------------

