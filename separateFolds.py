import os
import csv
import random
import itertools

def unpack_list(one_list):
    one_list = [i for elem in one_list for item in elem for i in item]
    return one_list

random.seed(10)
lista=[]
with open('ListaArquivosNetflix2.csv', newline='') as csvfile:
    csvlistanome = csv.reader(csvfile, delimiter=',')
    for count, row in enumerate(csvlistanome):
        lista.append(row)
n = 7
separados = [ lista[i:i+n] for i in range(0, len(lista), n) ]
random.shuffle(separados)

for i in range(0,59,6):
    # print(i)
    # separado.append(separados)
    test = separados[i:i+6]
    train = [item for item in separados if item not in test]
    print(len(test),'\n')
    #print(test,'\n')
    print(len(train),'\n')

test=unpack_list(test)
train = unpack_list(train)
print(test,'\n')
print(train,'\n')
