%Clear and initialize valiables
restoredefaultpath;
clear variables;
clc

csvPath='C:\Users\Adm\Desktop\AutoEncoderVideo\Resultados\Seeds\seed_Diivine+SinnoM\';
for seed = 1:10 
    for fold = 1:5
        %csvFile=strcat('test_',num2str(i),'.csv'); 
        csvFile=strcat('seed',num2str(seed),'Netflix_test',num2str(fold),'.csv'); 
        doMean = true;

        %Read csv table
        dataTable=readtable(fullfile(csvPath,csvFile),'delimiter',';','ReadVariableNames',1);
        %Data
        criteria={'HRC', 'audioDegradationType', 'audioInfluentialFactor', 'videoDegradationType', 'videoInfluentialFactor', 'adaptationAlgo','netcond','refFile'};
        comparisonSets={'Mqs', 'Mcs','linear','minkowski','power' ,'DAE_Video_cfv10_net','visqolAudio', 'visqol', 'p563', 'peaqBasic', 'diivine', 'viideo', 'biqi' , 'niqe' , 'brisque' , 'psnr' , 'ssim' ,'DAE_Speech', 'DAE_Music', 'DAE_Enviroment', 'DAE_Video', 'DAE_Video_st', 'DAE_AV', 'DAE_AV_2', 'DAE_Audio', 'DAE_Audio_seg','DAE_Audio_perferctSeg','DAE_Audio_perferctSegInput', 'DAE_Audio_CFV', 'DAE_Video_cfv10','DAE_AV_CFV10'}; %Add more sets to the csv
        %%
        %Set sets to compare
        setA=comparisonSets{1};
        setB=comparisonSets{6};
        %setB=comparisonSets{21};

        %%alternative
        setviideo=comparisonSets{12};
        setbiqi=comparisonSets{13};
        setniqe=comparisonSets{14};
        setbrisque=comparisonSets{15};
        setpsnr=comparisonSets{16};
        setssim=comparisonSets{17};
        setdiivine=comparisonSets{11};

        %AV
        setlinear=comparisonSets{3};
        setmink=comparisonSets{4};
        setpower=comparisonSets{5};

        %Set mean criteria
        meanCriteria = criteria{1};
        %Set group criteria
        groupCriteria = criteria{8};
        grupo = '';
        switch groupCriteria
            case 'netcond'
                grupo = 'netcond';
            case 'adaptationAlgo'
                grupo = 'adaptationAlgo';
        end
        grupo = 'refFile';
        %Get statistic Data
        [statisticChart,alpha] = statisticData(setA, setB, dataTable, groupCriteria, meanCriteria, doMean);

        statisticChart = cell2table(statisticChart);
        writetable(statisticChart, strcat(csvPath,grupo,'_seed',num2str(seed),'Netflix_test',num2str(fold),'_10.xlsx'));
    end
end