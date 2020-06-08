#!/bin/bash
#rotina para impressão

BIN=$(readlink "$0")
DIR=$(dirname "$BIN")
export LD_LIBRARY_PATH="$DIR/bin"
exec "$DIR/perl-local" -I"$DIR/local-lib/lib/perl5" "$DIR/slic3r.pl" "../data/outputCAD.stl" "--load" "my_config.ini" "--print-center" "100,100" "--output" "../data/saida.gcode" $@
