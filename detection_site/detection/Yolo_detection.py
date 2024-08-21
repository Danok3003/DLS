from ultralytics import YOLO
import cv2
import os
from django.conf import settings
import torch

def Detection_YOLO(photo):
    path = 'detection/static/detection/best.pt'
    photo = os.path.join(settings.BASE_DIR, 'detect_photo', 'detect_photo', 'before', photo)

    img = cv2.imread(photo)
    model_yolo = YOLO(path)

    with torch.no_grad():
        result = model_yolo(photo)
    result = result[0]

    cl_names = result.names

    for box in result.boxes:
        if box.conf[0] > 0.7:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cl = cl_names[int(box.cls[0])]
            cv2.rectangle(
                img,
                (x1, y1),
                (x2, y2),
                (255.0, 0, 0),
                2
            )
            cv2.putText(img, f'{cl}: {box.conf[0]:.2f}%', (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255.0, 0, 0), 2)
    image_name = 'photo_res.jpg'
    path_save = f'detection/static/detection/{image_name}'
    cv2.imwrite(path_save, img)
    return path_save

