import os

DATASET_LIST = ["153", "168", "833", "835", "869", "870"]

for ds in DATASET_LIST:
    images = [x[:-4] for x in os.listdir(f"{ds}/images")]
    labels = [x[:-4] for x in os.listdir(f"{ds}/labels")]

    print(set(images) - set(labels))