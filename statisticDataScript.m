%Clear and initialize valiables
restoredefaultpath;
clear variables;
clc
% csvPath='/home/gpds/Documents/AutoEncoderVideo/src/';
csvPath='C:\Users\Adm\Desktop\AutoEncoderVideo\src\';
% csvPath='C:\Users\Adm\Desktop\AutoEncoderVideo\src\otherMetrics\';
% csvPath='C:\Users\Adm\Desktop\AutoEncoderVideo\ResultadosMediaFeatures';
% csvFile='NotNormalizedExp\Experiment1_validation1-10.csv'; 
  for i = 1:10

%     csvFile=strcat('test_',num2str(i),'.csv'); 
    csvFile=strcat('test_',num2str(i),'.csv'); 
    
%     csvFile=strcat('Experiment_1.csv'); 
    doMean = true;

    %Read csv table
    dataTable=readtable(fullfile(csvPath,csvFile),'delimiter',';','ReadVariableNames',1);
    %Data

    criteria={'HRC', 'audioDegradationType', 'audioInfluentialFactor', 'videoDegradationType', 'videoInfluentialFactor', 'adaptationAlgo', 'trace','netcond'};
    comparisonSets={'Mqs', 'Mcs','linear','minkowski','power' ,'DAE_Video_cfv10_net','visqolAudio', 'visqol', 'p563', 'peaqBasic', 'diivine', 'viideo', 'biqi' , 'niqe' , 'brisque' , 'psnr' , 'ssim' ,'DAE_Speech', 'DAE_Music', 'DAE_Enviroment', 'DAE_Video', 'DAE_Video_st', 'DAE_AV', 'DAE_AV_2', 'DAE_Audio', 'DAE_Audio_seg','DAE_Audio_perferctSeg','DAE_Audio_perferctSegInput', 'DAE_Audio_CFV', 'DAE_Video_cfv10','DAE_AV_CFV10'}; %Add more sets to the csv
    %%
    %Set sets to compare
    setA=comparisonSets{1};
    setB=comparisonSets{6};
%     setB=comparisonSets{21};

    %%alternative
    setviideo=comparisonSets{12};
    setbiqi=comparisonSets{13};
    setniqe=comparisonSets{14};
    setbrisque=comparisonSets{15};
    setpsnr=comparisonSets{16};
    setssim=comparisonSets{17};
    setdiivine=comparisonSets{11};

    %Audio
    % setvisqolA=comparisonSets{7};
    % setvisqol=comparisonSets{8};
    % setp563=comparisonSets{9};
    % setpeaq=comparisonSets{10};

    %AV
    setlinear=comparisonSets{3};
    setmink=comparisonSets{4};
    setpower=comparisonSets{5};

    %Set mean criteria
    meanCriteria = criteria{1};
    %Set group criteria
    groupCriteria = criteria{4};
    grupo = '';
    switch groupCriteria
        case 'netcond'
            grupo = 'netcond';
        case 'adaptationAlgo'
            grupo = 'adaptationAlgo';
    end
    %Get statistic Data
    [statisticChart,alpha] = statisticData(setA, setB, dataTable, groupCriteria, meanCriteria, doMean);
%     [statisticChartviideo,alpha] = statisticData(setA, setviideo, dataTable, groupCriteria, meanCriteria, doMean);
%     [statisticChartbiqi,alpha] = statisticData(setA, setbiqi, dataTable, groupCriteria, meanCriteria, doMean);
%     [statisticChartniqe,alpha] = statisticData(setA, setniqe, dataTable, groupCriteria, meanCriteria, doMean);
%     [statisticChartbrisque,alpha] = statisticData(setA, setbrisque, dataTable, groupCriteria, meanCriteria, doMean);
%     [statisticChartpsnr,alpha] = statisticData(setA, setpsnr, dataTable, groupCriteria, meanCriteria, doMean);
%     [statisticChartssim,alpha] = statisticData(setA, setssim, dataTable, groupCriteria, meanCriteria, doMean);
%     [statisticChartdiivine,alpha] = statisticData(setA, setdiivine, dataTable, groupCriteria, meanCriteria, doMean);

    %Audio
    %[statisticChartvisqolAudio,alpha] = statisticData(setA, setvisqolA, dataTable, groupCriteria, meanCriteria, doMean);
    %[statisticChartvisqol,alpha] = statisticData(setA, setvisqol, dataTable, groupCriteria, meanCriteria, doMean);
    %[statisticChartp563,alpha] = statisticData(setA, setp563, dataTable, groupCriteria, meanCriteria, doMean);
    %[statisticChartpeaq,alpha] = statisticData(setA, setpeaq, dataTable, groupCriteria, meanCriteria, doMean);

    %AV
    %[statisticChartLinear,alpha] = statisticData(setA, setlinear, dataTable, groupCriteria, meanCriteria, doMean);
    %[statisticChartMink,alpha] = statisticData(setA, setmink, dataTable, groupCriteria, meanCriteria, doMean);
    %[statisticChartPower,alpha] = statisticData(setA, setpower, dataTable, groupCriteria, meanCriteria, doMean);
    % statisticChart = cell2table(statisticChart);
    statisticChart = cell2table(statisticChart);
    writetable(statisticChart, strcat(grupo,'_testes',num2str(i),'-10.xlsx'));
end