## Used libraries
- [ImageAI](https://github.com/OlafenwaMoses/ImageAI) - Model training and object detection
- [Label Studio](https://github.com/heartexlabs/label-studio) - Image annotation and dataset creation

## Installation
### Local environment
1. `pip install cython pillow>=7.0.0 numpy>=1.18.1 opencv-python>=4.1.2 torch>=1.9.0 --extra-index-url https://download.pytorch.org/whl/cu102 torchvision>=0.10.0 --extra-index-url https://download.pytorch.org/whl/cu102 pytest==7.1.3 tqdm==4.64.1 scipy>=1.7.3 matplotlib>=3.4.3 mock==4.0.3 pycocotools@git+https://github.com/gautamchitnis/cocoapi.git@cocodataset-master#subdirectory=PythonAPI`
2. `pip install imageai --upgrade`

### Label studio
1. `docker build -t heartexlabs/label-studio:latest .`
2. `docker run -it -p 805:8080 -v %cd%/image-annotation-tool:/label-studio/data heartexlabs/label-studio:latest label-studio --log-level DEBUG`

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
[Open Images Dataset V7](https://storage.googleapis.com/openimages/web/index.html)