from graphviz import Digraph

class A:
	def bar(self):
		print('A.bar')

class B(A):
	pass

class C(A):
	def bar(self):
		print('C.bar')

class D(B, C):
	def get(self):
		pass

	@classmethod
	def clsfun(cls):
		print(cls)