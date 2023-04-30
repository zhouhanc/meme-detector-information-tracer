#folders need to bebuilt
!echo 'create folders to store image...'
!rm -rf twitter_image facebook_image instagram_image reddit_image youtube_image 
!time 1
!ls -lhrt
!time 1
!mkdir twitter_image facebook_image instagram_image reddit_image youtube_image
!ls -lhrt
#packages need to be installed
!pip install img2vec_pytorch
!pip install informationtracer
!pip install easyocr
!pip install face_recognition