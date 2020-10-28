#!/bin/bash

conda create -n ort3d -y python=3.7
conda install -n ort3d -c conda-forge -y freecad
~/miniconda3/envs/ort3d/bin/pip install -r requirements.txt
wget https://dl.slic3r.org/linux/slic3r-1.3.0-linux-x64.tar.bz2
bzip2 -dc slic3r-1.3.0-linux-x64.tar.bz2 | tar xvf -
rm *.bz2
cd "$(data/models "$0")"
wget http://posefs1.perception.cs.cmu.edu/OpenPose/models/hand/pose_iter_102000.caffemodel
