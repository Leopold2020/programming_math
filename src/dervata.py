# import matplotlib.pyplot as plt
import numpy as np


def numDeriv(f,x,h):
    return (f(x+h)-f(x))/h
    

def funk(x):
    return 4*x*x




print(numDeriv(funk,3,0.01))


# xplot=np.linspace(0,2,10)
# yplot=funk(xplot)
#plt.title("Line graph")
# plt.plot(xplot, yplot, color="red")

# plt.show()
# print(yplot)