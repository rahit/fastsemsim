GO=../../GO/GO_2011-06-06.obo-xml
GOA=../../GOA/human
TEST=../../src/test/human_list.txt

echo "Output redirected to file log.txt"
(export PYTHONPATH="."; python2 examples/testSemSim.py ${GO} ${GOA} ${TEST} > log.txt)
