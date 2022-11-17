This script downloads images from Google search (or Bing search). 

google download images has a limit of 100 images.

You can also use bing where you can install a large number of images.
pip install bing-image-downloader
"""

from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()
arguments = {"keywords":"cristiano, messi, neymar",
             "limit":20,"print_urls":False}
paths = response.download(arguments)
#print complete paths to the downloaded images
print(paths)


#####################################

#Bing
from bing_image_downloader import downloader
downloader.download("monkey", limit=300,  output_dir='dataset', 
                    adult_filter_off=True, force_replace=False, timeout=60)
downloader.download("tiger", limit=300,  output_dir='dataset', 
                    adult_filter_off=True, force_replace=False, timeout=60)
                    
dataset directory will be created with 2 directories inside (monkey and tiger).
