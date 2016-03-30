#!/usr/bin/env python

import argparse
import subprocess
import sys
import time

def compare(*args):
    args = args[0]

    if len(args) == 2:
        oracle = args[0]
        test = args[1]
    elif len(args) == 1:
        oracle = "oracle"
        test = args[0]
    else:
        raise ValueError("Need to specify at least one test to run.")

    oracle_process = subprocess.Popen(['./{}'.format(oracle)], stdout=subprocess.PIPE)
    output = subprocess.check_output(['./compute-bleu'], stdin=oracle_process.stdout)
    oracle = float(output)

    tic = time.time()
    test_process = subprocess.Popen(['./{}'.format(test)], stdout=subprocess.PIPE)
    output = subprocess.check_output(['./compute-bleu'], stdin=test_process.stdout)
    test = float(output)

    return (oracle, test, time.time() - tic)

Modes = {
    'compare': compare,
}

print (Modes[sys.argv[1]](sys.argv[2:]))
