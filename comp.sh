#!/bin/bash

python build.py $1 $2 $3
cd out/$1
lilypond ThreeNotesScore.ly
open ThreeNotesScore.pdf