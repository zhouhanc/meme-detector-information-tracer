from dataload import download_image_from_information_tracer
from informationtracer import informationtracer
from text_encoding import get_txtencode
#from face_encoding import get_faceencode
from cluster import get_image_clusters
from display import display_image
import numpy as np
import subprocess
import pandas as pd
import os
import sys
def main(query,token,start_date,end_date,platform, n_class=3,npca=2,display=True):
    
    id_hash256 = informationtracer.trace(query=query, token=token, start_date=start_date, end_date=end_date)

    image_and_vec = download_image_from_information_tracer(platform, id_hash256, token)
    
    paths=[image_and_vec[i]['filename'] for  i in range(len(image_and_vec))]
    sorted_image_and_vec = sorted(image_and_vec, key=lambda x: x['filename'])
    X_img=[image['vector'] for image in sorted_image_and_vec]
    X_txt=get_txtencode(paths)
 #   face_encodings=get_faceencode(paths)
    X = np.concatenate([X_img, X_txt], axis=1)
    labels = get_image_clusters(vecs=X, n_cluster=n_class,npca=npca) 
    if display:
        for label in labels:
            print('displaying images in label {}...'.format(label))

            image_filename = [i['filename'] for i in sorted_image_and_vec]
            filename_to_display = [filename for filename, _label in zip(image_filename, labels) if _label==label]
            display_image(filename=filename_to_display)
    return zip(image_filename, labels)




if __name__=='__main__':
    query,token,start_date, end_date, platform=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]
    data=main(query,token,start_date,end_date,platform)
    pd.DataFrame(data).to_csv('result.csv')
