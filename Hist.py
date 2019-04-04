import pandas as pd
from functools import reduce
from itertools import tee 
from numpy import std
from statistics import stdev


df = pd.read_excel(r'info-historica.xlsx')
#lista = []
#lista.extend(df[1:].values.tolist())
#print(lista)

def gen():
 	for element in df[1:].values:
 		yield element


grd1 = filter(lambda x: x[4]=="GRD1",gen())
grd2 = filter(lambda x: x[4]=="GRD2",gen())
grd3 = filter(lambda x: x[4]=="GRD3",gen())
grd4 = filter(lambda x: x[4]=="GRD4",gen())
grd5 = filter(lambda x: x[4]=="GRD5",gen())
grd6 = filter(lambda x: x[4]=="GRD6",gen())
grd7 = filter(lambda x: x[4]=="GRD7",gen())
grd8 = filter(lambda x: x[4]=="GRD8",gen())
grd9 = filter(lambda x: x[4]=="GRD9",gen())
grd10 = filter(lambda x: x[4]=="GRD10",gen())

def gen(gen):
	for element in gen:
		yield element[5]
def contador(gen):
	contador = 0
	for element in gen:
		contador +=1
	return contador

grd1 , grd11 = tee(grd1)
grd2 , grd22 = tee(grd2)
grd3 , grd33 = tee(grd3)
grd4 , grd44 = tee(grd4)
grd5 , grd55 = tee(grd5)
grd6 , grd66 = tee(grd6)
grd7 , grd77 = tee(grd7)
grd8 , grd88 = tee(grd8)
grd9 , grd99 = tee(grd9)
grd10 , grd101 = tee(grd10)
numero1 = gen(grd1)
numero1, numero11 = tee(numero1)
numero2 = gen(grd2)
numero2, numero22 = tee(numero2)
numero3 = gen(grd3)
numero3, numero33 = tee(numero3)
numero4 = gen(grd4)
numero4, numero44 = tee(numero4)
numero5 = gen(grd5)
numero5, numero55 = tee(numero5)
numero6 = gen(grd6)
numero6, numero66 = tee(numero6)
numero7 = gen(grd7)
numero7, numero77 = tee(numero7)
numero8 = gen(grd8)
numero8, numero88 = tee(numero8)
numero9 = gen(grd9)
numero9, numero99 = tee(numero9)
numero10 = gen(grd10)
numero10, numero100 = tee(numero10)




contador1 = contador(grd11)
contador2 = contador(grd22)
contador3 = contador(grd33)
contador4 = contador(grd44)
contador5 = contador(grd55)
contador6 = contador(grd66)
contador7 = contador(grd77)
contador8 = contador(grd88)
contador9 = contador(grd99)
contador10 = contador(grd101)

a1 = reduce(lambda x,y: x + y ,numero1)
a2 = reduce(lambda x,y: x + y ,numero2)
a3 = reduce(lambda x,y: x + y ,numero3)
a4 = reduce(lambda x,y: x + y ,numero4)
a5 = reduce(lambda x,y: x + y ,numero5)
a6 = reduce(lambda x,y: x + y ,numero6)
a7 = reduce(lambda x,y: x + y ,numero7)
a8 = reduce(lambda x,y: x + y ,numero8)
a9 = reduce(lambda x,y: x + y ,numero9)
a10 = reduce(lambda x,y: x + y ,numero10)

b1 = stdev(numero11)
b2 = stdev(numero22)
b3 = stdev(numero33)
b4 = stdev(numero44)
b5 = stdev(numero55)
b6 = stdev(numero66)
b7 = stdev(numero77)
b8 = stdev(numero88)
b9 = stdev(numero99)
b10 = stdev(numero100)



lista  = []
lista.append((a1/contador1,b1))
lista.append((a2/contador2,b2))
lista.append((a3/contador3,b3))
lista.append((a4/contador4,b4))
lista.append((a5/contador5,b5))
lista.append((a6/contador6,b6))
lista.append((a7/contador7,b7))
lista.append((a8/contador8,b8))
lista.append((a9/contador9,b9))
lista.append((a10/contador10,b10))

for element in lista:
	print(element)




