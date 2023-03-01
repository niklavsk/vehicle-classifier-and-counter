from imageai.Detection.Custom import DetectionModelTrainer\

IMAGE_DATASET_DIRECTORY = "image-dataset"
NUM_OF_EXPERIMENTS=2 # 200
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
trainer.setTrainConfig(object_names_array=CATEGORIES_LIST, batch_size=4, num_experiments=NUM_OF_EXPERIMENTS)

trainer.trainModel()
