__author__ = 'TakuyaSakaguchi'

import pandas as pd

from Old_files.FileList import getExcelFileNamesInFolder


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

    return temp_df

def main():
    path = '/Users/TakuyaSakaguchi/PycharmProjects/Python3_skeleton/Data/'
    path_density = '/Users/TakuyaSakaguchi/PycharmProjects/Python3_skeleton/Data/density/'


    df = convertPathToDF(path)
    df_density = convertPathToDF(path_density)


    df_name=[]
    for i in range(len(df)):
        print (df[i]['Image Name'][0])
        df_name.append(df[i]['Image Name'][0])
    print(df_name)

    print(df_density[0]['N-E ID'])

if __name__ == "__main__":
    main()

    