# This is the main and GUI function of the hole software
# GUI code taken from https://stackoverflow.com/questions/55309042/how-to-read-file-input-in-pysimplegui-then-pass-it-on-to-a-number-crunching-proc
# Missing features: obtain a new set of point; run cad script with h and v values
# Calling script_cad command from: https://www.youtube.com/watch?v=2Fp1N6dof0Y
# Made by Julia Apolonio at 05/05/2020

# Importing necessary libraries
import PySimpleGUI as sg
import backup_click
import subprocess

# Theme for window color
sg.theme('DarkBlue')	

# First window: choose image path and atribute it into a variable
event, values = sg.Window('Adicione a imagem da mão', [[sg.Text('Nome do arquivo')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).Read()
path = values[0]

# Second window: choose reference points for one direction

# Define layout
layout = [  [sg.Text('Adicione os pontos de referência')],
            [sg.Button('Vertical'), sg.Button('Horizontal'), sg.Button('Cancelar')] ]

# Generate window
window = sg.Window('Sw medicao nao invasiva', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in ('Vertical'): #calls click detection function
    	v = backup_click.img_click(path,'v')
    
    elif event in ('Horizontal'):
        h = backup_click.img_click(path,'h')
    break


# Third window: choose reference points for another direction (same thing as upper block)
layout = [  [sg.Text('Adicione os pontos de referência')],
            [sg.Button('Vertical'), sg.Button('Horizontal'), sg.Button('Cancelar')] ]

window = sg.Window('Sw medicao nao invasiva', layout)

while True:
    event, values = window.read()
    if event in ('Vertical'):
        v = backup_click.img_click(path,'v')
    
    elif event in ('Horizontal'):
        h = backup_click.img_click(path,'h')
    break

# Fourth window: show to user hand dimensions in mm
layout = [  [sg.Text('As dimensões dessa mão são '+str(v)+' mm de largura e '+str(h)+' mm de altura.')],
            [sg.Button('Gerar Ortese'), sg.Button('Cancelar')] ]

window = sg.Window('Sw medicao nao invasiva', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancelar'):	# if user closes window or clicks cancel
        break
    subprocess.run('freecadcmd script_cad.py', shell = True) #calls CAD script directly at command line
    sg.popup_ok('Objeto criado') 
    break

#close GUI   
window.close()
