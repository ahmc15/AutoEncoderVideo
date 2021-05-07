import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import pickle
import os



path = 'C:/Users/Adm/Desktop/AutoEncoderVideo/Resultados/DB_Experiment1/'
subfolder = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))]
pathmetric = [path+name+'/' for name in subfolder]
for dir in pathmetric:
    packetloss={'pcc': [], 'scc' : [], 'rmse':[]}
    freezing={'pcc': [], 'scc' : [], 'rmse':[]}
    all={'pcc': [], 'scc' : [], 'rmse':[]}

    for i in range(1,11):
        namefile = dir+'testes'+str(i)+'-10.xlsx'
        try:
            excel_data_df = pd.read_excel(namefile, sheet_name='Sheet1')
            dicionario = excel_data_df.to_dict()
        except:
            excel_data_df = pd.read_excel(namefile, sheet_name='Planilha1')
            dicionario = excel_data_df.to_dict()
        packetloss['pcc'].append(dicionario['statisticChart2'][1])
        packetloss['scc'].append(dicionario['statisticChart2'][2])
        packetloss['rmse'].append(dicionario['statisticChart2'][3])

        freezing['pcc'].append(dicionario['statisticChart3'][1])
        freezing['scc'].append(dicionario['statisticChart3'][2])
        freezing['rmse'].append(dicionario['statisticChart3'][3])

        all['pcc'].append(dicionario['statisticChart4'][1])
        all['scc'].append(dicionario['statisticChart4'][2])
        all['rmse'].append(dicionario['statisticChart4'][3])

    packetloss['pcc'] = np.mean(np.array(packetloss['pcc']))
    packetloss['scc'] = np.mean(np.array(packetloss['scc']))
    packetloss['rmse'] = np.mean(np.array(packetloss['rmse']))

    freezing['pcc'] = np.mean(np.array(freezing['pcc']))
    freezing['scc'] = np.mean(np.array(freezing['scc']))
    freezing['rmse'] = np.mean(np.array(freezing['rmse']))

    all['pcc'] = np.mean(np.array(all['pcc']))
    all['scc'] = np.mean(np.array(all['scc']))
    all['rmse'] = np.mean(np.array(all['rmse']))

    mediafeatures={'packetloss':packetloss,'freezing':freezing, 'all':all}
    json_object = json.dumps(mediafeatures, indent = 4)

    with open(dir+"Overallmetrics.json", "w") as outfile:
        json.dump(mediafeatures, outfile,indent=4)
