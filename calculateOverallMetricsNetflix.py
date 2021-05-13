import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import pickle
import os

def dict_from_excel(file_path):
    try:
        excel_data_df = pd.read_excel(file_path, sheet_name='Sheet1')
        dicionario = excel_data_df.to_dict()
    except:
        excel_data_df = pd.read_excel(file_path, sheet_name='Planilha1')
        dicionario = excel_data_df.to_dict()
    return dicionario
def create_subpath(mainpath):
    list_subfolder = [subfolder for subfolder in os.listdir(mainpath) if os.path.isdir(os.path.join(mainpath,subfolder))]
    list_path_subfolder = [mainpath+subfolder+'/' for subfolder in list_subfolder]
    return list_path_subfolder

mainpath = 'C:/Users/Adm/Desktop/AutoEncoderVideo/Resultados/Seeds/'
pathmetric = create_subpath(mainpath)
for dir in pathmetric:
    all={'pcc': [], 'scc' : [], 'rmse':[]}
    for seed in range(1,11):
        for fold in range(1,6):
            namefile = dir+'adaptationAlgo_seed'+str(seed)+'Netflix_test'+str(fold)+'_10.xlsx'
            dicionario = dict_from_excel(namefile)
            all['pcc'].append(abs(dicionario['statisticChart6'][1]))
            all['scc'].append(abs(dicionario['statisticChart6'][2]))
            all['rmse'].append(abs(dicionario['statisticChart6'][3]))

# asd=[elem for elem in dicionario.keys()]
    all['pcc'] = np.mean(np.array(all['pcc']))
    all['scc'] = np.mean(np.array(all['scc']))
    all['rmse'] = np.mean(np.array(all['rmse']))

    mediafeatures={'all':all}
    json_object = json.dumps(mediafeatures, indent = 4)

    with open(dir+"Overallmetrics.json", "w") as outfile:
        json.dump(mediafeatures, outfile,indent=4)
