restoredefaultpath;
clear variables;
clc

%Set variables selection Training
dataType=15;
for fold = 1:10
    % csvPath='/home/gpds/Documents/AutoEncoderVideo/src/';
    % dataPath='/home/gpds/Documents/AutoEncoderVideo/NormalizedVisualFeatures/';
    csvPath='C:\Users\Adm\Desktop\AutoEncoderVideo\src\';
    dataPath='C:\Users\Adm\Desktop\AutoEncoderVideo\Features\';
    %DeepNet path
    % DNPath = '/home/gpds/Documents/AutoEncoderVideo/Data/deepNet.mat';
     DNPath = strcat('C:\Users\Adm\Desktop\AutoEncoderVideo\Data\deepNet',num2str(fold),'.mat');

    %Set Database and build dataPath
    switch dataType
        case 0 %Test
            testDataset='DataTest.csv';
            dataPath=strcat(dataPath,'Experiment_3');
        case 1 %Video Experiment_1
            testDataset=strcat('test_',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'Experiment_1\');
        case 2 %Video Experiment_3
            testDataset=strcat('test_',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'Experiment_1_patch\');
        case 3 %Video with Experiment_1 Brisque feature set
            testDataset=strcat('test_',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'BrisqueFeatures\');
        case 4 %Video with Experiment_1 Zeina Media set
            testDataset=strcat('test_',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'ZeinaMedia\');
        case 5 %Video with Experiment_1 Zeina Patches set
            testDataset=strcat('test_',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'ZeinaPatches\');
        case 6 %Video with Experiment_1 Zeina Patches set
            testDataset=strcat('test_',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'DiivineBrisque\');
        case 7 %Video with Experiment_1 Zeina Patches set
            testDataset=strcat('test_',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'DiivineZeinaMedia\');
        case 8 %Video with Experiment_1 Zeina Patches set
            testDataset=strcat('test_',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'DiivineBrisqueZeinaMedia\');
        case 9 %Video with Experiment_1 Zeina Patches set
            testDataset=strcat('test_',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'DiivineBrisqueZeinaPatches\');            
        case 10 %Video with Experiment_1 Zeina Patches set
            testDataset=strcat('test_',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'DiivineFeatures\'); 
        case 11 %Video with Experiment_1 Zeina Patches set
            testDataset=strcat('test_',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'DiivineZeinaPatches\');             
        case 12 %Video with Experiment_1 Zeina Patches set
            testDataset=strcat('Netflix_test',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'DB_Netflix_DiivineSinnoM\'); 
        case 13 %Video with Netflix DIIVINE set
            testDataset=strcat('Netflix_test',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'DB_Netflix_Diivine\'); 
        case 14 %Video with Experiment1 DIIVINE, Temporal Brisque set
            testDataset=strcat('test_',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'DB_Experiment1\DiivineTemporalBrisque\');
        case 15 %Video with Experiment1 DIIVINE, Temporal Brisque set
            testDataset=strcat('test_',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'DB_Experiment1\DiivineSinnoMTemporalBrisque\');
    end

    dataTable=readtable(fullfile(csvPath,testDataset),'delimiter',';','ReadVariableNames',1); 

    disp('Testing...');

    %Test the AutoEncoder Model
    testResults = doTestAutoEncoder(DNPath,dataTable,dataPath);
    %Process the results 
    daeVideoMos = processModelOutput(testResults(:,1));
    %Save results to csv File
    dataTable.DAE_Video_cfv10_net = cell2mat(daeVideoMos(:,1));

    writetable(dataTable, strcat(csvPath,testDataset), 'delimiter', ';');
    disp('Test Complete');
    %Confusion Matrix (to do)
    %a=getConfusionMatrixData(cell2mat(daeVideoMos(:,1)));
    %b=getConfusionMatrixData(dataTable{:,'Mqs'});
    %confusionPlot(getConfusionMatrixData(cell2mat(daeVideoMos(:,1))),getConfusionMatrixData(dataTable{:,'Mqs'}));
end
%%
function resultsProcessed = processModelOutput(output)
[numFiles,~] = size(output);
resultsProcessed = cell(numFiles,2);
for i=1:numFiles
    fileModelResult = output{i,1};
    [~,cols] = size(fileModelResult);
    mosVector = zeros(1,cols);
    for j=1:cols
        [value,index] = max(fileModelResult(:,j));
        mosVector(1,j) = value + index;
    end
    resultsProcessed{i,1} = mean(mosVector);
    resultsProcessed{i,2} = mosVector;
end

end

%%
function outMat = getConfusionMatrixData(inputMat)
numGroups = 4;
[rows,~] = size(inputMat);
outMat = zeros(numGroups,rows);
for i=1:rows
    group=floor(inputMat(i,1));
    if (group==5)
        outMat(4,i)=1;
    elseif (group==0)
        outMat(1,i)=1;
    else
        outMat(group,i)=1;
    end
end
end

%%
function confusionPlot(testSet, targetSet)
%degTypes=Conditions';
plotconfusion(targetSet,testSet);
%xticklabels(degTypes)
%yticklabels(degTypes)
end