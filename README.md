# cv.homework4
AR object visualization using OpenV

# Homework 4: Camera Pose Estimation and Augmented Reality

## Overview
This project performs camera calibration, estimates camera pose from a chessboard pattern, and projects a 3D cube (Augmented Reality object) onto the image using OpenCV.

- **Input**: `chessboard.avi` video (with visible 8x6 inner corner chessboard)
- **Output**: AR overlay of a 3D cube on the chessboard in video frames

---

## 📁 File Structure
```
.
├── step1_calibrate_camera.py       # Calibrate camera from video
├── step2_AR.py                     # Estimate pose & draw cube
├── chessboard.avi                  # Input video file
├── camera_matrix.npy               # Saved camera matrix (after step1)
├── dist_coeffs.npy                 # Saved distortion coefficients (after step1)
└── README.md                       # Project description
```

---

## 🎯 Goals
1. Detect chessboard corners in the video
2. Calibrate the camera using detected points
3. Estimate camera pose using `cv2.solvePnP`
4. Overlay a custom 3D object (cube) using `cv2.projectPoints`

---

## ⚙️ How to Run
### Step 1: Camera Calibration
```
python step1_calibrate_caamera.py
```
- Detects corners from `chessboard.avi`
- Saves: `camera_matrix.npy` and `dist_coeffs.npy`

### Step 2: AR Cube Overlay
```
python step2_AR.py
```
- Loads calibration
- Draws a 3D cube projected on the chessboard
- Press `Q` to quit

---

## 📌 Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy

---
## Outout examples

![1-6c5c8503](https://github.com/user-attachments/assets/09477f25-a711-491d-8da0-f4e84206a1bc)

![2-6c5c8503](https://github.com/user-attachments/assets/cfffa920-94a5-421a-a027-1f56408819ee)




## ✨ Customization
- You can change the cube to any shape by modifying the 3D points in `step2_ar_cube.py`
- You can increase accuracy by using more diverse calibration frames

---
