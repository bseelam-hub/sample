#!/usr/bin/python
import pathlib
#pathlib.Path('/home/brahma/gitdir').mkdir(parents=True, exist_ok=True)
import os
try:
    os.makedirs('/home/brahma/gitdir')
except OSError:
    pass
