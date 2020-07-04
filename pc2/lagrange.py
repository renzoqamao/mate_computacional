import scipy
import numpy
import matplotlib.pyplot as plt
import sympy
#puntos a interpolar
A= numpy.array([-3, -1 , 2, 4])
B= numpy.array([0, 4, 3, 1])

#array de polinomios
#polinomio = numpy.array([0, 0])
x = sympy.symbols("x")
##### lagrange en x , y
def base_coef(j , pts, A ):
        alfa = 1
        for i in range(pts):
            if i is not j:
                alfa = alfa * ( (x- A[i]) / (A[j]-A[i])   )
        return alfa
def Lagrange():
    polinomio = 0
    for r in range(4):
        polinomio = polinomio + base_coef(r,4,A)*B[r]
    return polinomio

poly=Lagrange()
polisimple = sympy.expand(poly)
print(poly)
print(polisimple)
fx = sympy.lambdify(x,poly) # funcion
muestras = 100
a = numpy.min(A)
b = numpy.max(A)
p_xi = numpy.linspace(a,b,muestras)

pfi = fx(p_xi)
#grafica
plt.plot(A,B,'o')
plt.plot(p_xi,pfi)
plt.show()
"""

#funcion de mezcla
 i es el numero de  funcion de corte
    pts es la cantidad de puntos
def mezcla(i , pts ):
        t = sympy.symbols("t")
        alfa = 1
        for k in range(pts):
            if i is not k:
                alfa = alfa * (t-k)/(i-k)
        print(type(alfa))
        return alfa


#calcular el polinomio
for r in range(2):
    for j in range(tamaño_fila):
        alf = mezcla(j,tamaño_fila)  # alf es simbolo se puede
        polinomio[:,r] = alf* x[:,j] +  polinomio[]
print(polinomio[0])
"""
