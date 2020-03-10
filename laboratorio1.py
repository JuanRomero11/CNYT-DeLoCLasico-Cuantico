from sys import stdin
import math

def suma(a,b):
    return (a[0]+b[0],a[1]+b[1])
def resta(a,b):
    return (a[0]-b[0],a[1]-b[1])
def multiplicacion(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def division(a,b):
    return ((a[0]*b[0]+a[1]*b[1])/((b[0]**2)+(b[1]**2)),((a[1]*b[0]-a[0]*b[1])/((b[0]**2)+(b[1]**2))))
def modulo(a):
    return (a[0]**2+a[1]**2)**(1/2)
def conjugado(a):
    return (a[0],-a[1])
def polar(a):
    return (modulo(a), math.atan(a[1]/a[0]))
def fase(a):
    return math.atan(a[1]/a[0])

def sumaVectoresComplejo(vector1,vector2):
    vectorFinal=[]
    for i in range(len(vector1)):
        vectorFinal.append(suma(vector1[i],vector2[i]))
    return vectorFinal

def InversaDeUnVector(vectorInicial):
    vectorFinal=[]
    for i in vectorInicial:
        vectorFinal+=[(-i[0],-i[1])]
    return vectorFinal

def EscalarPorVector(num,lis):
    final=[]
    for i in range(len(lis)):final+=[multiplicacion(num,lis[i])]
    return final

def sumaMatrices(matInicial,matInicial2):
    lista=[[None]*len(matInicial) for i in range(len(matInicial2))]
    for i in range(len(matInicial)):
        for j in range(len(matInicial2)):lista[i][j]=suma(matInicial[i][j],matInicial2[i][j])
    return lista

def complejoPorVector(c1,m1):
    matriz=[]
    for i in range(0,len(m1)):
            matriz.append(multiplicacion(m1[i],c1))
    return matriz

def inversaMatrizImaginaria(MatrizInicial):
    matriz = []
    for i in range(0,len(MatrizInicial)):
        matriz.append(InversaDeUnVector(MatrizInicial[i]))
    return matriz

def complejoPorMatriz(c1,MatrizInicial):
    matriz=[]
    for i in range(0,len(MatrizInicial)):
        vector=[]
        for j in range(0,len(MatrizInicial[0])):
            vector.append(multiplicacion(MatrizInicial[i][j],c1))
        matriz.append(vector)
    return matriz


def matrizTranspuesta(matrizInicial):
    matriz=[]
    for i in range(0,len(matrizInicial[0])):
        columna = [x[i] for x in matrizInicial]
        matriz.append(columna)
    return matriz 
        
     
def matrizConjugada(MatrizInicial):
    matriz=[]
    for i in range(0,len(MatrizInicial)):
        vector=[]
        for j in range(0,len(MatrizInicial[0])):
            vector.append((MatrizInicial[i][j][0],MatrizInicial[i][j][1]*-1))
        matriz.append(vector)
    return matriz
def productoVectoresImaginarios(c1,c2):
    ini = (0,0)
    for i in range(len(c1)):
        var = multiplicacion(c1[i],c2[i])
        ini = suma(ini,var)
    return ini
def accionMatrizSobreVector(v1,MatrizInicial):
    v = []
    for i in range(len(MatrizInicial)):    
            v.append(productoVectoresImaginarios(v1,MatrizInicial[i]))
    return v
def matrizAdjunta(MatrizInicial):
    matriz=matrizTranspuesta(MatrizInicial)
    matriz=matrizConjugada(matriz)
    return matriz


def productoMatricesImaginarias(MatrizInicial,m2):
    matriz = [[None] * len(m2[0]) for i in range(len(MatrizInicial))]
    for i in range(len(MatrizInicial)):
        for j in range(len(m2[0])):
            columna = [row[j] for row in m2]
            matriz[i][j] = productoVectoresImaginarios(MatrizInicial[i],columna)
    return matriz



def normaMatriz(mat):
    num1=0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            x=mat[i][j]
            num1+=(x[0]**2+x[1]**2)
    res=round(num1**0.5,3)
    return res
def distanciaMatrices(mat1,mat2):
    mat_fin=[[(0,0)]*len(mat1[0]) for x in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat_fin[i][j]=resta(mat1[i][j],mat2[i][j])
    res=normaMatriz(mat_fin)
    return res


def unitaria(mat):
    mat_fin=productoMatricesImaginarias(mat,matrizAdjunta(mat))
    mat_uni=[[(0,0)]*len(mat[0])for x in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i==j:
                mat_uni[i][j]=(1,0)
    if mat_fin==mat_uni:
        return True
    else:
        return False


def hermitiana(mat):
    if mat==matrizAdjunta(mat):
        return True
    else:
        return False


def productoTensor(m1,m2):
    matriz = []
    for i in range(len(m1)):
        matM = [[]] *len(m2)
        for j in range(len(m1[i])):
            m3 = complejoPorMatriz(m1[i][j],m2)
            for k in range(len(m2)):
                
                matM[k] = matM[k] + m3[k]
        for k in range(len(m2)):
            matriz.append(matM[k])
    return matriz

def productoTensorialVectores(v1,v2):
    vFinal = [0 for i in range(len(v1)*len(v2))]
    cont = 0
    for i in range(len(v1)):
        v3 = complejoPorVector(v1[i],v2)
        for k in range(len(v3)):
            vFinal[cont] = v3[k]
            cont+=1
    return vFinal


    

    
