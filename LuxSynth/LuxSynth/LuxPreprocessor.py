#!/usr/bin/env python3
## Copyright (c) MIT.  All rights reserved.
## lux (vjlux@gmx.at) 2016

############################################################
# Imports
############################################################

import logging

import LuxImage

############################################################
# Globals
############################################################

############################################################
# Classes
############################################################

class LuxPreprocessor(object):
    """Preprocessor class for raw data loading."""

    m_outputPath    = "./";
    m_inputPath     = "./";    

    def __init__(
        self,
        p_inputPath,
        p_outputPath):
        self.m_outputPath = p_outputPath;
    
