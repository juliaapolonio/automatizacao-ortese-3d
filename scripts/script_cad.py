# script CAD para alteracao de peça dadas altura_mao e largura_mao
# Feito por Julia Apolonio em 27/04/2020
#
# Para executa-lo, instale o FreeCAD no conda (conda install -c conda-forge freecad),
# modifique os paths de entrada e saida e execute esse script (freecadcmd.exe C:\<caminho>\script_cad.py)
#
# Como resultado, voce deve obter uma peça chamada "teste3.stl", que eh a ortese de mao redimensionada de acordo 
# com os valores de altura e largura colocados

# Bibliotecas necessárias
import FreeCAD as FC
import Mesh as ms

# Valores de operação de constraint no solido
heightQuota = 46
widthQuota = 7

# Valores de medida obtidos no script de processamento de img
heightSize = 30
widthSize = 70

# Abre o arquivo
App.openDocument(r"../data/ortese_mao_freecad.FCStd")

# Define o sketch
ActiveSketch = App.ActiveDocument.getObject('Sketch')

# Altera a altura
App.ActiveDocument.Sketch.setDatum(heightQuota, App.Units.Quantity(str(heightSize) + '.000000 mm'))

# Altera a largura
App.ActiveDocument.Sketch.setDatum(widthQuota, App.Units.Quantity(str(widthSize) + '.000000 mm'))

# Refresh
print("Running Refresh")
App.getDocument('ortese_mao_freecad').recompute()

# Salva o .stl
__objs__= []
__objs__.append(FC.getDocument("ortese_mao_freecad").getObject("Body"))
ms.export(__objs__,u"../data/outputCAD.stl")