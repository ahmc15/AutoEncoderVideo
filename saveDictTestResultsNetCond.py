import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import pickle

Trace_0={'pcc': [], 'scc' : [], 'rmse':[]}
Trace_1={'pcc': [], 'scc' : [], 'rmse':[]}
Trace_2={'pcc': [], 'scc' : [], 'rmse':[]}
Trace_3={'pcc': [], 'scc' : [], 'rmse':[]}
Trace_4={'pcc': [], 'scc' : [], 'rmse':[]}
Trace_5={'pcc': [], 'scc' : [], 'rmse':[]}
Trace_6={'pcc': [], 'scc' : [], 'rmse':[]}
all={'pcc': [], 'scc' : [], 'rmse':[]}

for i in range(1,6):
    path ='C:/Users/Adm/Desktop/AutoEncoderVideo/Resultados/DB_Netflix/Diivine/'
    namefile = path+'netcond_testes'+str(i)+'-10.xlsx'
    try:
        excel_data_df = pd.read_excel(namefile, sheet_name='Sheet1')
        dicionario = excel_data_df.to_dict()
    except:
        excel_data_df = pd.read_excel(namefile, sheet_name='Planilha1')
        dicionario = excel_data_df.to_dict()
    foldername = path.split("/")[6]
    # excel_data_df = pd.read_excel(namefile, sheet_name='Sheet1')
    # dicionario = excel_data_df.to_dict()
    Trace_0['pcc'].append(abs(dicionario['statisticChart2'][1]))
    Trace_0['scc'].append(abs(dicionario['statisticChart2'][2]))
    Trace_0['rmse'].append(abs(dicionario['statisticChart2'][3]))

    Trace_1['pcc'].append(abs(dicionario['statisticChart3'][1]))
    Trace_1['scc'].append(abs(dicionario['statisticChart3'][2]))
    Trace_1['rmse'].append(abs(dicionario['statisticChart3'][3]))

    Trace_2['pcc'].append(abs(dicionario['statisticChart4'][1]))
    Trace_2['scc'].append(abs(dicionario['statisticChart4'][2]))
    Trace_2['rmse'].append(abs(dicionario['statisticChart4'][3]))

    Trace_3['pcc'].append(abs(dicionario['statisticChart5'][1]))
    Trace_3['scc'].append(abs(dicionario['statisticChart5'][2]))
    Trace_3['rmse'].append(abs(dicionario['statisticChart5'][3]))

    Trace_4['pcc'].append(abs(dicionario['statisticChart6'][1]))
    Trace_4['scc'].append(abs(dicionario['statisticChart6'][2]))
    Trace_4['rmse'].append(abs(dicionario['statisticChart6'][3]))

    Trace_5['pcc'].append(abs(dicionario['statisticChart7'][1]))
    Trace_5['scc'].append(abs(dicionario['statisticChart7'][2]))
    Trace_5['rmse'].append(abs(dicionario['statisticChart7'][3]))

    Trace_6['pcc'].append(abs(dicionario['statisticChart8'][1]))
    Trace_6['scc'].append(abs(dicionario['statisticChart8'][2]))
    Trace_6['rmse'].append(abs(dicionario['statisticChart8'][3]))

    all['pcc'].append(abs(dicionario['statisticChart9'][1]))
    all['scc'].append(abs(dicionario['statisticChart9'][2]))
    all['rmse'].append(abs(dicionario['statisticChart9'][3]))

mediafeatures={'Trace_0':Trace_0,'Trace_1':Trace_1,'Trace_2':Trace_2,'Trace_3':Trace_3,'Trace_4':Trace_4,'Trace_5':Trace_5,'Trace_6':Trace_6, 'all':all}
json_object = json.dumps(mediafeatures, indent = 4)

with open(path+"netcond_metrics.json", "w") as outfile:
    json.dump(mediafeatures, outfile,indent=4)
