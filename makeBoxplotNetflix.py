'''
This script takes directory as input and plot the boxplot of the different degradation scenarios.

This code is intended to plot the scenario of a single feature set.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
import matplotlib
matplotlib.rc('pdf', fonttype=42)
plt.rcParams.update({'font.size': 16})

def plotting_boxplot( list_correlation_coeficients, xaxis_labels, yaxis_label, yaxis_lim = None):
    fig1, ax1 = plt.subplots(figsize=(10,8))
    plt.ylim(yaxis_lim)
    ax1.set_ylabel(yaxis_label)
    ax1.boxplot(list_correlation_coeficients,labels=xaxis_labels)
    return fig1, ax1

def saving_boxplot(figure, axis, save_mode=None, coef_name=None, criteria_name=None):
    if save_mode==True:
        plt.savefig(feature_set_path+criteria_name+'_'+coef_name+'.pdf')
    else:
        plt.show()


path = 'C:/Users/Adm/Desktop/AutoEncoderVideo/Resultados/DB_Netflix/'
subfolder = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))]
#subfolder = ['Diivine','Diivine+SinnoM']
pathmetric = [path+name+'/' for name in subfolder]


degradations = ['HuangBufferBasedAdaptor',	'OracleVMAFViterbiQualityBasedAdaptor',	'SimpleThroughputBasedAdaptor','VMAFViterbiQualityBasedAdaptor', 'all']
labels=['HuangBuffer',	'OracleVMAF',	'Simple \n Throughput','VMAF', 'all']
for feature_set_path in pathmetric:
    pearsoncc = []
    spearmancc = []
    rmsecc = []
    for key in degradations:
        with open(feature_set_path+'adaptationAlgo_metrics.json') as json_file:
            json_data = json.load(json_file)
        pearsoncc.append(json_data[key]['pcc'])
        spearmancc.append(json_data[key]['scc'])
        rmsecc.append(json_data[key]['rmse'])
    # labels = [elements for elements in json_data.keys()]
    fig, axis = plotting_boxplot( pearsoncc, xaxis_labels=labels, yaxis_label='Pearson Coefficient',yaxis_lim = [0.6,1])
    saving_boxplot(fig, axis, save_mode=False, coef_name='pcc',criteria_name='adaptationAlgo')

    fig, axis = plotting_boxplot(spearmancc, xaxis_labels = labels, yaxis_label='Spearman Coefficient', yaxis_lim = [0.6,1])
    saving_boxplot(fig, axis,save_mode=False, coef_name='scc',criteria_name='adaptationAlgo')

    fig, axis = plotting_boxplot(rmsecc, xaxis_labels = labels, yaxis_label='RMSE')
    saving_boxplot(fig, axis,save_mode=False, coef_name='rmse',criteria_name='adaptationAlgo')

degradations = ['Trace_0', 'Trace_1', 'Trace_2', 'Trace_3', 'Trace_4', 'Trace_5', 'Trace_6', 'all']
labels= ['Trace_0', 'Trace_1', 'Trace_2', 'Trace_3', 'Trace_4', 'Trace_5', 'Trace_6', 'all']
for feature_set_path in pathmetric:
    pearsoncc = []
    spearmancc = []
    rmsecc = []
    for key in degradations:
        with open(feature_set_path+'netcond_metrics.json') as json_file:
            json_data = json.load(json_file)
        pearsoncc.append(json_data[key]['pcc'])
        spearmancc.append(json_data[key]['scc'])
        rmsecc.append(json_data[key]['rmse'])
    fig, axis = plotting_boxplot( pearsoncc, xaxis_labels=labels, yaxis_label='Pearson Coefficient',yaxis_lim = [0,1])
    saving_boxplot(fig, axis, save_mode=True, coef_name='pcc',criteria_name='netcond')

    fig, axis = plotting_boxplot(spearmancc, xaxis_labels = labels, yaxis_label='Spearman Coefficient', yaxis_lim = [0,1])
    saving_boxplot(fig, axis,save_mode=True, coef_name='scc',criteria_name='netcond')

    fig, axis = plotting_boxplot(rmsecc, xaxis_labels = labels, yaxis_label='RMSE')
    saving_boxplot(fig, axis,save_mode=True, coef_name='rmse',criteria_name='netcond')
