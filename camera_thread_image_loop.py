import os
import sys
import eBUS as eb
sys.path.append(r'C:\Users\stagiaire_biorob\AppData\Local\Programs\Python\Python311\Lib\site-packages\ebus-python\samples')
import lib.PvSampleUtils as psu
sys.path.append(r'C:\Users\stagiaire_biorob\AppData\Local\Programs\Python\Python311\Lib\site-packages\ebus-python\samples\Acquire_image_loop.py')
from Acquire_image_loop import connect_to_device, open_stream, configure_stream, configure_stream_buffers, process_pv_buffer, acquire_image
import Talker_listener as tl
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(description="Description de votre programme.")
parser.add_argument('--n', type=int, required=True, help='Un nombre entier.')

args = parser.parse_args()

number = args.n

# Get the current date
now = datetime.now()

# Format the date and time
current_date = now.strftime("%d.%m.%Y")

chemin = r'C:\Users\stagiaire_biorob\Documents\Stage_Polarisation_UV\Donnee'

chemin += f'\{current_date}'


# Create the directory
os.makedirs(chemin, exist_ok=True)

kb = psu.PvKb() #give access to the keyboard

# Check if OpenCV is available
opencv_is_available=True
try:
    # Detect if OpenCV is available
    import cv2
    opencv_version=cv2.__version__
except:
    opencv_is_available=False
    print("Warning: This sample requires python3-opencv to display a window")

# Connect to camera
print("ImageProcessing:")
connection_ID = psu.PvSelectDevice()



# Set up socket communication
PORT = 65432


if connection_ID:
    device = connect_to_device(connection_ID)
    if device:
        stream = open_stream(connection_ID)
        if stream:
            configure_stream(device, stream)
            buffer_list = configure_stream_buffers(device, stream)
            for j in range(1,number):
                print("---------------", j, "---------------")
                tl.talker_bloquant(PORT) # Give the information to the 1st script to continue 
                acquire_image(device, stream, j, chemin) # Run a 3rd script to save the pictures 
                print("ending")
            buffer_list.clear()

            # Close the stream
            print("Closing stream")
            stream.Close()
            eb.PvStream.Free(stream);    

        # Disconnect the device
        print("Disconnecting device")
        device.Disconnect()
        eb.PvDevice.Free(device)  

print("End")
kb.stop() # Disconnect keyboard 

