import subprocess

def runSlicer():
    subprocess.call("../Slic3r/perl-local -I../Slic3r/local-lib/lib/perl5 ../Slic3r/slic3r.pl" + 
    " ../data/outputCAD2.stl --load ../data/my_config.ini --output ../data/saida.gcode", shell = True)

