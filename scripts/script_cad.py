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
import Mesh as ms
import os

def script(heightSize, widthSize):

    # Valores de operação de constraint no solido
    heightQuota = 101
    widthQuota = 96

    # Caminho valido para Windows e Linux 
    path = '..'+os.sep+'data'+os.sep

    # Abre o arquivo
    input_filename = 'ortese_mao_freecad.FCStd'
    input_path = path+input_filename

    App.openDocument(input_path)

    # Define o sketch
    ActiveSketch = App.ActiveDocument.getObject('Sketch')

    # Altera a altura
    App.ActiveDocument.Sketch.setDatum(heightQuota, App.Units.Quantity(str(heightSize) + ' mm'))

    # Altera a largura
    App.ActiveDocument.Sketch.setDatum(widthQuota, App.Units.Quantity(str(widthSize) + ' mm'))

    # Refresh
    print("Running Refresh")
    App.getDocument('ortese_mao_freecad').recompute()

    # Salva o .stl
    output_filename = 'outputCAD.stl'
    output_path = path+output_filename
    __objs__= []
    __objs__.append(App.getDocument("ortese_mao_freecad").getObject("Body"))
    ms.export(__objs__,output_path)


# Execute pipeline
if __name__ == "__main__":
    script(h,w)