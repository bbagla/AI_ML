import numpy as np 
import matplotlib.pyplot as plt 
from numpy.linalg import inv

def Check_Answer(vector , constant):	#To check which option is correct
	if float(vector.T * centre) == constant :
		return True
	else :
		return False


def mid_pt(B,C):     #Calculates the mid point of given points
	D = (B+C)/2
	return D

A = np.matrix('-2;4')    # Given point lying on the circle
B = np.matrix('0;2')	 # The Point where the circle touches the y-axis.

mid_AB = mid_pt(A,B)	 # Mid point of line joining A & B.

norm_vec1 = (A - B)/2 	# direction vector of the line segment joining A & B i.e. normal vector of their perpendicular bisector.
					 	# Note : Dividing by a constant doesn't change the direction vector.
#	Eqn. of the perpendicular bisector of line segment AB is of form
#			norm_vec1.T * X = p where p is some constant.

p = float(norm_vec1.T * mid_AB)		# As the perpendicular bisector passes through the mid point of AB,
									# we put X = mid_AB to calculate p. 
# To cumpute the centre of the circle, we take the intersection point of perpendicular bisector of AB and line y = 2
norm_vec2 = np.matrix('0;1')  	# Normal vector of line y = 2 

P = np.matrix('0.0;0.0')		# Combined matrix of constants of the two lines
P[0] = p 
P[1] = 2.0
transpose_N = np.concatenate((norm_vec1.T, norm_vec2.T)) 
								# N is the combined matrix of normal vectors of the two lines.
inv_N_T  = inv(transpose_N)		# Inverse of the transpose of N.

centre = inv_N_T * P 			# Centre of the circle.

option_a_vec = np.matrix('4;5') #Options as given in the problem.
option_a_cons = 6
option_b_vec = np.matrix('2;-3')
option_b_cons = -10
option_c_vec = np.matrix('3;4')
option_c_cons = 3
option_d_vec = np.matrix('5;2')
option_d_cons = -4

ans = np.array([0,0,0,0])
ans[0] = Check_Answer(option_a_vec , option_a_cons)
ans[1] = Check_Answer(option_b_vec , option_b_cons)
ans[2] = Check_Answer(option_c_vec , option_c_cons)
ans[3] = Check_Answer(option_d_vec , option_d_cons)

print("Centre of the circle is ")
print(centre.T)
for i in range(0,3):	# Prints the option which is correct.
	if(ans[i] == True):
		 print("Answer is option " + chr(97+i))
