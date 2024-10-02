# Gesture-Controlled Media Player

This project implements a gesture-controlled media player using OpenCV, MediaPipe, and pyautogui. Users can control media playback, volume, and track navigation using hand gestures detected via the webcam.

## Features
- **Play/Pause**: Use gestures to start or pause the media.
- **Volume Control**: Increase or decrease volume with hand movements.
- **Skip Tracks**: Skip forward or backward with gestures.
- Supports default media players on Windows and Linux.

## How It Works
The system uses a webcam to detect hand gestures. MediaPipe's hand landmarks detection is used to capture specific finger movements, and pyautogui simulates media control keys based on recognized gestures.

### Supported Gestures:
- **Play/Pause**: Pinch gesture (Thumb and Index finger together).
- **Volume Up**: Raise Index finger while Thumb is down.
- **Volume Down**: Raise Middle finger while Thumb is down.
- **Skip Forward**: Move Thumb and Index finger to the right.
- **Skip Backward**: Move Thumb and Index finger to the left.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Gesture-Controlled-Media-Player.git
2.pip install opencv-python mediapipe pyautogui
3.python media_player.py
4.Select a media file: Choose the media file you want to play when prompted.

**Requirements**
Python 3.x
OpenCV
MediaPipe
pyautogui
A webcam

**Usage**
Run the script, select the media file, and use gestures in front of the webcam to control media playback.

**Future Improvements**
Add more gestures for additional controls.
Expand compatibility to more media players.
