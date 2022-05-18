import math
from mimetypes import init
from zlib import DEF_BUF_SIZE     #Importera matte bibloteket för att kunna få tag på matte funktioner

a = 4

h = 0.001





upphojning = pow(a, 4)      #pow är upphöjning
x = (a ** h - 1)/h


print(upphojning)
print(x)
print(math.log(4))      #Resultatet närmar sig lim h --> 0





def först(number):
    H = math.log(1)

    ((number + H) - (number)) / H
