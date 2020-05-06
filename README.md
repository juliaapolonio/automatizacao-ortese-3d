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

### This software is part of my undergraduate project for Biomedical Engineer, UFRN.

### Installing guidelines:

Install conda ...

conda create -n auto freecad

### This is necessary to execute FreeCAD within python
export PYTHONPATH=/home/diegomscoelho/miniconda2/envs/julia/lib:$PYTHONPATH