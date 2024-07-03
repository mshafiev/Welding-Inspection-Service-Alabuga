from ultralytics import YOLO

# Load a model
model = YOLO("model/best.pt")  # pretrained YOLOv8n model


def segmentation(path: str):
    results = model([path], stream=True)  # Возвращает генератор объектов Results

    for result in results:
        boxes = result.boxes  # Координаты объектов
        classes = result.names  # Названия классов
        if len(boxes) > 0:
            box = boxes[0]  # Берем первый предсказанный объект
            cls_id = int(box.cls[0])  # ID класса
            cls_name = classes[cls_id]  # Название класса
            return cls_id, cls_name
    return None, "No detections"