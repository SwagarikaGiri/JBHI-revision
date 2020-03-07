import numpy as np
import pandas as pd
import pickle
import csv


output_file='JBHI_all_accession_no_with_pdbid.csv'
list_accession_no_with_pid=[]
def filter_accession_no_with_pdb_id(file_path):
    file1 = open(file_path, 'r') 
    Lines = file1.readlines()
    for line in Lines:
         line=line.rstrip()
         line_array = line.split(",")
         if(line_array[0] not in list_accession_no_with_pid):
             list_accession_no_with_pid.append(line_array[0])
    with open(output_file,'w') as outputcsv_file:
        spamwriter = csv.writer(outputcsv_file,delimiter=',')
        for ele in list_accession_no_with_pid:
            spamwriter.writerow([ele])
        

   
  





if __name__=='__main__':
    filter_accession_no_with_pdb_id('../data/test_bp_accession_pbd_mapped.csv')
    filter_accession_no_with_pdb_id('../data/train_bp_accession_pbd_mapped.csv')
    filter_accession_no_with_pdb_id('../data/test_cc_accession_pbd_mapped.csv')
    filter_accession_no_with_pdb_id('../data/train_cc_accession_pbd_mapped.csv')
    filter_accession_no_with_pdb_id('../data/test_mf_accession_pbd_mapped.csv')
    filter_accession_no_with_pdb_id('../data/train_mf_accession_pbd_mapped.csv')
    print list_accession_no_with_pid
    print len(list_accession_no_with_pid)