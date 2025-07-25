import os
from django.http import HttpResponse
from django.shortcuts import render
import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
from utils.preprocess import preProcess
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
    eqGenerator("eqArchive.bin","./utils/storage/formulas/")
    vector = preProcess()
    grafica3D(_)
    return render(_, 'home/index.html')

def grafica3D(request, x = np.array([2,3,4]), y = np.array([3,4,3]), z = np.array([3,3,4])):
    fig = plt.figure(figsize=(10,10))
    graph = fig.add_subplot(111, projection='3d')

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