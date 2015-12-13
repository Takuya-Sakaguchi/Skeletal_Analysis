
import glob
import pandas as pd


def getExcelFileNamesInFolder(givenpath):
    tempFileList = glob.glob(givenpath + '*')
    finalFileList = []
    for file in tempFileList:
        if file[-3:] == 'xls' or file[-3:] == 'lsx':
            finalFileList.append(file)
    return finalFileList



def convertPathToDF(givenPath):
    # give a path to a folder containing excel files
    # return pandas df of all Exel files in the folder

    fileName = getExcelFileNamesInFolder(givenPath)

    #print(fileName)
    #print(len(fileName))
    xl =  [pd.ExcelFile(item) for item in fileName]

    #print(xl)
    #print(len(xl))

    sheetName = [i.sheet_names for i in xl]

    #print(sheetName)
    #print(len(sheetName))

    temp_df = [xl[i].parse(sheetName[i][len(sheetName[i])-1]) for i in range(len(fileName))]

    for i in range(len(temp_df)):
        temp_df[i]["fileName"] = fileName[i][fileName[i].rfind('/')+1:]

    return temp_df