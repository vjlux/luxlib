#!/usr/bin/env python3
## Copyright (c) MIT.  All rights reserved.
## lux (vjlux@gmx.at) 2016

############################################################
# Imports
############################################################

import argparse
import logging

import LuxImage as li
import LuxUtils as lu
import LuxPreprocessor as lp

import matplotlib.pyplot as plt

import open3d as o3d

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
    parser.add_argument('-v', '--verbosity',help='Set verbosity level.');
                       
    args = parser.parse_args();
    
    args.verbosity = 'debug';
    
    # setup runtime environment
    logging.basicConfig(level=LOGLEVELS[args.verbosity]);
    
    configFileName = '';
    config = lu.TryLoadConfig(configFileName);
    
    #print("Let's draw some primitives")
    #mesh_box = o3d.geometry.TriangleMesh.create_box(width=1.0,
    #                                                height=1.0,
    #                                                depth=1.0);
    #o3d.visualization.draw_geometries([mesh_box])
    
    pre = lp.LuxPreprocessor('','');
    depthFileName = "../Data/Images/navvis_depth.png";
    depth = pre.LoadDepthFromRGB24bitImage(depthFileName);
    
    print(str(depth[10,10]));
    
    plt.imshow(depth);

if __name__ == "__main__":

    Run();
     