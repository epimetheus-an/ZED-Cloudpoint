# this code follows the tutorial for the ZED-sdk: Object detection > Birds eye viewer

import sys
import numpy as np
import cv2
import pyzed.sl as sl
import argparse
import ogl_viewer.viewer as gl
import cv_viewer.tracking_viewer as cv_viewer
import platform
from collections import deque

def main():
    # create camera object 
    zed = sl.Camera()

    # 01 - set initial parameter
    init_params = sl.InitParameters()
    init_params.sdk_verbose = 1
    init_params.coordinate_units = sl.UNIT.MILLIMETER
    init_params.coordinate_system = sl.COORDINATE_SYSTEM.RIGHT_HANDED_Z_UP

    # 02 - OBJECT DETECTION: set initial parameter
    init_params.depth_minimum_distance = 15
    init_params.depth_maximum_distance = 300
    init_params.depth_mode = sl.DEPTH_MODE.NEURAL_PLUS

    # Open the camera
    err = zed.open(init_params)
    if err > sl.ERROR_CODE.SUCCESS:
        print("No camera detected. Exiting...")
        exit(1)

    # enable positional tracking
    positional_tracking_parameters = sl.PositionalTrackingParameters()
    positional_tracking_parameters.set_as_static = True
    positional_tracking_parameters.enable_area_memory = True # if camera is moved, the coordinates stays the same
    positional_tracking_parameters.set_floor_as_origin = True
    zed.enable_positional_tracking(positional_tracking_parameters)

    # enable object detection module
    obj_param = sl.ObjectDetectionParameters()
    obj_param.detection_model = sl.OBJECT_DETECTION_MODEL.MULTI_CLASS_BOX_ACCURATE
    obj_param.enable_tracking = True
    returned_state = zed.enable_object_detection(obj_param)

    # get camera's final information and serial number
    camera_configuration = zed.get_camera_information().camera_configuration
    camera_serial = zed.get_camera_information().serial_number
    print(f"ZED camera serial number: {camera_serial}")

    if returned_state != sl.ERROR_CODE.SUCCESS:
        print("enable_object_detection", returned_state, "\nExit program.")
        zed.close()
        exit()

    # Close camera
    zed.close()

if __name__ == "__main__":
    main()