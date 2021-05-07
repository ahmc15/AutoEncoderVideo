import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import json
import pickle
import os

path = 'C:/Users/Adm/Desktop/AutoEncoderVideo/Resultados/'
subfolder = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))]
pathmetric = [path+name+'/' for name in subfolder]
plt.rcParams.update({'font.size': 10})
#
for dir in pathmetric:
    try:
        h264=[]
        h265=[]

        for i in range(1,11):
            # path ='C:/Users/Adm/Desktop/AutoEncoderVideo/Resultados/Diivine+ZeinaMedia/'
            namefile = dir+'test_'+str(i)+'.csv'
            foldername = dir.split("/")[6]
            excel_data_df = pd.read_csv(namefile,sep=';')

            for row_label, row in excel_data_df.iterrows():
                if excel_data_df.loc[row_label,'videoCodec']=='H.264':
                    h264.append((excel_data_df.loc[row_label,'DAE_Video_cfv10_net'],excel_data_df.loc[row_label,'Mqs']))
                elif excel_data_df.loc[row_label,'videoCodec']=='H.265':
                    h265.append((excel_data_df.loc[row_label,'DAE_Video_cfv10_net'],excel_data_df.loc[row_label,'Mqs']))
        # print(h265)
        # x=[]
        # y=[]
        # x = [point[0] for point in h265]
        # y = [point[1] for point in h265]
        #  x2,y2 = zip(*h264)
        fig1, ax1 = plt.subplots(figsize=(10, 8))
        plt.ylim([0,5])
        plt.xlim([0,5])
        ax1.set_title(foldername)
        ax1.set_xlabel('Prediction')
        ax1.set_ylabel('MOS')
        plt.scatter(*zip(*h265))
        plt.scatter(*zip(*h264))
        plt.legend(['h265','h264'],loc='lower left')
        # plt.show()
        plt.savefig(dir+'scatterplot.pdf')
    except:
        pass
