FROM python:3.10

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip 
    
RUN pip install cython
RUN pip install pillow>=7.0.0
RUN pip install numpy>=1.18.1
RUN pip install opencv-python>=4.1.2
RUN pip install torch>=1.9.0 --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip install torchvision>=0.10.0 --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip install pytest==7.1.3
RUN pip install tqdm==4.64.1
RUN pip install scipy>=1.7.3
RUN pip install matplotlib>=3.4.3
RUN pip install mock==4.0.3
RUN pip install pycocotools@git+https://github.com/gautamchitnis/cocoapi.git@cocodataset-master#subdirectory=PythonAPI    

# Install ImageAI library
RUN pip install imageai --upgrade

WORKDIR /vehicle-classifier