import os
import shutil
import json

IMAGE_FOLDER = "images/"
OUTPUT_FOLDER = "output/"
IMAGE_DIRECTORY_PATH = "converted/images/"
LABEL_DIRECTORY_PATH = "converted/labels/"
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

# Opening JSON file
f = open('annotations.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Closing file
f.close()

# Iterating through the json
# list
for item in data:
	if not os.path.exists(IMAGE_DIRECTORY_PATH):
		os.makedirs(IMAGE_DIRECTORY_PATH)

	if not os.path.exists(LABEL_DIRECTORY_PATH):
		os.makedirs(LABEL_DIRECTORY_PATH)

	# if item["file_upload"].find('96f989b6-2020.03.20-2.AVI-16') == -1:
	# 	continue

	text_file_name = item['file_upload'][:-3] + 'txt'
	image = os.getcwd() + "/" + IMAGE_FOLDER + item['file_upload']
	# shutil.move(image, os.getcwd() + "/" + IMAGE_DIRECTORY_PATH + item['file_upload'])

	f = open(LABEL_DIRECTORY_PATH + text_file_name, 'w')
	f.write('')

	for annotation in item["annotations"]:
		for result in annotation["result"]:
			x = result["value"]["x"] / 100
			y = result["value"]["y"] / 100
			width = result["value"]["width"] / 100
			height = result["value"]["height"] / 100
			label = result["value"]["rectanglelabels"][0]

			f.write("{} {} {} {} {}".format(CATEGORIES_LIST[label], '{:.16f}'.format(x), '{:.16f}'.format(y), '{:.16f}'.format(width), '{:.16f}'.format(height)))
			f.write('\n')

	f.close()
