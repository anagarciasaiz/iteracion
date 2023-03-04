def cuadrados_perfectos(lim):
    cuadrados=[]
    for i in range(1,lim+1):
        n=1
        while n*n<=i:
            if n*n==i:
                cuadrados.append(i)
            n=n+1
    return cuadrados

import math
def raiz_cuadrada_entera(a):
    x = int(math.sqrt(a))
    return x
