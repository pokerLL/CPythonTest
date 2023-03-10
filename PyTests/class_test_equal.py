
class A:
	def __eq__(self,AnotherA):
		print(locals())
		return 1==AnotherA
		
		
if __name__ == "__main__":
	a = A()
	print(a == 1)