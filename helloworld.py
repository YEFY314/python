#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import os
import os.path
import scipy.stats as stats

"""获取指定目录及其子目录下的 py 文件路径说明：l 用于存储找到的 xlsx 文件路径 get_xlsx 函数，递归查找并存储 xlsx 文件路径于 l"""
list = []

def get_xlsx(path, list):
    fileList = os.listdir(path)   #获取path目录下所有文件
    for filename in fileList:
        pathTmp = os.path.join(path, filename)   #获取path与filename组合后的路径
        if os.path.isdir(pathTmp):   #如果是目录
            get_xlsx(pathTmp, list)        #则递归查找
        elif filename[-5:].upper()=='.XLSX':   #不是目录,则比较后缀名
            list.append(pathTmp)
# path = input('请输入路径:').strip()
path = r'D:\code\yefyExperiments\yefyExperiments\resultData'
get_xlsx(path, list)
print('在%s目录及其子目录下找到%d个xlsx文件\n分别为：\n' % (path, len(list)))
print(list)
all_array = []
for filePath in list:
    bk = xlrd.open_workbook(filePath, "rb")
    try:
        sh = bk.sheets()[0]
    except ValueError:
        print("no sheet in %s named Sheet1" % filePath)
    rows = sh.nrows
    cols = sh.ncols
    # print("nrows %d, ncols %d" % (rows, cols))

    # 获取第一行第一列数据
    cell_value = sh.cell_value(0, 0)

    array_9_1 = []
    array_9_2 = []
    array_9_3 = []
    array_9_5 = []
    array_9_9 = []
    array_16_1 = []
    array_16_2 = []
    array_16_3 = []
    array_16_4 = []
    array_16_6 = []
    array_16_8 = []

    # 获取各行数据
    for i in range(1, rows):
        row_data = sh.row_values(i)
        if row_data[0] == 1 and row_data[1] < 10000:
            if row_data[2] == 'array-9-1':
                array_9_1.append(row_data[1])
            elif row_data[2] == 'array-9-2':
                array_9_2.append(row_data[1])
            elif row_data[2] == 'array-9-3':
                array_9_3.append(row_data[1])
            elif row_data[2] == 'array-9-5':
                array_9_5.append(row_data[1])
            elif row_data[2] == 'array-9-9':
                array_9_9.append(row_data[1])
            elif row_data[2] == 'array-16-1':
                array_16_1.append(row_data[1])
            elif row_data[2] == 'array-16-2':
                array_16_2.append(row_data[1])
            elif row_data[2] == 'array-16-3':
                array_16_3.append(row_data[1])
            elif row_data[2] == 'array-16-4':
                array_16_4.append(row_data[1])
            elif row_data[2] == 'array-16-6':
                array_16_6.append(row_data[1])
            elif row_data[2] == 'array-16-8':
                array_16_8.append(row_data[1])
    all_list = []
    all_list.append(array_9_1)
    all_list.append(array_9_2)
    all_list.append(array_9_3)
    all_list.append(array_9_5)
    all_list.append(array_9_9)
    all_list.append(array_16_1)
    all_list.append(array_16_2)
    all_list.append(array_16_3)
    all_list.append(array_16_4)
    all_list.append(array_16_6)
    all_list.append(array_16_8)
    ave = []
    for item in all_list:
        ave.append(float("%.0f" % np.array(item).mean()))
    print(cell_value, ave)
    all_array.append(ave)
    plt.plot(range(11), ave, "r-o")
print(np.mean(np.array(all_array), axis=0))

plt.ylim(0, 8000)
plt.show()
    # print(all_list)
    # for item in all_list:
    #     x = range(len(item))
    #     plt.plot(x, item, 'r-o',)
    # plt.ylim(0, 6000)
    # plt.show()
# x = np.arange(0, 5, 1)
# print(x)
# plt.plot(x, x, 'r-o')
# plt.show()







