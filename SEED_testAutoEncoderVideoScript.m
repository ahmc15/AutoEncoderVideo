restoredefaultpath;
clear variables;
clc

%Set variables selection Training
dataType=13;
for seed = 1:10
for fold = 1:5
    csvPath='C:\Users\Adm\Desktop\AutoEncoderVideo\src\NetflixSeeds\';
    dataPath='C:\Users\Adm\Desktop\AutoEncoderVideo\Features\';
    resultPath='C:\Users\Adm\Desktop\AutoEncoderVideo\Resultados\';
    %DeepNet path
    DNPath = strcat('C:\Users\Adm\Desktop\AutoEncoderVideo\Data\seed',num2str(seed),'deepNet',num2str(fold),'.mat');

    %Set Database and build dataPath
    switch dataType 
        case 12 %Video with Experiment_1 Zeina Patches set
            testDataset=strcat('seed',num2str(seed),'Netflix_test',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'DB_Netflix_DiivineSinnoM\'); 
        case 13 %Video with Netflix DIIVINE set
            testDataset=strcat('seed',num2str(seed),'Netflix_test',num2str(fold),'.csv');
            dataPath=strcat(dataPath,'DB_Netflix_Diivine\'); 
    end

    dataTable=readtable(fullfile(csvPath,testDataset),'delimiter',';','ReadVariableNames',1);
    disp('Testing...');
    %Test the AutoEncoder Model
    testResults = doTestAutoEncoder(DNPath,dataTable,dataPath);
    %Process the results 
    daeVideoMos = processModelOutput(testResults(:,1));
    %Save results to csv File
    dataTable.DAE_Video_cfv10_net = cell2mat(daeVideoMos(:,1));
    writetable(dataTable, strcat(resultPath,testDataset), 'delimiter', ';');
    disp('Test Complete');   
end
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