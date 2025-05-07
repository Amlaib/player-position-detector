import cv2
import os
import math
import csv

class CentroidTracker:
    def __init__(self, max_distance=50):
        self.next_id = 0
        self.objects = {}  # id -> (x, y)
        self.max_distance = max_distance

    def update(self, detections):
        updated_objects = {}

        for det in detections:
            cx, cy = det

            matched_id = None
            min_distance = self.max_distance

            for obj_id, (ox, oy) in self.objects.items():
                distance = math.hypot(cx - ox, cy - oy)
                if distance < min_distance:
                    min_distance = distance
                    matched_id = obj_id

            if matched_id is not None:
                updated_objects[matched_id] = (cx, cy)
            else:
                updated_objects[self.next_id] = (cx, cy)
                self.next_id += 1

        self.objects = updated_objects
        return self.objects

def main():
    video_path = os.path.join(os.getcwd(), 'videos', 'input.mp4')
    print(f"Trying to open video: {video_path}")

    if not os.path.exists(video_path):
        print(f"Video file not found: {video_path}")
        return

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return
    else:
        print("Video file opened successfully.")

    back_sub = cv2.createBackgroundSubtractorMOG2()

    tracker = CentroidTracker(max_distance=80)

    output_csv = open('player_positions.csv', mode='w', newline='')
    csv_writer = csv.writer(output_csv)
    csv_writer.writerow(['Frame', 'Object ID', 'X', 'Y'])

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Reached end of video or cannot read frame.")
            break

        # Resize frame to 1600x900 for display
        frame = cv2.resize(frame, (1600, 900))

        fg_mask = back_sub.apply(frame)
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        current_centers = []

        for contour in contours:
            area = cv2.contourArea(contour)
            if 60 < area < 500:
                x, y, w, h = cv2.boundingRect(contour)
                cx = x + w // 2
                cy = y + h // 2

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)
                current_centers.append((cx, cy))

        # Update tracker with current detections
        objects = tracker.update(current_centers)

        # Label objects
        for obj_id, (cx, cy) in objects.items():
            cv2.putText(frame, f"ID {obj_id}", (cx - 10, cy - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.putText(frame, f"({cx},{cy})", (cx - 30, cy + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 2)

            # Write to CSV
            csv_writer.writerow([int(cap.get(cv2.CAP_PROP_POS_FRAMES)), obj_id, cx, cy])

        cv2.imshow('Player Position Detector - Tracking', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            print("Exiting video display.")
            break

    cap.release()
    cv2.destroyAllWindows()
    output_csv.close()

if __name__ == '__main__':
    main()