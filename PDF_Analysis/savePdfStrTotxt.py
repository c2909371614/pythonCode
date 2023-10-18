# -*- coding: utf-8 -*-
import PyPDF2  

def getPdfText(name:str):
    # 获取PDF文件中的文本  
    pdf_text = ""  
    # 打开PDF文件  
    with open(name, 'rb') as pdf_file:  
        # 创建一个PDF阅读器对象  
        pdf_reader = PyPDF2.PdfReader(pdf_file)    
        for page_num in range(len(pdf_reader.pages)):  
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()
            print("读取文本中。。。第%d页" %(page_num+1))
            # if(page_num < 1):
            #     print(page.extract_text())
    # 打印PDF文件中的文本  
    print(pdf_text[1:100])
    return pdf_text

def saveStrToTxt(filename:str, str:str):
    '''保存字符到txt'''
    with open(filename, 'w') as file:
        file.write(str)

def savePdfStrToText(pathName:str):
    '''
    @ 读取pdf中的文本并保存到txt中
    @ pathName = 'PDF_Analysis/塔罗全书' 不带后缀
    '''
    pdf_text:str = getPdfText(pathName + '.pdf')
    saveStrToTxt(pathName + ".txt",pdf_text)

if __name__ == "__main__":
    print("main")
    pathName = 'PDF_Analysis/塔罗全书'
    savePdfStrToText(pathName)
