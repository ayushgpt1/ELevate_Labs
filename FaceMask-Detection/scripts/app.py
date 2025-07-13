import cv2
import numpy as np
import threading
from tkinter import *
from PIL import Image, ImageTk
from tensorflow.keras.models import load_model

# Load model
model = load_model('../model/mask_detector.h5')
labels = ["Mask", "No Mask"]
IMG_SIZE = 224
box_color = (0, 255, 255)

# Load DNN face detector
face_net = cv2.dnn.readNetFromCaffe(
    '../face_detector/deploy.prototxt',
    '../face_detector/res10_300x300_ssd_iter_140000.caffemodel'
) 
# Detect up to 4 faces
def detect_faces_dnn(frame):
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
                                 (104.0, 177.0, 123.0), swapRB=False, crop=False)
    face_net.setInput(blob)
    detections = face_net.forward()
    faces = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.4:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            x1, y1, x2, y2 = box.astype("int")
            faces.append((x1, y1, x2 - x1, y2 - y1))
    return faces[:4]

# Start webcam detection
# ...existing code...

def start_detection():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    def update_frame():
        if not running[0]:
            cap.release()
            return

        ret, frame = cap.read()
        if not ret:
            root.after(10, update_frame)
            return

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = detect_faces_dnn(frame)

        for i, (x, y, w, h) in enumerate(faces):
            face = rgb[y:y+h, x:x+w]
            face = cv2.resize(face, (IMG_SIZE, IMG_SIZE))
            face = face.astype("float32") / 255.0
            face = np.expand_dims(face, axis=0)

            prediction = model.predict(face, verbose=0)[0]
            confidence = np.max(prediction)
            label_index = np.argmax(prediction)

            if confidence > 0.7:
                label = labels[label_index]
                text = f"{label} - Person {i+1}"
                cv2.rectangle(frame, (x, y), (x+w, y+h), box_color, 2)
                cv2.putText(frame, text, (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, box_color, 2)

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)

        root.after(10, update_frame)  # Schedule next frame

    update_frame()

# ...existing code...

    threading.Thread(target=run, daemon=True).start()

def stop_app():
    running[0] = False
    root.destroy()

# Tkinter GUI setup
root = Tk()
root.title("Face Mask Detection")
root.geometry("900x700")
root.resizable(False, False)

video_label = Label(root)
video_label.pack()

btn_frame = Frame(root)
btn_frame.pack(pady=20)

start_btn = Button(btn_frame, text="Start Detection", font=("Arial", 14), bg="green", fg="white", command=start_detection)
start_btn.pack(side=LEFT, padx=10)

exit_btn = Button(btn_frame, text="Exit", font=("Arial", 14), bg="red", fg="white", command=stop_app)
exit_btn.pack(side=RIGHT, padx=10)

running = [True]
root.mainloop()
