#coding = utf-8
import json
import os
import pandas as pd
import inspect

def ExcelToJson():
    dir_path = os.path.dirname(os.path.abspath(__file__))#当前目录
    # dir_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))#当前目录
    print("当前目录:",dir_path)
    file_names = os.listdir(dir_path)
    all_data = pd.DataFrame()
    path = dir_path + "\\" + "json"
    if(not os.path.exists(path)):
        os.makedirs(path)
    for file_name in file_names:
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(dir_path, file_name)
            data = pd.read_excel(file_path)
            data_dict = data.to_dict(orient='records')
            print("file_name:" + file_name)
            jsonFileName = path + "\\" + file_name.split(".")[0] + ".json"
            # print(jsonFileName)
            with open(jsonFileName, "w") as file:
                json_str = json.dump(data_dict, file)
    os.system("pause")
print(__name__)
if __name__ == '__main__':
    print("运行")
    ExcelToJson()

