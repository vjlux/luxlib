#!/usr/bin/env python3
## Copyright (c) MIT.  All rights reserved.
## lux (vjlux@gmx.at) 2016

############################################################
# Imports
############################################################

import logging

import LuxImage

import open3d as o3d
import numpy as np

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
    
    def LoadDepthFromRGB24bitImage(self, p_depthImageFileName):
        
        #depth = np.array([]);
        
        #color_raw = o3d.io.read_image("../../TestData/RGBD/color/00000.jpg")
        depth_raw = o3d.io.read_image(p_depthImageFileName);
        
        
        return depth_raw;