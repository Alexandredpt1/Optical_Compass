#!/usr/bin/env python3

import sys
sys.path.append('elliptec-main\src')
import elliptec

# Test settings (adjust based on hardware)
port = 'COM5'
address = '0'
allowed_error = 0.1

def home():
    '''Rotator homes to the home offset set.'''
    # Create objects
    controller = elliptec.Controller(port)
    ro = elliptec.Rotator(controller, address=address)
    
    # Home the rotator to firmware-set position
    ro.home()

    # See if homing moved to home offset set
    reached_angle = ro.get_angle()
    home_offset = ro.get_home_offset()

    # Close the connections for other tests
    controller.close_connection()
    print("Homing to :", reached_angle)
    print(abs(reached_angle - home_offset)) 
    
    

def reach_angle(angle, theorical_angle):
    # Create objects
    controller = elliptec.Controller(port)
    ro = elliptec.Rotator(controller, address=address)

    # reach the input angle
    ro.shift_angle(angle)
    reached_angle = ro.get_angle()
    print(reached_angle)
    error = abs(reached_angle - theorical_angle)
    print(error)
    assert error <= allowed_error, "Reached angle should equal target."

    # Close the connection
    controller.close_connection()