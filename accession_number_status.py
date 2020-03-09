import numpy as np
import pandas as pd
import pickle
import csv

deepgo_bp_train ='../data/train-bp.pkl'
deepgo_bp_test='../data/test-bp.pkl'
deepgo_cc_train='../data/train-cc.pkl'
multipred_cc_test='../data/test-cc.pkl'
multipred_mf_train='../data/train-mf.pkl'
multipred_mf_test='../data/test-mf.pkl'

def get_dataframe(baseCode, function):
    if(baseCode=='deepgo'):
        baseRootTrain='../data/train-'+str(function)+'.pkl'
        baseRootTest='../data/test-'+str(function)+'.pkl'
        try:
            df_train = pd.read_pickle(accession_status_file)
            df
    elif(baseCode=='multipred'):
        baseRootTrain='../data/train-'+str(function)+'.pkl'
        baseRootTest='../data/test-'+str(function)+'.pkl'
    else:
        print "Sorry the data was not loaded"

def load_train_test_data(accession_object):
    accession_number=accession_object['accession']
    bp=accession_object['bp']
    cc=accession_object['cc']
    mf=accession_object['mf']
    if(accession_object['status'==True]):

    elif(accession_object['status'==False]):
    else:
        return "Sorry Accession No Cannot be Accepted due to computational limitations2"


def analyze_accession_status(accession_number):
    accession_status_file='AccessionNumberStatusFileWithAccessionIndex.pkl'
    df1 = pd.read_pickle(accession_status_file)
    try:
        accession_object = df1.loc[accession_number]
        return accession_object['bp']
    except:
        return "Sorry Accession No Cannot be Accepted due to computational limitations"







if __name__=='__main__':
    message=analyze_accession_status('Q86SG5')
    print message
    
