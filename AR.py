import cv2
import numpy as np

# Load camera calibration
camera_matrix = np.load('camera_matrix.npy')
dist_coeffs = np.load('dist_coeffs.npy')

pattern_size = (8, 6)
square_size = 1.0

# Prepare object points
objp = np.zeros((pattern_size[0]*pattern_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:8, 0:6].T.reshape(-1, 2) * square_size

# Cube points (drawn on the first square of the chessboard)
cube = np.float32([
    [0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0],
    [0, 0, -1], [0, 1, -1], [1, 1, -1], [1, 0, -1]
])

def draw_cube(img, imgpts):
    imgpts = np.int32(imgpts).reshape(-1, 2)
    # Base
    img = cv2.drawContours(img, [imgpts[:4]], -1, (255, 0, 0), 3)
    # Sides
    for i in range(4):
        img = cv2.line(img, imgpts[i], imgpts[i + 4], (0, 255, 0), 3)
    # Top
    img = cv2.drawContours(img, [imgpts[4:]], -1, (0, 0, 255), 3)
    return img

cap = cv2.VideoCapture('chessboard.avi')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret_corners, corners = cv2.findChessboardCorners(gray, pattern_size, None)

    if ret_corners:
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1),
                                    (cv2.TermCriteria_EPS + cv2.TermCriteria_MAX_ITER, 30, 0.001))

        ret_pnp, rvec, tvec = cv2.solvePnP(objp, corners2, camera_matrix, dist_coeffs)

        imgpts, _ = cv2.projectPoints(cube, rvec, tvec, camera_matrix, dist_coeffs)

        frame = draw_cube(frame, imgpts)

    cv2.imshow('AR Cube', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
