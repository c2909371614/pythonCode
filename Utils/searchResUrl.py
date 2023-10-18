# -*- coding: utf-8 -*-

import json
import os

def isNeedFile(name:str, ends:list):
    for i in range(len(ends)):
        if name.endswith(ends[i]):
            return True
    return False

def generate_relative_paths(folder_path, parent_folder='', ends = [".py", ".png", ".jpg"]):
    file_paths = []
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            if not isNeedFile(filename, ends):
                continue
            relative_path = os.path.join(parent_folder, filename)
            file_paths.append(relative_path)
        elif os.path.isdir(filepath):
            new_parent_folder = os.path.join(parent_folder, filename)
            file_paths.extend(generate_relative_paths(filepath, new_parent_folder))
    return file_paths

def dealPath(relative_paths:list):
    nameToPath = {}
    for path in relative_paths:
        pathStr = str(path)
        newPath = pathStr.replace("\\", "/")
        newPathArr = newPath.split("/")
        name = newPathArr[len(newPathArr)-1]
        nameArr = name.split(".")
        newName = nameArr[1] + "_" + nameArr[0]
        nameToPath[newName] = newPath
        print(name,":", newPath)
    return nameToPath

if __name__ == '__main__':
    ends = [".py", ".png", ".jpg", ".prefab"]
    # 示例用法
    file_path = os.path.abspath(__file__)
    folder_path = os.path.dirname(os.path.dirname(file_path))#获取上层路径
    relative_paths = generate_relative_paths(folder_path, ends = ends)
    nameToPath = dealPath(relative_paths)
    # print(nameToPath)
    # nameToPathJson = json.dumps(nameToPath, indent=4, separators=(",\n", ": "))
    nameToPathJson = json.dumps(nameToPath, indent=4)
    nameToPathJson = "/**由脚本自动生成**/ \n export default <const>" + nameToPathJson
    with open("urlMap.ts", "w") as file:
        file.write(nameToPathJson)
    # 输出所有文件的相对路径
    # for path in relative_paths:
    #     print(path)