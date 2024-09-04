import sys
sys.path.append("/root/yolov8/ultralytics-8.1.0/")
from ultralytics import YOLO

if __name__ == '__main__':
    # Load a model
    #model = YOLO(r'path/to/xxx.yaml')  # build a new model from YAML
    model = YOLO(r'yolov8-yoloms.yaml')
    model.info()