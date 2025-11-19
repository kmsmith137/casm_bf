#!/usr/bin/env python

import argparse
import cupy as cp

from CasmReferenceBeamformer import CasmReferenceBeamformer

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Run casm_bf timings')
    parser.add_argument('-g', '--gpu', type=int, default=0, help='GPU ID to use (integer)')
    parser.add_argument('--ncu', action='store_true', help="Just run a single kernel (intended for profiling with nvidia 'ncu')")
    
    args = parser.parse_args()
    
    with cp.cuda.Device(args.gpu):
        lib = CasmReferenceBeamformer.libcasm_bf()
        lib.casm_bf_run_timings(args.ncu)
