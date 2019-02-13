import numpy as np 
import matplotlib.pyplot as plt 

A = np.array([-2,4])
B = np.array([0,2])
M = np.array([-1,3])
T = np.array([-1,-1])
O = np.array([-2,2])
slope = np.array([2,-3])

len = 10
lam_1 = np.linspace(0,1,len)
x_AB = np.zeros((2,len))
x_BC = np.zeros((2,len))
x_CA = np.zeros((2,2*len))
for i in range (len):
	temp1 = A + lam_1[i]* (B - A)
	x_AB[:,i]= temp1.T
	temp2 = M + lam_1[i]* T
	x_BC[:,i]= temp2.T
	temp3 = O + lam_1[i] * slope
	temp4 = O - lam_1[i] * slope
	x_CA[:,i] = temp3.T 
	x_CA[:,len+i]= temp4.T
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$OM$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$Opt_B$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.05), A[1] * (1 - 0.05) ,'A')
plt.plot(B[0], B[1], 'o')
plt.text(0.05, B[1] * (1) , 'B')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 + 0.05), M[1] * (1 - 0.1) ,'M')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.05) ,'O')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
r=2
t =np.arange(0,2*np.pi,0.01)
x=-2+2*np.sin(t);
y=2+2*np.cos(t);
plt.legend(loc='best')
plt.plot(x,y)
plt.yticks(range(-1,6))
plt.xticks(range(-5,2))
plt.show()
