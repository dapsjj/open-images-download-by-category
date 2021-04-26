# open-images-download-by-category
## [Open image official website](https://storage.googleapis.com/openimages/web/index.html)
If you think the image file is too large, you don't want to download all kinds of pictures,you can download images of the specified categories as needed.(如果嫌所有类别图像太大，不想下载所有类别图片的话，你可以根据自己的需要下载指定类别的图像)

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
 classes_custom.txt
 | 
 put_the_specified_category_image_into_CSV.py (如果你的内存够大，则忽略这个代码，如果内存小，那么该代码用于把指定类别的数据放到csv,新生成的csv用于替换原始的train-annotations-machine-imagelabels.csv，类别就变少了，就不会再出现内存问题了)
 ```
     
## Download one class in separated folder(下载一个类别)
`python main.py downloader_ill --sub m --classes Football --type_csv train --limit 1000`  
or  
`python main.py downloader_ill --sub m --classes classes_custom.txt --type_csv train --limit 1000`


## Download different classes in a Specified folder(下载多个类别到一个文件夹)
`python main.py downloader_ill --sub m --classes Apple Banana Football --multiclasses 1 --type_csv train --limit 1000`  
or  
`python main.py downloader_ill --sub m --classes classes_custom.txt --type_csv train --limit 1000`

