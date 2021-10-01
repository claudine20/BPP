import pandas as pd
import numpy as np

df = pd.DataFrame([(10, 20),(-5,-6), (30, 40),(-3,-4)], columns=["A", "B"])
print(df)

# Gastos mensuales
print("Suma gastos mensuales:")
gastos = df[df < 0]
suma_gastos = gastos.sum()
print(suma_gastos)

# ¿Qué mes se ha gastado más? = mes de abril(-34133.0)
def maxi_gastado():
    gastos = df[df < 0]
    suma_gastos = gastos.sum()
    return min(suma_gastos)
print("El mes que más se ha gastado  es:",min(suma_gastos))


print(df.sum())

def maxi_ahorado():
    return max(df.sum())
print("El mes que más se ha ahorrado  es:",max(df.sum()))
#Llamamos a la función
maxi_ahorado()
