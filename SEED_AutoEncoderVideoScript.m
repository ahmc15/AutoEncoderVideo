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
for seed = 1:10
for fold = 1:5
csvPath='C:\Users\Adm\Desktop\AutoEncoderVideo\src\NetflixSeeds\';
dataPath='C:\Users\Adm\Desktop\AutoEncoderVideo\Features\';
disp('DAE-Model - Video');
disp('=================');

% Set trainDataset (csv files) and feature folder (dataPath)
selectedData=13;
  
switch selectedData 
    case 12 %Video with Netflix_2 DIIVINE+SinnoM set
        trainDataset=strcat('seed',num2str(seed),'Netflix_train',num2str(fold),'.csv');
        dataPath=strcat(dataPath,'DB_Netflix_DiivineSinnoM\');
    case 13 %Video with Netflix_2 DIIVINE+SinnoM set
        trainDataset=strcat('seed',num2str(seed),'Netflix_train',num2str(fold),'.csv');
        dataPath=strcat(dataPath,'DB_Netflix_Diivine\');
end
  
    %%
    %Get input for AE
    inputAE = getAETrainingInput(trainDataset,dataPath,csvPath);
    input = inputAE.trainingInput;
    target = inputAE.trainingTarget;
    save(strcat('Data\seed',num2str(seed),'videoData',num2str(fold),'.mat'),'inputAE');

    %%
    if (~isempty(input))
        dataAE=doAutoEncoderTraining(input);
        disp('Training AE completed...')
        softNet = doRegression(dataAE.f2, target);
        disp('Regression completed...')
        deepNet = doDeepNetTraining(dataAE.AE1, dataAE.AE2, softNet, input, target);
        save(strcat('Data\seed',num2str(seed),'deepNet',num2str(fold),'.mat'),'deepNet');
        disp('DeepNet completed...')
    end
end
end