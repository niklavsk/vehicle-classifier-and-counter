import os
from imageai.Detection.Custom import CustomObjectDetection

DATASET_LABELS_DIRECTORY_PATH = "testing-dataset/labels/"
DATASET_IMAGES_DIRECTORY_PATH = "testing-dataset/images/"
PRETRAINED_MODEL_PATH = "yolov3_image-dataset_mAP-0.42817_epoch-29.pt"
PRETRAINED_MODEL_CONFIG = "image-dataset_yolov3_detection_config.json"
RESULTS_DIRECTORY = "testing-results/"
CATEGORIES_LIST = {
	"Bicycles": "0",
	"Buses": "1",
	"Motorcycles": "2",
	"Multi-trailer trucks": "3",
	"Other vehicles": "4",
	"Passenger cars": "5",
	"Pedestrians": "6",
	"Pick-ups and vans < 3,5t": "7",
	"Semi-trailer trucks": "8",
	"Trucks > 3,5t": "9"
}

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(PRETRAINED_MODEL_PATH)
detector.setJsonPath(PRETRAINED_MODEL_CONFIG)
detector.loadModel()

entries = os.listdir(DATASET_IMAGES_DIRECTORY_PATH)
for entry in entries:
	lines = []

	try:
		detections = detector.detectObjectsFromImage(input_image=DATASET_IMAGES_DIRECTORY_PATH + entry, output_type="array")
		for detection in detections[1]:
			lines.append(str(CATEGORIES_LIST[detection["name"]], detection["box_points"]))

			with open(RESULTS_DIRECTORY + 'readme.txt', 'w') as f:
				f.write('\n'.join(lines))

	except:
		with open(RESULTS_DIRECTORY + 'readme.txt', 'w') as f:
			f.write('\n'.join(lines))



