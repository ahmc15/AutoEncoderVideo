from os import listdir
from os.path import isfile, join, splitext
from random import shuffle 
import csv

folder = 'Experiment_1'
main_path = '/home/gpds/Documents/AutoEncoderVideo/VisualFeatures'
path = join(main_path, folder)
files = []
for f in listdir(path):
	if isfile(join(path, f)):
		files.append(f)


	
amnt_train = int(len(files) * 0.8)
amnt_test = len(files) - amnt_train
shuffle(files)
with open(folder + '_train.csv','w', newline='') as train_file:
	fields_name = ['testFile'];
	train_w = csv.DictWriter(train_file, delimiter=';',fieldnames=fields_name)
	train_w.writeheader()
	for i in range(amnt_train):
		train_w.writerow({'testFile': splitext(files[i])[0]})

with open(folder + '_test.csv', 'w+') as test_file:
	test_w = csv.DictWriter(test_file, delimiter=';', fieldnames=fields_name)
	test_w.writeheader()
	for i in range(amnt_test):
		test_w.writerow({'testFile': splitext(files[i])[0]})
	



