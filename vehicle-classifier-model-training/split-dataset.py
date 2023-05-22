EXPORT_LABELS_DIRECTORY_PATH = "image-dataset/export/labels/"
EXPORT_IMAGES_DIRECTORY_PATH = "image-dataset/export/images/"
TRAINING_DIRECTORY_PATH = "image-dataset/train/"
VALIDATION_DIRECTORY_PATH = "image-dataset/validation/"
TRAIN_VALID_SPLIT = 0.7

import os
import shutil
import numpy

def copyImagesWithLabels(files, destination):
	if os.path.exists(destination + "annotations/"):
		shutil.rmtree(destination + "annotations/")
		os.makedirs(destination + "annotations/")

	if os.path.exists(destination + "images/"):
		shutil.rmtree(destination + "images/")
		os.makedirs(destination + "images/")

	for file in files:
		annotation = os.getcwd() + "/" + EXPORT_LABELS_DIRECTORY_PATH + file + ".txt"
		image = os.getcwd() + "/" + EXPORT_IMAGES_DIRECTORY_PATH + file

		shutil.copy(annotation, destination + "annotations/" + file + ".txt")

		if os.path.isfile(image + ".png"):
			shutil.copy(image + ".png", destination + "images/" + file + ".png")

		else:
			shutil.copy(image + ".jpg", destination + "images/" + file + ".jpg")


entries = os.listdir(EXPORT_LABELS_DIRECTORY_PATH)

# fix bounding boxes
for entry in entries:
    #read input file
    fin = open(EXPORT_LABELS_DIRECTORY_PATH + entry, "rt")

    #read file contents to string
    data = fin.read()

    #replace all occurrences of the required string
    data = data.replace("-0.0000000000000002", "0.0")
    data = data.replace("-0.0000000000000001", "0.0")
    data = data.replace("-0.0", "0.0")
    data = data.replace("0.0000000000000000", "0.0")
    data = data.replace("1.0000000000000000", "1.0")
    data = data.replace("1.0000000000000002", "1.0")
    data = data.replace("1.0000000000000004", "1.0")
    data = data.replace("1.0000000000000007", "1.0")
    data = data.replace("1.0000000000000009", "1.0")

    if data.find("-") != -1:
        print(entry)
        print(data)

    #close the input file
    fin.close()

    #open the input file in write mode
    fin = open(EXPORT_LABELS_DIRECTORY_PATH + entry, "wt")

    #overrite the input file with the resulting data
    fin.write(data)

    #close the file
    fin.close()

entries_no_ext = [x[:-4] for x in entries]
numpy.random.shuffle(entries_no_ext)

training, validation = entries_no_ext[:round(len(entries_no_ext) * TRAIN_VALID_SPLIT)], entries_no_ext[round(len(entries_no_ext) * TRAIN_VALID_SPLIT):]

copyImagesWithLabels(training, os.getcwd() + "/" + TRAINING_DIRECTORY_PATH)
copyImagesWithLabels(validation, os.getcwd() + "/" + VALIDATION_DIRECTORY_PATH)
