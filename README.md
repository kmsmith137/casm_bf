## casm_bf

A mini-repo containing the CASM beamformer as two source files (`CasmBeamformer.{hpp,cu}`),
intended for including in the larger CASM pipeline.

**Reference:** see the "CASM beamformer" overleaf (let me know if you need access!)

  https://www.overleaf.com/project/68e147bd38d7ce3e40931bf1
   
**Dependencies:** nvcc, cupy (+ matplotlib if you want to reproduce the plots in the overleaf).
I'm using the following conda environment:
```
# Note: also installs a recent nvcc (v12.9, May 2025).
# The ubuntu nvcc installed on the casm node is pretty old (v12.0, Jan 2023).
# With the older nvcc, the beamformer still compiles, but runs ~6% slower.

conda create -n casm_bf cuda-nvcc cupy matplotlib cuda-sanitizer-api
conda activate casm_bf
```
**Build beamformer, run tests, run timings**:
```
git clone https://github.com/kmsmith137/casm_bf
cd casm_bf

make

# The '-g1' flag runs on GPU 1 (instead of GPU 0, the default).
# Currently, on the casm node, GPU 0 is locked to the base clock (1500 MHz),
# whereas the other GPUs can run at the boost clock (~2300 MHz).
# Also, GPU 0 is sometimes used for real-time acquisitions.

python run_tests.py -g1
python run_timings.py -g1
```
Timing results should look similar to this:
```
# Timing summary
# col 1: number of beams
# col 2: load fraction (lower is better)
32 0.401172
1024 0.419574
2048 0.440874
3072 0.465645
4096 0.48823
```
**Digging into the code:**

 - I recommend starting with the python reference implementation
   in [CasmReferenceBeamformer.py](CasmReferenceBeamformer.py), specifically
   the constructor, the `beamform()` method, and the `_beamform_exact()` method.
   Note that this implements exact brute-force beamforming, not the interpolation-based
   algorithm from the overleaf. This code establishes the beamforming API, and details
   such as sign conventions.

 - Next, see the `_beamform_interpolated()` method, which implements the interpolation-based
   beamforming algorithm. There is a unit test that verifies that `_beamform_exact()` and
   `_beamform_interpolated()` are 99% correlated for random inputs (including randomizing
   frequency channels and beam locations).

 - Next, see [CasmBeamformer.hpp](CasmBeamformer.hpp) for the C++ API. It is intended to
   be as similar as possible to the python API, so it should be self-explanatory after
   reading the python code.

 - Finally, if it's helpful to read the cuda implementation, see [CasmBeamformer.cu](CasmBeamformer.cu).
 
 

