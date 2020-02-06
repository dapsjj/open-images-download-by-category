# open-images-download-by-category
You can download images of the specified categories as needed(你可以根据自己的需要下载指定类别的图像)

## Project structure(项目结构)：            
```
modules
 └──bounding_boxes.py
 └──csv_downloader.py
 └──downloader.py
 └──image_level.py
 └──parser.py
 └──show.py
 └──utils.py
 | 
OID
 ├──csv_folder_nl
 |     └──class-descriptions.csv 
 |     └──train-annotations-machine-imagelabels.csv 
 | 
 └──Dataset_nl
 | 
 main.py
 | 
 put_the_specified_category_image_into_CSV.py (把指定类别的数据放到csv,用于替换train-annotations-machine-imagelabels.csv)
 ```
     
## Download one class in separated folder(下载一个类别)
`python main.py downloader_ill --sub m --classes Football --type_csv train --limit 1000`


## Download different classes in separated folder(下载多个类别)
`python main.py downloader_ill --sub m --classes Apple Banana Football --multiclasses 1 --type_csv train --limit 1000`

