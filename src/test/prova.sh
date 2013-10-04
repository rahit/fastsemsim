export TEST_DIR=$1
export OLD_PP=$PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$TEST_DIR
export TEST_FILE=$TEST_DIR/startfastSemSim.py
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix max --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix BMA --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimRel --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss G-SESAME --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Cosine --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICND --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimICNP --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Resnik --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Lin --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimGIC --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimUI --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jiang-Conrath --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss SimIC --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Dice --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss TO --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss NTO --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Jaccard --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type obj --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type obj --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type obj --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type term --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type term --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type term --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type objset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type objset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type objset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type termset --query_input ontology --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type termset --query_input file --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode pairs -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
echo python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
python $TEST_FILE --o_type Ontology -o ./data/Os/DiseaseOntology_Human_2013.09.09.obo --o_file_format obo -a ./data/ACs/DO_human_ac.txt --ac_type plain --tss Czekanowski-Dice --tmix avg --query_type SS --query_ss_type termset --query_input ac --query_file ./data/fly_list_example.txt --query_mode list -vvv --out_file temp.txt
RES=$?
echo ""
if ! [ $RES -eq 0 ];then
exit
fi
