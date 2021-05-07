import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
import matplotlib

matplotlib.rc('pdf', fonttype=42)
numberFolds = 5
packetloss={'pcc': np.zeros(numberFolds), 'scc' : np.zeros(numberFolds), 'rmse':np.zeros(numberFolds)}
freezing={'pcc': np.zeros(numberFolds), 'scc' : np.zeros(numberFolds), 'rmse':np.zeros(numberFolds)}

pearsoncc = []
spearmancc = []
rmsecc = []
labels = []

path = 'C:/Users/Adm/Desktop/AutoEncoderVideo/Resultados/DB_Netflix/'
subfolder = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))]
# subfolder = ['Diivine','Brisque+SinnoP',  'Diivine+Brisque', 'Diivine+SinnoM', 'Diivine+SinnoP','Diivine+Brisque+SinnoM', 'Diivine+Brisque+SinnoP',  'SinnoP', 'Diivine+SinnoM+TemporalBrisque','Diivine+TemporalBrisque']
subfolder = ['Diivine','Diivine+SinnoM']
# path = 'C:/Users/Adm/Desktop/AutoEncoderVideo/ResultadosMetricas/'
# subfolder = ['PSNR','SSIM','VIIDEO', 'DIIVINE', 'BIQI', 'BRISQUE','NIQE','NAVE','NAVEv2' ]
pathmetric = [path+name+'/' for name in subfolder]
# degradations = ['packetloss', 'freezing','all']
# degradations = ['Trace_0', 'Trace_1', 'Trace_2', 'Trace_3', 'Trace_4', 'Trace_5', 'Trace_6', 'all']
degradations = ['HuangBufferBasedAdaptor',	'OracleVMAFViterbiQualityBasedAdaptor',	'SimpleThroughputBasedAdaptor','VMAFViterbiQualityBasedAdaptor', 'all']
# labels=[label.replace('+','\n ') for label in subfolder]
# labels=['Feature \n set 1', 'Feature \n set 2', 'Feature \n set 3', 'Feature \n set 4', 'Feature \n set 5', 'Feature \n set 6', 'Feature \n set 7', 'Feature \n set 8', 'Feature \n set 9', 'Feature \n set 10' ]
labels=['Diivine', 'Diivine \n SinnoM']
plt.rcParams.update({'font.size': 16})
for key in degradations:
    pearsoncc = []
    spearmancc = []
    rmsecc = []
    for dir in pathmetric:
        with open(dir+'adaptationAlgo_metrics.json') as json_file:
            data = json.load(json_file)
        pearsoncc.append(data[key]['pcc'])
        spearmancc.append(data[key]['scc'])
        rmsecc.append(data[key]['rmse'])
    fig1, ax1 = plt.subplots(figsize=(10, 8))
    # ax1.set_title(key)
    plt.ylim([0.6,1])
    ax1.set_ylabel('Pearson Coefficient')
    # plt.xticks(rotation = 35,ha='right')
    ax1.boxplot(pearsoncc,labels=labels)
    # plt.show()
    plt.savefig(path+key+'adaptationAlgo__pcc.pdf')
    #
    fig1, ax1 = plt.subplots(figsize=(10, 8))
    # ax1.set_title(key)
    plt.ylim([0.6,1])
    ax1.set_ylabel('Spearman Coefficient')
    ax1.boxplot(spearmancc,labels=labels)
    # plt.show()
    plt.savefig(path+key+'adaptationAlgo__scc.pdf')
    #
    fig1, ax1 = plt.subplots(figsize=(10, 8))
    # ax1.set_title(key)
    # plt.ylim([0.2,0.9])
    ax1.set_ylabel('RMSE')
    # plt.xticks(rotation=15, ha='right' )
    ax1.boxplot(rmsecc,labels=labels)
    # plt.show()
    plt.savefig(path+key+'adaptationAlgo__rmse.pdf')
