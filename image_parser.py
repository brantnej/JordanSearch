from imageai.Detection import ObjectDetection

imageai_model_path = "models/yolov3.pt"

def new_image_model():
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(imageai_model_path)
    detector.loadModel()
    return detector

def detect_objects(detector, image):
    detection = detector.detectObjectsFromImage(input_image=image)
    return detection