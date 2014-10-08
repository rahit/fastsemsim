#!/bin/bash
# $1="../../Os/DiseaseOntology_Human_2014.09.09.obo"
# $2="DiseaseOntology_Human_2014.09.09.count.txt"
grep "\[Term\]" S1 -A 1 | grep "id" | sort  | uniq  | wc > $2
