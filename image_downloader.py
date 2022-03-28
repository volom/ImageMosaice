from bing_image_downloader import downloader
import time
from tqdm import tqdm

# put your requests key word for searching and download images from bing
list_requests = []

for request in tqdm(list_requests, position=0, leave=True):
    downloader.download(request, limit=10,  output_dir='./titles_dir', adult_filter_off=False, force_replace=False, timeout=10, verbose=True)
    time.sleep(3)