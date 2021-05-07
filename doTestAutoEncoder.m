function [resultMat] = doTestAutoEncoder(deepNet,dataTable,dataPath)

resultMat=testDeepNet(deepNet,dataTable,dataPath);

end

%%
function testResponse = testDeepNet(deepNet,dataTable,dataPath)
fileExtension = '.mat';
load(deepNet);
numRows=size(dataTable,1);
testResponse = cell(numRows,1);
for i=1:numRows
    fileName=cell2mat(fullfile(dataPath,strcat(dataTable.testFile(i),fileExtension)));
    load(fileName);
    responseDeepNet=deepNet(visualFeatures);
    
    %Build true responsoe for comparisson
    [row, col] = size(responseDeepNet);
    responseTrue=zeros(row,col);
    trueMos=dataTable.Mqs(i);
    if (isnan(trueMos))
        trueMos = 3;
    end
    group=floor(trueMos);
    if (group==5)
        responseTrue(row,1:end)=1;
    elseif (group==0)
        responseTrue(1,1:end)=1;
    else
        responseTrue(group,1:end)=1;
    end
    
    testResponse{i,1}=responseDeepNet;
    testResponse{i,2}=responseTrue;
end

end