import os

DATASET_FOLDER_LOCATION = "/home/paulo/nao/workspace/larc-2020/datasets"
DATASET_LIST = ["153", "168", "833", "835", "869", "870"]

for dataset_name in DATASET_LIST:

    for png_file in [x for x in os.listdir(f"{DATASET_FOLDER_LOCATION}/yolov5/dataset/{dataset_name}/images") if x.endswith(".png")]:
        if(png_file[:-4] + ".txt" not in os.listdir(f"{DATASET_FOLDER_LOCATION}/yolov5/dataset/{dataset_name}/labels")):
            open(f"{DATASET_FOLDER_LOCATION}/yolov5/dataset/{dataset_name}/labels/{png_file[:-4]}.txt", "w").close()
    for jpg_file in [x for x in os.listdir(f"{DATASET_FOLDER_LOCATION}/yolov5/dataset/{dataset_name}/images") if x.endswith(".jpg")]:
        if(jpg_file[:-4] + ".txt" not in os.listdir(f"{DATASET_FOLDER_LOCATION}/yolov5/dataset/{dataset_name}/labels")):
            open(f"{DATASET_FOLDER_LOCATION}/yolov5/dataset/{dataset_name}/labels/{jpg_file[:-4]}.txt", "w").close()