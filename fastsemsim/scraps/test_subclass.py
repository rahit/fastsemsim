class A(object):
	def __init__(self):
		self.metodo("init A")
		self.stringas = self.metodostatico("init A")
	#

	def metodo(self, stringa_init):
		self.stringa = "medoto A - " + stringa_init

	@staticmethod
	def metodostatico(stringa_init):
		return("medoto statico A - " + stringa_init)

	#
#


class B(A):
	def __init__(self):
		super(B,self).__init__()
		# self.metodo("init A")
	#

	def metodo(self, stringa_init):
		self.stringa = "medoto B - " + stringa_init
	#

	@staticmethod
	def metodostatico(stringa_init):
		return("medoto statico B - " + stringa_init)
#

a = A()
b = B()
print(a.stringa)
print(a.stringas)
print(b.stringa)
print(b.stringas)
