import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import json
import pickle
import os
import matplotlib
matplotlib.rc('pdf', fonttype=42)
path = 'C:/Users/Adm/Desktop/AutoEncoderVideo/Resultados/DB_Experiment1/'
subfolder = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))]
pathmetric = [path+name+'/' for name in subfolder]
plt.rcParams.update({'font.size': 14})
for dir in pathmetric:
    try:
        h264={'ANC1': [],'HRC3': [],'HRC1': []}
        h265={'HRC5': [],'HRC4': [],'HRC2': []}
        for i in range(1,11):
            # path ='C:/Users/Adm/Desktop/AutoEncoderVideo/Resultados/Diivine+ZeinaMedia/'
            namefile = dir+'test_'+str(i)+'.csv'
            foldername = dir.split("/")[6]
            excel_data_df = pd.read_csv(namefile,sep=';')
            for row_label, row in excel_data_df.iterrows():
                if excel_data_df.loc[row_label,'videoDegradationType']=='packetLoss':
                    if excel_data_df.loc[row_label,'HRC']=='ANC1':
                        h264['ANC1'].append((excel_data_df.loc[row_label,'DAE_Video_cfv10_net'],excel_data_df.loc[row_label,'Mqs']))

                    elif excel_data_df.loc[row_label,'HRC']=='HRC3':
                        h264['HRC3'].append((excel_data_df.loc[row_label,'DAE_Video_cfv10_net'],excel_data_df.loc[row_label,'Mqs']))

                    elif excel_data_df.loc[row_label,'HRC']=='HRC1':
                        h264['HRC1'].append((excel_data_df.loc[row_label,'DAE_Video_cfv10_net'],excel_data_df.loc[row_label,'Mqs']))

                    elif excel_data_df.loc[row_label,'HRC']=='HRC5':
                        h265['HRC5'].append((excel_data_df.loc[row_label,'DAE_Video_cfv10_net'],excel_data_df.loc[row_label,'Mqs']))

                    elif excel_data_df.loc[row_label,'HRC']=='HRC4':
                        h265['HRC4'].append((excel_data_df.loc[row_label,'DAE_Video_cfv10_net'],excel_data_df.loc[row_label,'Mqs']))

                    elif excel_data_df.loc[row_label,'HRC']=='HRC2':
                        h265['HRC2'].append((excel_data_df.loc[row_label,'DAE_Video_cfv10_net'],excel_data_df.loc[row_label,'Mqs']))

        fig1, ax1 = plt.subplots(figsize=(8, 8))
        ax1.set_ylim([0,5])
        ax1.set_xlim([0,5])
        # ax1.set_title(foldername)
        ax1.set_xlabel('Prediction')
        ax1.set_ylabel('MOS')
        ax1.grid(True)
        ax1.scatter(*zip(*h265['HRC5']))
        ax1.scatter(*zip(*h265['HRC4']))
        ax1.scatter(*zip(*h265['HRC2']))
        ax1.legend(['H.265 HRC5 BR=8000kb/s, PLR=1%','H.265 HRC4 BR=1000kb/s, PLR=3%','H.265 HRC2 BR=400kb/s, PLR=8%'],loc='lower left')
        plt.savefig(dir+foldername+'_h265_packetLoss.pdf')

        fig1, ax1 = plt.subplots(figsize=(8,8))
        ax1.set_ylim([0,5])
        ax1.set_xlim([0,5])
        ax1.set_xlabel('Prediction')
        ax1.set_ylabel('MOS')
        ax1.grid(True)
        ax1.scatter(*zip(*h264['ANC1']))
        ax1.scatter(*zip(*h264['HRC3']))
        ax1.scatter(*zip(*h264['HRC1']))
        ax1.legend(['H.264 ANC1 BR=64000kb/s, PLR=0%','H.264 HRC3 BR=2000kb/s, PLR=5%','H.264 HRC1 BR=500kb/s, PLR=10%'],loc='lower left')
        # plt.show()
        plt.savefig(dir+foldername+'_h264_packetLoss.pdf')
    except:
        pass
