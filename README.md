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
Depois de completar a instalação, reinicie o terminal e execute o arquivo `install.sh` para a instalação de todos os requisitos. Ative o ambiente com `conda activate ort3d`.   
Para executar o script, use  
`python scripts/gui.py`  

A saída do script (arquivo G-CODE) vai estar em /data/saida.gcode

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
After installation is complete, reboot terminal and run `install.sh` to install all requirements. Activate the environment using `conda activate ort3d`.    
To run the software  
`python scripts/gui.py`  

This will create your output file (.gcode) at /data/saida.gcode  

### This software is part of my undergraduate project for Biomedical Engineer, UFRN.
