# # from pushbullet import Pushbullet
# # API_TOKEN= "o.wMCsInQzLIdhHo4E0j9iJREgTy0PAcES"
# # pb = Pushbullet(API_TOKEN)
# # dev = pb.get_device("Samsung SM-A156E")
# # print(dev)
# # print(dev.has_sms)
# # push = pb.push_sms(device=dev,number="9845743299",message="this is a sample sms")
# # print(push)
# import cv2
# from ultralytics import YOLO
# from pushbullet import Pushbullet
# import time
# # import tkinter as tk
# API_TOKEN = "o.wMCsInQzLIdhHo4E0j9iJREgTy0PAcES"
# # Initialize camera
# cam = cv2.VideoCapture("http://192.168.215.225:8080/video")
# if not cam.isOpened():
#     print("Error: Could not access the camera.")
#     exit()

# def CaptureImage():
#     print("Capturing Image:")
#     ret, image = cam.read()
#     if not ret:
#         print("Error: Failed to capture image.")
#         return False

#     save_path = "testimage.jpg"  # Save image in the current directory
#     cv2.imwrite(save_path, image)
#     print("Image captured successfully and saved as", save_path)
#     return save_path
# model = YOLO("yolov10n.pt")

# def marking_things(path):
#     while True:
#         ret, image = cam.read()
#         result = model(image)
#     # print(result)
#         for i in result[0].boxes.data:
#             x1, y1, x2, y2 = map(int, i[:4])  # Convert coordinates to integers
#             confidence = i[4].item()  # Confidence score
#             class_id = int(i[5].item())  # Class ID  # Get class name from ID
            
#             # Draw rectangle around the object
#             cv2.rectangle(image, (x1, y1), (x2, y2), (255, 255, 0), 2)
            
#             # Display the label (class name + confidence score)
#             label = f"{result[0].names[class_id]} {confidence:.2f}"
#             cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
#             cv2.imwrite("result.jpg",image)
#             time.sleep(10000)
#     # for i in result[0].boxes.data:
#     #     class_id = i[5]
#     #     x1 , x2 , y1, y2 = map(int ,i[:4])
#     #     cv2.rectangle(image,(x1,y1),(x2,y2),(255,255,0),2)
#     #     cv2.putText(image, f"{i.name} {i[4]:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
#     #     cv2.imwrite("result.jpg",image)

# # Main workflow
# image_path = CaptureImage()
# if image_path:
#     print("initaiuwdhbc")
#     marking_things(image_path)

# # Release camera
# cam.release()
# cv2.destroyAllWindows()
import cv2
from ultralytics import YOLO
import time

# Initialize Pushbullet API
# from pushbullet import Pushbullet
API_TOKEN = "o.wMCsInQzLIdhHo4E0j9iJREgTy0PAcES"
# pb = Pushbullet(API_TOKEN)

# Initialize camera


# Load YOLO model
model = YOLO("yolov8n.pt")

def process_and_display():
    """Processes video frames and displays detection results in real-time."""
    

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
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)
        
        # Display the frame
        cv2.imshow("YOLO Detection", frame)

        # Break on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

# Main workflow
if __name__ == "__main__":
    print("Starting real-time object detection...")
    process_and_display()
