""""
功能:格式化相应的文件夹下的文件,主要为重命名文件。由于之前的例子采用的是两位数的命名的方式。
诸如：
    01-xxx.html
    02-xxx.html
    03-xxx.html
    
但是随着例子越来越多,将采用如下命名方式。
诸如：
    001-xxx.html
    002-xxx.html
    003-xxx.html
    
手动修改这么多文件比较麻烦，所以通过写一个python的脚本来简化文件重名的过程

os.rename(src , dst)

获取当前目录
import os
os.getcwd()



"""

from fileinput import filename
import os

print("rename tools started!")

# 需要管理的文件夹
cwdDir = os.getcwd()

regWorkList = ['\\\\01.html\\\\case','\\\\02.css\\\\case','\\\\03.js\\\\case'] 
# 遍历文件夹
# print(regWorkList)
for dir in regWorkList:
    # print(dir)
    tmpDir = cwdDir+dir
    # print(tmpDir)
    
    fileList = os.listdir(tmpDir)
    for file in fileList:
        fileName = os.path.splitext(file)[0]
        fileSuffix = os.path.splitext(file)[1]
        
        newFileName = ""
        # print(fileSuffix)
        if fileSuffix != '.html':
            continue
        
        
        if fileName[2] == '-':
            newFileName = '0'+fileName
        else:
            continue
        
        # print("filename:"+fileName)
        os.rename(os.path.join(tmpDir,fileName+fileSuffix),os.path.join(tmpDir,newFileName+fileSuffix))

# 打印结束的信息
print("rename tools ended!")