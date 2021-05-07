import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import pickle

packetloss={'pcc': [], 'scc' : [], 'rmse':[]}
freezing={'pcc': [], 'scc' : [], 'rmse':[]}
all={'pcc': [], 'scc' : [], 'rmse':[]}

for i in range(1,11):
    path ='C:/Users/Adm/Desktop/AutoEncoderVideo/Resultados/DB_Experiment1/Diivine+TemporalBrisque/'
    namefile = path+'testes'+str(i)+'-10.xlsx'
    try:
        excel_data_df = pd.read_excel(namefile, sheet_name='Sheet1')
        dicionario = excel_data_df.to_dict()
    except:
        excel_data_df = pd.read_excel(namefile, sheet_name='Planilha1')
        dicionario = excel_data_df.to_dict()
    foldername = path.split("/")[6]
    # excel_data_df = pd.read_excel(namefile, sheet_name='Sheet1')
    # dicionario = excel_data_df.to_dict()
    packetloss['pcc'].append(abs(dicionario['statisticChart2'][1]))
    packetloss['scc'].append(abs(dicionario['statisticChart2'][2]))
    packetloss['rmse'].append(abs(dicionario['statisticChart2'][3]))

    freezing['pcc'].append(abs(dicionario['statisticChart3'][1]))
    freezing['scc'].append(abs(dicionario['statisticChart3'][2]))
    freezing['rmse'].append(abs(dicionario['statisticChart3'][3]))

    all['pcc'].append(abs(dicionario['statisticChart4'][1]))
    all['scc'].append(abs(dicionario['statisticChart4'][2]))
    all['rmse'].append(abs(dicionario['statisticChart4'][3]))

mediafeatures={'packetloss':packetloss,'freezing':freezing, 'all':all}
json_object = json.dumps(mediafeatures, indent = 4)

with open(path+"metrics.json", "w") as outfile:
    json.dump(mediafeatures, outfile,indent=4)
