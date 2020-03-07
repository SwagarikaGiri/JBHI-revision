import numpy as np
import pandas as pd
import pickle
import csv
from numpy import array


#only that with pdbid
pdb_id_file='JBHI_all_accession_no_with_pdbid.csv'
# all in deepgo
accession_no_file='JBHI_all_accession_no_without_header.csv'
output_file='JBHI_accession_no_with_status.csv'


def generate_accession_no_status_code_pickle():
    df1=pd.read_csv(pdb_id_file)
    #accession_no is for the accession no filtered after parth's code
    accession_no = df1.iloc[:, 0].tolist()
    #accession no function is all the data we have from deepgo's code
    df1=pd.read_csv(accession_no_file)
    pdbid_status=[]
    all_accession_no = df1['accession_no'].values
    print type(all_accession_no)
    for ele in all_accession_no:
        if(ele in accession_no):
            pdbid_status.append(True)
        else:
            pdbid_status.append(False)
    status=np.array(pdbid_status)
    accession=df1['accession_no'].values
    bp=df1['bp'].values
    mf=df1['mf'].values
    cc=df1['cc'].values
    res_df = pd.DataFrame({
        'accession': accession,
        'bp': bp,
        'cc':cc,
        'mf':mf,
        'status':status})
    # res_df.to_pickle('AccessionNumberStatusFile'+ '.pkl')
    print res_df


def generate_status_csv():
    df1=pd.read_csv(pdb_id_file)
    #accession_no is for the accession no filtered after parth's code
    accession_no = df1.iloc[:, 0].tolist()
    file1 = open(accession_no_file, 'r') 
    Lines = file1.readlines()
    with open(output_file,'w') as outputcsv_file:
        spamwriter = csv.writer(outputcsv_file,delimiter=',')
        for line in Lines:
            line=line.rstrip()
            line_array = line.split(",")
            if(line_array[0] in accession_no):
                line_array.append(True)
            else:
                line_array.append(False)
            spamwriter.writerow(line_array)

  


        


    
 







if __name__ == '__main__':
    # generate_accession_no_status_code_pickle()
    generate_status_csv()

