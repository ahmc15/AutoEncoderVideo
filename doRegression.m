function regressionModel = doRegression(input,target)
softnet = trainSoftmaxLayer(input,target,'LossFunction','crossentropy','ShowProgressWindow',false);
regressionModel = softnet;
end

