from GUI import GUI
from HAL import HAL
import cv2
import numpy as np

# Constants for control and image processing
KP = 0.005               # Proportional gain
TARGET_SPEED = 2.5       # Constant speed setting for the robot
LOWER_RED = np.array([0, 100, 100])
UPPER_RED = np.array([10, 255, 255])
ALPHA = 0.2              # Smoothing factor for steering signal

prev_steering = 0.0      # Global variable for smoothing

def process_frame(frame):
    
    global prev_steering

    frame_roi = frame

    # Convert the frame (or ROI) to HSV color space
    hsv = cv2.cvtColor(frame_roi, cv2.COLOR_BGR2HSV)

    # Create a binary mask where red colors fall within the threshold
    mask = cv2.inRange(hsv, LOWER_RED, UPPER_RED)

    # Apply morphological operations to reduce noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours from the binary mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return frame, None
    
    # Assume the largest contour corresponds to the line
    line_contour = max(contours, key=cv2.contourArea)
    M = cv2.moments(line_contour)
    
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        # Fallback: use the center of the frame if detection fails
        h, w = frame.shape[:2]
        cX, cY = w // 2, h // 2

    # Compute the error (offset of the centroid from the image center)
    image_center = frame.shape[1] // 2
    error = cX - image_center
    steering = KP * error

    # Smooth the steering signal to avoid jitter
    steering = ALPHA * steering + (1 - ALPHA) * prev_steering
    prev_steering = steering

    # Draw the detected contour and centroid onto the frame for debugging
    cv2.drawContours(frame, [line_contour], -1, (0, 255, 0), 2)
    cv2.circle(frame, (cX, cY), 5, (0, 255, 0), -1)
    
    return frame, -steering  # Negative sign: negative for left turn, positive for right

while True:
    # Acquire the current image frame from the hardware abstraction layer
    frame = HAL.getImage()
    
    # Process the frame to compute the necessary steering command
    processed_frame, angular_velocity = process_frame(frame)
    
    if angular_velocity is not None:
        HAL.setV(TARGET_SPEED)
        HAL.setW(angular_velocity)
    else:
        # No line detected: apply a safe fallback behavior (stop the robot)
        HAL.setV(0)
        HAL.setW(0)

    # Display the frame (with overlayed contours and centroid)
    GUI.showImage(processed_frame)
   
