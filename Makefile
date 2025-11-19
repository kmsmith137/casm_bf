# Disable built-in rules and variables (must be first).
MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-builtin-variables

# Compiler flags:
#  - need C++17 or later (I can't live without "if constexpr")
#  - assume that this is not a cross-compile (-march=native)
#  - compile SASS for RTX 4000 Ada (-gencode arch=compute_89,code=sm_89)
NVCC ?= nvcc -std=c++17 -m64 -O3 --compiler-options -Wall,-fPIC,-march=native -gencode arch=compute_89,code=sm_89

# If using a conda env, add -I$(CONDA_PREFIX)/include to nvcc flags.
ifneq ($(CONDA_PREFIX),)
CONDA_INCFLAGS = -I$(CONDA_PREFIX)/include
endif

libcasm_bf.so: CasmBeamformer.o
	$(NVCC) -shared -o $@ $^

CasmBeamformer.o: CasmBeamformer.cu CasmBeamformer.hpp
	$(NVCC) $(CONDA_INCFLAGS) -c -o $@ $<

clean:
	rm -f libcasm_bf.so CasmBeamformer.o *~
