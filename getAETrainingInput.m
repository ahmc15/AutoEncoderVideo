function inputAE = getAETrainingInput(dataSet,dataPath,csvPath)

%Reads the data from the csv file
dataTable=readtable(fullfile(csvPath,dataSet),'delimiter',';','ReadVariableNames',1);
[trainingInput,trainingTarget]=getTrainingInput(dataTable,dataPath);

%Output Info
inputAE.trainingInput=trainingInput;
inputAE.trainingTarget=trainingTarget;

end


%%
% This function builds two matrices: trainingInput and targetInput
function [trainingInput,targetInput]=getTrainingInput(dataTable,dataPath)
% Initialize variables
fileExtension = '.mat';
numGroups = 4;
trainingInput=[];
targetInput=[];
numRows=size(dataTable,1);



for i=1:numRows
    %read file
    fileName=cell2mat(fullfile(dataPath,strcat(dataTable.testFile(i),fileExtension)));
    
    %Load visual features
    load(fileName);
    
    %Build matrix input
    trainingInput = [trainingInput, visualFeatures];
    [~, numFrames] = size(visualFeatures);
    %Build matrix target
    targetPerFile = zeros(numGroups, numFrames);
    trueMos = dataTable.Mqs(i);
    if (isnan(trueMos))
        trueMos = 3;
    end
    group=floor(trueMos);
    if (group==5)
        targetPerFile(numGroups,:) = 1;
    elseif (group==0)
        targetPerFile(1,:) = 1;
    else
        targetPerFile(group,:) = 1;
    end
    
    targetInput = [targetInput,targetPerFile];
    
end
end
