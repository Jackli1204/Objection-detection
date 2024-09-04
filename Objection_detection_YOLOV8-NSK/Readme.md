

# Introduction

Welcome to our project! In this project, we focus on optimizing the YOLOv8 model as our baseline model for object detection tasks. All experiments and result analyses are based on the YOLOv8 architecture. Additionally, we have reproduced the YOLOv5 model, achieving the basic functionality of object detection. Below, you'll find instructions on how to run both YOLOv8 and YOLOv5 models.

The code for data analysis and data preprocessing can be found in the following notebooks:

Data_analysis.ipynb: Contains code for data analysis.
Data_preprocessing.ipynb: Includes code for data preprocessing.

The "Interpretation_without_notebook" folder is used for the Data_analysis.ipynb

For the implementation of YOLOv8, all related code can be accessed in the YOLOv8 folder. Similarly, for YOLOv5, you'll find all implementation code in the YOLOv5 folder.

# YOLOV8



1. Place the dataset folder "VOC" into the path `ultralytics-8.1.0/datasets`.

2. In the script `train.py` located at the path `ultralytics-8.1.0/ultralytics`, set the paths in the following code to the absolute path of the `ultralytics-8.1.0` directory after extraction, ensuring that the training utilizes the `ultralytics` library in the current folder rather than the `ultralytics` library in the system path.

   ```python
   import sys
   sys.path.append("ultralytics-8.1.0/")
   ```

   ​

3. In the `train.py` script, modify the YAML file in the following code to invoke the YOLOv8 model with different attention mechanisms. The YAML file path is `ultralytics-8.1.0/ultralytics/cfg/models/v8/*.yaml`.

   ```python
   model = YOLO(r'yolov8-pconv.yaml').load("yolov8n.pt")
   ```

   ​

4. In the `train.py` script, modify the following code to set the path for the dataset configuration file.

   ```python
   model.train(
           data=r'ultralytics-8.1.0/VOC2012.yaml',
           ...
   )
   ```

   ​

5. Run the command `python ...ultralytics-8.1.0/ultralytics/train.py` in the terminal to perform training.

6. After training, the best weight file `best.py` will be saved in the path `runs/train/exp*/weights`.

7. Open the script `val.py` located at the path `ultralytics-8.1.0/ultralytics`, and modify the following code to read the `best.py` file generated after training.

   ```python
    model = YOLO(r'runs/train/best.pt')
   ```

   ​

8. In the `val.py` script, modify the `data` parameter in the following code to change the dataset configuration file path, and modify the `split` parameter to enable the model to test on the validation or test set.

   ```python
   metrics=model.val(
           val=True,  # (bool) During training, validate/test
           data=r'/root/yolov8/ultralytics-8.1.0/VOC2012.yaml',
           split='val',  # (str) Dataset splits for validation, such as 'val', 'test', or 'train'.
           ...
   )
   ```

   ​

9. The script `detect.py` is used for prediction, and the method for modifying paths is the same as in `train.py` and `val.py`.

10. The .yaml files used in the experiment include `yolov8-EffectiveSE.yaml`, `yolov8-NAMAttention.yaml`,`yolov8-SKAttention.yaml`, etc. These files are stored in the directory `...\ultralytics-8.1.0\ultralytics\cfg\models\v8\`










## 


