import pandas as pd
import numpy as np
import pytest
import actividadL1

"""
En esta actividad debe implementar un conjunto de test unitarios para validar el conjunto de funciones que implementó en la actividad de la Lección 1.
Para desarrollar este conjunto de tests puede hacer uso de la herramienta unittest o pytest.
Comprobaremos las 5 funciones que hemos creado en la actividad 1
 """
# Test maxi_gastado()
def test_maxi_gastado():
    assert actividadL1.maxi_gastado()==-34133.0

# Test maxi_ahorado()
def test_maxi_ahorado():
    assert actividadL1.maxi_ahorado()==12064

# Test media de gastos al año:
def test_media_gastos():
    assert actividadL1.Media_gastoAnuales()==-24732.583333333332

 # Test gasto total a lo largo del año:
def test_gastos_total():
     assert actividadL1.gastos_totales()==-296791.0

 # Test ingresos totales a lo largo del año:
def test_ingresos_total():
     assert actividadL1.ingresos_totales()==280961.0
