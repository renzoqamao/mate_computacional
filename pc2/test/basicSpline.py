import scipy
import numpy
import matplotlib
import sympy
#puntos a interpolar
# A = [X,Y]
A= sympy.Matrix([[-1 , 1 , 3, 4, 6],
                [0, 4, -2, 3, 1] ] ) # 2x5

#i = 0
#print(A)
#print(A[: , i:i+4]) toda la col , fila 1 al 4
points = 5
grado = 3
# polinimo [ [0,0 ] . [0,0]  ]
polinomio = sympy.Matrix.zeros(2,points-grado) # 2x2

t = sympy.symbols("t")
h = sympy.symbols("h")
def N_normal(i,k,h):
    if k == 0:
        return h
    else:
        return ((t- i)/k)*N_normal(i,k-1,h)+ ((i+k+1-t)/k)*N_normal(i+1,k-1,h)

def B_spline(grado,points):
    for i in range(points-grado):
        for r in range(grado+1):
            polinomio[:, i ]  = polinomio[:,i] +  N_normal(r,grado,h) * A[:,r]  # 2x1
            #      fila i x col 2 = ix2 + 2xr
    return polinomio
def fun(i,t):
    if i<t and t<=i+1:
        return 1
    else:
        return 0
poly = B_spline(3,5)
# t empieza en 3 y termina en 4
# i empieza en 0
# primer trozo
px1= sympy.lambdify( [t,fun(0,t)], poly[:, 0])
px2 = sympy.lambdify([t,fun(1,t)], poly[:,1])

#VECTORES PARA GRAFICAS
muestras = 100
a = np.min(3)
b = np.max(5)
p_xi = numpy.linspace(a,b,muestras)

pfi1 = px(p_xi)
"""
muestras = 100
linea_t = numpy.linspace(4,6,muestras)
linea_pt = numpy.linspace()

polisimple = sympy.expand(poly)
print(poly)
print(polisimple)
"""
#GRAFICA

plt.plot(A[0,:],A[1,:],'o')
plt.plot(new_x,new_y)
plt.show()



import scipy
import numpy
import matplotlib
import sympy
#puntos a interpolar
# A = [X,Y]
A= sympy.Matrix([[-1 , 1 , 3, 4, 6],
                [0, 4, -2, 3, 1] ] ) # 2x5

#i = 0
#print(A)
#print(A[: , i:i+4]) toda la col , fila 1 al 4
points = 5
grado = 3
# polinimo [ [0,0 ] . [0,0]  ]
polinomio = sympy.Matrix.zeros(2,points-grado) # 2x2

#VECTORES PARA GRAFICAS
muestras = 100
a = np.min(3)
b = np.max(5)
p_t = numpy.linspace(a,b,muestras)  #  intervalo de t de 3 hasta 5

t = sympy.symbols("t")
h = sympy.symbols("h")
def N_base(i,val):
    if i<val and val<=i+1:
        return 1
    else:
        return 0

def N_normal(i,k):
    if k == 0:
        return N_base(i,t)
    else:
        return ((t- i)/k)*N_normal(i,k-1,h)+ ((i+k+1-t)/k)*N_normal(i+1,k-1,h)

f1= sympy.lambdify( t ,
    for i in range(points-grado):
        for r in range(grado+1):
            polinomio[:, i ]  = polinomio[:,i] +  N_normal(r,grado) * A[:,r]  # 2x1
            #      fila i x col 2 = ix2 + 2xr
 )(p_t)
