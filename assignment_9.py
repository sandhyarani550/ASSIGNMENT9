# -*- coding: utf-8 -*-
"""ASSIGNMENT 9

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nlMlIc4QWR2w5RIbRn3fR4tFeCZk5Nst
"""

# -*- coding: utf-8 -*-
"""Assignment9.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1A83Wq04cOgO1lXyCAYAfnwIgmJ-e43fS
"""
 
import numpy as np
 
 
def dir_vec(A,B):
  return B-A
 
def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))
 
#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
 
def tri_vert(a,b,c):
  p = (a**2 + c**2-b**2 )/(2*a)
  q = np.sqrt(c**2-p**2)
#Triangle vertices
  A = np.array([p,q]) 
  B = np.array([0,0]) 
  C = np.array([a,0]) 
  return  A,B,C
 
 
def line_dir_pt(m,A, dim):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,10,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
 
#Foot of the Altitude
def alt_foot(A,B,C):
  m = B-C
  n = np.matmul(omat,m) 
  N=np.vstack((m,n))
  p = np.zeros(2)
  p[0] = m@A 
  p[1] = n@B
  #Intersection
  P=np.linalg.inv(N.T)@p
  return P
 
#Intersection of two lines
def line_intersect(n1,A1,n2,A2):
  N=np.vstack((n1,n2))
  p = np.zeros(2)
  p[0] = n1@A1
  p[1] = n2@A2
  #Intersection
  P=np.linalg.inv(N)@p
#  P=np.linalg.inv(N.T)@p
  return P
 
#Radius and centre of the circumcircle
#of triangle ABC
def ccircle(A,B,C):
  p = np.zeros(2)
  n1 = dir_vec(B,A)
  p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
  n2 = dir_vec(C,B)
  p[1] = 0.5*(np.linalg.norm(B)**2-np.linalg.norm(C)**2)
  #Intersection
  N=np.vstack((n1,n2))
  O=np.linalg.inv(N)@p
  r = np.linalg.norm(A -O)
  return O,r
 
#Radius and centre of the incircle
#of triangle ABC
def icentre(A,B,C,k1,k2):
  p = np.zeros(2)
  t = norm_vec(B,C)
  n1 = t/np.linalg.norm(t)
  t = norm_vec(C,A)
  n2 = t/np.linalg.norm(t)
  t = norm_vec(A,B)
  n3 = t/np.linalg.norm(t)
  p[0] = n1@B- k1*n2@C
  p[1] = n2@C- k2*n3@A
  N=np.vstack((n1-k1*n2,n2-k2*n3))
  I=np.matmul(np.linalg.inv(N),p)
  r = n1@(I-B)
  #Intersection
  return I,r
 
dvec = np.array([-1,1]) 
#Orthogonal matrix
omat = np.array([[0,1],[-1,0]]) 
 
import matplotlib.pyplot as plt 
import numpy as np 
import subprocess
import shlex
 
A = np.array([-7.5,-2.5])
B = np.array([1,11.5])
C = np.array([10,-2.5])
D = np.array([10,11.5])
points = np.array((A,C,D,B))
 
x_AB = line_gen(A,B)
 
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
 
plt.plot(2, 0, 'o')
plt.text(-6.4, 0.2 , 'A')
plt.plot(0 , -3, 'o')
plt.text(-0.4, 10.2 , 'B')
plt.fill(points[:,0], points[:,1], 'k', alpha=0.7)
 
#plt.title('Solution of $-3x+2y>=-6$)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
# plt.axis('equal')
 
plt.show()