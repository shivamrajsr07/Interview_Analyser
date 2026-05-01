import cv2

def analyze_anxiety(video_path):
    """
    Simple anxiety detection based on face movement (proxy metric)
    More movement = more anxiety
    """

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return 50  # default neutral

    frame_count = 0
    movement_score = 0
    prev_gray = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev_gray is not None:
            diff = cv2.absdiff(prev_gray, gray)
            movement = diff.mean()
            movement_score += movement

        prev_gray = gray
        frame_count += 1

    cap.release()

    if frame_count == 0:
        return 50

    avg_movement = movement_score / frame_count

    # Normalize anxiety score (0–100)
    anxiety_score = min(max(int(avg_movement * 2), 0), 100)

    return anxiety_score