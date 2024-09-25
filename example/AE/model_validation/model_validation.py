import sys
import os

WORKDIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_DIR = os.path.abspath(os.path.join(WORKDIR, "..", "..", "python"))
sys.path.append(PYTHON_DIR)

import perflow as pf
from pag import *

pflow = pf.PerFlow()

nprocs = 8
binary = "cg.B.8"

# Run the binary and return program abstraction graphs
binary = os.path.join(WORKDIR, binary)
tdpag, ppag = pflow.run(
    binary=binary, cmd=f"mpirun -n {nprocs} --use-hw-threads {binary}", nprocs=nprocs
)

# Directly use a builtin model
pflow.mpi_profiler_model(tdpag=tdpag, ppag=ppag)
