import numpy as np
import pandas as pd
import pickle
import csv
import os

deepgo_bp_train ='../data/train-bp.pkl'
deepgo_bp_test='../data/test-bp.pkl'
deepgo_cc_train='../data/train-cc.pkl'
multipred_cc_test='../data/test-cc.pkl'
multipred_mf_train='../data/train-mf.pkl'
multipred_mf_test='../data/test-mf.pkl'

def get_dataframe(baseCode, function,accession_number):
    print str(baseCode)+" "+str(function)+" "+str(accession_number)
    testData={}
    if(baseCode=='deepgo'):
        baseRootTrain='../data/train-'+str(function)+'.pkl'
        baseRootTest='../data/test-'+str(function)+'.pkl'
        try:
            df_train = pd.read_pickle(baseRootTrain).set_index('accessions')
            df_test =pd.read_pickle(baseRootTest).set_index('accessions')
            try:
                testData=df_train.loc[accession_number]
            except:
                testData=df_test.loc[accession_number]
        except:
            print "Sorry the data was not loaded 1"
        print testData
    elif(baseCode=='multipred'):
        baseRootTrain='../data/multimodaltrain-'+str(function)+'.pkl'
        baseRootTest='../data/multimodaltest-'+str(function)+'.pkl'
        try:
            df_train = pd.read_pickle(baseRootTrain).set_index('accessions')
            df_test =pd.read_pickle(baseRootTest).set_index('accessions')
            try:
                testData=df_train.loc[accession_number]
            except:
                testData=df_test.loc[accession_number]
        except:
            print "Sorry the data was not loaded 2"  
        print testData
    return testData

def load_train_test_data(accession_object):
    accession_number=accession_object['accession']
    bp=accession_object['bp']
    cc=accession_object['cc']
    mf=accession_object['mf']
    if(accession_object['status'==True]):
        if(bp):
            get_dataframe('multipred','bp',accession_number)
        if(cc):
            get_dataframe('multipred','cc',accession_number)
        if(mf):
            get_dataframe('multipred','mf',accession_number)
    elif(accession_object['status'==False]):
        if(bp):
            get_dataframe('deepgo','bp',accession_number)
        if(cc):
            get_dataframe('deepgo','cc',accession_number)
        if(mf):
            get_dataframe('deepgo','mf',accession_number)
    else:
        return "Sorry Accession No Cannot be Accepted due to computational limitations2"


def analyze_accession_status(accession_number):
    accession_status_file='AccessionNumber_Structure_StatusFileWithAccessionIndex.pkl'
    print(os.getcwd())
    df1 = pd.read_pickle(accession_status_file)
    try:
        accession_object = df1.loc[accession_number]
        load_train_test_data(accession_object)
    except:
        return "Sorry Accession No Cannot be Accepted due to computational limitations"





  




if __name__=='__main__':
    message=analyze_accession_status('Q86SG5')
    print message
    
