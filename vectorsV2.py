# Better version of vectors
#----------------------------------Imports-------------------------------------------------
import math 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
#--------------------------------------Vectors----------------------------------------------

class vector:
	def __init__ (self,x,y,z =0):
		self.x = x
		self.y = y
		self.z = z
		self.coords = (self.x,self.y,self.z)
		self.coords2 = (self.x , self.y)

	def __str__(self):
		return f'vector: ({self.x},{self.y},{self.z})'

	def __add__(self, other_vector):
		x = self.x + other_vector.x
		y = self.y + other_vector.y
		z = self.z + other_vector.z
		new_vector = vector(x,y,z)
		return new_vector

	def __sub__(self , other_vector):
		x = self.x - other_vector.x
		y = self.y - other_vector.y
		z = self.z - other_vector.z
		new_vector = vector(x,y,z)
		return new_vector

	def __mul__(self,other_vector):
		prod =  (self.x * other_vector.x) + (self.y * other_vector.y) + (self.z * other_vector.z)
		return prod

	def __len__(self):
		mag = math.sqrt((self.x **2) + (self.y**2) + (self.z**2))
		return mag

	def cross(self, other):
		new_x = (self.y * other.z) - (self.z * other.y)
		new_y = (self.z * other.x) - (self.x * other.z)
		new_z = (self.x * other.y) - (self.y * other.x) 
		return vector(new_x , new_y , new_z)

	def inverse(self):
		self.x = self.x * -1
		self.y = self.y * -1
		self.z = self.z * -1
		return

	def plot(self):
		ax.plot([0,self.x]  , [0,self.y] , [0,self.z])

	def from_plot(self,other_vector):
		ax.plot([0 + other_vector.x,self.x + other_vector.x],
		 		[0 + other_vector.y,self.y + other_vector.y] ,
		  		[0 + other_vector.z,self.z + other_vector.z])

# --------------PLOTTING STUFF------------------------
if __name__ == '__main__':
	fig = plt.figure()
	ax = plt.axes(projection='3d')
	ax.set_title('Vector Plot')
	ax.scatter([0],[0],[0])

#------------------WORK STATION----------------------

#-----------------------------------------------------
plt.show()

