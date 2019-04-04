import pandas as pd

df = pd.read_excel(r'Grd.xlsx')
#lista = []
#lista.extend(df[2:].values.tolist())
#print(lista)
#for element in df:
    #print(df[element].values.tolist())

#for element in df[2:].values:
 	#print(element)
def gen():
 	for element in df[2:].values:
 		yield element
i=0
for valor in gen():
	print(valor)
	i+=1
	if i ==10:
		break
 	
