import glob
import os

j=0

test = 134
valid = 482
train = 3542
path = 'C:/Users/Pablo Martin/Documents/DataSetTemporal/Car Crash Detection.v36-90-rotate.darknet/test/'
for i, filename in enumerate(glob.glob(path + '*.jpg')):
    os.rename(filename, os.path.join(path, 'test_' + str(i+test) + '.jpg'))

for i, filename in enumerate(glob.glob(path + '*.txt')):
    os.rename(filename, os.path.join(path, 'test_' + str(i+test) + '.txt'))


path = 'C:/Users/Pablo Martin/Documents/DataSetTemporal/Car Crash Detection.v36-90-rotate.darknet/valid/'
for i, filename in enumerate(glob.glob(path + '*.jpg')):
    os.rename(filename, os.path.join(path, 'valid_' + str(i+valid) + '.jpg'))

for i, filename in enumerate(glob.glob(path + '*.txt')):
    os.rename(filename, os.path.join(path, 'valid_' + str(i+valid) + '.txt'))


path = 'C:/Users/Pablo Martin/Documents/DataSetTemporal/Car Crash Detection.v36-90-rotate.darknet/train/'
for i, filename in enumerate(glob.glob(path + '*.jpg')):
    os.rename(filename, os.path.join(path, 'train_' + str(i+train) + '.jpg'))

for i, filename in enumerate(glob.glob(path + '*.txt')):
    os.rename(filename, os.path.join(path, 'train_' + str(i+train) + '.txt'))    