import os

path =  'E:/face-mask-detection/train_images/New folder'
files = os.listdir(path)
i = 25877

for ff in files:
    os.rename(os.path.join(path, ff), os.path.join(path, 'train_' + str(i).zfill(8) + '.jpg'))
    i +=1