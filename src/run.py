from random import *
import sys
import Poblacion

genes, pares = int(sys.argv[1]), int(sys.argv[2])
tamano_poblacion = genes * 5
maxima_generacion = 1000 * genes
solucion = []
"""Creamos la primera generacion"""
poblacion = Poblacion.Poblacion(tamano_poblacion, genes, 0, pares)

seguir = True
while seguir and maxima_generacion > poblacion.generacion:
    """Buscamos si existe solucion en la poblacion actual"""
    print "GENERACION : "
    print poblacion.toString()
    solucion = poblacion.getPerfectCromosoma()
    if len(solucion) > 0:
        seguir = False
        break
    """Creamos la siguiente generacion"""
    print "###########################"
    print "Nueva GENERACION", poblacion.generacion
    print "###########################"
    poblacion.newGeneration()

solucion_text = ""
for i in range(0, len(solucion)):
    if solucion[i] == 1:
        solucion_text += 'B'
    else:
        solucion_text += 'A'
print "Solucion "
print "----------"
print solucion_text

# Pasamos a las siguientes generaciones
