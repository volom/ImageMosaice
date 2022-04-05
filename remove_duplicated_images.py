# removing duplicated images in the given directory

import hashlib
import os
from tqdm import tqdm
images_dir = r''
file_list = os.listdir(images_dir)

duplicates = []
hash_keys = dict()

for index, filename in  tqdm(enumerate(os.listdir(images_dir)), position=0, leave=True):  
    if os.path.isfile(f'{images_dir}/{filename}'):
        with open(f'{images_dir}/{filename}', 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys: 
            hash_keys[filehash] = index
        else:
            duplicates.append((index,hash_keys[filehash]))


for index in tqdm(duplicates, position=0, leave=True):
    os.remove(f'{images_dir}/{file_list[index[0]]}')
