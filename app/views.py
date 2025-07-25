import os
from django.http import HttpResponse
from django.shortcuts import render
import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
from utils.preprocess import preProcess
from utils.processingMatrix import proccessmatrix
from app.data.DataGenerate import archiveGenerator
from app.data.EquationGenerate import eqGenerator
import numpy as np

count = 0

def index(_):
    global count
    if count > 4:
        # Max iterations reached
        return HttpResponse(b"STOP!!")
    count += 1
    archiveGenerator("generalArchive","./utils/storage/sources/")
    eqGenerator("eqArchive","./utils/storage/formulas/")
    preProcess()
    vectores = proccessmatrix()
    grafica3D(_, vectores[:][0], vectores[:][1], vectores[:][2])
    distancias = distPoints(vectores[:][0], vectores[:][1], vectores[:][2])
    return render(_,'home/index.html',{'distancias': distancias,})

def grafica3D(request, x, y, z):
    fig = plt.figure(figsize=(10,10))
    graph = fig.add_subplot(111, projection='3d')

    x, y, z = chechvectors(x, y, z)

    x = np.append(x, x[0])
    y = np.append(y, y[0])
    z = np.append(z, z[0])

    graph.plot(x, y, z, color='blue', linestyle='--', marker='o', markersize=5, linewidth=1)
    
    graph.set_xlabel('Eje X', fontsize=12)
    graph.set_ylabel('Eje Y', fontsize=12)
    graph.set_title('Resultados', fontsize=16)
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    file = "graphics.png"
    path = os.path.join("app/static/graphics/", file)
    plt.savefig(path, format='png', dpi=100, bbox_inches='tight')
    plt.close()
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def chechvectors(x,y,z):
    if isinstance(x, np.ndarray):
        if  np.isnan(x).any():
            x = np.array([0, 0, 0])
    else:
        x = np.array([0, 0, 0])

    if isinstance(y, np.ndarray):
        if  np.isnan(y).any():
            y = np.array([1, 1, 1])
    else:
        y = np.array([1, 1, 1])

    if isinstance(z, np.ndarray):
        if  np.isnan(z).any():
            z = np.array([2, 2, 2])
    else:
        z = np.array([2, 2, 2])

    return x,y,z

def distPoints(x,y,z):
    x, y, z = chechvectors(x, y, z)
    dist1= np.linalg.norm(x - y)
    dist2 = np.linalg.norm(x - z)
    dist3 = np.linalg.norm(y - z) 
    distA = "Distancia entre A y B: " + str(dist1)
    distB = "Distancia entre A y C: " + str(dist2)
    distC = "Distancia entre B y C: " + str(dist3)
    distancias = {'AB': distA,'AC': distB,'BC': distC}
    return distancias