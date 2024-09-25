import sys
import os

WORKDIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_DIR = os.path.abspath(os.path.join(WORKDIR, "..", "..", "python"))
sys.path.append(PYTHON_DIR)

import perflow as pf
from pag import *

pflow = pf.PerFlow()

binary = "cg.B.x"
nprocs = 8

# Run the binary and return a program abstraction graph
binary = os.path.join(WORKDIR, binary)
tdpag, ppag = pflow.run(
    binary=binary, cmd=f"mpirun -np {nprocs} --use-hw-threads {binary}", nprocs=nprocs
)

# draw pags and save as PDF files
pflow.draw(tdpag, save_pdf=f"{WORKDIR}/cg.B.{nprocs}.tdpag")
pflow.draw(ppag, save_pdf=f"{WORKDIR}/cg.B.{nprocs}.ppag")
