import matplotlib.pyplot as plt
import math
import laboratorio1
MA = [[[0,0],[1/6,0],[5/6,0]],[[1/3,0],[1/2,0],[1/6,0]],[[2/3,0],[1/3,0],[0,0]]]
MB = [[[1/3,0],[2/3,0]], [[2/3,0],[1/3,0]]]
VA = [[0.2,0],[0.1,0],[0.6,0]]
VB = [[0.7,0],[0.15,0]]
def sistemaProbabilistico(clicks):
    m1 = laboratorio1.productoTensor(MA,MB)
    vectorI= laboratorio1.productoTensorialVectores(VA,VB)
    estado = vectorI
    for i in range(clicks):
        estado = laboratorio1.accionMatrizSobreVector(estado,m1)
    fig = plt.figure(u'grafica') 
    ax = fig.add_subplot(111)
    nombres = ['00','01','02','10','11','12']
    datos = [estado[0][0],estado[1][0],estado[2][0],estado[3][0],estado[4][0],estado[5][0]]
    xx = range(len(datos))
    ax.bar(xx, datos, width=0.5, align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(nombres)
    plt.show()
    return estado
print(sistemaProbabilistico(5))
