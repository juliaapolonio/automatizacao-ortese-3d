#!/usr/bin/env python
# script CAD para alteracao de peça dadas altura_mao e largura_mao
# Feito por Julia Apolonio em 27/04/2020
#
# Para executa-lo, instale o FreeCAD no conda (conda install -c conda-forge freecad),
# modifique os paths de entrada e saida e execute esse script (freecadcmd.exe C:\<caminho>\script_cad.py)
#
# Como resultado, voce deve obter uma peça chamada "teste3.stl", que eh a ortese de mao redimensionada de acordo 
# com os valores de altura e largura colocados

# Bibliotecas necessárias
import FreeCAD as App
import Mesh 
import os

def script(heightSize, widthSize):

    # Definindo os fatores de escala
    defaultHeight = 190.00
    defaultWidth = 80.00

    scaleh = heightSize/defaultHeight
    scalew = widthSize/defaultWidth

    # Caminho valido para Windows e Linux 
    path = '..'+os.sep+'data'+os.sep

    # Abre o arquivo
    input_filename = 'outputCAD.stl'
    input_path = path+input_filename
    Mesh.open(input_path)
    App.setActiveDocument("Unnamed")
    App.ActiveDocument=App.getDocument("Unnamed")   

    # Mesh operations
    mesh = App.ActiveDocument.outputCAD.Mesh.copy()
    mat = App.Matrix()
    mat.scale(scalew,scaleh,1)
    mesh.transform(mat)
    Mesh.show(mesh)
    App.getDocument("Unnamed").removeObject("outputCAD")

    # Salva o .stl
    output_filename = 'outputCAD2.stl'
    output_path = path+output_filename
    mesh.write(output_path)

# Execute pipeline
if __name__ == "__main__":
    script(h,w)