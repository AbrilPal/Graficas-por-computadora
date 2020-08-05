# Andrea Abril Palencia Gutierrez, 18198
# Graficas por computadora, seccion 20
# 04/08/2020

def normal_fro(self, norm):
    return((norm[0]**2+norm[1]**2+norm[2]**2)**(1/2))
    
def resta_lis(self, x0, x1, y0, y1, z0, z1):
    resultado=[]
    resultado.append(x0-x1)
    resultado.append(y0-y1)
    resultado.append(z0-z1)
    return resultado

def division_lis_fro(self, norm, frobenius):
    if (frobenius==0):
        resultado=[]
        resultado.append(float('NaN'))
        resultado.append(float('NaN'))
        resultado.append(float('NaN'))
        return resultado
    else:
        resultado=[]
        resultado.append(norm[0]/ frobenius)
        resultado.append(norm[1]/ frobenius)
        resultado.append(norm[2]/ frobenius)
        return resultado

def cruz_lis(self, v0, v1):
    resultado=[]
    resultado.append(v0[1]*v1[2]-v1[1]*v0[2])
    resultado.append(-(v0[0]*v1[2]-v1[0]*v0[2]))
    resultado.append(v0[0]*v1[1]-v1[0]*v0[1])
    return resultado

def punto(self, normal, lightx, lighty, lightz):
    return (normal[0]*lightx+normal[1]*lighty+normal[2]*lightz)

def baryCoords(A, B, C, P):
    # u es para la A, v es para B, w para C
    try:
        u = ( ((B.y - C.y)*(P.x - C.x) + (C.x - B.x)*(P.y - C.y) ) /
              ((B.y - C.y)*(A.x - C.x) + (C.x - B.x)*(A.y - C.y)) )

        v = ( ((C.y - A.y)*(P.x - C.x) + (A.x - C.x)*(P.y - C.y) ) /
              ((B.y - C.y)*(A.x - C.x) + (C.x - B.x)*(A.y - C.y)) )

        w = 1 - u - v
    except:
        return -1, -1, -1

    return u, v, w