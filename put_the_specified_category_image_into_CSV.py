import csv

title = [['ImageID','Source','LabelName','Confidence']]

with open(r'./OID/csv_folder_nl/train-annotations-machine-imagelabels_bk.csv','r', encoding='utf-8') as f,open(r'./OID/csv_folder_nl/Leaf.csv','w',newline='',encoding='utf-8') as f_out:
    writer = csv.writer(f_out)
    alllist=[]
    i=1
    for row in f:
        row = row.replace('\n', '')
        line = row.split(',')
        '''
        /m/04_bsf Wheelie
        /m/07tdy9 Cartwheel #没有这个类别的数据
        /m/083wq Wheel
        /m/014j1m Apple
        /m/06gfj Road
        /m/09p3jz Curb
        /m/01k0mv Road surface
        /m/03m3q7q Rocky road
        /m/06gfj Road
        /m/015rt Bay leaf
        /m/01rynr Maple leaf
        /m/0262mx0 Banana leaf
        /m/09t49 Leaf
        '''
        if line[2] =='/m/09t49':
            print(i)
            alllist.append(line)
            i += 1
    writer.writerows(title)
    writer.writerows(alllist)

#You can also do it with chunksize.(你也可以用pandas的read_csv方法加参数chunksize去分块实现)
#import pandas as pd
#chunksize = 1000
#for chunk in pd.read_csv(r'./OID/csv_folder_nl/train-annotations-machine-imagelabels_bk.csv',chunksize=chunksize):
#    currentData=chunk.values.tolist()
#    print(currentData)
