# Face Mask Detection with Real-Time Alert System

This project detects whether individuals are wearing face masks using a webcam or IP camera in real-time. It leverages a MobileNetV2-based CNN model and OpenCV’s deep learning (DNN) face detector to provide reliable multi-face detection with a simple user interface.

## Features

- Real-time face mask detection using webcam or IP Webcam app
- Uses OpenCV DNN face detector for robust multi-face support
- MobileNetV2-based classifier trained on diverse mask/no-mask faces
- Tkinter GUI interface for non-technical users
- Supports up to 4 simultaneous face detections
- Optimized for performance on low-end systems
- Setup script for easy installation and usage

## Dataset

This project uses the Face Mask 12K Images Dataset provided by Ashish Jangra on Kaggle:

https://www.kaggle.com/datasets/ashishjangra27/face-mask-12k-images-dataset

## Folder Structure

| Folder / File                  | Description |
|-------------------------------|-------------|
| scripts/                      | Python scripts (`app.py` for GUI, `train.py` for model training) |
| face_detector/                | Pre-trained OpenCV DNN face detector (prototxt + caffemodel) |
| setup.bat                     | Windows batch script to install dependencies and launch app |
| requirements.txt              | Python dependencies used in this project |
| README.md                     | Project documentation |

## Requirements

Install the following dependencies before running the project (also included in `requirements.txt`):

tensorflow==2.13.0  
keras==2.13.1  
opencv-python==4.8.0.74  
numpy==1.24.3  
pandas==1.5.3  
matplotlib==3.7.1  
flask==2.3.2  
scikit-learn==1.2.2  
playsound==1.2.2  
imutils==0.5.4  
Pillow==9.5.0

To install all dependencies:

pip install -r requirements.txt

## Running the Project

### Using the GUI (Recommended):

1. Ensure Python 3.8+ is installed.
2. Place the trained model in `model/mask_detector.h5`
3. Run the setup script:

setup.bat

This will:
- Create a virtual environment
- Install required packages
- Launch the Tkinter-based GUI for live detection

## Screenshots

<img width="639" height="478" alt="Screenshot 2025-07-27 145146" src="https://github.com/user-attachments/assets/211ba8a5-795e-431d-a15c-d953b1b1e10b" />


## Acknowledgments

- Ashish Jangra – [Kaggle Face Mask Dataset](https://www.kaggle.com/datasets/ashishjangra27/face-mask-12k-images-dataset)
- TensorFlow & Keras for model training
- OpenCV for face detection and image processing
