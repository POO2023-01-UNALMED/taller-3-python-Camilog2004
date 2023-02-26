class TV:
	#Constructor
	_numTV=0
	def __init__(self,marca,estado):
		TV._numTV+=1
		self._marca=marca
		self._canal=1
		self._precio=500
		self._estado=estado
		self._volumen=1
		self._control=None
	#Metodos get

	def getMarca(self):
		return self._marca

	def getControl(self):
		return self._control

	def getPrecio(self):
		return self._precio

	def getVolumen(self):
		return self._volumen

	def getCanal(self):
		return self._canal

	def getEstado(self):
		return self._estado

	

	#Metodos set

	def setMarca(self,marca):
		self._marca=marca

	def setControl(self,control):
		self._control=control

	def setPrecio(self,precio):
		self._precio=precio

	def setVolumen(self,volumen):
		if volumen>=0 and volumen<=7 and estado==True:
			self._volumen=volumen

	def setCanal(self,canal):
		if canal>=1 and canal<=120 and estado==True:
			self._canal=canal

	

	#Otros metodos

	def turnOn(self):
		if self._estado==False:
			self._estado=True

	def turnOff(self):
		if self._estado==True:
			self._estado=False

	def canalUp(self):
		if self._canal>=1 and self._canal<120 and self._estado==True:
			self._canal+=1

	def canalDown(self):
		if self._canal>1 and self._canal<=120 and self._estado==True:
			self._canal-=1

	def volumenUp(self):
		if self._volumen>=0 and self._volumen<7 and self._estado==True:
			self._volumen+=1

	def volumenDown(self):
		if self._volumen>0 and self._volumen<=7 and self._estado==True:
			self._volumen-=1

	@classmethod

	def setNumTV(cls,numero):
		self._numTV=numero

	@classmethod

	def getNumTV(cls):
		return self._numTV




