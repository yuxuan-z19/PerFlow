import sys
import os

WORKDIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_DIR = os.path.abspath(os.path.join(WORKDIR, "..", "..", "python"))
sys.path.append(PYTHON_DIR)

import perflow as pf
from pag import *

pflow = pf.PerFlow()

nprocs = 8
binary = "cg.B.x"

# Run the binary and return a program abstraction graph
binary = os.path.join(WORKDIR, binary)
tdpag, ppag = pflow.run(
    binary=binary, cmd=f"mpirun -np {nprocs} --use-hw-threads {binary}", nprocs=nprocs
)

# # draw pags and save as PDF files
# pflow.draw(tdpag, save_pdf = './cg.B.8.tdpag')
# pflow.draw(ppag, save_pdf = './cg.B.8.ppag')

# Perform imbalance analysis
pflow.imbalance_analysis(tdpag.vs, nprocs=nprocs)
