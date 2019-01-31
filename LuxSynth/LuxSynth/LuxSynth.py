#!/usr/bin/env python3
## Copyright (c) MIT.  All rights reserved.
## lux (vjlux@gmx.at) 2016

############################################################
# Imports
############################################################

import argparse
import logging

import LuxPreprocessor
import LuxUtils

############################################################
# Globals
############################################################

LOGLEVELS = {  'debug':logging.DEBUG,
               'info':logging.INFO,
               'warning':logging.WARNING,
               'error':logging.ERROR,
               'critical':logging.CRITICAL};

############################################################
# Methods
############################################################
    
def Run():
    parser = argparse.ArgumentParser();
    
    # preprocessing stage
    parser.add_argument('-p', '--preprocess'    ,help='Run lux synth preprocessor.');
        
    args = parser.parse_args();

    # setup runtime environment
    logging.basicConfig(level=LOGLEVELS[args.verbosity]);
    
    config = LuxUtils.TryLoadConfig();

    # preprocessing stage
    if args.preprocess != None:
        pre.RunPreprocessing(args.preprocess, config);

if __name__ == "__main__":

    Run();
     