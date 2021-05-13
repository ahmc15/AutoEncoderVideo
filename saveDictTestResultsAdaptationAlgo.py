import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import pickle

HuangBufferBasedAdaptor={'pcc': [], 'scc' : [], 'rmse':[]}
OracleVMAFViterbiQualityBasedAdaptor={'pcc': [], 'scc' : [], 'rmse':[]}
SimpleThroughputBasedAdaptor={'pcc': [], 'scc' : [], 'rmse':[]}
VMAFViterbiQualityBasedAdaptor={'pcc': [], 'scc' : [], 'rmse':[]}
all={'pcc': [], 'scc' : [], 'rmse':[]}

for seed in range(1,11):
    for fold in range(1,6):
        path ='C:/Users/Adm/Desktop/AutoEncoderVideo/Resultados/'
        namefile = path+'adaptationAlgo_seed'+str(seed)+'Netflix_test'+str(fold)+'_10.xlsx'
        try:
            excel_data_df = pd.read_excel(namefile, sheet_name='Sheet1')
            dicionario = excel_data_df.to_dict()
        except:
            excel_data_df = pd.read_excel(namefile, sheet_name='Planilha1')
            dicionario = excel_data_df.to_dict()
        foldername = path.split("/")[6]
        # excel_data_df = pd.read_excel(namefile, sheet_name='Sheet1')
        # dicionario = excel_data_df.to_dict()
        HuangBufferBasedAdaptor['pcc'].append(abs(dicionario['statisticChart2'][1]))
        HuangBufferBasedAdaptor['scc'].append(abs(dicionario['statisticChart2'][2]))
        HuangBufferBasedAdaptor['rmse'].append(abs(dicionario['statisticChart2'][3]))

        OracleVMAFViterbiQualityBasedAdaptor['pcc'].append(abs(dicionario['statisticChart3'][1]))
        OracleVMAFViterbiQualityBasedAdaptor['scc'].append(abs(dicionario['statisticChart3'][2]))
        OracleVMAFViterbiQualityBasedAdaptor['rmse'].append(abs(dicionario['statisticChart3'][3]))

        SimpleThroughputBasedAdaptor['pcc'].append(abs(dicionario['statisticChart4'][1]))
        SimpleThroughputBasedAdaptor['scc'].append(abs(dicionario['statisticChart4'][2]))
        SimpleThroughputBasedAdaptor['rmse'].append(abs(dicionario['statisticChart4'][3]))

        VMAFViterbiQualityBasedAdaptor['pcc'].append(abs(dicionario['statisticChart5'][1]))
        VMAFViterbiQualityBasedAdaptor['scc'].append(abs(dicionario['statisticChart5'][2]))
        VMAFViterbiQualityBasedAdaptor['rmse'].append(abs(dicionario['statisticChart5'][3]))

        all['pcc'].append(abs(dicionario['statisticChart6'][1]))
        all['scc'].append(abs(dicionario['statisticChart6'][2]))
        all['rmse'].append(abs(dicionario['statisticChart6'][3]))

mediafeatures={'HuangBufferBasedAdaptor':HuangBufferBasedAdaptor, 'OracleVMAFViterbiQualityBasedAdaptor':OracleVMAFViterbiQualityBasedAdaptor,
                'SimpleThroughputBasedAdaptor':SimpleThroughputBasedAdaptor, 'VMAFViterbiQualityBasedAdaptor':VMAFViterbiQualityBasedAdaptor, 'all':all}
json_object = json.dumps(mediafeatures, indent = 4)

with open(path+"adaptationAlgo_metrics.json", "w") as outfile:
    json.dump(mediafeatures, outfile,indent=4)
