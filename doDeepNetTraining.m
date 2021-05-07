function deepNet = doDeepNetTraining(AE1, AE2, softNet, input, target)
deepNet = stack(AE1,AE2,softNet);
deepNet = train(deepNet,input,target);
end

