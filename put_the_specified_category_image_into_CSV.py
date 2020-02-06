
import csv

with open(r'./OID/csv_folder_nl/train-annotations-machine-imagelabels_bk.csv','r', encoding='utf-8') as f,open(r'./OID/csv_folder_nl/Wheel.csv','w',newline='',encoding='utf-8') as f_out:
    writer = csv.writer(f_out)
    alllist=[]
    i=1
    for row in f:
        row = row.replace('\n', '')
        line = row.split(',')
        '''
        /m/04_bsf Wheelie
        /m/083wq Wheel
        '''
        if line[2] =='/m/083wq':
            print(i)
            alllist.append(line)
            i += 1
    writer.writerows(alllist)

#You can also do it with chunksize.
#import pandas as pd
#chunksize = 1000
#for chunk in pd.read_csv(r'./OID/csv_folder_nl/train-annotations-machine-imagelabels_bk.csv',chunksize=chunksize):
#    print(chunk)
