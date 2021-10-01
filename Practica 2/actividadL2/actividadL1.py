import pandas as pd
import numpy as np
import csv
import re


""" APARTADO 1:"""
#  script que cargue el fichero cotizacion.csv y cronstruya un dataframe en pandas:
# Los datos son separados por tabulaciones

with open('C:/Users/claud/Documents/FORMACIÓN/ATOM/Buenas pr prog en Python/Clase1/finanzas2020.csv', newline='') as csvfile:
	read_csv = csv.reader(csvfile, delimiter='\t')
	dataset = []
	for row in read_csv:
		dataset.append(row)

processed_data = []
for i in range(1, len(dataset)):
	aux_dataset = []
	for j in dataset[i]:
		try:
			aux = int(j)
			aux_dataset.append(aux)
		except:
			aux_dataset.append(0)
			print("No puedo convertir el valor ", j)
	processed_data.append(aux_dataset)

print(processed_data)

df = pd.DataFrame(processed_data, columns=dataset[0])


# Gastos mensuales
print("Suma gastos mensuales:")
gastos = df[df < 0]
suma_gastos = gastos.sum()
print(suma_gastos)

# Pregunta 1: ¿Qué mes se ha gastado más? = mes de abril(-34133.0)
def maxi_gastado():
    gastos = df[df < 0]
    suma_gastos = gastos.sum()
    return min(suma_gastos)
print("El mes que más se ha gastado  es:",min(suma_gastos))

#Llamamos a la función
maxi_gastado()

# Ingresos mensuales:
print("La suma de los ingresos mensuales es:")
ingresos = df[df > 0]
suma_ingresos = ingresos.sum()
print(suma_ingresos)

# Importes mensuales ahorrado
print("La suma de los importes mensuales ahorrados es:")
print(df.sum())

# Pregunta 2: ¿Qué mes se ha ahorrado más? = mes de Enero (12064)
def maxi_ahorado():
    return max(df.sum())
print("El mes que más se ha ahorrado  es:",max(df.sum()))
#Llamamos a la función
maxi_ahorado()

# Pregunta 3:¿Cuál es la media de gastos al año?
def Media_gastoAnuales():
	return suma_gastos.mean()
print("La media de gastos al año es:", suma_gastos.mean())
#Llamamos a la función
Media_gastoAnuales()

# Pregunta 4: ¿Cuál ha sido el gasto total a lo largo del año?
def gastos_totales():
	return sum(suma_gastos)
print("El gasto total anual es:",sum(suma_gastos))

#Llamamos a la función
gastos_totales()

# Pregunta 5:¿Cuáles han sido los ingresos totales a lo largo del año?
def ingresos_totales():
	return sum(suma_ingresos)
print("Los ingresos totales a lo largo del año son:",sum(suma_ingresos))

#Llamamos a la función
ingresos_totales()

""" APARTADO 2:"""
# Compruebe que el fichero existe y que tiene 12 columnas, una para cada mes del año.
try:
    fichero = open('C:/Users/claud/Documents/FORMACIÓN/ATOM/Buenas pr prog en Python/Clase1/finanzas2020.csv', "r")
    lines = fichero.readlines()
except:
    print("No he encontrado el fichero. O no existe o esta en otro directorio")
else:# Este else es optativo, es simplemente para cerrar el fichero y el buffer.
    fichero.close()
print("He terminado de leer y a partir de aqui puedo ejecutar más cosas")
print(list(df.columns))
print(len(df.columns))
