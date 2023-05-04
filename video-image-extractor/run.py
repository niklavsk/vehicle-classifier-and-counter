import cv2 as cv
import os

INPUT_LIST = os.listdir('videos/')
OUTPUT_FOLDER = 'images'

# create folder for images in current path if not exists
current_path = os.getcwd()
folder_path = os.path.join(current_path, OUTPUT_FOLDER)

if not os.path.exists(folder_path):
    os.mkdir(folder_path)

# save frame every # seconds
seconds = 5

for entry in INPUT_LIST:
    file = 'videos/' + entry
    cap = cv.VideoCapture(file)
    frame_count = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv.CAP_PROP_FPS) # Gets the frames per second

    # calculates number of frames that creates 5 seconds of video
    frame_offset = fps * seconds

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print('Error opening video stream or file')
        continue

    current_frame = 1

    while current_frame <= frame_count:
        cap.set(cv.CAP_PROP_POS_FRAMES, current_frame)
        ret, frame = cap.read()

        # save frame
        file_path = os.path.join(folder_path, entry + '-' + str(int(current_frame / frame_offset) + 1) + '.jpg')
        cv.imwrite(file_path, frame)

        current_frame += frame_offset
