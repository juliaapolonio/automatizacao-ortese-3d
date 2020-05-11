# Automatização da confecção de órteses 3D

Amorim, J A<sup>1</sup>, Nagem D A P<sup>1</sup>

<sup>1</sup> Laboratório de Inovação Teconológica em Saúde, UFRN

## Descrição

Esse repositório contém os scripts para automatização da confecção de órteses 3D.

O software consiste de 3 passos:

* Processamento da imagem para obter as dimensões da mão;
* Modificação do modelo 3D com base nas dimensões em um programa CAD;
* Criação de um arquivo gcode com base no objeto modificado e em parâmetros da impressora do usuário.

Input: Imagem (qualquer suportada por [OpenCV](https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56))

Output: Arquivo GCODE

## Instruções para instalar e executar

Primeiro, instale o [miniconda3](https://docs.conda.io/en/latest/miniconda.html)  
Depois de completar a instalação, abra o terminal ou o prompt de comando e crie um novo environment chamado "ort3d" usando   
`conda create -n ort3d python=3.7`    
Então, entre no novo environment  
`conda activate ort3d`  
Nesse environment, instale o freeCAd usando  
`conda install -c conda-forge freecad`  
Navegue até o caminho desse arquivo. Depois, você vai precisar instalar todas as dependências usando  
`pip install -r requirements.txt`  
E para o freeCAD funcionar, use também  
`export PYTHONPATH=~/miniconda3/envs/ort3d/lib:$PYTHONPATH`  
Para executar, use  
`python scripts/gui.py`  


### Esse software é parte do meu TCC no curso de Engenharia Biomédica, UFRN.

# Automatization of 3d-printed orthosis manufacturing process

## Description

This repository contains the scripts for automatization of 3d-printed orthosis manufacturing process.

The software has 3 main steps: 

* Image processing to obtain hand dimensions;
* 3D model modifying based on the dimensions in a CAD software;
* G-code file creation based on the object and user's printer parameters.

Input: Image (any supported by [OpenCV](https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56))

Output: GCODE file

## Instructions for installing and executing

First, install [miniconda3](https://docs.conda.io/en/latest/miniconda.html)  
After installation is complete, open terminal or command prompt and create a new environment called "ort3d" using   
`conda create -n ort3d python=3.7`    
Then, enter on your new environment  
`conda activate ort3d`  
On this new environment, install FreeCAD using  
`conda install -c conda-forge freecad`  
Navigate to this file path. After that, you will need to install all software dependencies using   
`pip install -r requirements.txt`  
And to get things woring with freeCAD, also use  
`export PYTHONPATH=~/miniconda3/envs/ort3d/lib:$PYTHONPATH`  
To run the software, type  
`python scripts/gui.py`  


### This software is part of my undergraduate project for Biomedical Engineer, UFRN.
