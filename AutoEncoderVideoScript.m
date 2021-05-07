restoredefaultpath;
clear variables;
clc

%%
%%% Path variables
% - csvPath: path to the folder where the csv file is located. A cvs file
% lists all files considered for the training and testing of the model.
%
% - dataPath: path to the folder where the extracted features are located.

% csvPath='/home/gpds/Documents/AutoEncoderVideo/src/';
% dataPath='/home/gpds/Documents/AutoEncoderVideo/NormalizedVisualFeatures/';
% csvPath='C:\Users\Adm\Desktop\AutoEncoderVideo\src\';
% dataPath='C:\Users\Adm\Desktop\AutoEncoderVideo\VisualFeatures\';
for i = 1:10
csvPath='C:\Users\Adm\Desktop\AutoEncoderVideo\src\';
dataPath='C:\Users\Adm\Desktop\AutoEncoderVideo\Features\';
disp('DAE-Model - Video');
disp('=================');

% Set trainDataset (csv files) and feature folder (dataPath)
selectedData=15;
  
switch selectedData
    case 0 %Test
        trainDataset='DataTrain.csv';
        dataPath=strcat(dataPath,'Experiment_3');
    case 1 %Video with Experiment_1 set
%         trainDataset='Experiment_1.csv';
        trainDataset=strcat('train_',num2str(i),'.csv');
        dataPath=strcat(dataPath,'Experiment_1');
    case 2 %Video with Experiment_1 Patch feature set
        trainDataset=strcat('train_',num2str(i),'.csv');
        dataPath=strcat(dataPath,'Experiment_1_patch\');
    case 3 %Video with Experiment_1 Brisque  set
        trainDataset=strcat('train_',num2str(i),'.csv');
        dataPath=strcat(dataPath,'BrisqueFeatures\');
    case 4 %Video with Experiment_1 Zeina Media set
        trainDataset=strcat('train_',num2str(i),'.csv');
        dataPath=strcat(dataPath,'ZeinaMedia\');
    case 5 %Video with Experiment_1 Zeina Patches set
        trainDataset=strcat('train_',num2str(i),'.csv');
        dataPath=strcat(dataPath,'ZeinaPatches\');
    case 6 %Video with Experiment_1 Zeina Patches set
        trainDataset=strcat('train_',num2str(i),'.csv');
        dataPath=strcat(dataPath,'DiivineBrisque\');
    case 7 %Video with Experiment_1 Zeina Patches set
        trainDataset=strcat('train_',num2str(i),'.csv');
        dataPath=strcat(dataPath,'DiivineZeinaMedia\');
    case 8 %Video with Experiment_1 Zeina Patches set
        trainDataset=strcat('train_',num2str(i),'.csv');
        dataPath=strcat(dataPath,'DiivineBrisqueZeinaMedia\');
    case 9 %Video with Experiment_1 Zeina Patches set
        trainDataset=strcat('train_',num2str(i),'.csv');
        dataPath=strcat(dataPath,'DiivineBrisqueZeinaPatches\'); 
    case 10 %Video with Experiment_1 Zeina Patches set
        trainDataset=strcat('train_',num2str(i),'.csv');
        dataPath=strcat(dataPath,'DiivineFeatures\');         
    case 11 %Video with Experiment_1 Zeina Patches set
        trainDataset=strcat('train_',num2str(i),'.csv');
        dataPath=strcat(dataPath,'DiivineZeinaPatches\'); 
    case 12 %Video with Netflix_2 DIIVINE+SinnoM set
        trainDataset=strcat('Netflix_train',num2str(i),'.csv');
        dataPath=strcat(dataPath,'DB_Netflix_DiivineSinnoM\');
    case 13 %Video with Netflix_2 DIIVINE+SinnoM set
        trainDataset=strcat('Netflix_train',num2str(i),'.csv');
        dataPath=strcat(dataPath,'DB_Netflix_Diivine\');
    case 14 %Video with Netflix_2 DIIVINE+SinnoM set
        trainDataset=strcat('train_',num2str(i),'.csv');
        dataPath=strcat(dataPath,'DB_Experiment1\DiivineTemporalBrisque\');
    case 15 %Video with Netflix_2 DIIVINE+SinnoM set
        trainDataset=strcat('train_',num2str(i),'.csv');
        dataPath=strcat(dataPath,'DB_Experiment1\DiivineSinnoMTemporalBrisque\');
end
  
    %%
    %Get input for AE
    inputAE = getAETrainingInput(trainDataset,dataPath,csvPath);
    input = inputAE.trainingInput;
    target = inputAE.trainingTarget;
    save(strcat('Data\videoData',num2str(i),'.mat'),'inputAE');

    %%
    if (~isempty(input))
        dataAE=doAutoEncoderTraining(input);
        disp('Training AE completed...')
        softNet = doRegression(dataAE.f2, target);
        disp('Regression completed...')
        deepNet = doDeepNetTraining(dataAE.AE1, dataAE.AE2, softNet, input, target);
        save(strcat('Data\deepNet',num2str(i),'.mat'),'deepNet');
        disp('DeepNet completed...')
    end
end