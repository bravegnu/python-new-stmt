#!/bin/bash

sed -e 's/repeat\(.*\):/for _ in range(\1):/' < $1 > out.py