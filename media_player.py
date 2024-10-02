import cv2
import mediapipe as mp
import pyautogui
import tkinter as tk
from tkinter import filedialog
import os
import platform
import time

# Initialize MediaPipe Hands and OpenCV
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

# Initialize Video Capture
cap = cv2.VideoCapture(0)

# Initialize Tkinter for file selection
root = tk.Tk()
root.withdraw()  # Hide the root window

# Prompt to select a media file
file_path = filedialog.askopenfilename(title="Select a Media File", filetypes=(("Media files", "*.mp3 *.mp4 *.avi"), ("All files", "*.*")))

# Check if a file was selected
if file_path:
    # Open the selected media file with the default media player
    if platform.system() == 'Windows':
        os.startfile(file_path)  # Use os.startfile() on Windows
    else:
        # For macOS or Linux
      subprocess.call(['open', file_path] if platform.system() == 'Darwin' else ['xdg-open', file_path])
else:
    print("No media file selected. Exiting...")
    exit()

# Define functions for media control
def play_pause():
    # Use pyautogui to simulate play/pause (space key works for most media players)
    pyautogui.press("space")

def volume_up():
    pyautogui.press("volumeup")

def volume_down():
    pyautogui.press("volumedown")

def skip_forward():
    pyautogui.hotkey('ctrl', 'right')

def skip_backward():
    pyautogui.hotkey('ctrl', 'left')

# Main loop for gesture detection
while True:
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the frame horizontally for a selfie view
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Retrieve landmarks for gesture detection
            landmarks = hand_landmarks.landmark

            # Example gesture control based on landmark positions:
            thumb_tip = landmarks[4]
            index_tip = landmarks[8]
            middle_tip = landmarks[12]

            # Gesture: Play/Pause (Index and Thumb close together)
            if abs(thumb_tip.x - index_tip.x) < 0.05 and abs(thumb_tip.y - index_tip.y) < 0.05:
                play_pause()
                time.sleep(0.5)  # Prevent multiple detections for the same gesture

            # Gesture: Volume Up (Index finger up, thumb down)
            elif index_tip.y < landmarks[6].y and thumb_tip.y > landmarks[5].y:
                volume_up()
                time.sleep(0.5)

            # Gesture: Volume Down (Middle finger up, thumb down)
            elif middle_tip.y < landmarks[10].y and thumb_tip.y > landmarks[5].y:
                volume_down()
                time.sleep(0.5)

            # Gesture: Skip Forward (Index and thumb pointing right)
            elif thumb_tip.x < landmarks[5].x and index_tip.x < thumb_tip.x:
                skip_forward()
                time.sleep(0.5)

            # Gesture: Skip Backward (Index and thumb pointing left)
            elif thumb_tip.x > landmarks[5].x and index_tip.x > thumb_tip.x:
                skip_backward()
                time.sleep(0.5)

    # Show the frame
    cv2.imshow('Gesture Controlled Media Player', frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
