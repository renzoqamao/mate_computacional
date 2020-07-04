import numpy
import scipy.interpolate as si
from matplotlib import pyplot as plt
# puntos de control
ptscontrol = numpy.array([[-1.,0.],
                         [1.,4.],
                         [3.,-2.],
                         [4.,3.],
                         [6.,1.]])
muestra=200
grado = 3

def b_spline(cv,muestra,grado):
    tam = cv.shape[0] # tamaño
    kv = numpy.clip(numpy.arange(tam+grado+1)-grado,0,tam-grado) # toma un ([0,1,2,3,4,5,6,7] -3=[-3,-2, -1 , 0, 1 ,2 ,3 ,4] , 0 , 2)
     #=> [0,0,0,0,1,2,2,2,2]
    t  = numpy.linspace(0,tam-grado,muestra) # t = [0,2] con 200 puntos
    #retorna un par de t y b-spline(t)
    return numpy.array( si.splev(t , ( kv , cv.T , grado) )  ).T
for d in range(2):
    p = b_spline(ptscontrol,muestra,grado)
    x_spline,y_spline = p.T
    print(x_spline)
    print(y_spline)
    plt.plot(x_spline,y_spline,'k-',label='Grado %s'%d)
plt.plot(ptscontrol[:,0],ptscontrol[:,1], 'o--', label='Control Points')
plt.show()
