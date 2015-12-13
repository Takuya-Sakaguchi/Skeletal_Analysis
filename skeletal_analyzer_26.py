


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from FileIO import convertPathToDF
from FileIO import getExcelFileNamesInFolder
from allParameters import *





def getImageNames(givenDf):
    # from given df, take out 'Image Name' and return as a list.
    df_name = []
    for i in range(len(givenDf)):
        #print(df[i]['Image Name'][0])
        df_name.append(givenDf[i]['Image Name'][0])
    return df_name


def collectValuesFromDfSet(givenValue, givenDF):
    # give value to extract and DataFrame working,
    # this function return new DataFrame containing tow Series, "FileNamePy" and the asked value
    tempValueList = []
    tempNameList = []
    for i in range(len(givenDF)):
        tempValueList.append(givenDF[i][givenValue][0])
        tempNameList.append(givenDF[i]["Image Name"][0])
    tempDf = pd.DataFrame({'FileNamePy':tempNameList, givenValue:tempValueList})
    return tempDf

def collectValuesFromDfSet2(givenValue, givenDF):
    # give value to extract and DataFrame working,
    # this function return new DataFrame containing tow Series, "FileNamePy" and the asked value
    tempValueList = []
    tempNameList = []
    tempTreatmentList = []
    for i in range(len(givenDF)):
        tempValueList.append(givenDF[i][givenValue][0])
        tempNameList.append(givenDF[i]["Image Name"][0])
        tempTreatmentList.append((givenDF[i]["treatment"][0]))
    tempDf = pd.DataFrame({'FileNamePy':tempNameList, givenValue:tempValueList, 'treatment':tempTreatmentList})
    return tempDf

def collectValuesFromDfSet3(givenValue, givenDF):
    # give value to extract and DataFrame working,
    # this function return new DataFrame containing tow Series, "FileNamePy" and the asked value
    tempValueList = []
    tempNameList = []
    tempTypeList = []
    for i in range(len(givenDF)):
        tempValueList.append(givenDF[i][givenValue][0])
        tempNameList.append(givenDF[i]["Image Name"][0])
        tempTypeList.append((givenDF[i]["type"][0]))
    tempDf = pd.DataFrame({'FileNamePy':tempNameList, givenValue:tempValueList, 'type':tempTypeList})
    return tempDf




def matlibBarPlot(givenIndex, givenDf):
    plt.barh(np.arange(len(givenDf)), givenDf[givenIndex], align = "center")
    plt.yticks(np.arange(len(givenDf)), givenDf["FileNamePy"])
    plt.xlabel(givenIndex)
    plt.show()

def matlibBarPlot2(givenIndex, givenDf, figNumber):
    plt.figure(figNumber)
    plt.barh(np.arange(len(givenDf)), givenDf[givenIndex], align = "center")
    plt.yticks(np.arange(len(givenDf)), givenDf["treatment"])
    plt.xlabel(givenIndex)


def matlibBarPlot3(givenIndex, givenDf, figNumber):
    plt.figure(figNumber)
    plt.barh(np.arange(len(givenDf)), givenDf[givenIndex], align = "center")
    plt.yticks(np.arange(len(givenDf)), givenDf["type"])
    plt.xlabel(givenIndex)



def getSkeletalVersion(givenOneDf):
    #give only one df and return the version number as a string, "5.3" or "5.2"
    columnList = givenOneDf.columns

    if "6+ branch Nodes" in columnList:
        return "5.3"
    elif "5+ branch Nodes" in columnList:
        return "5.2"
    else:
        return KeyError



def addAllBranchRatioToDf(givenDf):
    for i in range(len(givenDf)):
        givenDf[i]['3branchRatio'] = givenDf[i]['3 Branch Nodes'] / givenDf[i]['Total Nodes'] *100
        givenDf[i]['4branchRatio'] = givenDf[i]['4 Branch Nodes'] / givenDf[i]['Total Nodes'] *100
        givenDf[i]['5branchRatio'] = givenDf[i]['5 Branch Nodes'] / givenDf[i]['Total Nodes'] *100
        givenDf[i]['6+branchRatio'] = givenDf[i]['6+ branch Nodes'] / givenDf[i]['Total Nodes'] *100
    return givenDf


def convert52To53(givenDf):
    #input df containing both 5.2 and 5.3 datasheets.
    # this function convert 5.2 format to 5.3 and retrun df.
    for i in range(len(givenDf)):
        if getSkeletalVersion(givenDf[i]) == "5.3":
            givenDf[i]["VersionPy"] = "5.3"
        elif getSkeletalVersion(givenDf[i]) == "5.2":
            givenDf[i]=givenDf[i].rename(columns = {"5+ branch Nodes":"5 Branch Nodes"})
            givenDf[i]=givenDf[i].rename(columns = {'Vascular Segments':'Network Segments'})
            givenDf[i]=givenDf[i].rename(columns = {'Vascular Volume (mm3)':'Network Volume (mm3)'})
            givenDf[i]["VersionPy"] = "5.2 to 5.3"
            givenDf[i]["6+ branch Nodes"] = 0
    return givenDf



def listUpNameAndVersion(givenDf):
    for i in range(len(givenDf)):
            print(getSkeletalVersion(givenDf[i]), givenDf[i]["Image Name"][0])


def addAverageAndNumberToDf(givenDf):
    for i in range(len(givenDf)):
        givenDf[i]["AverageNNLength"] = givenDf[i]['Node-Node Segment Length (um)'].mean(axis = 0)
        givenDf[i]["AverageNELength"] = givenDf[i]['Node-EP Segment Length (um)'].mean(axis = 0)
        givenDf[i]["AverageNNThickness"] = givenDf[i]['Node-Node Segment Thickness (um)'].mean(axis = 0)
        givenDf[i]["AverageNEThickness"] = givenDf[i]['Node-EP Segment Thickness (um)'].mean(axis = 0)
        givenDf[i]["NNNumber"] = givenDf[i]['Node-Node Segment Length (um)'].count()
        givenDf[i]["NENumber"] = givenDf[i]['Node-EP Segment Length (um)'].count()

    return givenDf



def printOutVersion(givenDf):
    for givenDf in df_total:
        print(givenDf["fileName"][0], " ", getSkeletalVersion(givenDf))




def pathToDfWith53ConversionRatioAverage_integration(givenPath):
    tempDf = []
    tempDf = convertPathToDF(givenPath)
    tempDf = convert52To53(tempDf)
    tempDf = addAllBranchRatioToDf(tempDf)
    tempDf = addAverageAndNumberToDf(tempDf)
    return tempDf


############ main lines #############################


path_CDK_CB = '/Users/TakuyaSakaguchi/PycharmProjects/Skeletal_Analysis/CDK5DATA/' \
              'CDK5_paper_data/Cassandra_CDK5Organizer_files/Liver_analysis_excel/'


path_CDK_IG = '/Users/TakuyaSakaguchi/PycharmProjects/Skeletal_Analysis/CDK5DATA/' \
              'CDK5_paper_data/Isabel_LRI2Organier_files/Liver_analysis_excel/'

ref_excel_cb = '/Users/TakuyaSakaguchi/PycharmProjects/Skeletal_Analysis/CDK5DATA/CDK5 skeleton organizer 2015 v2.xls'

ref_excel_ig = '/Users/TakuyaSakaguchi/PycharmProjects/Skeletal_Analysis/' \
               'CDK5DATA/NorchR-LRI2 skeleton organizer 2015 v2.xls'

df_cb = pathToDfWith53ConversionRatioAverage_integration(path_CDK_CB)

df_ig = pathToDfWith53ConversionRatioAverage_integration(path_CDK_IG)





pickle.dump(df_cb,open('dfCDK5CB_pickle.p','wb'))
pickle.dump(df_ig,open('dfCDK5IG_pickle.p','wb'))



xl = pd.ExcelFile(ref_excel_cb)
df_ref_cb = xl.parse('Sheet1')

xl = pd.ExcelFile(ref_excel_ig)
df_ref_ig = xl.parse('Sheet1')


for i in range(len(df_cb)):
    df_cb[i]["type"] = str(df_ref_cb[df_ref_cb["Liver analysis excel file"]==df_cb[i].fileName[0]]["pyType"].values)

for i in range(len(df_ig)):
    df_ig[i]["type"] = str(df_ref_ig[df_ref_ig["Liver analysis excel file"]==df_ig[i].fileName[0]]["pyType"].values)


df_total = df_cb + df_ig

plt.style.use('ggplot')

'''
figCounter = 0

for item in listOfIndex:
    newDf = collectValuesFromDfSet3(item, df_cb)
    newDf = newDf.sort_values('type')
    newDf.index = range(0, len(newDf))
    matlibBarPlot3(item, newDf, figCounter)
    figCounter += 1

plt.show()

figCounter = 0
for item in listOfIndex:
    newDf = collectValuesFromDfSet3(item, df_ig)
    newDf = newDf.sort_values('type')
    newDf.index = range(0, len(newDf))
    matlibBarPlot3(item, newDf, figCounter)
    figCounter += 1
plt.show()

figCounter = 0
for item in listOfIndex:
    newDf = collectValuesFromDfSet3(item, df_total)
    newDf = newDf.sort_values('type')
    newDf.index = range(0, len(newDf))
    matlibBarPlot3(item, newDf, figCounter)
    figCounter += 1
plt.show()

print(type(df_total))
print(df_total[0])




plt.show()

'''



'''
for item in listOfIndex:
    newDf = collectValuesFromDfSet(item, df_total)
    matlibBarPlot(item, newDf)
'''


'''
#print(df[0]['VersionPy'][0])
for i in range(len(df)):
    print(df[i]['Image Name'][0], df[i]['VersionPy'][0])

First_Df = collectValuesFromDfSet('4branchRatio', df)
Second_Df = collectValuesFromDfSet('NNNumber', df)


#print(skeletalLengthDf)
#print(NNNumberDf)
integratedDf = pd.concat([First_Df,Second_Df["NNNumber"]], axis = 1)
print(integratedDf)

print(integratedDf[1:3])

plt.scatter(integratedDf['4branchRatio'], integratedDf["NNNumber"])
plt.show()

'''

'''
'Skeletal Length (mm)',
       'Average Thickness (um)', 'Total Nodes', '3 Branch Nodes',
       '4 Branch Nodes', '5 Branch Nodes', '6+ branch Nodes','3branchRatio', '4branchRatio','3branchRatio',
        '4branchRatio', '5branchRatio', '6+branchRatio', "AverageNNLength", "AverageNELength",
       "AverageNNThickness", "AverageNEThickness", "NNNumber",
'''

'''
for item in listOfIndex:
    newDf = collectValuesFromDfSet(item, df)
    matlibBarPlot(item, newDf)
'''

'''
df_density = convertPathToDF(path_density)

for i in range(len(df_density)):
    print(df_density[i]['Image Name'][0])

print(getExcelFileNamesInFolder(path_density))

longFileName = getExcelFileNamesInFolder(path_density)
shortFileName = []
for item in longFileName:
    shortFileName.append(item[item.rindex("/")+1:])
print(shortFileName)

for i in range(len(df_density)):
    df_density[i]["OriginalFileName"] = shortFileName[i]

for i in range(len(df_density)):
    print(df_density[i]["OriginalFileName"][0], df_density[i]["Image Name"][0])

imageNameList = []
for i in range(len(df)):
    print(df[i]["Image Name"][0])
    imageNameList.append(df[i]["Image Name"][0])

print(imageNameList)


pickle.dump(treatmentDic,open('treatmentDic.p','wb'))

treatmentList = ['WT','DMSO','Olo', 'Ipa3', 'Limk', 'CE']

pickle.dump(treatmentList, open('treatmentList.p','wb'))

for i in range(len(df)):
    print(treatmentDic[df[i]["Image Name"][0]])
    df[i]["treatment"]=treatmentDic[df[i]["Image Name"][0]]

print(df[0]["treatment"][0])

panelDic = {}
for i in range(len(df)):
    panelDic[df[i]["treatment"][0] + str(i)] = df[i]


#wp = pd.Panel({"DMSO1": df[0],"WT1":df[1]})
wp = pd.Panel(panelDic)

print(wp.describe)
print(wp['DMSO0']['treatment'][0])

numberContainingOlo = []
for i in range(len(df)):
    if df[i]["treatment"][0] == 'Olo':
        numberContainingOlo.append(i)

print(numberContainingOlo)

totalNodesOlo = []
for i in numberContainingOlo:
    totalNodesOlo.append(df[i]['Total Nodes'][0])

totalNodesOlo = np.array(totalNodesOlo)
print(totalNodesOlo)
print(totalNodesOlo.mean())
print(totalNodesOlo.std())


figCounter = 1




for item in listOfIndex:
    newDf = collectValuesFromDfSet2(item, df)
    newDf = newDf.sort_values('treatment')
    newDf.index = range(0, len(newDf))
    matlibBarPlot2(item, newDf, figCounter)
    figCounter += 1


plt.show()

'''


"""
for item in listOfIndex:
    newDf = collectValuesFromDfSet(item, df)
    matlibBarPlot(item, newDf)
"""
