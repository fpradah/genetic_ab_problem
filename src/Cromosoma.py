from random import *
import sys

class Cromosoma :
	"""Cromosoma Base de la solucion"""
	def __init__(self,genes,pares):
		self.genes = genes
		self.pares = pares
		self.cromosoma = self.createRandom()
		self.totalPares = self.getPares()
		self.puntuacion = self.getPuntuacion()
	def getCromosoma(self):
		return cromosoma
	def createRandom(self):
		return [randint(0,1) 
		for b in range(1,self.genes+1)]
	def getPuntuacion(self):
		total_pares = self.getPares() 
		if self.pares == 0 and total_pares == 0 : return 1
		if self.pares == 0 and total_pares == 1 : return 0.5
		if self.pares == 0 : return float(total_pares)/1
		return float(total_pares)/float(self.pares)
	def cruzar(self,pareja):
		# Escogemos el pocentaje de la pareja
		total_actual = int(self.genes * 0.6)
		# Escogemos los genes de la pareja
		for gen in range(total_actual,self.genes-1) :
			self.cromosoma[gen] = pareja[gen]
	def mutar(self,porcentaje_mutacion):
		total_mutacion = int(len(self.cromosoma) * porcentaje_mutacion)
		for i in range(0,total_mutacion) :
			# Elegimo una posicion random de gen
			posicion_gen = randint(0,self.genes-1)
			# La remplazamos por un valor aleatorio
			self.cromosoma[posicion_gen] = randint(0,1)
	def getPares(self):
		self.totalPares = 0
		for i in range(0,len(self.cromosoma)):
			if (self.cromosoma[i]==1):
				continue
			for j in range(i,len(self.cromosoma)):
				if (self.cromosoma[i]<self.cromosoma[j]):
					self.totalPares = self.totalPares + 1
		return self.totalPares
	def isSolution(self):
		return self.puntuacion == 1
	def isBestSolution(self):
		return self.puntuacion > 0.8 or self.puntuacion < 1.2
	def toString(self):
		print self.cromosoma,"Puntuacion",self.puntuacion,"Pares",self.pares,"Total Pares",self.getPares()