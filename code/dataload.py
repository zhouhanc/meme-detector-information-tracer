import glob
from pprint import pprint
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
from os import path
import requests
from img2vec_pytorch import Img2Vec
from PIL import Image
import subprocess

# Initialize Img2Vec converter
img2vec_ = Img2Vec(cuda=False)

def download_image_from_information_tracer(platform, id_hash256, token):
  """
    return a list of dictionaries, each containing info about 
    image text, image path, platform

  """
  subprocess.run(['rm', '-rf', 'twitter_image', 'facebook_image', 'instagram_image', 'reddit_image', 'youtube_image'])
  subprocess.run(['mkdir', 'twitter_image' ,'facebook_image' ,'instagram_image' ,'reddit_image','youtube_image'])

  print('downloading images from {}...'.format(platform))
  url = 'https://informationtracer.com/loadsource?token={}&source={}&id_hash256={}&limit=1000&truncated=yes'.format(token, platform, id_hash256)
  all_posts = requests.get(url).json()
  image_info = []
  # error handling, 
  if 'message' in all_posts:
    print('===== JOB FAILED, maybe check variable id_hash256 and token?')
    print(all_posts)
    print('=====')
    return 

  index = 0
  for post in all_posts:
      if post['media_url']:
        try:
          img_data = requests.get(post['media_url']).content
          img_file_name = '{}_image/'.format(platform) + str(index) + '.jpg'
          # if path.exists(img_file_name):
          #   print('path {} exists'.format(img_file_name))
          #   continue
          with open(img_file_name, 'wb') as handler:
              handler.write(img_data)              
          vec = img2vec_.get_vec(pil_loader(img_file_name), tensor=False)
          index += 1
          image_info.append({
              'filename': img_file_name,
              'vector': vec,
              'platform': platform,
              'text': post['text'],
          })
        # vecs.append(img2vec_.get_vec(pil_loader(img_path), tensor=False))
        except Exception as e:
          print(post['media_url'])
          print(e)

  return image_info
  
def pil_loader(path):
    # open path as file to avoid ResourceWarning (https://github.com/python-pillow/Pillow/issues/835)
    with open(path, 'rb') as f:
        img = Image.open(f)
        return img.convert('RGB')

