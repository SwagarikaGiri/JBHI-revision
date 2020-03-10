import numpy as np
import pandas as pd
import pickle
import csv

structure_bp='../data/struct_features/struct_features_bp.csv'
structure_mf='../data/struct_features/struct_features_mf.csv'
structure_cc='../data/struct_features/struct_features_cc.csv'
df_bp=pd.read_csv(structure_bp)
df_cc=pd.read_csv(structure_cc)
df_mf=pd.read_csv(structure_mf)
#accession_no is for the accession no filtered after parth's code
considered_accession_list=[]
considered_accession_list=considered_accession_list+df_bp.iloc[:, 0].tolist()
considered_accession_list=considered_accession_list+df_mf.iloc[:, 0].tolist()
considered_accession_list=considered_accession_list+df_cc.iloc[:, 0].tolist()
considered_accession_set=set(considered_accession_list)
print len(considered_accession_set)
print len(considered_accession_list)

def generate_updated_csv_after_considering_struct_data():
    output_file='JBHI_Accession_Status_Updated.csv'
    accession_no_file='JBHI_Accession_No_Status.csv'
    file1 = open(accession_no_file, 'r') 
    Lines = file1.readlines()
    with open(output_file,'w') as outputcsv_file:
        spamwriter = csv.writer(outputcsv_file,delimiter=',')
        col1=['accession','bp','cc','mf','status']
        spamwriter.writerow(col1)
        for line in Lines:
            col1=[]
            line=line.rstrip()
            line_array = line.split(",")
            col1=col1+line_array[0:3]
            if(line_array[0] in considered_accession_set):
                col1.append(True)
            else:
                col1.append(False)
            spamwriter.writerow(line_array)

def generate_updated_pickle_after_considering_struct_data():
    df_csv=pd.read_csv('JBHI_Accession_Status_Updated.csv')
    print df_csv['accession']
    accession=df_csv['accession'].values
    bp=df_csv['bp'].values
    mf=df_csv['mf'].values
    cc=df_csv['cc'].values
    status=df_csv['status'].values
    res_df = pd.DataFrame({
        'accession': accession,
        'bp': bp,
        'cc':cc,
        'mf':mf,
        'status':status,'index':accession})
    res_df=res_df.set_index('index')
    res_df.to_pickle('AccessionNumber_Structure_StatusFileWithAccessionIndex'+ '.pkl')
    print res_df

if __name__=='__main__':
    generate_updated_pickle_after_considering_struct_data()
