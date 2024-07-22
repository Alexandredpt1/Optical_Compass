#!/usr/bin/env python3

import subprocess
import sys
import time
sys.path.append(r'C:\Users\stagiaire_biorob\AppData\Local\Programs\Python\Python311\Lib\site-packages\ebus-python\samples')
import lib.PvSampleUtils as psu
sys.path.append(r'C:\Users\stagiaire_biorob\Documents\Stage_Polarisation_UV\Logiciels\control_moteur\elliptec-main\tests')
from test_rotator import reach_angle, home
import Talker_listener as tl
import argparse

parser = argparse.ArgumentParser(description="Description de votre programme.")
parser.add_argument('--n', type=int, default=101, help='Un nombre entier.')

args = parser.parse_args()

number = args.n + 1


# Choose the script you want to run in a different terminal
camera_thread_image_loop = r'C:\Users\stagiaire_biorob\Documents\Stage_Polarisation_UV\Logiciels\Moteur+Caméra\camera_thread_image_loop.py' # Will saves the pictures at the 4 angles

# Give the path to python 3.11 to run the script in 3.11
python_path = r'C:\Users\stagiaire_biorob\AppData\Local\Programs\Python\Python311\python.exe' 

# Run the chosen script
subprocess.Popen(['start', 'cmd', '/k', python_path, camera_thread_image_loop, '--n', str(number)], shell=True)

for j in range(1,number):

    print("---------------", j, "---------------")

    # Set up socket communication
    PORT = 65432
    PORT2 = 65431

    # Give the list of angles to reach (it is relative) 
    relatives_angles = [0, 45, 45, 45]

    # Set a counter
    theorical_angles = 0

    # Homing the motor
    home()

    # Wait confirmation that the camera is ready
    tl.listener_bloquant(PORT)

    # Time of the beginning of the acquitsition
    ts = time.time()

    # Change the port to avoid conflicts
    PORT += 1

    for i in range(4):
        print("avant le if:", i)    
        if i >= 1 :
            print("nombre boucle:", i)
            tl.listener_bloquant(PORT2) # Wait the information from the 2nd script to continue
        print("Port Ouvert:", PORT)
        reach_angle(relatives_angles[i], theorical_angles) # Reach the angle
        print("enregistre l'image")
        print("avant")
        tl.talker_bloquant(PORT) # Give the information to the 2nd script to save the picture
        print("après")
        PORT += 1 # Change the port to avoid conflicts

        theorical_angles += 45 # Defines the relative motor position

    # Time of the end of the acquitsition
    tf = time.time()
    print("Time of acquisition : ", tf - ts)
    tl.listener_bloquant(PORT2) # End the 2nd script


print("fin de la boucle")
