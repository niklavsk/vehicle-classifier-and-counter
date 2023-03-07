from imageai.Detection.Custom import DetectionModelTrainer

IMAGE_DATASET_DIRECTORY = "image-dataset"
NUM_OF_EXPERIMENTS = 200
BATCH_SIZE = 16
PRETRAINED_MODEL_PATH = "image-dataset/models/yolov3_image-dataset_mAP-0.00001_epoch-1.pt"
CATEGORIES_LIST = [
    "Bicycles", 
    "Buses", 
    "Motorcycles", 
    "Multi-trailer trucks", 
    "Other vehicles", 
    "Passenger cars", 
    "Pedestrians", 
    "Pick-ups and vans < 3,5t", 
    "Semi-trailer trucks",
    "Trucks > 3,5t"
]

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory=IMAGE_DATASET_DIRECTORY)
trainer.setTrainConfig(object_names_array=CATEGORIES_LIST, batch_size=BATCH_SIZE, num_experiments=NUM_OF_EXPERIMENTS, train_from_pretrained_model=PRETRAINED_MODEL_PATH)

trainer.trainModel()
