import math
import tkinter as tk
import time


scaling_factor = 25 * 1 
class vector:                                                           #-----------------------VECTORS---------------------------
    def __init__(self,x,y,z = 0):


        self.x = x
        self.y = y
        self.z = z
        
    def add(self , other_vector):
        new_x = self.x + other_vector.x
        new_y = self.y + other_vector.y
        new_z = self.z + other_vector.z

        new_vector = vector(new_x,new_y,new_z)
        return new_vector

    def inverse(self):
        self.x = self.x * -1
        self.y = self.y * -1
        self.z = self.z * -1
        return


    def subtract(self,other_vector):
        other_vector.inverse()
        new_vector = self.add(other_vector)
        return new_vector

    def dot_product(self,other_vector):
        prod =  (self.x * other_vector.x) + (self.y * other_vector.y) + (self.z * other_vector.z)
        return prod

    def magnitude(self):
        mag = math.sqrt( (self.x**2) + (self.y**2) + (self.z**2))
        return mag


    def from_origin(self):
        new_vector = self.add(origin)
        new_vector.y -= 2 * self.y
        return new_vector.x , new_vector.y


    def scale(self , scaler):
        new_x = self.x * scaler
        new_y = self.y * scaler
        new_z = self.z * scaler

        scaled_vector = vector(new_x,new_y,new_z)
        return scaled_vector
            
    def plot(self , color ='red'):
        run = True
        scaled = self.scale(scaling_factor)
        line = canvas.create_line(w/2 , h/2 , scaled.from_origin() , fill=color)

    def transform(self, matrix):
        
        x_vec = matrix[0].scale(self.x)
        y_vec = matrix[1].scale(self.y)
        z_vec = matrix[2].scale(self.z)

        new_vector = x_vec.add(y_vec.add(z_vec))
        return new_vector


    


class matrix:                                                                   #--------------------------MATRiCES---------------------------
    def __init__( self, vector_i : vector, vector_j  : vector, vector_k = vector(0,0,0)):
        self.vector_i = vector_i
        self.vector_j = vector_j
        self.vector_k = vector_k

        self.matrix = [vector_i,
                       vector_j,
                       vector_k,]




    def matmul(self,other_matrix):
        new_vec1  = self.vector_i.transform(other_matrix.matrix)
        new_vec2  = self.vector_j.transform(other_matrix.matrix)
        new_vec3  = self.vector_k.transform(other_matrix.matrix)

        new_matrix = matrix(new_vec1 , new_vec2 , new_vec3)
        return new_matrix








win = tk.Tk()
run = False

h = 1000
w = 1000

canvas = tk.Canvas(win , bg='white' , height=h,width = w)
origin = vector(w/2,h/2,0)

X_axis = canvas.create_line(0 , h/2 , w , h/2)
Y_axis = canvas.create_line(w/2 , 0 , w/2 , h)


scaling_constant = 1
if scaling_factor <= 10:
    scaling_constant = 0
else:
    scaling_constant =1

for i in range(0,w,int(scaling_factor*scaling_constant ) + 1):
    linei = canvas.create_line(i,h/2 - scaling_factor*scaling_constant/5 , i , h/2 + scaling_factor*scaling_constant/5)

for j in range(0,h,int(scaling_factor*scaling_constant) + 1):
    linej = canvas.create_line(w/2 - scaling_factor*scaling_constant/5 , j , w/2 + scaling_factor*scaling_constant/5 , j)


i_hat = vector(1,0,0)
j_hat = vector(0,1,0)
k_hat = vector(0,0,1)


i_hat.plot(color = 'orange')
j_hat.plot(color = 'green')


#-------------------------------------------------

#=================================================


canvas.pack()
win.mainloop()



