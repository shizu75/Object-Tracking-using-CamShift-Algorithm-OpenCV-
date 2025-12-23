# Object Tracking using CamShift Algorithm (OpenCV)

## Project Overview
This project implements **real-time object tracking** in a video using the **CamShift (Continuously Adaptive Mean Shift)** algorithm provided by **OpenCV**. The tracker is initialized with a manually defined Region of Interest (ROI) and then continuously tracks the object across video frames based on color distribution.

The project demonstrates classical computer vision techniques for motion tracking without using deep learning.

---

## Objectives
- Understand object tracking using traditional computer vision
- Learn how CamShift adapts tracking window size dynamically
- Use HSV color space for robust color-based tracking
- Track an object in a real video sequence
- Visualize tracking results in real time

---

## Technologies Used
- Python 3
- OpenCV (cv2)
- NumPy

---

## Input Description
### Video Input
- A local video file is used as input
- The tracker initializes using the **first frame** of the video

### Region of Interest (ROI)
- Manually defined bounding box:
  - x, y, width, height
- ROI represents the object to be tracked throughout the video

---

## Methodology

### 1. Video Capture
- Video is loaded using OpenCV’s `VideoCapture`
- First frame is extracted to initialize tracking

---

### 2. ROI Initialization
- A specific region is selected manually
- ROI is converted from **BGR to HSV color space**
- HSV is preferred due to robustness against lighting changes

---

### 3. Histogram Creation
- A mask filters low-saturation and low-value pixels
- Histogram of the ROI is computed
- Histogram is normalized to improve tracking stability

---

### 4. CamShift Tracking
- Each new frame is converted to HSV
- Back-projection is computed using ROI histogram
- CamShift algorithm updates:
  - Object position
  - Bounding box size
- Bounding rectangle drawn on the tracked object

---

### 5. Real-Time Visualization
- Tracked object displayed in a window
- Tracking continues until:
  - Video ends, or
  - User presses the **'p'** key

---

## Key Concepts Demonstrated
- Region of Interest (ROI)
- HSV color space
- Histogram back-projection
- Mean Shift vs CamShift
- Real-time video processing
- Classical object tracking techniques

---

## Output
- Live video window showing:
  - Tracked object
  - Dynamically adapting bounding box
- Smooth tracking based on color consistency

---

## How to Run the Project

### Prerequisites
Install required libraries:
- opencv-python
- numpy

---

### Steps
1. Update the video file path in the script
2. Adjust ROI coordinates if needed
3. Run the Python script
4. Observe:
   - Real-time object tracking
   - Bounding box updates
5. Press **'p'** to stop tracking

---

## Learning Outcomes
- Practical understanding of object tracking algorithms
- Experience with OpenCV video processing
- Ability to implement color-based tracking
- Knowledge of CamShift behavior and limitations

---

## Limitations
- Manual ROI selection
- Tracking may fail under:
  - Severe lighting changes
  - Occlusion
  - Similar-colored background objects

---

## Future Improvements
- Automatic ROI selection
- Integrate object detection before tracking
- Use multiple object tracking
- Combine with deep learning trackers
- Improve robustness using adaptive masking

---

## Use Case
This project is suitable for:
- Computer vision learning
- Academic labs and assignments
- Classical vision-based tracking demonstrations
- Precursor to advanced tracking systems

---

## Author
Soban Saeed
Developed as an educational computer vision project demonstrating object tracking using the CamShift algorithm in OpenCV.
