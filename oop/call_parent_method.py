# Python program to demonstrate
# calling the parent's class method
# inside the overridden method using
# super()


class DogParent():
	
	def show(self):
		print( "\n I am DogParent \n" )
		
class DogChild( DogParent ):
	
	def show(self):
		
		# Calling the parent's class
		# method
		super().show()
		print( "\n and me DogChild \n " )
		
# Driver's code
obj = DogChild()
obj.show()
