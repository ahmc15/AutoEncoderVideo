from os import listdir
from os.path import isfile, join, splitext
import csv


main_path = '/home/gpds/Documents/AutoEncoderVideo/src'
with open('UnB-AVQ-2018-Experiment1.csv','r') as f:
	reader= csv.reader(f)
	list = list(reader)
	list = list[1:]
	amnt_rows = len(list)
	amnt_testing = int(amnt_rows * 0.1)
	amnt_validation = int(amnt_rows * 0.2)
	amnt_training = amnt_rows - amnt_testing - amnt_validation

with open('Experiment1_validation.csv','w', newline='') as test_file:
	fields_names =['refFile', 'testFile', 'Mqs', 'Mcs', 'HRC', 'videoDegradationType', 'videoCodec', 'videoBitrate', 'packetLossRate','freezingPauses', 'freezingLength'];
	validation_w = csv.writer(test_file, delimiter=';')
	validation_w.writerow(fields_names)
	for i in range(168,216):
		validation_w.writerow(list[i])
	for i in range(408,456):
		validation_w.writerow(list[i])
	for i in range(528,576):
		validation_w.writerow(list[i])

with open('Experiment1_train.csv','w', newline='') as train_file:
	fields_names =['refFile', 'testFile', 'Mqs', 'Mcs', 'HRC', 'videoDegradationType', 'videoCodec', 'videoBitrate', 'packetLossRate','freezingPauses', 'freezingLength'];
	train_w = csv.writer(train_file, delimiter=';')
	train_w.writerow(fields_names)
	for i in range(168):
		train_w.writerow(list[i])
	for i in range(216,408):
		train_w.writerow(list[i])
	for i in range(456,528):
		train_w.writerow(list[i])
	for i in range(576,648):
		train_w.writerow(list[i])

with open('Experiment1_test.csv','w', newline='') as test_file:
	fields_names =['refFile', 'testFile', 'Mqs', 'Mcs', 'HRC', 'videoDegradationType', 'videoCodec', 'videoBitrate', 'packetLossRate','freezingPauses', 'freezingLength'];
	test_w = csv.writer(test_file, delimiter=';')
	test_w.writerow(fields_names)
	for i in range(amnt_validation + amnt_training, amnt_rows):
		test_w.writerow(list[i])
