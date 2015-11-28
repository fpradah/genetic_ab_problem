from random import *
import sys
import Cromosoma
import Poblacion

genes = int(sys.argv[1])
pares = int(sys.argv[2])
tamano_poblacion = genes*5
maxima_generacion = 1000*genes
solucion = []
"""Creamos la primera generacion"""  
poblacion = Poblacion.Poblacion(tamano_poblacion,genes,0,pares)

seguir = 1
while seguir and maxima_generacion > poblacion.generacion :
	"""Buscamos si existe solucion en la poblacion actual"""
	print "GENERACION : "
	poblacion.toString()
	solucion = poblacion.getPerfectCromosoma()
	if len(solucion) > 0 : 
		seguir = 0
		break
	"""Creamos la siguiente generacion"""  
	print "###########################"
	print "Nueva GENERACION",poblacion.generacion
	print "###########################"
	poblacion.newGeneration()

print "Solucion",solucion

# Pasamos a las siguientes generaciones
