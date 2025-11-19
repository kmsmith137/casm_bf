#!/usr/bin/env python

import argparse
import cupy as cp

from CasmReferenceBeamformer import CasmReferenceBeamformer


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Run casm_bf unit tests')
    parser.add_argument('-g', '--gpu', type=int, default=0, help='GPU ID to use (integer)')
    
    args = parser.parse_args()
    niter = 100
    
    with cp.cuda.Device(args.gpu):
        lib = CasmReferenceBeamformer.libcasm_bf()
    
        # This test is slower than the others, so just run it once.
        CasmReferenceBeamformer.test_interpolative_beamforming()

        for i in range(niter):
            print(f'\nIteration {i+1}/{niter}\n')
            
            lib.casm_bf_test_microkernels()
            CasmReferenceBeamformer.test_cuda_python_equivalence(linkage='ctypes')

        print(f'\nUnit tests passed! (GPU={args.gpu})')
