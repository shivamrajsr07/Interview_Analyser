import cv2

def analyze_eye_contact(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return 0

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    total_frames = 0
    face_frames = 0
    frame_skip = 5  # 🔥 SPEED BOOST

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # Skip frames
        if frame_count % frame_skip != 0:
            continue

        total_frames += 1

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            face_frames += 1

    cap.release()

    if total_frames == 0:
        return 0

    return round((face_frames / total_frames) * 100, 2)