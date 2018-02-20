#!/usr/bin/env python

import os
from fabricate import *

TEX = 'texi2pdf'
PROJ_ROOT = '.'
SOURCE = os.path.join(PROJ_ROOT, 'source', 'resume.tex')

setup(dirs=[PROJ_ROOT,
            os.path.join(PROJ_ROOT, 'source')])

def build():
    run(TEX, SOURCE)

def check():
    return int(outofdate(build))

def clean():
    autoclean()

def rebuild():
    clean()
    build()

main()
