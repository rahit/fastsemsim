.. fastsemsim documentation master file, created by Marco Mina

.. py:module:: fastsemsim

FastSemSim Documentation
========================

:Release: |version|
:Date: |today|
:Homepage: https://sites.google.com/site/fastsemsim/

FastSemSim is a Python package for calculating semantic similarity over ontologies (yes, including the Gene Ontology).

FastSemSim has three main components:

* An underlying library of data structures to represent ontologies and annotation corpora, and algorithms to calculate semantic similarity measures.

* A comprehensive API, built on top of the library, to load and play with ontologies and annotation corpora and calculate semantic similarity scores within the Python environment.

* A command line interface (CLI) to compute semantic similarity without requiring programming skills.

This reference manual details modules and classes included in FastSemSim, as well as the command line interface usage.
The sections library, API andd CLI describe the aforementioned components and include some examlples.

.. toctree::
   :maxdepth: 2

   library.rst

   API.rst
   
   cmdline.rst


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
