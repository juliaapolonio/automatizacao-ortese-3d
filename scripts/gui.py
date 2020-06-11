# This is the main and GUI function of the hole software
# GUI code taken from https://stackoverflow.com/questions/55309042/how-to-read-file-input-in-pysimplegui-then-pass-it-on-to-a-number-crunching-proc
# Missing features: obtain a new set of point; run cad script with h and v values
# Calling script_cad command from: https://www.youtube.com/watch?v=2Fp1N6dof0Y
# Made by Julia Apolonio at 05/05/2020

# Importing necessary libraries
import PySimpleGUI as sg
import subprocess
import os
import sys

# ADD FreeCAD PYTHONPATH
home = os.environ['HOME']
sys.path.append(home + '/miniconda3/envs/ort3d/lib')

# Native libraries
import click as ck
import script_cad as sc
import slicer as sl

# Make sure that scripts is executed within gui.py directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Theme for window color'
sg.theme('GreenMono')	

# First window: choose image path and atribute it into a variable
# Define layout
layout = [[sg.Text('Nome do arquivo')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]

# Generate window
window = sg.Window('Adicione a imagem da mão', layout)

# Loop to read events and values of window
while True:
    event, values = window.read()

    # Closes window and stop the script 
    if event in ('Cancel'):
        window.close()
        exit()

    if event in ('OK'):
        path = values[0]

    # Only allows the scrpit to continue is path is given
    if not path:
        sg.popup("O arquivo não foi fornecido")
        continue
    break

# Closes first window
window.close()

# Second window: choose reference points for one direction
# Define layout
layout = [  [sg.Text('Adicione os pontos de referência')],
            [sg.Button('Vertical'), sg.Button('Horizontal'), sg.Button('Confirmar'), sg.Button('Cancelar')]]

# Generate window
window = sg.Window('Sw medicao nao invasiva', layout)

# Declare parameters to choose horizontal or vertical
h = None
v = None

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event in (None, 'Cancelar'):
        window.close()
        exit()

    elif event in ('Vertical'): # calls click detection function
        v = ck.img_click(path)
    
    elif event in ('Horizontal'):
        h = ck.img_click(path)

    elif event in ('Confirmar'):
        if h is None:
            sg.popup_ok('Pontos horizontais não fornecidos')
        elif v is None:
            sg.popup_ok('Pontos verticais não fornecidos')            
        else:
            break 

window.close()

# Third window: show to user hand dimensions in mm
# Follows the same process as other loops
layout = [  [sg.Text('As dimensões dessa mão são '+str(v)+' mm de largura e '+str(h)+' mm de altura.')],
            [sg.Button('Gerar Ortese'), sg.Button('Cancelar')] ]

window = sg.Window('Sw medicao nao invasiva', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancelar'):	# If user closes window or clicks cancel
        window.close()
        exit()
    # CAD script call
    sc.script(h,v)
    sg.popup_ok('Objeto criado') 
    break

layout = [  [sg.Text("O arquivo .stl foi gerado. Gerar G-Code?")],
            [sg.Button('Fatiar'), sg.Button('Cancelar')] ]

window = sg.Window('Sw medicao nao invasiva', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancelar'):	# If user closes window or clicks cancel
        window.close()
        exit()
    # CAD script call
    sl.runSlicer()
    sg.popup_ok('G-Code gravado!') 
    break

#close GUI   
window.close()
