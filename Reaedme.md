# Fall Detection using YOLOv8 Pose Estimation

A real-time AI-powered fall detection system built using **YOLOv8 Pose Estimation**, **OpenCV**, and **Python**.  
This project detects human body posture using pose estimation and identifies falls based on body orientation angles.

---

# Features

- Real-time pose estimation
- Human fall detection
- Body angle analysis
- Persistent fall verification
- Live angle display
- Pose landmark visualization
- Works on videos and webcam feeds

---

# Demo

The system:

1. Detects human body keypoints using YOLOv8 Pose
2. Calculates body orientation angle
3. Tracks posture over multiple frames
4. Detects horizontal body posture
5. Triggers fall alert when fall persists

---

# Tech Stack

- Python
- OpenCV
- Ultralytics YOLOv8 Pose
- Math Library

---

# Project Structure

```bash
fall-detection/
│
├── fall(2).mp4
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Anwaarhere27/Fall-Detection.git
cd fall-detection
```

---

## 2. Create Virtual Environment (Optional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install ultralytics opencv-python
```

---

# Download YOLOv8 Pose Model

The project uses YOLOv8 Pose Estimation model:

```python
model = YOLO("yolov8n-pose.pt")
```

The model will automatically download on first run.

---

# Run the Project

```bash
python main.py
```

Press:

```bash
q
```

to quit the application.

---

# How Fall Detection Works

The system uses body keypoints to estimate body posture.

It calculates the angle between:

- Shoulder midpoint
- Hip midpoint

---

# Pose Keypoints Used

| Body Part | Index |
|------------|-------|
| Left Shoulder | 5 |
| Right Shoulder | 6 |
| Left Hip | 11 |
| Right Hip | 12 |

---

# Fall Detection Logic

## Step 1 — Calculate Body Midpoints

```python
shoulder_mid
hip_mid
```

---

## Step 2 — Calculate Body Angle

```python
angle = calculate_angle(shoulder_mid, hip_mid)
```

---

## Step 3 — Detect Horizontal Posture

If body angle becomes nearly horizontal:

```python
ANGLE_THRESHOLD = 40
```

the system considers it a possible fall.

---

## Step 4 — Persistent Fall Verification

To reduce false positives, the posture must persist for multiple frames:

```python
FALL_FRAMES_THRESHOLD = 5
```

---

# Example Output

```bash
FALL DETECTED!
Angle: 18
```

---

# Pose Visualization

The application visualizes:

- Shoulder midpoint
- Hip midpoint
- Pose keypoints
- Body orientation angle

---

# Webcam Support

To use webcam instead of video:

Replace:

```python
cap = cv2.VideoCapture("fall(2).mp4")
```

with:

```python
cap = cv2.VideoCapture(0)
```

---

# Configuration

## Angle Threshold

Lower values detect more horizontal posture:

```python
ANGLE_THRESHOLD = 40
```

---

## Fall Persistence Frames

Increase for fewer false positives:

```python
FALL_FRAMES_THRESHOLD = 5
```

---

# Future Improvements

- Real-time alert system
- SMS/email notifications
- Elderly monitoring dashboard
- Multi-person fall detection
- Person tracking integration
- Action recognition
- Hospital surveillance integration
- Edge device deployment

---

# Requirements

Example `requirements.txt`

```txt
ultralytics
opencv-python
numpy
```

---

# Screenshots

Add screenshots here:

```bash
screenshots/output.png
```

---


# Author

**Anwaar Muhammad**  
AI/ML Engineer | Computer Vision | Generative AI

GitHub: https://github.com/Anwaarhere27