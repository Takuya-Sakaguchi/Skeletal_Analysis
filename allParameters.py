



path = '/Users/TakuyaSakaguchi/PycharmProjects/Python3_skeleton/Data/'
path_density = '/Users/TakuyaSakaguchi/PycharmProjects/Python3_skeleton/Data/density/'
path_csv = '/Users/TakuyaSakaguchi/PycharmProjects/Python3_skeleton/Data/CSV/'

#df_density = convertPathToDF(path_density)

allListOfIndex = ['Image Name', 'Network Volume (mm3)', 'Skeletal Length (mm)',
       'Average Thickness (um)', 'Total Nodes', '3 Branch Nodes',
       '4 Branch Nodes', '5 Branch Nodes', '6+ branch Nodes',
       'Network Segments', 'Node-Node Segment #', 'Connecting Node 1',
       'Connecting Node 2', 'Node-Node Segment Length (um)',
       'Node-Node Segment Thickness (um)', 'Node-EP Segment #',
       'Connecting Node 1.1', 'Connecting EP 2', 'Node-EP Segment Length (um)',
       'Node-EP Segment Thickness (um)', 'Average connection length',
       'Average connection thickness', 'Average TB length',
       'Average TB thickness', "AverageNNLength", "AverageNELength",
       "AverageNNThickness", "AverageNEThickness", "NNNumber", "NENumber"]

listOfIndexfor_52 = [ 'Skeletal Length (mm)',
       'Average Thickness (um)', 'Total Nodes', '3 Branch Nodes',
       '4 Branch Nodes', 'Network Segments']


listOfIndex = ['Network Volume (mm3)', 'Skeletal Length (mm)',
       'Average Thickness (um)', 'Total Nodes', '3 Branch Nodes',
       '4 Branch Nodes', '5 Branch Nodes', '6+ branch Nodes','3branchRatio', '4branchRatio','3branchRatio',
        '4branchRatio', '5branchRatio', '6+branchRatio', "AverageNNLength", "AverageNELength",
       "AverageNNThickness", "AverageNEThickness", "NNNumber", "NENumber"]

ListOfDensityIndex = ['Image Name', 'Node-Node Connection ID', 'N-N Linearity',
       'Node-EP Connection ID', 'N-E Linearity', 'Radial Volume (voxels)',
       'Radial Radius (um)', 'Node ID', 'Nodes: Nodes/Radial Volume',
       'Nodes: N-N Voxels/Radial Volume', 'Nodes: N-E Voxels/Radial Volume',
       'Nodes: EP/Radial Volume', 'N-N ID', 'N-N Midpt: Nodes/Radial Volume',
       'N-N Midpt: N-N Voxels/Radial Volume',
       'N-N Midpt: N-E Voxels/Radial Volume', 'N-N Midpt: EP/Radial Volume',
       'N-E ID', 'N-E Midpt: Nodes/Radial Volume',
       'N-E Midpt: N-N Voxels/Radial Volume',
       'N-E Midpt: N-E Voxels/Radial Volume', 'N-E Midpt: EP/Radial Volume',
       'Mean N-N linearity', 'StDev Mean N-N linearity', 'Mean N-E linearity',
       'StDev Mean N-E linearity', 'Mean Linearity', 'StDev Mean Linearity',
       'Radial volume (voxels)', 'Radius (um)', 'Mean node density',
       'StDev mean node density', 'Mean N-N density', 'StDev mean N-N density',
       'Mean N-E density', 'StDev mean N-E density', 'Mean density',
       'StDev mean density', '# segments (>450)', '% segments (>450)',
       'Gen Col1', 'Gen Col2', 'Gen Col3', 'Nodes', 'N-N', 'N-E', 'Total',
       'Count Nodes', 'Count N-N', 'Count N-E', 'Get Value']


treatmentDic = {'NotchGFP_FLKRFP_1%DMSO_5dpf': 'DMSO',
 '051415 WT NotchR LRI2 d5 e1': 'WT',
 '051815 WT NotchR LRI2 d5 e3': 'WT',
 '051815 WT NotchR LRI2 d5 e4':'WT',
 '051915 WT NotchR LRI2 d5 e1':'WT',
 '051915 WT NotchR LRI2 d5 e2': 'WT',
 '052015 WT NotchR LRI2 d5 e3 2': 'WT',
 '052015 WT NotchR LRI2 d5 e4': 'WT',
 '052115 WT NotchR LRI2 d5 e2': 'WT',
 '052115 WT NotchR LRI2 d5 e3': 'WT',
 '052815 LRI2 NGFP d5 10uM olo e1':"Olo",
 '052915 LRI2 NGFP d5 10uM olo e2':'Olo',
 '061815 LRI2 NGFP d5 limk e1':'Limk',
 '061915 LRI2 NGFP d5 limk e2':'Limk',
 '062215 LRI2 NGFP d5 IPA3 e3':'IPA3',
 '062315 LRI2 NGFP d5 IPA3 e4':'IPA3',
 '062415 LRI2 NGFP d5 IPA3 e5':'IPA3',
 '062515 LRI2 NGFP d5 IPA3 e2':'IPA3',
 '062615 LRI2 NGFP d5 IPA3 e3':'IPA3',
 '062915 LRI2 NGFP d5 olo e1':'Olo',
 '062915 LRI2 NGFP d5 olo e2':'Olo',
 '063015 LRI2 NGFP d5 olo e3':'Olo',
 '063015 LRI2 NGFP d5 olo e4':'Olo',
 '070115 LRI2 NGFP d5 olo e5':'Olo',
 '070215 LRI2 NGFP d5 IPA3 e1':'Ipa3',
 '070215 LRI2 NGFP d5 limk e4':'Limk',
 '070615 LRI2 NGFP d5 limk e1':'Limk',
 '070615 LRI2 NGFP d5 limk e2':'Limk',
 '070715 LRI2 NGFP d5 DMSO e1':'DMSO',
 '070715 LRI2 NGFP d5 DMSO e2':'DMSO',
 '070815 LRI2 NGFP d5 DMSO e2':'DMSO',
 '070815 LRI2 NGFP d5 DMSO e4':'DMSO',
 '070915 LRI2 NGFP d5 DMSO e3':'DMSO',
 '071015 LRI2 NGFP d5 CE e2':'CE',
 '071015 LRI2 NGFP d5 CE e3':'CE',
 '071515 LRI2 NGFP d5 CE e1':'CE',
 '071515 LRI2 NGFP d5 CE e4':'CE',
 '071715 LRI2 NGFP d5 CE e1':'CE',
 'Olo_NGFP-LRI2_1':'Olo',
 '13013 notch flk1 wt d5':"WT"}



######################### all comments from here ###############################

'''
Image Name                          1 non-null object
Network Volume (mm3)                1 non-null float64
Skeletal Length (mm)                1 non-null float64
Average Thickness (um)              1 non-null float64
Total Nodes                         1 non-null float64
3 Branch Nodes                      1 non-null float64
4 Branch Nodes                      1 non-null float64
5 Branch Nodes                      1 non-null float64
6+ branch Nodes                     1 non-null float64
Network Segments                    1 non-null float64
Node-Node Segment #                 221 non-null float64
Connecting Node 1                   221 non-null float64
Connecting Node 2                   221 non-null float64
Node-Node Segment Length (um)       222 non-null float64
Node-Node Segment Thickness (um)    222 non-null float64
Node-EP Segment #                   154 non-null float64
Connecting Node 1.1                 154 non-null float64
Connecting EP 2                     154 non-null float64
Node-EP Segment Length (um)         155 non-null float64
Node-EP Segment Thickness (um)      155 non-null float64
'''

