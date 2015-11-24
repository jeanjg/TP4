from Listas import *

class MataCerebros(object):

	def __init__(self, cintaSize = 15):
		#Here we need to implement ListeDouble (cf. Listas.py)
		self.cintaList = ListaDoble()
		for i in xrange(1,cintaSize):
			self.cintaList.append(0)
		self.currentCelda = self.cintaList.head
		self.actionDict = {"+": self.add, "-": self.remove, ">": self.up, "<": self.down, ".": self.printascii };


	def add(self):
		if self.currentCelda: 
			self.currentCelda.dato +=1
			return self.currentCelda.dato

	def remove(self):
		if self.currentCelda: 
			self.currentCelda.dato -=1
			return self.currentCelda.dato

	def up(self):
		self.currentCelda=self.currentCelda.prox
		return self.currentCelda

	def down(self):
		self.currentCelda=self.currentCelda.prev
		return self.currentCelda

	def printascii(self):
		#print chr(self.celda[self.currentCelda])
		print self.currentCelda.dato

	def command(self,action):
		self.actionDict[action]()

	def __str__(self):
		self.cintaList.show()
		return ""

	def process_action(self,colas, firstCelda = 0):
		#print self
		while not colas.es_vacia():
			action=colas.desencolar()
			#print action
			if type(action) is str:
				#WORK GREAT
				self.command(action)
			else:
				#PART OF THE PROBLEM
				cicleCelda = self.currentCelda
				cicleCola = action
				while not self.celda[0] == 0:
					newCola = Cola()
					while not cicleCola.es_vacia():
						cAction = cicleCola.desencolar()
						newCola.encolar(cAction)
						self.command(cAction)
					cicleCelda = newCola

