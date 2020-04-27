#script CAD para alteracao de peça dadas altura_mao e largura_mao
#Feito por Julia Apolonio em 27/04/2020
#
#Para executa-lo, instale o FreeCAD no conda (conda install -c conda-forge freecad),
#modifique os paths de entrada e saida e execute esse script (freecadcmd.exe C:\<caminho>\script_cad.py)
#
#Como resultado, voce deve obter uma peça chamada "teste3.stl", que eh a ortese de mao redimensionada de acordo 
#com os valores de altura e largura colocados

#abre o arquivo
import FreeCAD
FreeCAD.open(u"C:/Users/pc/Documents/ortese_mao_freecad.FCStd")

#define o sketch
ActiveSketch = App.ActiveDocument.getObject('Sketch')

#altera a altura
App.ActiveDocument.Sketch.setDatum(46,App.Units.Quantity('30.000000 mm'))

#altera a largura
App.ActiveDocument.Sketch.setDatum(7,App.Units.Quantity('70.000000 mm'))

#refresh
App.getDocument('ortese_mao_freecad').recompute()

#salva o stl
import Mesh
__objs__=[]
__objs__.append(FreeCAD.getDocument("ortese_mao_freecad").getObject("Body"))
Mesh.export(__objs__,u"C:/Users/pc/Documents/teste3_stl.stl")

#fecha tudo 
del __objs__
App.closeDocument("ortese_mao_freecad")
App.setActiveDocument("")
