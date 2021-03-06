#!/usr/bin/env python3
## Copyright (c) MIT.  All rights reserved.
## lux (vjlux@gmx.at) 2016

############################################################
# Imports
############################################################

import argparse
import logging

import LuxPreprocessor as pre
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
    parser.add_argument('-p', '--preprocess',help='Run lux synth preprocessor.');
    parser.add_argument('-v', '--verbosity',help='Set verbosity level.');
                       
    args = parser.parse_args();
    
    args.verbosity = 'debug';
    
    # setup runtime environment
    logging.basicConfig(level=LOGLEVELS[args.verbosity]);
    
    configFileName = '';
    config = LuxUtils.TryLoadConfig(configFileName);

    # preprocessing stage
    if args.preprocess != None:
        pre.RunPreprocessing(args.preprocess, config);

if __name__ == "__main__":

    Run();
     