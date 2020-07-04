import scipy
import numpy
import matplotlib.pyplot as plt
import sympy
import math
#puntos a interpolar
A= sympy.Matrix([[-3, -1 , 2, 4],
                [0, 4, 3, 1]])

#array de polinomios
polinomio = sympy.Matrix([[0],
                        [0]])
t = sympy.symbols("t")

def combinatoria(i,n):
    return math.factorial(n) / (math.factorial(i)* math.factorial(n-i))

##### lagrange en x , y
def bernstein(i,n):
        ber = combinatoria(i,n)*((t**i))*((1-t)**(n-i))
        return ber
def Bezier(points):
    for r in range(points):
        polinomio[: , 0 ]  = polinomio[: , 0] + bernstein(r,points-1)*A[:,r]
    return polinomio

poly=Bezier(4)

polysimplex = sympy.expand(poly[0,0])
polysimpley = sympy.expand(poly[1,0])
#print(poly)
print(polysimplex)
print(polysimpley)
fx = sympy.lambdify(t,polysimplex) # funcion
fy = sympy.lambdify(t,polysimpley)
muestras = 100
lin_t = numpy.linspace(0,1,muestras)

pfix = fx(lin_t)
pfiy = fy(lin_t)
#grafica
plt.plot(A[0,:],A[1, :],'o')
plt.plot(pfix,pfiy)
plt.show()
