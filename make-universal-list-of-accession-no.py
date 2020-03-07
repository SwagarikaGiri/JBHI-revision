import numpy as np
import pandas as pd
import pickle
import csv

output_file="JBHI_all_accession_no.csv"
accession_no_function= dict()
unique_accession_no=[]

def save_global_accession_no(accession_no_function,functionKey):
    fileTrain='../data/train-'+str(functionKey)+'.pkl'
    fileTest='../data/test-'+str(functionKey)+'.pkl'
    df1 = pd.read_pickle(fileTrain)
    df2 = pd.read_pickle(fileTest)
    accessionList =df1['accessions']
    for element in accessionList:
        if element not in unique_accession_no:
            unique_accession_no.append(element)
        if(str(element),functionKey) in accession_no_function:
            accession_no_function[str(element),functionKey]= accession_no_function[str(element),functionKey]+1
        else:
             accession_no_function[str(element),functionKey]=1


def create_unique_accession_list_function_csv(output_file,unique_accession_no,accession_no_function):
    functions=['bp','cc','mf']
    with open(output_file,'w') as outputcsv_file:
        spamwriter = csv.writer(outputcsv_file,delimiter=',')
        col1=['accession_no','bp','cc','mf']
        spamwriter.writerow(col1)
        for accession_no in unique_accession_no:
            col1=[]
            col1.append(accession_no)
            for function in functions:
                if(accession_no,function) in accession_no_function:
                    col1.append('1')
                else:
                    col1.append('0')
            print col1
            spamwriter.writerow(col1)   

if __name__=='__main__':
    save_global_accession_no(accession_no_function,'bp')
    save_global_accession_no(accession_no_function,'cc')
    save_global_accession_no(accession_no_function,'mf')
    # print accession_no_function
    print unique_accession_no
    print len(unique_accession_no)
    create_unique_accession_list_function_csv(output_file,unique_accession_no,accession_no_function)
