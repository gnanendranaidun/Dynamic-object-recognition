import cv2
from ultralytics import YOLO
import time

# Initialize Pushbullet API
# from pushbullet import Pushbullet
# API_TOKEN = "o.wMCsInQzLIdhHo4E0j9iJREgTy0PAcES"
# pb = Pushbullet(API_TOKEN)

# Initialize camera


# Load YOLO model
model = YOLO("yolov8n.pt")

def process_and_display():
    """Processes video frames and displays detection results in real-time."""
    i=1
    while True:
        try:

            cam = cv2.VideoCapture("http://192.168.51.225:8080/video")
            if not cam.isOpened():
                print("Error: Could not access the camera.")
                exit()
        except:
            print("can't find stuff")
            pass
        ret, frame = cam.read()
        cv2.imwrite("testimage.jpg", frame)

        if not ret:
            print("Error: Failed to capture frame.")
            break
    
        
        # YOLO detection
        results = model(frame)
        for box in results[0].boxes.data:
            x1, y1, x2, y2 = map(int, box[:4])  # Bounding box coordinates
            confidence = box[4].item()  # Confidence score
            class_id = int(box[5].item())  # Class ID
            
            # Draw rectangle and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 2)
            label = f"{results[0].names[class_id]} {confidence:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
        
        # Display the frame
        cv2.imwrite("result.jpg", frame)

        # Break on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # i-=1

    cam.release()
    cv2.destroyAllWindows()

# Main workflow
if __name__ == "__main__":
    print("Starting real-time object detection...")
    process_and_display()
