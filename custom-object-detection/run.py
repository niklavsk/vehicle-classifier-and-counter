from imageai.Detection.Custom import CustomVideoObjectDetection
from matplotlib import pyplot as plt
import os

EXECUTION_PATH = os.getcwd()
INPUT_FILE_NAME = "traffic.mp4"
OUTPUT_FILE_NAME = "traffic_output"
MODEL_PATH = "image-dataset_model.pt"
MODEL_JSON_PATH = "image-dataset_yolov3_detection_config.json"
CATEGORY_COLOR_MAP = {
    'Bicycles': 'red',
    'Buses': 'steelblue',
    'Motorcycles': 'orange',
    'Multi-trailer trucks': 'gray',
    'Other vehicles': 'chocolate',
    'Passenger cars': 'green',
    'Pedestrians': 'pink',
    'Pick-ups and vans < 3,5t': 'indigo',
    'Semi-trailer trucks': 'limegreen',
    'Trucks > 3,5t': 'gold'
}

resized = False

def forSecond(frame_number, output_arrays, count_arrays, average_count, returned_frame):
	try:
		plt.clf()

		this_colors = []
		labels = []
		sizes = []

		counter = 0

		for eachItem in average_count:
			counter += 1
			labels.append(eachItem + " = " + str(average_count[eachItem]))
			sizes.append(average_count[eachItem])
			this_colors.append(CATEGORY_COLOR_MAP[eachItem])

		global resized

		if (resized == False):
			print("resized")
			manager = plt.get_current_fig_manager()
			manager.resize(1800, 700)
			resized = True

		plt.subplot(1, 2, 1)
		plt.title("Second : " + str(frame_number))
		plt.axis("off")
		plt.imshow(returned_frame, interpolation="none")

		plt.subplot(1, 2, 2)
		plt.title("Analysis: " + str(frame_number))
		plt.pie(sizes, labels=labels, colors=this_colors, shadow=True, startangle=140, autopct="%.2f")

		plt.pause(0.01)

	except:
  		print("Something went wrong")

def forFull(output_arrays, count_arrays, average_output_count):
    # TODO: Add write to file

    print("FOR FULL:")
    # print("Array for the outputs of each frame ", output_arrays)
    # print("Array for output count for unique objects in each frame : ", count_arrays)
    # print("Output average count for unique objects in the last minute: ", average_output_count)

video_detector = CustomVideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath(MODEL_PATH)
video_detector.setJsonPath(MODEL_JSON_PATH)
video_detector.loadModel()

plt.show()

video_detector.detectObjectsFromVideo(input_file_path=INPUT_FILE_NAME,
                                          output_file_path=OUTPUT_FILE_NAME,
                                          frames_per_second=10,
                                          per_second_function=forSecond,
                                        #   per_frame_function=forFrame,
                                        #   per_minute_function=forMinute,
                                          video_complete_function=forFull,
                                          minimum_percentage_probability=30,
                                          return_detected_frame=True,
                                          log_progress=True)
