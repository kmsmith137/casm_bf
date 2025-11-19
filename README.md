Reference: see the "CASM beamformer" overleaf:

Dependencies: nvcc, cupy (+ matplotlib if you want to reproduce the plots in the overleaf).

I'm using the following conda environment:
```
# Note: also installs a recent nvcc (v12.9, May 2025).
# The ubuntu nvcc installed on the casm node is pretty old (v12.0, Jan 2023).
# With the older nvcc, the beamformer still compiles, but runs ~6% slower.
conda create -n casm_bf cuda-nvcc cupy matplotlib cuda-sanitizer-api
conda activate casm_bf
```
Build beamformer, run tests, run timings:
```
make

# The '-g1' flag runs on GPU 1 (instead of GPU 0, the default).
# Currently, on the casm node, GPU 0 is locked to the base clock (1500 MHz),
# whereas the other GPUs can run at the boost clock (~2300 MHz).

python run_tests.py -g1
python run_timings.py -g1
```

