#!/bin/bash

python build.py $1 $2
cd out
lilypond out_$1.ly
open out_$1.pdf