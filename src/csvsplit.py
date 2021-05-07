from os import listdir
from os.path import isfile, join, splitext
from random import shuffle 
import csv


main_path = '/home/gpds/Documents/AutoEncoderVideo/src'
with open('UnB-AVQ-2018-Experiment1.csv','r') as f:
	reader= csv.reader(f)
	list = list(reader)
	list = list[1:]
	amnt_rows = len(list)
	amnt_training = int(amnt_rows * 0.8)
	amnt_testing = amnt_rows - amnt_training
	shuffle(list)

with open('Experiment1_train.csv','w', newline='') as train_file:
	fields_names =['refFile', 'testFile', 'Mqs', 'Mcs', 'HRC', 'videoDegradationType', 'videoCodec', 'videoBitrate', 'packetLossRate','freezingPauses', 'freezingLength'];
	train_w = csv.writer(train_file, delimiter=';')
	train_w.writerow(fields_names)
	for i in range(amnt_training):
		train_w.writerow(list[i])

with open('Experiment1_test.csv','w', newline='') as test_file:
	fields_names =['refFile', 'testFile', 'Mqs', 'Mcs', 'HRC', 'videoDegradationType', 'videoCodec', 'videoBitrate', 'packetLossRate','freezingPauses', 'freezingLength'];
	test_w = csv.writer(test_file, delimiter=';')
	test_w.writerow(fields_names)
	for i in range(amnt_training, amnt_rows):
		test_w.writerow(list[i])
