# meme-detector-information-tracer

meme detector using image from information tracer

#Getting Started

## Pre-requisite
* Python
* informationtracer token

## Installation
```
!pip install img2vec_pytorch
!pip install informationtracer
!pip install easyocr
!pip install transformers
!pip install face_recognition
```
## Clone the repository
```
git clone https://github.com/zhouhanc/meme-detector-information-tracer.git
```

## Usage

* You can run the main.py with the following code:
'''
python main.py <querywords> <token> <start_date> <end_date> <platform>
'''

* There are also some default parameters as below:

- "n_class" : the number of classes for image clustering, default 3.
- "npca" : the number of dimensions of X after dimensionality reduction, default 2.
- "display" : whether to show the clustered images in each group, default False.

The corresponding code is as below:
'''
python main.py <querywords> <token> <start_date> <end_date> <platform> <n_class> <npca> <display>
'''


