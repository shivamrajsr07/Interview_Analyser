import cv2
import mediapipe as mp

def analyze_body_language(video_path):
    try:
        # SAFE ACCESS
        if not hasattr(mp, "solutions"):
            return 50  # fallback

        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose()

        cap = cv2.VideoCapture(video_path)

        good_posture_frames = 0
        total_frames = 0

        frame_skip = 5
        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1
            if frame_count % frame_skip != 0:
                continue

            total_frames += 1

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb)

            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark

                left_shoulder = landmarks[11].y
                right_shoulder = landmarks[12].y

                if abs(left_shoulder - right_shoulder) < 0.05:
                    good_posture_frames += 1

        cap.release()

        if total_frames == 0:
            return 0

        return round((good_posture_frames / total_frames) * 100, 2)

    except Exception as e:
        print("Body language error:", e)
        return 50