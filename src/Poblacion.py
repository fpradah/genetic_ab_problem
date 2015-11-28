from random import *
import sys
import Cromosoma

class Poblacion :
	"""Poblacion de la solucion"""
	def __init__(self,tamano,genes,generacion,pares):
		self.tamano = tamano
		self.generacion = generacion
		self.poblacion = []
		self.createPoblacion(genes,pares)
		# Maximo de individuos en siguiente generacion
		self.herencia = 0.4
		# Invidivuos mutados sobre los heredados
		self.mutacion = 0.2
		self.porcentaje_mutacion = 0.6
		self.genes = genes
		self.pares = pares
	"""Creamos una poblacion aleatoria""" 
	def createPoblacion(self,genes,pares):
		for i in range(0,self.tamano) :
			cromosoma = Cromosoma.Cromosoma(genes,pares)
			self.addCromosoma(cromosoma)
	"""Agregamos un individuo a la poblacion""" 
	def addCromosoma(self,cromosoma):
		self.poblacion.append(cromosoma)
	"""Logica para indentificar el mejor individuo""" 
	def getPerfectCromosoma(self):
		solucion = Cromosoma.Cromosoma(0,0)
		for i in range(0,self.tamano) :
			if self.poblacion[i].isSolution() : 
				solucion = self.poblacion[i]
				break
		return solucion.cromosoma
	"""Logica para identificar a los mejores individuos""" 
	def getBestCromosomas(self):
		best_cromosomas = []
		for i in range(0,self.tamano) :
			if self.poblacion[i].puntuacion > 0.9 and self.poblacion[i].puntuacion < 1 :
				best_cromosomas.append(self.poblacion[i])
		return best_cromosomas
	"""Maximo numero de individuos que pueden pasar a sig generacion""" 
	def getMaximaHerencia(self):
		return int(self.tamano * self.herencia)
	"""Maximo individuos que pueden mutar""" 
	def getMaximaMutacion(self):
		return int(self.tamano * self.mutacion)
	"""Creamos una nueva generacion""" 
	def newGeneration(self):
		nueva_poblacion = []
		self.generacion += 1
		max_herencia = self.getMaximaHerencia()
		max_mutacion = self.getMaximaMutacion()		
		max_cruce = self.tamano - max_herencia - max_mutacion
		best_cromosomas = self.getBestCromosomas()
		for pos_heredado in range(0,max_herencia) :
			if (pos_heredado >= len(best_cromosomas)):
				heredado = Cromosoma.Cromosoma(self.genes,self.pares)
			else :
				heredado = best_cromosomas[pos_heredado]
			nueva_poblacion.append(heredado)
		for pos_mutado in range(0,max_mutacion) :
			if (pos_heredado >= len(best_cromosomas)):
				mutado = Cromosoma.Cromosoma(self.genes,self.pares)
			else :
				mutado = best_cromosomas[pos_mutado]
			mutado.mutar(self.porcentaje_mutacion)
			nueva_poblacion.append(mutado)
		for pos_cruzado in range(0,max_cruce) :
			if (pos_heredado >= len(best_cromosomas)):
				cruzado = self.poblacion[pos_cruzado]
			else :
				cruzado = best_cromosomas[pos_cruzado]
			pos_pareja = randint(0,self.tamano-1) 
			pareja = self.poblacion[pos_pareja]
			cruzado.cruzar(pareja.cromosoma)
			nueva_poblacion.append(cruzado)
		self.poblacion = nueva_poblacion
	def toString(self):
		print "Poblacion",self.poblacion
		for i in range(0,self.tamano-1):
			self.poblacion[i].toString()






