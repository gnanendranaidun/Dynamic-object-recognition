# Dynamic-object-recognition: Real-Time Object Detection using YOLOv8 and OpenCV

## Overview
This project implements real-time object detection using YOLOv8 and OpenCV. It captures video frames from an IP camera and detects objects using a pre-trained YOLOv8 model. The detected objects are annotated with bounding boxes and class labels.

## Project Structure
- `dynamic-recognition.py`: Runs real-time object detection and displays results on the screen.
- `frame-wise-recognition.py`: Captures and saves processed frames with object detection results.
- `result.jpg`: The latest processed image with detected objects.
- `testimage.jpg`: A captured test frame from the video stream.

## Requirements
### Dependencies
Make sure you have the following installed:
- Python 3.x
- OpenCV (`cv2`)
- Ultralytics YOLO (`ultralytics`)

Install dependencies using:
```sh
pip install opencv-python ultralytics pushbullet
```

## Setup & Usage
### 1. Configure the Camera
Ensure your IP camera is accessible over the network. Update the `cv2.VideoCapture` URL in the script with your camera’s IP address and port.

### 2. Run Dynamic Recognition
```sh
python dynamic-recognition.py
```
This script will:
- Access the camera feed.
- Perform object detection.
- Display results in real-time.

### 3. Run Frame-wise Recognition
```sh
python frame-wise-recognition.py
```
This script will:
- Capture frames from the camera.
- Perform object detection.
- Save images with bounding boxes.

### 4. Exit
Press `q` to stop the script and release the camera resources.

## Troubleshooting
- **Error: Could not access the camera.**
  - Ensure your IP camera is reachable.
  - Check the camera URL in the script.
- **Error: Failed to capture frame.**
  - Ensure the camera is streaming video.
- **YOLO model not found?**
  - Ensure `yolov8n.pt` is downloaded and placed in the working directory.
  - Download using:
    ```sh
    from ultralytics import YOLO
    YOLO("yolov8n.pt").download()
    ```

## Future Enhancements
- Add Pushbullet notifications when specific objects are detected.
- Improve frame processing speed with GPU acceleration.
- Implement logging and detailed analytics.

## License
This project is open-source and available for modification and improvement.

