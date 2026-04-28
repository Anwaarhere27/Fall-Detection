import cv2
import math
from ultralytics import YOLO

# Load pose model
model = YOLO("yolov8n-pose.pt")

# Load video
video_path = "fall(2).mp4"
cap = cv2.VideoCapture(video_path)

# Fall detection settings
ANGLE_THRESHOLD = 40  # degrees (lower = more horizontal)
FALL_FRAMES_THRESHOLD = 5

# Track fall persistence per detected person index
fall_counter = {}

# Window (prevents auto scaling issues)
cv2.namedWindow("Fall Detection", cv2.WINDOW_NORMAL)

def calculate_angle(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return abs(math.degrees(math.atan2(dy, dx)))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run pose estimation
    results = model(frame, verbose=False)

    if results[0].keypoints is not None:
        keypoints = results[0].keypoints

        for i in range(len(keypoints.xy)):
            kpts = keypoints.xy[i]

            try:
                # COCO keypoints
                ls = kpts[5]   # left shoulder
                rs = kpts[6]   # right shoulder
                lh = kpts[11]  # left hip
                rh = kpts[12]  # right hip

                # Midpoints
                shoulder_mid = (
                    (ls[0] + rs[0]) / 2,
                    (ls[1] + rs[1]) / 2
                )

                hip_mid = (
                    (lh[0] + rh[0]) / 2,
                    (lh[1] + rh[1]) / 2
                )

                # Body angle
                angle = calculate_angle(shoulder_mid, hip_mid)

                person_id = i  # simple index-based tracking

                if person_id not in fall_counter:
                    fall_counter[person_id] = 0

                # Fall condition (horizontal posture)
                if angle < ANGLE_THRESHOLD:
                    fall_counter[person_id] += 1
                else:
                    fall_counter[person_id] = 0

                # Detect fall
                if fall_counter[person_id] >= FALL_FRAMES_THRESHOLD:
                    cv2.putText(frame, "FALL DETECTED!", (50, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

                # Draw keypoints
                cv2.circle(frame, (int(shoulder_mid[0]), int(shoulder_mid[1])), 5, (255, 0, 0), -1)
                cv2.circle(frame, (int(hip_mid[0]), int(hip_mid[1])), 5, (0, 255, 0), -1)

                # Show angle
                cv2.putText(frame, f"Angle: {int(angle)}",
                            (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 255, 0), 2)

            except:
                continue

    # Display frame (NO RESIZE → no zoom distortion)
    cv2.imshow("Fall Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()