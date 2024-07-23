# Optical_Compass
This repository allows you to control the ell14 elliptec motor from thorlabs simultaneously with a camera (here was used the GO-8105M-5GE-UV camera from JAI) and to process skylight polarization images.

## Description

This project is composed of the following codes :
* main_loop \
This Python script is designed to control a camera and a motor, coordinating their actions through socket communication. The script ensures that the camera takes pictures at specific angles by commanding the motor to move to those angles and then signaling the camera to capture the images. The script runs a secondary script in a separate terminal to handle image capture.
    * By default, the program will run for 100 iterations, but you can choose the number by adding --n your_number at the end of the command : py -3.11 main_loop.py --n your_number

* motor_rotation \
This Python script is designed to control and test an Elliptec rotator via a specified serial port. The functions are inspired from the tests functions of https://github.com/roesel/elliptec.git.

* camera_thread_image_loop.py \
This Python script is designed to acquire and save images from a GigE Vision or USB3 Vision camera using the eBUS SDK, incorporating elements from the Python API scripts based on Python version 3.11 (available at https://www.jai.com/support-software/jai-software/). It integrates socket communication to coordinate with an external script and leverages OpenCV for image processing. The script accepts a command-line argument to specify the number of iterations for image acquisition.

* Acquire_image_loop.py \
This piece of code is a modification of ImageProcessing.py from the Python API based on Python version 3.11: https://www.jai.com/support-software/jai-software/.
The code was designed for image acquisition using GigE Vision or USB3 Vision devices, with the help of the eBUS SDK. It includes various functions for connecting to devices, streaming, and processing image buffers. I incorporates socket communication to coordinate actions with an external motor control script.

* Talker_listener.py \
This Python script provides functions for socket communication between two scripts using blocking and non-blocking listeners and talkers. It uses Python's built-in socket module to handle TCP/IP communication on a local machine (127.0.0.1).

* Image_Processing.py \
This Python script processes a series of polarization images taken at different angles to compute and visualize various polarization parameters such as Degree of Polarization (DoP) and Angle of Polarization (AoP). The script uses libraries like imageio, numpy, and matplotlib for image reading, data processing, and visualization.

* Data folder \
The folder that will contain all the images taken

## Getting Started

Download the code and  extract it in your workspace

### Installation

Install python 3.11

Install the Python API based on Python version 3.11: https://www.jai.com/support-software/jai-software/ (control the JAI camera)

Install the github repository: https://github.com/roesel/elliptec (control the ELL14 motor).

### Requirements

Install the libraries in the requirement.txt with the command pip install -r requirements.txt

### Executing program

Connect your ELL14 motor and your camera. If you want to change the parameters of the camera, use the JAI software. You can download eBUS SDK software for JAI here: https://www.jai.com/support-software/jai-software/.

When all is connected, you can run the main_loop.py script. It will automatically run for 100 iterations, so if you want to change the number, you can run this command : py -3.11 main_loop.py --n your_number.

### Image Processing
To process the images, you need to import 4 images in the Image_Processing folder and run the Image_processing.py script. It will display the Degree of Polarization (DoP) and the Global and Local Angle of Polarization (AoP).

## Help
Any advise for common problems or issues, see the documentation with the code or contact me.

## Author
Alexandre Dupont \
email: minidupsalex@gmail.com

## Version History
* 0.1
    * Initial release

## Acknowledgments
This works contains code taken from:\
* https://github.com/roesel/elliptec \
* https://www.jai.com/support-software/jai-software/



