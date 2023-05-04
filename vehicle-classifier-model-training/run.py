from imageai.Detection.Custom import DetectionModelTrainer

IMAGE_DATASET_DIRECTORY = "image-dataset"
NUM_OF_EXPERIMENTS = 50
BATCH_SIZE = 16
PRETRAINED_MODEL_PATH = "image-dataset/models/yolov3_image-dataset_mAP-0.29628_epoch-15.pt"
CATEGORIES_LIST = [
    "Motorcycles",
    "Passenger cars",
    "Pick-ups and vans < 3,5t",
    "Trucks > 3,5t",
    "Multi-trailer trucks",
    "Semi-trailer trucks",
    "Buses",
    "Pedestrians",
    "Bicycles",
    "Other vehicles"
]

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory=IMAGE_DATASET_DIRECTORY)
trainer.setTrainConfig(object_names_array=CATEGORIES_LIST,
                       batch_size=BATCH_SIZE,
                       num_experiments=NUM_OF_EXPERIMENTS,
                    #    train_from_pretrained_model=PRETRAINED_MODEL_PATH
                       )

trainer.trainModel()
