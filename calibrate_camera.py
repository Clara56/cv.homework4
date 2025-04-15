import cv2
import numpy as np

# Chessboard settings
pattern_size = (8, 6)
square_size = 1.0  

objp = np.zeros((pattern_size[0]*pattern_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:8, 0:6].T.reshape(-1, 2) * square_size

objpoints = []  # 3D points
imgpoints = []  # 2D points

cap = cv2.VideoCapture('chessboard.avi')
frame_count = 0
found_frames = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret_corners, corners = cv2.findChessboardCorners(gray, pattern_size, None)

    if ret_corners:
        found_frames += 1
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1),
                                     (cv2.TermCriteria_EPS + cv2.TermCriteria_MAX_ITER, 30, 0.001))
        imgpoints.append(corners2)

        # Show detection
        cv2.drawChessboardCorners(frame, pattern_size, corners2, ret_corners)
        cv2.imshow('Corners', frame)
        cv2.waitKey(100)

    if found_frames >= 15:  
        break

cap.release()
cv2.destroyAllWindows()

# Calibrate
ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(
    objpoints, imgpoints, gray.shape[::-1], None, None
)

print("Camera matrix:\n", camera_matrix)
print("Distortion coefficients:\n", dist_coeffs)

np.save('camera_matrix.npy', camera_matrix)
np.save('dist_coeffs.npy', dist_coeffs)
