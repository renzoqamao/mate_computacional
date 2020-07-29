#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


A = np.array([ [220, -20 ],
               [-0.05, 0.1],
               [0.05, -0.1],
               [1, -1]       ])
# pivotar tambien las variables
xb =['x3','x4','x2']
xn =['x1']
#-------------------
def particion(A):
    b = A[1:A.shape[0],0]
    co = A[0,0]
    ct = A[0,1:A.shape[1]]
    N = A[1:A.shape[0],1:A.shape[1]]
    print("b:",b)
    print("co:",co)
    print("ct:",ct)
    print("N:",N)
    return b,co,ct,N
b,co,ct,N = particion(A)


# In[3]:


#función pivote
def pivotacion(A, fila, columna):
    # , fila = r ,  columna = s
    r = fila
    s = columna
    B = np.zeros(A.shape)

    for i in range(A.shape[0]):  # las filas
        for j in range(A.shape[1]): # las columnas
            if i==0:
                if j==0:
                    B[i][j] = A[i][j]-(A[i][s]/A[r][s])*A[r][j]
                elif j==s:
                    B[i][j] =  A[i][j] / A[r][s]
                else:
                    B[i][j] = A[i][j] - A[i][s]*(A[r][j]/A[r][s])

            elif i==r:
                if j==0:
                    B[i][j] = - A[i][j]/A[r][s]
                elif j==s:
                    B[i][j] =   1 /A[r][s]
                else:
                    B[i][j] = - A[i][j]/A[r][s]
            else:
                if j==0:
                    B[i][j] = A[i][j]-(A[i][s]/A[r][s])*A[r][j]
                elif j==s:
                    B[i][j] =  A[i][s] / A[r][s]
                else:
                    B[i][j] = A[i][j] - A[i][s]*(A[r][j]/A[r][s])


    return B


# In[4]:


# función elemento minimo de c
def minimo_c(A):
    ind = np.argmin(A[0,1:A.shape[1]])
    print("elemento minimo de c: ",A[0][ind+1])
    if A[0][ind+1]<0:
        return True
    else:
        return False


# In[5]:


#SELECCIONAR COLUMNA DE VARIABLE NO BASICA
def select_non_basic(A):
    ind = np.argmin(A[0,1:A.shape[1]])
    columna = ind+1
    return columna
#SELECCIONAR FILA DE VARIABLE BASICA
def select_basic(A,s):
    b=A[1:A.shape[0],0]  # b 14 ,2
    #print(b)
    N=A[1:A.shape[0],s]  # N -3, -1
    #print(N)
    c =np.zeros(b.shape[0])  # c = 0 , 0
    for i in range(c.shape[0]):
        if N[i]==0:
            c[i]=0
        else:
            c[i] = -b[i]/N[i]
    #print(c)
    ind = np.argmax(c) # indice de la variable maxima
    #print('ind max',ind)
    for i in range(c.shape[0]):
        if c[i]<0:
            c[i]=c[ind]+1
    ind = np.argmin(c)  # indice en c -> en la matriz es fila = ind+1
    #print('ind min',ind)
    fila = ind+1
    return fila


# In[6]:


def metodo_regularizacion(A,b):
    ind = np.argmin(b) # indice en b
    print("elemento minimo de b: ",A[ind+1][0])  # en la matriz A esta en la posicion ind+1 , 0
    pivot = False
    if A[ind+1][0]<0:
        pivot = True
        print("se necesita regularizacion")
        k = 200
        x_r =np.array([  [k]  ])
        for i in range(A.shape[0]-1):
            x_r = np.append(x_r,np.array([  [1] ]), axis=0)
        print("x_r:",x_r)
        A=np.append(A,x_r,1)
        print("matriz con variable artificial")
        print(A)
        #agregamos una variable más a la lista xn
        print('variable artificial X , xn: ',xn)
        xn.append('X')  #xn=[x1,x2,X]
        print('xb:',xb)
        print('xn:',xn)
        #--------
        
        print('vamos a pivotar ','fila:',ind+1,'columna:',A.shape[1]-1)
        A = pivotacion( A , (ind+1), (A.shape[1]-1))
        print("matriz pivotada con b>0 ->")
        
        #-----modificamos los xn y xb xn=[x1,x2,x4]  xb =[x3,X]
        aux= xn[A.shape[1]-2]
        aux2 = xb[ind]
        xn.pop(A.shape[1]-2)
        xb.pop(ind)
        xn.insert(A.shape[1]-2,aux2)
        xb.insert(ind,aux)
        #--------------------------
        print(A)
        
        #imprime
        print("xb:",xb)
        print("xn:",xn)
        #------------
        return A
    else:
        print("no se necesita regularización")
        return A


# In[7]:


#resolver
A=metodo_regularizacion(A,b)
while minimo_c(A):
    columna = select_non_basic(A)  #print(columna,A[0][columna])
    fila = select_basic(A,columna) #print( fila, A[fila][0] )
    print('fila:',fila,'columna:',columna)
    A=pivotacion(A,fila,columna)
    #pivotacion en las x
    aux= xn[columna-1]
    aux2 = xb[fila-1]
    xn.pop(columna-1)
    xb.pop(fila-1)
    xn.insert(columna-1,aux2)
    xb.insert(fila-1,aux)
    print("xb:",xb)
    print("xn:",xn)
    #--------
    print(A)


# In[ ]:





# In[ ]:




