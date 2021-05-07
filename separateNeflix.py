import os
import csv
import random
import itertools
random.seed(10)

def unpack_list(one_list):
    one_list = [i for item in one_list for i in item]
    return one_list

lista=[]
with open('netflixDataset.csv', newline='') as csvfile:
    csvlistanome = csv.reader(csvfile, delimiter=';')
    for count, row in enumerate(csvlistanome):
        lista.append(row)

cabecalho = lista[0]
corpo = lista[1:]
n = 28
separados = [ corpo[i:i+n] for i in range(0, len(corpo), n) ]
random.shuffle(separados)
contador = 1
print(len(separados))
# for count, ele in enumerate(separados[0]):
#     print(separados[2][count])

for i in range(0,15,3):
    test = separados[i:i+3]
    train = [item for item in separados if item not in test]
    test = unpack_list(test)
    train = unpack_list(train)

    with open('Netflix_test'+str(contador)+'.csv', 'w', newline='') as csvfile:
        csv_test = csv.writer(csvfile, delimiter=';')
        csv_test.writerow(cabecalho)
        for linha, elemento in enumerate(test):
            csv_test.writerow(test[linha])
    with open('Netflix_train'+str(contador)+'.csv', 'w', newline='') as csvfile:
        csv_train = csv.writer(csvfile, delimiter=';')
        csv_train.writerow(cabecalho)
        for linha, elemento in enumerate(train):
            csv_train.writerow(train[linha])
    contador += 1
