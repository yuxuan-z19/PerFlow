import sys
import os

WORKDIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_DIR = os.path.abspath(os.path.join(WORKDIR, "..", "..", "python"))
sys.path.append(PYTHON_DIR)

import perflow as pf
from pag import *

pflow = pf.PerFlow()

# Run the binary and return a program abstraction graph
nprocs = 32
binary = "cg.B.x"

binary = os.path.join(WORKDIR, binary)
tdpag, ppag = pflow.run(
    binary=binary,
    cmd=f"mpirun -n {nprocs} --use-hwthread-cpus {binary}",
    nprocs=nprocs,
)

# get the latest pag dir
pag_dir_list = sorted(
    [dir for dir in os.listdir(WORKDIR) if f"-{nprocs}p-" in dir], reverse=True
)
pag_dir = os.path.join(WORKDIR, pag_dir_list[0])
pflow.readPag(dir=pag_dir)

# # draw pags and save as PDF files
# pflow.draw(tdpag, save_pdf = './cg.B.8.tdpag')
# pflow.draw(ppag, save_pdf = './cg.B.8.ppag')

# Perform imbalance analysis
pflow.communication_pattern_analysis_model(nprocs=nprocs)
