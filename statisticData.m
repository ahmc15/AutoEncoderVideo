function [corrTable,alpha] = statisticData(setA, setB, dataTable, groupCriteria, meanCriteria, doMean)

groupConditions=unique(dataTable.(groupCriteria),'stable')';
groupConditionsStr = strings(size(groupConditions));
[groupConditionsStr{:}]=groupConditions{:};
numGroupCond = length(groupConditionsStr);

CorrRes=cell(1,1);
CorrRes{2,1} = 'PCC';
CorrRes{3,1} = 'SCC';
CorrRes{4,1} = 'RMSE';
for i=1:numGroupCond
    rows = string(dataTable.(groupCriteria))==groupConditionsStr{i};
    groupConditionTable=dataTable(rows,:);
    
    [meanA,meanB] = getSetsToCompare(setA,setB,groupConditionTable,meanCriteria, doMean);
    %With mean stage
    
%     meanConditions=unique(groupConditionTable.(meanCriteria),'stable');
%     [meanConditions{:}]=convertCharsToStrings(meanConditions{:});
%     numMeanCond = length(meanConditions);
%     meanA=[];
%     meanB=[];
%     for j=1:numMeanCond
%         meanRows=groupConditionTable.(meanCriteria) == meanConditions{j};
%         meanConditionTable = groupConditionTable(meanRows,:);
%         
%         meanA=[meanA; trimmean(meanConditionTable{:,setA},5)];
%         meanB=[meanB; trimmean(meanConditionTable{:,setB},5)];
%     end
    
    %Without mean stage
%     nonans = ~isnan(groupConditionTable{:,setA});
%     meanA = groupConditionTable{:,setA}(nonans);
%     meanB = groupConditionTable{:,setB}(nonans);
    
    %Get correlation
    CorrRes{1,i+1} = groupConditionsStr{i};
    CorrRes{2,i+1}=corr(meanA,meanB,'Type','Pearson');
    CorrRes{3,i+1}=corr(meanA,meanB,'Type','Spearman');
    CorrRes{4,i+1}=getrmse(meanA,meanB);
end

[A,B] = getSetsToCompare(setA,setB,dataTable,meanCriteria, doMean);

%With mean stage
% allMeanConditions=unique(dataTable.(meanCriteria),'stable');
% [allMeanConditions{:}]=convertCharsToStrings(allMeanConditions{:});
% numAllMeanCond = length(allMeanConditions);
% 
% A=[];
% B=[];
% %alphaSet=[];
% for i=1:numAllMeanCond
%     allRows = dataTable.(meanCriteria) == allMeanConditions{i};
%     allMeanConditionTable=dataTable(allRows,:);
%     
%     %Calculate cronbach
%     %setByConditions = cleanNanMat(allMeanConditionTable{:,setA});
%     %alphaSet = [alphaSet;setByConditions'];
%     
%     %Get A and B sets
%     A=[A;trimmean(allMeanConditionTable{:,setA},5)];
%     B=[B;trimmean(allMeanConditionTable{:,setB},5)];
% end

%Without mean stage
% nonans = ~isnan(dataTable{:,setA});
% A=dataTable{:,setA}(nonans);
% B=dataTable{:,setB}(nonans);

%Get correlation
CorrRes{1,numGroupCond+2}='All';
CorrRes{2,numGroupCond+2}=corr(A,B,'Type','Pearson');
CorrRes{3,numGroupCond+2}=corr(A,B,'Type','Spearman');
CorrRes{4,numGroupCond+2}=getrmse(A,B);
%alpha=cronbach(alphaSet);
alpha=0;
corrTable=CorrRes;
end

%%
function [rmse] = getrmse(data, predicted)
%err = data - predicted;
%squareError = err.^2;
%mse = mean(squareError);
%rmse = sqrt(mse);
rmse = sqrt(sum((data(:)-predicted(:)).^2)/numel(data));
end

%%
function a=cronbach(X)
%Syntax: a=cronbach(X)
%_____________________
%
% Calculates the Cronbach's alpha of a data set X.
%
% a is the Cronbach's alpha.
% X is the data set.
%
%
% Reference:
% Cronbach L J (1951): Coefficient alpha and the internal structure of
% tests. Psychometrika 16:297-333
%
%
% Alexandros Leontitsis
% Department of Education
% University of Ioannina
% Ioannina
% Greece
%
% e-mail: leoaleq@yahoo.com
% Homepage: http://www.geocities.com/CapeCanaveral/Lab/1421
%
% June 10, 2005.
if nargin<1 | isempty(X)==1
   error('You shoud provide a data set.');
else
   % X must be a 2 dimensional matrix
   if ndims(X)~=2
      error('Invalid data set.');
   end
end
% Calculate the number of items
k=size(X,2);
% Calculate the variance of the items' sum
VarTotal=var(sum(X'));
% Calculate the item variance
SumVarX=sum(var(X));
% Calculate the Cronbach's alpha
a=k/(k-1)*(VarTotal-SumVarX)/VarTotal;
end

%%
function outMat = cleanNanMat(inMat)
meanValue=nanmean(inMat);
inMat(isnan(inMat)) = meanValue;
outMat = inMat;
end

%%
function [outA, outB] = getSetsToCompare(inA,inB,table,meanCriteria, doMean)
if (doMean)
    meanConditions=unique(table.(meanCriteria),'stable');
    meanConditionsStr = strings(size(meanConditions));
    [meanConditionsStr{:}]= meanConditions{:};
    numMeanCond = length(meanConditions);
    meanA=[];
    meanB=[];
    for j=1:numMeanCond
        meanRows= string(table.(meanCriteria)) == meanConditionsStr{j};
        meanConditionTable = table(meanRows,:);
        
        %nonans = ~isnan(table{:,inA})
        %meanA=[meanA; meanConditionTable{:,inA}];
        %meanB=[meanB; meanConditionTable{:,inB}];
        
        meanA=[meanA; trimmean(meanConditionTable{:,inA},5)];
        meanB=[meanB; trimmean(meanConditionTable{:,inB},5)];
    end
else
    nonans = ~isnan(table{:,inA});
    meanA = table{:,inA}(nonans);
    meanB = table{:,inB}(nonans);
end
outA=meanA;
outB=meanB;
end
