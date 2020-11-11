import os
import numpy as np

yolo_dir = "/home/paulo/nao/workspace/larc-2020/datasets/yolov5/dataset"
DATASET_LIST = ["153", "168", "833", "835", "869", "870"]

train_p = 0.7
test_p = 0.2
val_p = 0.1

open(f"{yolo_dir}/train.txt", "w").close()
open(f"{yolo_dir}/test.txt", "w").close()
open(f"{yolo_dir}/validate.txt", "w").close()

for ds in DATASET_LIST:
    images_names = os.listdir(f"{yolo_dir}/{ds}/images")
    train, validate, test = np.split(images_names, [int(len(images_names)*train_p), int(len(images_names)*(train_p+test_p))])
    with open(f"{yolo_dir}/train.txt", "a+") as f:
        for image_name in train:
            f.write(f"{yolo_dir}/train/{ds}/images/{image_name}\n")
    with open(f"{yolo_dir}/validate.txt", "a+") as f:
        for image_name in validate:
            f.write(f"{yolo_dir}/validate/{ds}/images/{image_name}\n")
    with open(f"{yolo_dir}/test.txt", "a+") as f:
        for image_name in test:
            f.write(f"{yolo_dir}/test/{ds}/images/{image_name}\n")
