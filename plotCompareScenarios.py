import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import json
import pickle
import os

path = 'C:/Users/Adm/Desktop/AutoEncoderVideo/Resultados/DB_Experiment1/'
subfolder = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))]
pathmetric = [path+name+'/' for name in subfolder]
plt.rcParams.update({'font.size': 14})
for dir in pathmetric:
    try:
        h264={'HRC3': [],'HRC9': []}
        h265={'HRC8': [],'HRC4': []}
        for i in range(1,11):
            # path ='C:/Users/Adm/Desktop/AutoEncoderVideo/Resultados/Diivine+ZeinaMedia/'
            namefile = dir+'test_'+str(i)+'.csv'
            foldername = dir.split("/")[6]
            excel_data_df = pd.read_csv(namefile,sep=';')
            for row_label, row in excel_data_df.iterrows():
                if excel_data_df.loc[row_label,'videoDegradationType']=='packetLoss':
                    if excel_data_df.loc[row_label,'HRC']=='HRC3':
                        h264['HRC3'].append((excel_data_df.loc[row_label,'DAE_Video_cfv10_net'],excel_data_df.loc[row_label,'Mqs']))

                    elif excel_data_df.loc[row_label,'HRC']=='HRC4':
                        h265['HRC4'].append((excel_data_df.loc[row_label,'DAE_Video_cfv10_net'],excel_data_df.loc[row_label,'Mqs']))

                if excel_data_df.loc[row_label,'videoDegradationType']=='frameFreezing':
                    if excel_data_df.loc[row_label,'HRC']=='HRC9':
                        h264['HRC9'].append((excel_data_df.loc[row_label,'DAE_Video_cfv10_net'],excel_data_df.loc[row_label,'Mqs']))

                    elif excel_data_df.loc[row_label,'HRC']=='HRC8':
                        h265['HRC8'].append((excel_data_df.loc[row_label,'DAE_Video_cfv10_net'],excel_data_df.loc[row_label,'Mqs']))



        fig1, ax1 = plt.subplots(figsize=(8, 8))
        ax1.set_ylim([0,5])
        ax1.set_xlim([0,5])
        # ax1.set_title(foldername)
        ax1.set_xlabel('Prediction')
        ax1.set_ylabel('MOS')
        ax1.grid(True)
        ax1.scatter(*zip(*h264['HRC3']))
        ax1.scatter(*zip(*h265['HRC4']))
        # ax1.scatter(*zip(*h265['HRC2']))
        ax1.legend(['H.264 HRC3 BR=2000kb/s, PLR=5%','H.265 HRC4 BR=1000kb/s, PLR=3%'],loc='lower left')
        # plt.savefig(dir+foldername+'_packetLoss.pdf')
        plt.show()

        # fig1, ax1 = plt.subplots(figsize=(8,8))
        # ax1.set_ylim([0,5])
        # ax1.set_xlim([0,5])
        # ax1.set_xlabel('Prediction')
        # ax1.set_ylabel('MOS')
        # ax1.grid(True)
        # # ax1.scatter(*zip(*h264['ANC1']))
        # ax1.scatter(*zip(*h264['HRC9']))
        # ax1.scatter(*zip(*h265['HRC8']))
        # # ax1.legend(['h264 ANC1 BR=64000kb/s, PLR=0%','h264 HRC3 BR=2000kb/s, PLR=5%','h264 HRC1 BR=500kb/s, PLR=10%'],loc='lower left')
        # ax1.legend(['H.264 HRC9 BR=2000kb/s, N=2, P=1-3, L=1-3', 'H.265 HRC8 BR=1000kb/s, N=2, P=2-3, L=2-2'],loc='lower left')
        #
        # # plt.show()
        # plt.savefig(dir+foldername+'_FrameFreezing.pdf')

    except:
        pass
