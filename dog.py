class Dog:
	type = 'canine'

	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

	def update_breed(self, breed):
		self.breed = breed

