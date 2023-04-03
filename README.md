## Used libraries
- [ImageAI](https://github.com/OlafenwaMoses/ImageAI) - Model training and object detection
- [Label Studio](https://github.com/heartexlabs/label-studio) - Image annotation and dataset creation

## Installation
### Local environment
1. `pip install -r requirements.txt`
2. `pip install imageai --upgrade`

### Docker environment
1. `docker-compose up -d`
2. `docker exec -it vehicle-classifier-and-counter_app_1 bash`

### Label studio
1. `docker build -t heartexlabs/label-studio:latest .`
2. `docker run -it -p 805:8080 -v %cd%/image-annotation-tool:/label-studio/data heartexlabs/label-studio:latest label-studio --log-level DEBUG`

### Label studio backend (seperate folder)
1. `git clone https://github.com/heartexlabs/label-studio-ml-backend`
2. `cd label-studio-ml-backend/label_studio_ml/examples/mmdetection`
3. `docker-compose up`
4. `label-studio-ml init coco-detector --from mmdetection.py`
5. `LABEL_STUDIO_HOSTNAME=http://host.docker.internal:805 label-studio-ml start coco-detector --with config_file=./faster_rcnn_r50_fpn_1x_coco.py checkpoint_file=./faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth`

## Perform video object detection and analysis
### Get images from videos
1. Place videos in the `video-image-extractor/videos` folder
2. `cd video-image-extractor`
3. `python run.py`

### Annotate chosen/gathered images

### Export annotated image dataset

### Split image dataset into training and validation sets

### Train object detection model

### Copy newest model to object detection directory

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
