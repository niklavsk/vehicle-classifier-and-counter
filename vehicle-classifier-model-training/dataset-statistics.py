EXPORT_LABELS_DIRECTORY_PATH = "image-dataset/export/labels/"
CATEGORY_COUNTS = [
	{
		"instanceCount": 0,
		"imageCount": 0,
		"label": "Bicycles"
	},
	{
		"instanceCount": 0,
		"imageCount": 0,
		"label": "Buses",
	},
	{
		"instanceCount": 0,
		"imageCount": 0,
		"label": "Motorcycles",
	},
	{
		"instanceCount": 0,
		"imageCount": 0,
		"label": "Multi-trailer trucks",
	},
	{
		"instanceCount": 0,
		"imageCount": 0,
		"label": "Other vehicles",
	},
	{
		"instanceCount": 0,
		"imageCount": 0,
		"label": "Passenger cars",
	},
	{
		"instanceCount": 0,
		"imageCount": 0,
		"label": "Pedestrians",
	},
	{
		"instanceCount": 0,
		"imageCount": 0,
		"label": "Pick-ups and vans < 3,5t",
	},
	{
		"instanceCount": 0,
		"imageCount": 0,
		"label": "Semi-trailer trucks",
	},
	{
		"instanceCount": 0,
		"imageCount": 0,
		"label": "Trucks > 3,5t",
	},
]

import os
import csv

entries = os.listdir(EXPORT_LABELS_DIRECTORY_PATH)
remaining = len(entries)

for entry in entries:
	print("Remaining: {}".format(remaining))

	imageInstances = [
		False,
		False,
		False,
		False,
		False,
		False,
		False,
		False,
		False,
		False,
	]

	#read input file
	fin = open(EXPORT_LABELS_DIRECTORY_PATH + entry, "r")
	lines = fin.readlines()
	fin.close()

	for line in lines:
		data = line.split()
		if len(data) != 5: continue

		index = int(data[0])
		CATEGORY_COUNTS[index]["instanceCount"] = CATEGORY_COUNTS[index]["instanceCount"] + 1
		imageInstances[index] = True

	for index, value in enumerate(imageInstances):
		if value: CATEGORY_COUNTS[index]["imageCount"] = CATEGORY_COUNTS[index]["imageCount"] + 1

	remaining = remaining - 1

with open('category_counts.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Label", "Image Count", "Instance Count"])

	for line in CATEGORY_COUNTS:
		writer.writerow([line["label"], line["imageCount"], line["instanceCount"]])
