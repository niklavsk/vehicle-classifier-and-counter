## Used libraries
- [ImageAI](https://github.com/OlafenwaMoses/ImageAI) - Model training and object detection
- [Label Studio Frontend](https://github.com/heartexlabs/label-studio) - Image annotation and dataset creation
- [Label Studio ML Backend](https://github.com/heartexlabs/label-studio-ml-backend) - Image pre-annotation for easier dataset creation

## Installation
### Local environment
1. `pip install -r requirements.txt`
2. `pip install imageai --upgrade`

### Docker environment
1. `docker-compose up -d`
2. `docker exec -it vehicle-classifier-and-counter_app_1 bash`

### Label studio (docker environment)
1. `docker build -t heartexlabs/label-studio:latest .`
2. `docker run -it -p 805:8080 -v %cd%/image-annotation-tool:/label-studio/data heartexlabs/label-studio:latest label-studio --log-level DEBUG`

### Label studio (local environment)
1. `brew tap heartexlabs/tap`
2. `brew install heartexlabs/tap/label-studio`
3. `label-studio start -p 805 -db label_studio.sqlite3 --data-dir .`

### Label studio backend (seperate folder)
1. `git clone https://github.com/heartexlabs/label-studio-ml-backend`
2. `cd label-studio-ml-backend`
3. `python3.8 -m venv venv`
4. `source venv/bin/activate`
5. `pip install -U -e .`
6. `pip install -r label_studio_ml/examples/mmdetection/requirements.txt`
7. `pip install mmdet==2.6.0 mmcv-full==1.2.0`
8. `cd label_studio_ml/examples/mmdetection`
9. `label-studio-ml init coco-detector --script mmdetection.py`
10. `LABEL_STUDIO_HOSTNAME=http://localhost:805 label-studio-ml start coco-detector --with config_file=./faster_rcnn_r50_fpn_1x_coco.py checkpoint_file=./faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth`

## Perform video object detection and analysis
### Get images from videos
1. Place videos in the `video-image-extractor/videos` folder
2. `cd video-image-extractor`
3. `python run.py`

### Annotate chosen/gathered images
1. Go to `http://localhost:805`
2. Set annotation labels under `<Project>/Settings/Labeling Interface`
3. Add ML backend under `<Project>/Settings/Machine Learning`
4. Import images
5. Start annotating images by pressing `Label all images`

### Export annotated image dataset

### Split image dataset into training and validation sets

### Train object detection model
1. `cd vehicle-classifier-model-training`
2. `python fix-bounding-boxes.py`
- In case of error `find . -name '.DS_Store' -type f -delete`
3. `python run.py`

### Copy newest model to object detection directory
1. Copy the created model from `vehicle-classifier-model-training/image-dataset/models/` to `custom-object-detection/`
2. Rename the copied model to `image-dataset_model.pt`
3. `cp vehicle-classifier-model-training/image-dataset/json/image-dataset_yolov3_detection_config.json custom-object-detection/image-dataset_yolov3_detection_config.json`

### Run video analysis script
1. Place video in the `custom-object-detection` folder
2. `cd custom-object-detection`
3. Change the name of the video in the `run.py` file
4. `python run.py`

## Classes of road users and vehicles (Satiksmes dalībnieku kategorijas)
- Motorcycles (Motocikli)
- Passenger cars (Vieglie transportlīdzekļi)
- Pick-ups and vans < 3,5t (Kravas transportlīdzekļi < 3,5t)
- Trucks > 3,5t (Kravas transportlīdzekļi > 3,5t)
- Multi-trailer trucks (Kravas transportlīdzekļi ar piekabēm)
- Semi-trailer trucks (Vilcēji ar puspiekabēm)
- Buses (Autobusi)
- Pedestrians (Gājēji)
- Bicycles (Velosipēdi)
- Other vehicles (Citi transportlīdzekļi)

## Image sources for model creation
[Vehicle dataset](https://drive.google.com/drive/folders/1a-v4os2Ekr-IezLE-pGNJ7R0plZyf6bE)\
[Traffic videos from "Pilsēta cilvēkiem"](https://www.pilsetacilvekiem.lv/)\
[Open Images Dataset V7](https://storage.googleapis.com/openimages/web/index.html)
