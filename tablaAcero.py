import numpy as np
import math
import pandas as pd

#Función para determinar la cantidad de varillas dado el área requerida
def barrasAcero(areaAcero):
    varilla = np.array([8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 25.0, 28.0, 32.0])
    areaVarilla = math.pi * pow(varilla / 10, 2) / 4 #cm2
    cantidadBarras = areaAcero / areaVarilla
    cantidadBarrasRed = np.ceil(cantidadBarras)

    exportResult = pd.Series(cantidadBarrasRed , index = varilla)
    
    return exportResult

#Datos de área requerida
areaReq = 5 #cm2
print (barrasAcero(areaReq)) 