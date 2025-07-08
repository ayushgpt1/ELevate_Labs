import os
import cv2

input_path = "../dataset"
output_size = (100, 100)

for label in ["with_mask", "without_mask"]:
    folder = os.path.join(input_path, label)
    for img_name in os.listdir(folder):
        img_path = os.path.join(folder, img_name)
        img = cv2.imread(img_path)
        if img is None:
            continue
        img_resized = cv2.resize(img, output_size)
        gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(img_path, gray)
