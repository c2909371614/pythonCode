#coding = utf-8
import os
import pandas as pd

def mergeExcel():
    dir_path = os.path.dirname(os.path.abspath(__file__))#当前目录
    file_names = os.listdir(dir_path)
    all_data = pd.DataFrame()
    path = "res"
    if(not os.path.exists(path)):
        os.makedirs(path)
    resPathName = path + '/mergedAllExcel.xlsx'
    # df = pd.read_excel(resPathName)
    writer = pd.ExcelWriter(resPathName, engine='openpyxl')
    for file_name in file_names:
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(dir_path, file_name)
            data = pd.read_excel(file_path)
            print("file_name:" + file_name)
            data.to_excel(writer, sheet_name = file_name, index=False)
    writer.save()
    os.system("pause")
print(__name__)
if __name__ == '__main__':
    print("运行")
    mergeExcel()

