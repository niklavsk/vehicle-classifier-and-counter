EXPORT_LABELS_DIRECTORY_PATH = "image-dataset/export/labels/"
EXPORT_IMAGES_DIRECTORY_PATH = "image-dataset/export/images/"
TRAINING_DIRECTORY_PATH = "image-dataset/train/"
VALIDATION_DIRECTORY_PATH = "image-dataset/validation/"
TRAIN_VALID_SPLIT = 0.7

import os
import shutil
import numpy

def moveImagesWithLabels(files, destination):
	for file in files:
		annotation = os.getcwd() + "/" + EXPORT_LABELS_DIRECTORY_PATH + file + ".txt"
		image = os.getcwd() + "/" + EXPORT_IMAGES_DIRECTORY_PATH + file

		shutil.move(annotation, destination + "annotations/" + file + ".txt")

		if os.path.isfile(image + ".png"):
			shutil.move(image + ".png", destination + "images/" + file + ".png")

		else:
			shutil.move(image + ".jpg", destination + "images/" + file + ".jpg")


entries = os.listdir(EXPORT_LABELS_DIRECTORY_PATH)

# fix bounding boxes
for entry in entries:
    #read input file
    fin = open(EXPORT_LABELS_DIRECTORY_PATH + entry, "rt")

    #read file contents to string
    data = fin.read()

    #replace all occurrences of the required string
    data = data.replace("1.0000000000000002", "1.0")
    data = data.replace("1.0000000000000004", "1.0")
    data = data.replace("1.0000000000000007", "1.0")
    data = data.replace("1.0000000000000009", "1.0")

    if data.find("1.00") != -1:
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

moveImagesWithLabels(training, os.getcwd() + "/" + TRAINING_DIRECTORY_PATH)
moveImagesWithLabels(validation, os.getcwd() + "/" + VALIDATION_DIRECTORY_PATH)
